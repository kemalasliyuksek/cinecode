"""Regressions for silent failures: Turkish capitals, waived checks, partial downloads, unsafe inputs, parallel runs."""
import contextlib
import io
import json
import os
import tempfile

os.environ["CINECODE_NO_OPEN"] = "1"   # boards and drafts never pop up during tests
from pathlib import Path
import shutil
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import asset_search
import footage_cut
import formats
import guard
import mix

FFMPEG = shutil.which("ffmpeg") and shutil.which("ffprobe")


class Reply(io.BytesIO):
    """A urlopen answer whose body may be shorter than the length it announces (a dropped connection)."""
    def __init__(self, body, length=None):
        super().__init__(body)
        self.headers = {"Content-Length": str(len(body) if length is None else length)}

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False


def size_of(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=width,height", "-of", "csv=p=0", str(path)],
                         capture_output=True, text=True).stdout
    return tuple(int(x) for x in out.strip().split(",")[:2])


class Hardening(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="cinecode-hard-")
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name)

    def make(self):
        import make
        return make

    def test_turkish_capitals_name_the_format_and_the_music_choice(self):
        make = self.make()
        (self.path / "STATE.md").write_text("# State: Deneme\n- **Format:** DİKEY, 30 sn\n", encoding="utf-8")
        with patch.object(make, "PROJECT", self.path):
            self.assertEqual(make.frame_size(None), (1080, 1920))
        film = self.path / "film.html"
        film.write_text("const OWN_MUSIC = null;\nfunction score(ctx) {\n  pad(ctx, 0, 4);\n}\n", encoding="utf-8")
        with patch.object(make, "PROJECT", self.path):
            line = make.music_choice_line(str(film), None, "- **Music:** MÜZİK YOK (user)\n")
        self.assertIn("MUSIC NOT CHOSEN", line)

    def test_only_the_sound_line_waives_a_silent_master(self):
        make = self.make()
        silent = "SILENT SOUNDTRACK\nOK"
        for state in ("# State: Sessiz Gece\n- **Sound (Q4):** narrator + music\n",
                      "- **Sound:** not silent, music and effects\n", "- **Sound:** music only\n",
                      "- **Sound (Q4):** narrator + music\n- **Sound identity:** a silent room, one bell\n"):
            self.assertNotEqual(make.master_summary(silent, state)[0], "silent by choice", state)
        for state in ("- **Sound (Q4):** silent, by choice\n", "- **Ses / Sound:** sessiz film\n"):
            self.assertEqual(make.master_summary(silent, state)[0], "silent by choice", state)

    def test_a_cc0_row_never_prints_none_required_as_a_credit(self):
        make = self.make()
        (self.path / "LICENSES.csv").write_text(
            "file,title,author,source_url,licence,licence_url,attribution_text,modifications,downloaded_at,used_in,notes\n"
            "audio/samples/cello/,cello (VCSL),Versilian Studios,https://x,CC0-1.0,https://cc0,none required,,,score,\n",
            encoding="utf-8")
        with patch.object(make, "PROJECT", self.path):
            make.credits_file("Film", "")
        text = (self.path / "Film-credits.txt").read_text(encoding="utf-8")
        self.assertNotIn("none required", text)
        self.assertIn('"cello (VCSL)" by Versilian Studios', text)

    def test_a_second_render_step_waits_for_the_one_running(self):
        film = self.path / "film"
        (film / "tools").mkdir(parents=True)
        (film / "logs").mkdir()
        shutil.copy(ROOT / "scripts" / "make.py", film / "tools" / "make.py")
        (film / "STATE.md").write_text("# State: x\n", encoding="utf-8")
        (film / "logs" / "make.running").write_text(f"{os.getpid()} draft 0\n", encoding="utf-8")
        r = subprocess.run([sys.executable, str(film / "tools" / "make.py"), "stills"], capture_output=True, text=True,
                           cwd=film, env=dict(os.environ, HOME=str(self.path), USERPROFILE=str(self.path)))
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BUSY", r.stdout)
        self.assertIn(str(os.getpid()), (film / "logs" / "make.running").read_text(encoding="utf-8"))

    def test_a_download_is_whole_or_nothing(self):
        dest = str(self.path / "clip.mp4")
        with patch.object(asset_search.urllib.request, "urlopen", return_value=Reply(b"x" * 1000, 5_000_000)):
            with self.assertRaises(OSError):
                asset_search.download("https://cdn.example/clip.mp4", dest)
        self.assertEqual(os.listdir(self.path), [], "no file and no .part left behind")
        with patch.object(asset_search.urllib.request, "urlopen", return_value=Reply(b"x" * 100)):
            with self.assertRaises(ValueError):
                asset_search.download("https://cdn.example/clip.mp4", dest, limit=10)
        with patch.object(asset_search.urllib.request, "urlopen", return_value=Reply(b"whole")):
            asset_search.download("https://cdn.example/clip.mp4", dest)
        self.assertEqual(Path(dest).read_bytes(), b"whole")

    def test_remote_answers_name_web_addresses_only(self):
        self.assertEqual(asset_search.web_url("http://images-assets.nasa.gov/a.jpg"), "https://images-assets.nasa.gov/a.jpg")
        for bad in ("file:///etc/passwd", "concat:a.mp3|b.mp3", "/etc/passwd", "ftp://x/y", "https:///nohost"):
            with self.assertRaises(ValueError, msg=bad):
                asset_search.web_url(bad)
        with patch.object(asset_search.urllib.request, "urlopen") as opened:
            with self.assertRaises(ValueError):
                asset_search.get("file:///etc/passwd", as_json=False)
        opened.assert_not_called()

    def test_a_missing_thumbnail_keeps_every_other_tile_in_its_numbered_place(self):
        pic = self.path / "a.png"
        pic.write_bytes(b"fixture")
        calls = []
        with patch.object(asset_search.subprocess, "run", side_effect=lambda cmd, **k: calls.append(cmd)), \
                contextlib.redirect_stdout(io.StringIO()):
            sheet = asset_search.contact_sheet([{"n": 1, "thumb": str(pic)}, {"n": 2, "thumb": "file:///etc/passwd"},
                                                {"n": 3, "thumb": str(pic)}], str(self.path / "board"))
        self.assertIsNotNone(sheet)
        cmd = calls[0]
        self.assertIn("xstack=inputs=3", cmd[cmd.index("-filter_complex") + 1], "three tiles: the second one dark")
        self.assertEqual(cmd.count("lavfi"), 1)

    def test_mix_numbers_never_reach_the_filter_graph_as_words(self):
        self.assertEqual(mix.num("0.5"), 0.5)
        for bad in ("0.1,volume=-60dB", True, "nan", float("inf"), None):
            with self.assertRaises((ValueError, TypeError), msg=repr(bad)):
                mix.num(bad)
        plan = self.path / "mix.json"
        (self.path / "a.wav").write_bytes(b"")
        plan.write_text(json.dumps({"duration": 2, "out": str(self.path / "out.wav"),
                                    "layers": [{"file": str(self.path / "a.wav"), "fade_in": "0.1,volume=-60dB"}]}))
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "mix.py"), str(plan)], capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("take numbers", r.stdout + r.stderr)

    def test_words_match_across_turkish_and_english_capitals(self):
        self.assertEqual(footage_cut.norm("Internet"), footage_cut.norm("internet"))
        self.assertEqual(footage_cut.norm("IŞIK"), footage_cut.norm("ışık"))
        self.assertEqual(formats.slug("KIRMIZI"), formats.slug("kırmızı"))
        self.assertEqual(formats.slug("İstanbul"), "istanbul")

    @unittest.skipIf(os.name == "nt" or (hasattr(os, "geteuid") and os.geteuid() == 0), "needs Unix permissions")
    def test_a_locked_folder_hides_no_film_beside_it(self):
        film = self.path / "zz-film"
        (film / "tools").mkdir(parents=True)
        (film / "STATE.md").write_text("x", encoding="utf-8")
        (film / "tools" / "qc.py").write_text("", encoding="utf-8")
        locked = self.path / "aa-locked"
        (locked / "inner").mkdir(parents=True)
        locked.chmod(0)
        self.addCleanup(locked.chmod, 0o755)
        self.assertEqual(guard.films_below(str(self.path)), [film])
        self.assertTrue(guard.film_near(str(self.path)))

    @unittest.skipUnless(shutil.which("git"), "needs git")
    def test_a_snapshot_never_runs_the_users_signing_or_hooks(self):
        config = self.path / "gitconfig"
        hooks = self.path / "hooks"
        hooks.mkdir()
        (hooks / "post-commit").write_text("#!/bin/sh\ntouch \"$HOOK_RAN\"\n", encoding="utf-8")
        (hooks / "post-commit").chmod(0o755)
        config.write_text(f"[commit]\n\tgpgsign = true\n[gpg]\n\tprogram = false\n[core]\n\thooksPath = {hooks.as_posix()}\n",
                          encoding="utf-8")
        film = self.path / "film"
        film.mkdir()
        env = dict(os.environ, GIT_CONFIG_GLOBAL=str(config), HOOK_RAN=str(self.path / "ran"))
        subprocess.run(["git", "init", "-q"], cwd=film, check=True, env=env)
        (film / "STATE.md").write_text("x", encoding="utf-8")
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "snapshot.py"), "gate"], cwd=film, capture_output=True,
                           text=True, env=env)
        self.assertEqual(r.stdout.strip(), "snapshot: gate", r.stdout + r.stderr)
        self.assertFalse((self.path / "ran").exists(), "the user's hooks ran on a film snapshot")

    @unittest.skipUnless(FFMPEG, "needs ffmpeg")
    def test_a_steady_tone_is_mastered_without_compression(self):
        tone, out = self.path / "tone.wav", self.path / "master.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "sine=f=440:d=4", "-ar", "48000", str(tone)],
                       check=True)
        r = subprocess.run([sys.executable, str(ROOT / "scripts" / "master_audio.py"), str(tone), str(out)],
                           capture_output=True, text=True)
        self.assertIn("normalization_type=linear", r.stdout, r.stdout + r.stderr)

    @unittest.skipUnless(FFMPEG, "needs ffmpeg")
    def test_a_long_films_sheet_stays_under_the_guards_image_limit(self):
        for name, size, secs in (("wide.mp4", "1920x1080", 180), ("tall.mp4", "1080x1920", 90)):
            video = self.path / name
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=gray:s={size}:r=1:d={secs}",
                            "-c:v", "libx264", "-preset", "ultrafast", str(video)], check=True)
            out = self.path / f"qc-{name}"
            r = subprocess.run([sys.executable, str(ROOT / "scripts" / "qc.py"), "sheet", str(video)], capture_output=True,
                               text=True, env=dict(os.environ, QC_OUT=str(out)))
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            w, h = size_of(out / "sheet.jpg")
            self.assertLessEqual(w * h, guard.IMAGE_MAX_PIXELS, name)


if __name__ == "__main__":
    unittest.main()

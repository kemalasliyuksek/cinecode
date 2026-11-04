"""Capture regressions. Standard library only; opt into real Chrome with CINECODE_BROWSER_TESTS=1."""
import functools
import hashlib
import http.server
import json
import os
import tempfile

os.environ["CINECODE_VIEWER_WAIT"] = "0"   # a final never waits for a viewer in tests
os.environ["CINECODE_NO_OPEN"] = "1"   # boards and drafts never pop up during tests
os.environ["CINECODE_SHOWN"] = os.path.join(tempfile.gettempdir(), "cinecode-test-shown.json")
os.environ["CINECODE_SHOWN_MUSIC"] = os.path.join(tempfile.gettempdir(), "cinecode-test-music.json")
os.environ["CINECODE_SHOWN_SOUNDS"] = os.path.join(tempfile.gettempdir(), "cinecode-test-sounds.json")
os.environ["CINECODE_SOUNDS_CACHE"] = os.path.join(tempfile.gettempdir(), "cinecode-test-sound-cache")
os.environ["CINECODE_SAMPLES_CACHE"] = os.path.join(tempfile.gettempdir(), "cinecode-test-samples")
from pathlib import Path
import shutil
import subprocess
import threading
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
NODE = os.environ.get("CINECODE_NODE") or shutil.which("node")
SCRIPT = ROOT / "scripts" / "capture.mjs"


def invoke(args, cwd, env=None):
    return subprocess.run([NODE, str(SCRIPT), *args], cwd=cwd, capture_output=True, text=True, timeout=35,
                          env={**os.environ, **(env or {})})


def long_tmpdir(base):
    """A real folder whose path alone passes the 107 characters a Unix socket path may have."""
    path = Path(base) / ("a-temp-folder-with-a-long-name-" * 4) / ("and-one-more-level-of-it-" * 4)
    path.mkdir(parents=True)
    return path


@unittest.skipIf(not NODE or os.name == "nt", "Chrome's socket folder is a Unix matter; Node.js is required")
class ChromeTempFolder(unittest.TestCase):
    """Chrome aborts when $TMPDIR/org.chromium.Chromium.XXXXXX/SingletonSocket passes the socket path limit. A stand-in
    Chrome reports the TMPDIR it was started with, so this runs on every machine and crashes no real browser."""
    ROOM = 45                                    # /org.chromium.Chromium.XXXXXX/SingletonSocket, the longest brand
    LIMIT = 103                                  # macOS; Linux allows 107

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ct-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.fake = self.root / "fake-chrome"
        self.fake.write_text('#!/bin/sh\nprintf "%s" "$TMPDIR" > "$CINECODE_TEST_SEEN"\n'
                             'if [ -d "$TMPDIR" ]; then : > "$CINECODE_TEST_SEEN.dir"; fi\nexit 1\n', encoding="utf-8")
        self.fake.chmod(0o755)
        self.seen = self.root / "seen"

    def started_with(self, tmpdir):
        result = invoke(["--url", "page.html", "--probe"], self.root,
                        {"TMPDIR": str(tmpdir), "CHROME_PATH": str(self.fake), "CINECODE_TEST_SEEN": str(self.seen)})
        self.assertIn("Chrome did not start", result.stderr)     # the stand-in exits; only its TMPDIR matters here
        return self.seen.read_text(encoding="utf-8")

    def test_a_long_tmpdir_is_replaced_by_a_short_folder_that_exists_and_is_removed_after(self):
        if not any(os.access(r, os.W_OK) for r in ("/tmp", os.environ.get("XDG_RUNTIME_DIR", ""), "/var/tmp") if r):
            self.skipTest("no short temp folder is writable here (a sandbox)")
        given = long_tmpdir(self.root)
        got = self.started_with(given)
        self.assertNotEqual(got, str(given))
        self.assertLessEqual(len(got) + self.ROOM, self.LIMIT, got)
        self.assertTrue(Path(str(self.seen) + ".dir").exists(), "the short folder did not exist when Chrome started")
        self.assertFalse(Path(got).exists(), "the short folder was left behind")

    def test_a_short_tmpdir_is_left_as_it_is(self):
        if len(str(self.root)) + self.ROOM > self.LIMIT:
            self.skipTest("this machine's own temp folder is long")
        self.assertEqual(self.started_with(self.root), str(self.root))


@unittest.skipUnless(NODE, "Node.js is required")
class Arguments(unittest.TestCase):
    def test_help(self):
        result = invoke(["--help"], ROOT)
        self.assertEqual(result.returncode, 0)
        self.assertIn("--fresh", result.stdout)

    def test_invalid_values_fail_before_browser_or_output(self):
        cases = [("--workers", "1.5"), ("--workers", "abc"), ("--workers", "0"),
                 ("--workers", "Infinity"), ("--workers",), ("--start", "0.5"),
                 ("--end", "-1"), ("--quality", "2"), ("--quality",), ("--format", "webp"),
                 ("--frames", "0,no"), ("--frames", "0,"), ("--frames", "-1"), ("--frames", "0.5")]
        with tempfile.TemporaryDirectory() as tmp:
            for case in cases:
                with self.subTest(case=case):
                    result = invoke(["--url", "missing.html", "--out", "frames", *case], tmp)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(case[0], result.stderr)
                    self.assertNotIn("Chrome did not start", result.stderr)
                    self.assertFalse((Path(tmp) / "frames").exists())


PAGE = """<!doctype html><canvas id="c" width="32" height="32"></canvas><script type="module">
import { tint } from './lib/theme.mjs';
const c=document.getElementById('c'),g=c.getContext('2d'),im=new Image();
im.src=new URLSearchParams(location.search).get('still')||'assets/image.svg';
window.READY=im.decode().then(()=>({frames:4,fps:24,width:32,height:32,renderer:'regression-test'}));
window.captureFrame=(i)=>{g.drawImage(im,0,0);g.fillStyle=tint;g.fillRect(i,0,4,4);return c.toDataURL()};
</script>"""


@unittest.skipUnless(NODE and os.environ.get("CINECODE_BROWSER_TESTS") == "1", "set CINECODE_BROWSER_TESTS=1 for Chrome tests")
class Browser(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="cinecode-test-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in ["assets", "review", "lib"]:
            (self.root / name).mkdir()
        (self.root / "STATE.md").write_text("test film", encoding="utf-8")
        (self.root / "index.html").write_text(PAGE, encoding="utf-8")
        (self.root / "lib/theme.mjs").write_text("export const tint = '#ffffff';", encoding="utf-8")
        self.image("assets/image.svg", "#ff0000")

    def image(self, path, color):
        (self.root / path).write_text('<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32">'
                                      '<rect width="32" height="32" fill="' + color + '"/></svg>', encoding="utf-8")

    def cap(self, *args, url="index.html", out="frames", frames="0", ok=True):
        result = invoke(["--url", url, "--out", out, "--frames", frames, *args], self.root)
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def digest(self, out="frames"):
        return hashlib.sha256((self.root / out / "000000.png").read_bytes()).hexdigest()

    def test_resume_and_fresh(self):
        self.cap()
        self.assertIn("0 rendered, 1 skipped", self.cap().stdout)
        self.assertIn("1 rendered, 0 skipped", self.cap("--fresh").stdout)

    @unittest.skipIf(os.name == "nt", "Chrome's socket folder is a Unix matter")
    def test_renders_under_a_tmpdir_too_long_for_chromes_socket(self):
        result = invoke(["--url", "index.html", "--out", "frames", "--frames", "0"], self.root,
                        {"TMPDIR": str(long_tmpdir(self.root))})
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue((self.root / "frames/000000.png").is_file())

    def test_status_file_does_not_invalidate_inputs(self):
        self.cap("--status", "progress.json")
        self.assertIn("0 rendered, 1 skipped", self.cap("--status", "progress.json").stdout)
        self.assertEqual(json.loads((self.root / "progress.json").read_text())["state"], "done")

    def test_status_parent_is_created(self):
        self.cap("--status", "new-folder/status.json")
        self.assertEqual(json.loads((self.root / "new-folder/status.json").read_text())["state"], "done")

    def test_changed_image_with_preserved_date_and_size(self):
        self.cap()
        old = self.digest()
        path = self.root / "assets/image.svg"
        stat = path.stat()
        self.image("assets/image.svg", "#0000ff")
        os.utime(path, ns=(stat.st_atime_ns, stat.st_mtime_ns))
        self.assertEqual(path.stat().st_size, stat.st_size)
        self.cap()
        self.assertNotEqual(old, self.digest())
        self.cap(out="control")
        self.assertEqual(self.digest(), self.digest("control"))

    def test_still_via_params_and_url_query(self):
        for url_query in [False, True]:
            with self.subTest(url_query=url_query):
                self.image("review/style.svg", "#ff0000")
                url = (self.root / "index.html").as_uri() + "?still=review/style.svg" if url_query else "index.html"
                args = [] if url_query else ["--params", "still=review/style.svg"]
                out = "query" if url_query else "params"
                self.cap(*args, url=url, out=out)
                old = self.digest(out)
                self.image("review/style.svg", "#0000ff")
                self.cap(*args, url=url, out=out)
                self.assertNotEqual(old, self.digest(out))

    def test_imported_module_outside_named_asset_folders(self):
        self.cap()
        old = self.digest()
        (self.root / "lib/theme.mjs").write_text("export const tint = '#000000';", encoding="utf-8")
        self.cap()
        self.assertNotEqual(old, self.digest())

    def test_unrelated_file_does_not_restart_capture(self):
        self.cap()
        (self.root / "unrelated.json").write_text('{"note":"changed"}', encoding="utf-8")
        self.assertIn("0 rendered, 1 skipped", self.cap().stdout)

    def test_a_page_that_throws_while_loading_fails_fast_with_its_error(self):
        (self.root / "broken.html").write_text(
            "<!doctype html><canvas id='c' width='32' height='32'></canvas><script>"
            "window.WORLD=new Promise(r=>{window.__ready=r});"
            "window.READY=window.WORLD.then(()=>({frames:2,fps:24,width:32,height:32,renderer:'regression-test'}));"
            "window.captureFrame=()=>document.getElementById('c').toDataURL();</script>"
            "<script type='module' src='lib/broken.mjs'></script>", encoding="utf-8")
        (self.root / "lib/broken.mjs").write_text("const a = (1 +;\nwindow.__ready();\n", encoding="utf-8")
        started = time.time()
        result = self.cap(url="broken.html", ok=False)
        self.assertLess(time.time() - started, 30, "a page that threw never waits out the whole frame timeout")
        self.assertIn("SyntaxError", result.stderr)
        self.assertIn("broken.mjs:1", result.stderr, "the error names its file and line")

    def test_params_change_invalidates_capture(self):
        self.cap("--params", "seed=1")
        self.assertIn("1 rendered, 0 skipped", self.cap("--params", "seed=2").stdout)

    def test_legacy_frames_without_stamp_are_not_trusted(self):
        self.cap()
        (self.root / "frames/.capture-stamp").unlink()
        self.assertIn("1 rendered, 0 skipped", self.cap().stdout)

    def test_invalid_range_keeps_existing_frames_and_reports_failure(self):
        self.cap()
        old = self.digest()
        for frames in ["99", "0,99"]:
            self.cap("--status", "status.json", frames=frames, ok=False)
            self.assertEqual(self.digest(), old)
            self.assertEqual(json.loads((self.root / "status.json").read_text())["state"], "failed")

    def test_invalid_ready_fails(self):
        (self.root / "index.html").write_text(PAGE.replace("frames:4", "frames:0"), encoding="utf-8")
        result = self.cap("--status", "status.json", ok=False)
        self.assertIn("READY", result.stderr)
        self.assertEqual(json.loads((self.root / "status.json").read_text())["state"], "failed")

    def test_a_failed_render_leaves_no_chrome_profile_behind(self):
        tmp = self.root / "tmp"                                        # its own temp folder: other renders may run
        tmp.mkdir()
        run = lambda: subprocess.run([NODE, str(SCRIPT), "--url", "index.html", "--out", "frames", "--frames", "0"],
                                     cwd=self.root, capture_output=True, text=True, timeout=90,   # READY waits 30 s

                                     env=dict(os.environ, TMPDIR=str(tmp), TEMP=str(tmp), TMP=str(tmp)))
        (self.root / "index.html").write_text(PAGE.replace("frames:4", "frames:0"), encoding="utf-8")
        self.assertNotEqual(run().returncode, 0)
        (self.root / "index.html").write_text("<html><body>no READY here</body></html>", encoding="utf-8")
        self.assertNotEqual(run().returncode, 0)                       # a page that never defines READY at all
        self.assertEqual(list(tmp.glob("cinecode-chrome-*")), [])
        (tmp / "cinecode-chrome-999999-left").mkdir()                    # its capture is gone: swept on the next run
        (tmp / f"cinecode-chrome-{os.getpid()}-busy").mkdir()             # a live render elsewhere: kept
        run()
        self.assertEqual(sorted(p.name for p in tmp.glob("cinecode-chrome-*")), [f"cinecode-chrome-{os.getpid()}-busy"])

    def test_caught_optional_missing_resource_does_not_break_capture(self):
        text = PAGE.replace("window.READY=im.decode().then", "const optional=fetch('missing.json').catch(()=>null);\nwindow.READY=Promise.all([im.decode(),optional]).then")
        (self.root / "index.html").write_text(text, encoding="utf-8")
        self.cap()

    def test_remote_page_is_rendered_fresh(self):
        class Quiet(http.server.SimpleHTTPRequestHandler):
            def log_message(self, *args):
                pass
        Quiet.extensions_map = dict(Quiet.extensions_map, **{".js": "text/javascript", ".mjs": "text/javascript",
                                                             ".svg": "image/svg+xml", ".html": "text/html"})
        handler = functools.partial(Quiet, directory=str(self.root))
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        worker = threading.Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            url = "http://127.0.0.1:%d/index.html" % server.server_port
            self.cap(url=url)
            old = self.digest()
            self.image("assets/image.svg", "#0000ff")
            self.cap(url=url)
            self.assertNotEqual(old, self.digest())
        finally:
            server.shutdown()
            server.server_close()
            worker.join(timeout=5)

    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg and ffprobe are required")
    def test_repeated_frames_keep_their_places_in_multi_worker_video(self):
        text = PAGE.replace("window.captureFrame=(i)=>{", "window.captureFrame=async(i)=>{if(i===0)await new Promise(r=>setTimeout(r,500));")
        (self.root / "index.html").write_text(text, encoding="utf-8")
        result = invoke(["--url", "index.html", "--video", "repeated.mp4", "--workers", "2", "--frames", "0,1,2,1"], self.root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=nb_frames", "-of", "csv=p=0", "repeated.mp4"], cwd=self.root, capture_output=True, text=True, check=True)
        self.assertEqual(probe.stdout.strip(), "4")

    def test_the_quick_template_draws_a_cast_model_sheet(self):
        text = (Path(__file__).resolve().parent.parent / "templates" / "quick" / "film.html").read_text(encoding="utf-8")
        text = text.replace("const CAST = {};", "const CAST = { ada: { hairStyle: 'bob', top: '#c8402f' }, "
                            "bo: { hairStyle: 'curly', build: 1.2 }, cy: { hairStyle: 'cap' }, di: { hairStyle: 'long' } };")
        (self.root / "film.html").write_text(text, encoding="utf-8")
        for who in ("ada", "bo", "cy", "di"):
            result = invoke(["--url", "film.html", "--out", f"sheet-{who}", "--frames", "0", "--format", "jpeg",
                             "--params", f"w=960&h=540&modelsheet={who}"], self.root)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue((self.root / f"sheet-{who}" / "000000.jpg").stat().st_size > 20000)

    def test_the_text_check_finds_touching_lines_and_lost_type_and_passes_clean_type(self):
        text = (Path(__file__).resolve().parent.parent / "templates" / "quick" / "film.html").read_text(encoding="utf-8")
        extra = """const baseFrame = window.renderFrame;
window.renderFrame = (f) => {
  baseFrame(f);
  const c = q.get('case'), px = Math.round(H * 0.07);
  g.setTransform(1, 0, 0, 1, 0, 0); g.globalAlpha = 1; g.textAlign = 'left'; g.font = `700 ${px}px sans-serif`;
  g.fillStyle = '#000'; g.fillRect(0, H * 0.55, W, H * 0.45);
  if (c === 'touch') { g.fillStyle = '#fff'; g.fillText('USTSATIR', W * 0.1, H * 0.7); g.fillText('ALTSATIR', W * 0.1, H * 0.7 + px * 0.55); }
  if (c === 'lost') { g.fillStyle = '#f2f2f2'; g.fillRect(0, H * 0.6, W, H * 0.2); g.fillStyle = '#ffffff'; g.fillText('KAYBOLAN', W * 0.1, H * 0.72); }
  if (c === 'clean') { g.fillStyle = '#fff'; g.fillText('USTSATIR', W * 0.1, H * 0.65); g.fillText('ALTSATIR', W * 0.1, H * 0.85); }
};
"""
        text = text.replace("// Text check (make.py runs", extra + "// Text check (make.py runs", 1)
        (self.root / "film.html").write_text(text, encoding="utf-8")
        out = {}
        for case in ("touch", "lost", "clean"):
            r = invoke(["--url", "film.html", "--text-check", "1", "--params", f"w=360&h=640&shutter=0&weave=0&tone=0&textcheck=1&case={case}"], self.root)
            out[case] = r.stdout + r.stderr
        self.assertRegex(out["touch"], r'TEXT OVERLAP .*"(USTSATIR|ALTSATIR)" and "(USTSATIR|ALTSATIR)"')
        self.assertRegex(out["lost"], r'LOW CONTRAST .*"KAYBOLAN"')
        self.assertNotIn("SATIR", "".join(l for l in out["clean"].splitlines(True) if "OVERLAP" in l or "CONTRAST" in l))

    def test_a_frame_that_never_finishes_fails_instead_of_hanging(self):
        text = PAGE.replace("window.captureFrame=(i)=>{", "window.captureFrame=(i)=>{if(i===2)return new Promise(()=>{});")
        (self.root / "index.html").write_text(text, encoding="utf-8")
        os.environ["CINECODE_FRAME_TIMEOUT"] = "3"
        try:
            result = invoke(["--url", "index.html", "--out", "frames"], self.root)
        finally:
            del os.environ["CINECODE_FRAME_TIMEOUT"]
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("gave no answer in 3 s", result.stdout + result.stderr)

    @unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg and ffprobe are required")
    def test_multi_worker_video_contains_every_frame(self):
        result = invoke(["--url", "index.html", "--video", "picture.mp4", "--workers", "2"], self.root)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        probe = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "stream=nb_frames", "-of", "csv=p=0", "picture.mp4"], cwd=self.root, capture_output=True, text=True, check=True)
        self.assertEqual(probe.stdout.strip(), "4")


if __name__ == "__main__":
    unittest.main()

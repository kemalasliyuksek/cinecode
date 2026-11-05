<p align="center">
  <img src="docs/media/lockup.png" alt="cinecode" width="560">
</p>

<p align="center">
  <b>用代码写成的电影。</b><br>
  短片、YouTube 长视频、广告、科普视频和音乐视频。你只需带来创意和品味；AI 编程智能体负责写剧本、用代码构建每一帧画面、设计声音，最后交给你一个成品 MP4。
</p>

<p align="center">
  <a href="README.md">Türkçe</a> ·
  <a href="README.en.md">English</a> ·
  <a href="README.ja.md">日本語</a> ·
  <a href="#安装">安装</a> ·
  <a href="#快速开始">快速开始</a> ·
  <a href="#常见问题">常见问题</a>
</p>

<p align="center">
  <a href="https://github.com/sarpstar/cinecode/actions/workflows/tests.yml"><img src="https://img.shields.io/github/actions/workflow/status/sarpstar/cinecode/tests.yml?branch=main&label=tests&style=flat-square" alt="tests"></a>
  <img src="https://img.shields.io/badge/license-MIT-C37232?style=flat-square" alt="license: MIT">
  <img src="https://img.shields.io/badge/agents-Claude%20Code%20%C2%B7%20Cursor-1a1a1a?style=flat-square" alt="agents: Claude Code, Cursor">
  <img src="https://img.shields.io/badge/render-three.js%20%C2%B7%20ffmpeg-1a1a1a?style=flat-square" alt="render: three.js, ffmpeg">
</p>

<p align="center">
  <img src="docs/media/reel.gif" alt="cinecode 制作的影片 30 秒集锦：日出时的石拱、雪中的版画风邮政列车、雕花的手表机芯、沙漠里的 3D 野兔、代码雨下的微缩城市、水下的波普风鲸鱼、穿过橙色鸟居的道路、三支竖屏科普短片、麦田中架在轨道上的电影摄影机、金色光柱下的狗群、一根火柴、一家面包店和一张爵士海报、提灯的森林童话、夜色中远在海平线上的一艘船" width="100%">
</p>
<p align="center"><sub>cinecode 制作的影片 30 秒集锦。每一帧都在无头 Chrome 中由代码渲染而成。</sub></p>

它运行在你自己电脑上的 **Claude Code**（桌面应用、VS Code 扩展、终端）或 **Cursor** 中。不需要任何付费服务；只有在你需要旁白时，才会用到你自己的 Gemini 密钥（有免费额度）、ElevenLabs，或免费的土耳其语语音。

## 能做什么

### 用代码做出的短片

用一句话说出你的想法，剩下的一起来完成。

- **不落俗套。** 智能体会把你的想法和一件从世界上随机抽取的真实事物碰撞在一起：一件博物馆藏品、一种动物、一张太空照片、一项古老的发明、一处历史遗迹、一门手艺。所以你得到的不是谁都会先想到的那部片子，而是连你自己都没想到的版本。
- **不重复自己。** 每个提案都会和你做过的片子比对，同一部片子不会给你第二次。
- **最终由你拍板。** 影片用什么做成由你决定：真实光照的 3D、2D 动画、颜料、水墨、纸艺、黏土、动态图形或像素。你从一组真实电影剧照组成的面板里挑选画面风格，并在整部片子动工之前先看到并确认前两个场景。

### YouTube 长视频

十分钟乃至更长的纪录片、科普视频和视频随笔，在电影模式下按幕和章节来制作：

- 经过调研的剧本，凡涉及真实人物或事件的说法都附有出处；
- 在第一分钟埋下一个悬而未决的问题，再用一张好奇心地图让观众一路看到结尾；
- 用你的语言配旁白（土耳其语和英语语音，含免费的土耳其语语音），并为它做专属的声音处理，绝不直接使用引擎的原始声音；
- 来自开放档案馆的历史照片、地图、文献和影像素材；没有图像的地方就用代码来呈现：自动绘制的地图、计数器、图表、复原的场景；
- 形式需要时加入章节卡，为每一幕凭听感挑选音乐，母带处理到 −14 LUFS，并附上一份可放进视频简介的致谢文件。

### 广告与产品片

你的产品、配色、字体、标志和行动号召。产品会被精细地建模，并像影棚拍摄那样布光；软件则配有 UI 主视觉镜头；一项“专属性测试”确保这部片子无法套用到任何其他品牌上；同时提供带安全区的 9:16、1:1 和 16:9 版本。

### 社交平台科普短视频

30 到 60 秒的竖屏影片：第一秒就抛出问题，动态文字采用经过土耳其语字符检验的开源字体搭配，图表逐线搭建，文字在手机尺寸下依然清晰可读。

### 音乐视频（MV）

带上你的歌：先测出它的节拍网格，剪辑点落在小节上，重音落在拍点上，每一句歌词对应一个画面。

### 更多

- **像你喜欢的某个视频，但又不一样：** 测量它的形式（剪辑、节奏、光线、色彩），再在这个形式上做出全新的影片，绝不使用它的画面。
- **剪辑你自己的素材：** 口播或录屏，依据逐词计时的转录稿来剪，去掉停顿，图形与台词同步出现。
- **同一格式的系列片：** 保存一部影片的格式，下一集就按它来做。

从 15 秒的短片到十分钟以上的影片都可以。快速模式在一次会话内完成最长约 3 分钟的影片；电影模式则通过逐步确认来完成更长的作品。影片越长，所需的时间和用量就越多。

## 用 cinecode 制作

<table>
  <tr>
    <td width="33%"><img src="docs/media/stills/motor.jpg" alt="Motor：落日天空下，一道浪在破碎的瞬间凝固"><br><sub><b>Motor</b> · 凝固的瞬间 · 90 秒</sub></td>
    <td width="33%"><img src="docs/media/stills/tren.jpg" alt="The Mail Train：版画风雪景中的一节红色邮政车厢"><br><sub><b>The Mail Train</b> · 一段版画之旅 · 25 秒</sub></td>
    <td width="33%"><img src="docs/media/stills/ilktik.jpg" alt="İlk Tik：雕刻在金色手表机芯上的城市天际线"><br><sub><b>İlk Tik</b> · 手表广告 · 50 秒</sub></td>
  </tr>
  <tr>
    <td><img src="docs/media/stills/atlama.jpg" alt="Atlama Programı：绿色代码雨下的纸做城市"><br><sub><b>Atlama Programı</b> · 一部微缩致敬作品 · 50 秒</sub></td>
    <td><img src="docs/media/stills/koltuk.jpg" alt="Boş Koltuk：空旷田野中架在轨道上的电影摄影机"><br><sub><b>Boş Koltuk</b> · 自行搭建的片场 · 80 秒</sub></td>
    <td><img src="docs/media/stills/kopek.jpg" alt="Yüz Köpek：光柱下化作光点的狗群"><br><sub><b>Yüz Köpek</b> · 数据纪录片 · 90 秒</sub></td>
  </tr>
  <tr>
    <td><img src="docs/media/stills/titanik.jpg" alt="Titanik, Son Saatler：在黑暗海面上沉没的巨轮"><br><sub><b>Titanik, Son Saatler</b> · 纪录片 · 5 分钟</sub></td>
    <td><img src="docs/media/stills/cinecode.jpg" alt="cinecode：由彩色窗户组成的波普风高楼"><br><sub><b>cinecode</b> · 波普风宣传片 · 60 秒</sub></td>
    <td><img src="docs/media/stills/fener.jpg" alt="Fener：月下的女孩与树精"><br><sub><b>Fener</b> · 动画童话 · 60 秒</sub></td>
  </tr>
  <tr>
    <td><img src="docs/media/stills/gokyuzu.jpg" alt="Gökyüzü neden mavi?：分解光线的棱镜，配大号黄色文字"><br><sub><b>Gökyüzü neden mavi?</b> · 科普短片 · 45 秒，9:16</sub></td>
    <td><img src="docs/media/stills/firin.jpg" alt="Kuzguncuk Fırın：烤炉旁灯下新出炉的芝麻圈"><br><sub><b>Kuzguncuk Fırın</b> · 面包店广告 · 15 秒，9:16</sub></td>
    <td><img src="docs/media/stills/kibrit.jpg" alt="Tek Kibrit：泛着铜色光芒的版刻城市"><br><sub><b>Tek Kibrit</b> · 图形短片 · 63 秒，9:16</sub></td>
  </tr>
</table>

## 工作方式

1. **你说出创意。** 一句话就够；如果给出完整的需求说明，就直接开工。
2. **它会问几个问题**（对创意的几种解读、影片用什么做成、时长与画幅、画面风格、声音和音乐），每个问题都有一个标着 ★ 的推荐答案。
3. **它以文字形式展示方案：** 逐秒的节拍表，以及一张可以逐行修改的导演卡。然后在其余部分动工之前，先以静帧展示两个场景。
4. **它渲染一版草稿，** 进行检查（首帧即有运动、响度、可读性、重复），展示给你看，并由一位独立的观看者在毫无背景的情况下审看。你的意见只会改动它涉及的部分。
5. **成片：** 全尺寸，母带处理到 −14 LUFS，并附上可放进视频简介的致谢信息。

## 两种模式

智能体会首先问你这个问题，并根据你的目标推荐其中一种。

| | **快速模式** | **电影模式** |
|---|---|---|
| 一句话概括 | 整部影片在一个文件里，几个问题，一版低分辨率草稿，1–2 轮修改 | 先确认路线图和完整剧本；之后每个阶段经你同意后逐步制作，或直接做到草稿；包含调研和分层声音 |
| 最适合 | 一分钟以内的任何内容，包括品牌和客户项目；社交短片、科普视频、广告，最长约 3 分钟的作品；几分钟内拿到短片初稿，约 3 次确认 | 包含多个场景、调研或档案素材的较长影片：纪录片、带旁白的作品、电影节短片；逐阶段约需 6–8 次确认，一路直通约 3 次 |
| 流程 | 几个问题（含媒介、旁白、音乐和参考）→ 可选调研（与你的影片风格相近的电影剧照，以及题材真实时的真实形态）→ 文字方案（节拍、导演卡、参考板）→ 先以静帧展示两个场景请你确认，再做其余部分 → 低分辨率草稿 → 最多 2 轮基于草稿的修改 → 最终渲染 | 6 个问题 → 路线图 → 剧本 → 风格帧 → 动态分镜 → 渲染；可以逐阶段经你同意推进，也可以从剧本直接做到草稿 |
| 画面 | 一个自包含的 `film.html`：场景是时间的函数，使用 Canvas 2D 或 three.js / WebGL，含屏幕文字 | 带八种风格预设的 three.js 场景，逐镜头渲染 |
| 声音 | 从第 1 版起就在同一文件中设计（Web Audio，离线渲染）：每个场景一层环境底噪，音效按画面的提示表触发，共享一个混响，音乐来自编曲表 | 经过设计的声音标识，包含分层底噪、拟音、高光时刻、人声和音乐 |
| 智能体 | 由一个主对话负责构建、渲染和修改（速度快）；调研在后台进行，辅助智能体只用于预测测试、重复检查、旁白录制和对每版草稿的独立审看 | 主对话构建它掌握上下文的部分；辅助智能体并行承担相互独立的部分（声音、旁白、调研、审看）以及长片的各个章节 |

你可以先用快速模式开始，之后再把影片转到电影模式：节拍表会变成路线图。

## 两种用途

与模式一同询问：模式决定工作做多深，用途决定这是一部什么样的影片。之后的一切（问题默认值、参考、确认节点、检查）都随用途而定。

| | **电影感影片** | **广告与产品**（品牌、发布、推广、科普） |
|---|---|---|
| 目标 | 一个故事、一种氛围或一件艺术作品，看起来像实拍的，而不是渲染出来的 | 一部只属于某个主题的影片，讲清楚它是谁的、观众下一步该做什么 |
| 画面 | 电影感处理：浅景深与镜头特性、胶片颗粒、摄影师的运动惯性；按需开启（默认关闭）快速运动时的 180° 运动模糊、基于工具包自带印片曲线的胶片影调，以及片门抖动；为每个镜头选择运镜 | 专属性与竞品测试，以下方字幕条显示屏幕上的名字，软件配 UI 主视觉镜头，使用你的品牌色和字体（开源字体来自 Fontsource；你自己的品牌字体只保留在本地），片尾卡带行动号召 |
| 声音 | 以环境声为主，一个标志性声音，音乐由你挑选 | 默认旁白 + 音乐 |
| 交付 | 你选择的画幅 | 带安全区的 9:16、1:1 和 16:9 版本 |
| 附加 | — | 可选：依据逐词计时的转录稿剪辑你自己的素材或录屏（需要 Whisper）：裁掉停顿，标出口吃和重录供你确认，图形与台词同步 |

详情：`references/purpose-cinematic.md`、`references/purpose-ad.md`、`references/footage-edit.md`。运动、运镜词汇、字体、声画同步、开头钩子、每个镜头一个动作以及各项检查，两种用途共用。

## 你会得到什么

- **一套写作体系**，用于写出巧妙、简短、切题的剧本（两种模式通用）：先发散再收敛，故事有转折时就让转折清晰，先定结尾，用画面说话而非直白讲述，字数预算，英语和土耳其语的陈词滥调禁用清单，朗读一遍并删减 30%，以及以初次观看者视角的检查。
- **一套有命名的运镜与转场词汇**（`references/camera-moves.md`）：运镜、焦点变化和转场（推轨推进、环绕、滑动变焦、FPV、手持、变速、移焦、匹配剪辑、甩镜、J-cut……），并说明每一种给观众带来的感受、默认时长、速度和缓动。每个镜头的运镜只需一行：*“推轨推进，3 秒，缓慢的缓入缓出，朝向人物”*。两个引擎都把它们实现为时间的纯函数（`film.html` 的 2.5D 摄像机，three.js 用 `starter/camera.mjs`）。
- **快速模式起始模板：** `film.html`，包含确定性的时间线、带景深层的 2.5D 摄像机、转场、画面与声音共用的提示表、带种子的随机数（种子数据带惰性缓存）、文字辅助工具和按变音符号留足尺寸的名字标签，以及小巧的 Web Audio 音色（pad、底鼓、滴答声、打击、上升音效、呼啸声、拨弦、柔和主旋律、拟音、环境底噪、共享的生成式混响），还有一张每次渲染前都会检查的编曲表。在浏览器中点开它，画面和声音会一起播放。
- **电影模式访谈**：六个问题，分三轮简短进行（轮次之间展示方向板）；以及**八种风格预设**（电影感写实、动漫/赛璐璐、粉彩绘本、黏土动画、剪纸/拼贴、复古/合成波/VHS、高光泽商业风、手绘水墨），还可以依据你自己的参考图走出一套自定义风格。这八个风格家族在快速模式中同样可用（调色、质感、卡通着色、一拍二的手绘动画）。
- **属于这部影片的声音：** 旁白绝不以引擎的原始声音输出。每部影片都会选定声音呈现的方式（贴近、磁带、电台、合唱、水下、机械……）、所处的空间（房间、大厅、石砌中殿、户外），还可以把影片的标志性声音融入其中；每一句台词都落在同一对白电平上。
- **像这个视频，但……：** 把你喜欢的视频放进 `refs/`，说出想改什么。它的形式会被测量出来（剪辑与镜头时长、节奏、色板与光线、BPM、剪辑点如何卡在节拍上），你改动想改的部分，然后在这个形式上做出全新的影片，绝不使用它的画面或音乐。
- **你自己的歌：** 带来一首歌或一段音轨，影片会跟随它的节拍网格：在整首歌上测量速度，片段在小节线处截取，剪辑和重音落在小节和拍点上，每句歌词对应一个画面；有旁白时音乐会自动压低。
- **方向板（电影模式）：** 你说出创意后，会在一张图中展示三个视觉方向，每个方向由一种风格加上两三部体现该风格的真实电影剧照组成（来自 FilmGrab，仅作氛围参考），并附上测得的色板；你选中的方向会被量化为影片的光线和色彩，风格帧也会以它为准进行检查。
- **为每个创意找到的风格：** 来自真实电影的方向（电影剧照、摄影指导和摄影师，仅作氛围参考），以及一套作为词汇的风格配方（木刻、浮世绘、皮影戏、孔版印刷、默片等等；大部分出自 LemoLab，见致谢）；只会读取被选中的那一个。
- **设计师级的字体排印**（`references/typography.md`）：授权干净、经过土耳其语检验的字体及搭配，来自独立开源字体厂和 Fontsource；每部影片发三组搭配，并以影片自身的风格做成字体样张卡展示；字体排印参考来自 Fonts In Use、Art of the Title、Typewolf、Are.na，以及你放在 `refs/type/` 里的截图（包括 Instagram 收藏），并被量化为字体方向；一份口味日志会跨影片学习你的选择；手机尺寸可读性、对比度和变音符号检查；可选的逐词锁定口播字幕。
- **声音设计基本功：** 每部影片一个轻量的声音标识、分层底噪、经过测试的 ffmpeg 配方、−14 LUFS 母带处理。
- **小巧、零依赖的工具：** 帧捕获（也可直接输出 MP4，并把页面的配乐输出为 WAV）、动态分镜生成器、混音器、母带处理、质量检查（包括量化的开头钩子检查、去除运镜后每个场景中主体的动作，以及每个场景的响度和刺耳度），还有带授权日志的开放授权素材搜索。

## 环境要求

- 一个能运行本地工具的 AI 编程智能体：**Claude Code**（桌面应用、VS Code 扩展或终端）或 **Cursor**。claude.ai 上的普通聊天无法在你的电脑上运行工具；Claude Code 可以（ffmpeg、Chrome、各种脚本）。
- Node.js 22+、Python 3.9+、ffmpeg 和 Google Chrome（或 Chromium / Edge）；缺什么，智能体会在你同意后安装。别的都不需要，Windows 上也一样：工具包运行在 Claude Code 自带的 PowerShell 中，不需要 bash；Git 只用于安装和更新工具包，从不用于渲染。如果工具包的守护程序没有在 Claude Code 会话中运行，影片的设置会显示 GUARD OFF（测试在每次推送时于 Windows 和 Linux 上运行，每次改动前也会在 macOS 上运行；完整地在 Windows 上做一部影片尚未试过）。这些钩子需要较新版本的 Claude Code（exec 形式的钩子和 `onFailure`，2.1.295 或更高版本）；在旧版客户端上，守护程序可能无法注册，但影片照样可以制作。
- 在 Linux 上，需要能写出 H.264 的 ffmpeg（libx264）。Fedora 自带的 `ffmpeg-free` 不包含它；完整的 ffmpeg 来自 RPM Fusion（启用该仓库后运行 `sudo dnf swap ffmpeg-free ffmpeg --allowerasing`）。缺少时，`make.py` 会说明原因并停止。
- 一块 Chrome 能调用的 GPU（任何较新的 Mac，或显卡驱动正常的 PC）。
- 磁盘空间：快速模式会把帧直接写入 MP4，几百 MB 就够；电影模式渲染时每部影片需要几 GB。

缺了其中某项？直接开始就好：智能体会先检查机器，并提出安装缺少的部分（安装任何东西之前都会先询问）。除此之外什么都不会安装：脚本只使用内置功能，three.js 从 CDN 加载固定版本的库。

**免费的土耳其语语音（如果你需要）**（工具包不会安装其中任何一个；否则旁白使用基于你密钥的 Gemini TTS，或以系统语音临时替代）：
- Canberk Aslan 的 [EMA Lightning](https://huggingface.co/canberkkkkkk/ema-lightning)（Apache 2.0）：一个清晰的声音，可在 CPU 上离线运行，连同 PyTorch 约 800 MB。安装后工具包即可使用：`python3 tools/tts.py --install ema`，然后用 `--engine ema`。
- [VoxCPM2 Türkçe ses tasarımı](https://github.com/alexturkey/voxcpm2-turkce-ses-tasarimi)（Apache 2.0）：根据文字描述设计声音，内置七位现成的旁白（纪录片腔、低沉的讲故事人、新闻主播）；需要 Apple Silicon 或 NVIDIA 显卡，约 3.7 GB。
- Özgür Güler 的 [Ahenk](https://github.com/ozguradmin/ahenk-turkish-tts)：疑问语调、情绪和笑声（大模型，需 NVIDIA 显卡），以及 Ahenk Cep（小模型，CPU 即可）；权重采用 CC BY 4.0，因此使用它们的影片需要注明 Ahenk。

## 安装

打开 Claude Code（桌面应用的 **Code** 标签页、VS Code 扩展或终端），然后说：

> 请从 https://github.com/sarpstar/cinecode 安装 cinecode 技能

它会用 git 从 GitHub 把工具包拉取到 `~/.claude/skills/cinecode`（Windows：`%USERPROFILE%\.claude\skills\cinecode`）；在没有 git 的 Windows 电脑上，它会在你同意后先安装 git（`winget install --id Git.Git -e`）。然后新开一个对话。以后说一句 **“更新 cinecode”** 就能获取最新版本。只在一个位置安装，以免智能体看到两份副本。

手动安装，同样只需一行：

```bash
git clone https://github.com/sarpstar/cinecode.git ~/.claude/skills/cinecode
```

这个技能会被日常的影片、动画和广告相关说法触发（"kısa film"、"animasyon"、"reklam filmi"、"ürün videosu"、"tanıtım videosu"、"make a short film"、"product video"、"ad"）。

### 1. Claude 桌面应用（Code）

打开 Claude 桌面应用，切换到 **Code**，为你的影片选择一个空文件夹，然后输入 **“我想做一部短片”**（土耳其语：**"Kısa film yapmak istiyorum"**）。

### 2. VS Code 扩展（Claude Code）

安装 Claude Code 扩展，打开一个空文件夹，打开 Claude Code 面板，输入同一句话。

### 3. 终端

```bash
mkdir my-film && cd my-film && claude
```

然后输入同一句话。

### 4. Cursor

在 Cursor 的 Agent 对话中，请它以同样的方式安装到 `~/.cursor/skills/cinecode`，或者：

```bash
git clone https://github.com/sarpstar/cinecode.git ~/.cursor/skills/cinecode
```

在 Cursor 中打开一个空文件夹，打开 Agent 对话，输入同一句话。工具包自带的检查（`make.py`、`qc.py`）运行方式相同；而那些在出错当下就拦住若干错误的守护钩子（剧本还没展示就先发问、草稿没有展示、刚获确认就停下）只在 Claude Code 中运行。

## 快速开始

1. 在你的智能体中打开一个空文件夹（参见“安装”）。
2. 写下你的创意。创意是你唯一需要提供的东西；其余拿不准的就别写，智能体会来问：

   ```text
   我们用 cinecode 做一部影片吧：<讲的是什么，一两句话>。

   （知道的话可以补充以下内容；不写的话工具包会来问：）
   时长：<15 秒 / 1 分钟 / 5 分钟……>
   在哪里播放：<Instagram 竖屏 / YouTube 横屏……>
   声音：<要旁白 / 不要人声 / 用我自己的歌：文件>
   风格：<你想到的某部电影、某张照片或某位画家，或者“你来推荐”>
   ```

   模式不用写：智能体会根据工作量推荐一种。你写得越少，它问得越多；一份完整的需求说明（节拍、文案、时长、画幅）会不经提问直接做出草稿。
3. 选择模式和用途（电影感影片，或广告与产品），在一两轮简短问答中回答问题（推荐选项标有 ★）。
4. 在每个检查点确认或修改。成片会以 `<title>.mp4` 的形式放在影片文件夹的最上层。

## 快速模式分步说明

| # | 步骤 | 你要做的 |
|---|---|---|
| 1 | **几个问题：** 你的创意、媒介（影片用什么做成）、时长与画幅、风格与情绪、声音（旁白 + 音乐、只有音乐和音效，或屏幕文字 + 音乐；有旁白时还有声音类型和语言）、单独的音乐问题（你凭听感挑选的真实录音、你自己的音轨、用代码编写，或不要音乐）、参考（搜索、只用你的，或跳过）；声音标识用一行给出建议 | 回答，或说“ok” |
| 1b | **轻量调研（如果你选了）：** 为题材的关键元素寻找开放授权参考，影片越长参考越多（15–30 秒 2–3 个，60 秒 3–5 个，再往上每章 2 个；另加你的 `refs/`） | — |
| 2 | **方案（一个文字确认节点）：** 一句话梗概、转折、带运镜说明的逐秒节拍表（一条连贯的流程，较长的影片按内部章节分组）、文字或台词；做过调研时附上参考板；一张简短的导演卡（风格、摄像机、运动、节奏、转场、字体、声音、后期效果），可逐行修改 | 确认、替换某个参考、提一条意见，或要求更多参考 |
| 3 | **先看两个场景：** 在其余部分动工之前，以静帧展示整体风格和两个场景（开场，以及与开场差别最大的那一场） | 继续，或提一条意见 |
| 4 | **构建与草稿：** 一个包含画面和声音的 `film.html`，一版不含后期效果的半尺寸草稿，母带处理到 −14 LUFS，并检查开头钩子 | 观看，然后确认或提意见 |
| 5 | **基于草稿的修改：** 最多两轮针对性修改，每轮都以新草稿展示 | 把意见一次性发过来 |
| 6 | **最终渲染：** 全尺寸，加上你开启的后期效果（运动模糊、印片影调、片门抖动；默认全部关闭），并再次检查 | 观看 |

## 电影模式的六个步骤

| # | 步骤 | 你要做的 |
|---|---|---|
| 1 | **访谈：** 六个问题，分三轮简短进行，轮次之间展示方向板 | 回答，或选择 ★ 选项 |
| 2 | **路线图：** 概念、带时间的镜头列表（数量视时长而定：30 秒 4–8 个，较长的影片按章节和幕分组）、画面风格、声音标识、开头钩子、风险 | 确认或修改条目 |
| 3 | **剧本与文字：** 切入角度、转折、台词（或无对白）、屏幕文字；完整剧本一次性展示 | 确认或修改；选择制作方式：逐阶段推进，或全部直接做到草稿 |
| 4 | **风格帧：** 一张最终画质的静帧，作为之后每一帧的标准 | 确认或提意见 |
| 5 | **动态分镜：** 一段带临时声音、已按时间排好的低分辨率视频 | 节奏对吗？ |
| 6 | **渲染、声音、成片：** 先出一版配好混音的半尺寸草稿剪辑，再出全尺寸画面，然后母带处理、检查、交付 | 观看，把意见一次性发过来 |

意见只会作用于它涉及的镜头、台词或声音层；每一轮都是一个新版本。你确认成片后，智能体会询问是否清理草稿和中间文件；交付的影片、你的参考、素材、音频源和意见始终保留。

**内置规则（两种模式通用）：** 前 2 秒从第 1 帧起就有运动（经过测量）；每一帧都是时间的纯函数（重新渲染结果完全一致）；每个外部文件在下载时都会登记一行授权信息；耗时的渲染在后台运行并写入状态文件；渲染时，影片页面只读取自己的影片文件夹，不读取磁盘上的其他任何文件；智能体查看的是小尺寸的缩略图拼板而不是全尺寸帧，从而控制成本。

**谁来干活（电影模式）：** 主对话构建它已经掌握上下文的部分；一个全新的辅助智能体会依据项目文件接收任务说明，并指定所用模型，负责可以并行的独立部分（声音、旁白录制、调研、独立审看）或长片的某一章；你的意见会原样保存在 `notes/round-N.md` 中，只处理它涉及的镜头；出现缺陷时，先在少量测试帧上诊断，再决定是否重建。在检查点，智能体可能会建议新开一个对话：在 Claude 桌面应用中，你同意后它会自动打开；在其他地方，你自己新开一个对话并粘贴一行 **“从 STATE.md 继续”**（土耳其语：**"STATE.md'den devam et"**）。详情：`references/context-protocol.md`。对话的每一步都会重新读取整个对话，因此让对话保持简短才是让一部影片省钱的关键：每个辅助智能体都从任务所需的模型起步（涉及品味和判断的用你对话所用的模型，文件处理和素材查找用更轻量的模型），渲染结果只用四行回报（`tools/make.py`），图片也保持小尺寸。在 Claude Code 中，这个技能通过三个启动工具包守护程序的钩子来强制执行这些做法；其检查包括：对话变大时发出提醒、对话中不出现大图、每个辅助智能体最多 25 步、不就用户尚未看到的内容发问、密钥文件保持关闭。

## 包含哪些内容

```text
cinecode/
├── SKILL.md              技能本体：流程、提问和硬性规则；每个电影对话都从这里开始
├── AGENTS.md             给读取 AGENTS.md 的智能体的入口
├── references/           创作指南
│   ├── quick-mode.md     快速模式，逐步说明
│   ├── film-mode.md      电影模式：六个需要确认的步骤
│   ├── writing.md        剧本、开场钩子、预测测试、重复检查
│   ├── looks.md          画面风格、光线、质感；配合 craft.md 和 finish.md
│   ├── camera-moves.md   镜头语言；运动见 motion.md 和 motion-design.md
│   ├── typography.md     字体排印；声音见 sound.md，用你自己的歌见 music-video.md
│   └── purpose-*.md      电影短片，或广告与产品片
├── scripts/              工具（Python 标准库和 Node）
│   ├── init_film.py      建立影片文件夹
│   ├── make.py           静帧、样片和成片，各一条命令
│   ├── capture.mjs       在无头 Chrome 中逐帧渲染
│   ├── deal.py, dice.py  灵感卡和外部骰子
│   ├── direction.py      风格面板；配合 styles.py、asset_search.py、fonts.py
│   ├── mix.py            混音；master_audio.py（−14 LUFS）、tts.py（旁白）、beat_grid.py
│   ├── qc.py             质量检查；配合 scene_check.py、words_check.py
│   └── guard.py          守卫：当场执行规则（配合 hook.cjs，Claude Code）
├── templates/            新影片的文件和快速模式的起始页面
├── starter/              three.js 场景：八种画面风格、命名的运镜、文字层
├── styles/               58 份风格配方（51 份来自 lemo-opuscar，MIT；7 份为本套件自有）
├── docs/                 README 图片和字体库
└── tests/                测试套件，每次推送都在 Windows 和 Linux 上运行
```

套件建立的影片文件夹：

```text
my-film/
├── <片名>.mp4            成片
├── STATE.md              影片进度；每个新对话都从这里接着做
├── film.html             快速模式：影片本身，一页代码
├── ROADMAP.md, SCRIPT.md 电影模式：路线图和剧本；场景在 engine/ 中
├── refs/, research/      你的参考和调研
├── audio/, assets/       声音和下载的素材；许可证记在 LICENSES.csv
├── review/, renders/     检查帧和样片
└── tools/                套件工具在这部影片里的副本
```

**文件保存在哪里：** 每部影片都是一个独立文件夹（成片以 `<title>.mp4` 的形式放在它的最上层）。在不同影片之间延续使用的东西保存在 `~/.cinecode/` 中：你的 API 密钥（`keys.env`，只需输入一次）、保存的格式、口味日志和下载缓存。工具包自身的文件夹从不写入。

## 常见问题

**纯代码，还是混合？** 代码是核心：画面由代码生成，不产生模型费用。影片越长、越偏重事实，就会有越多真实素材在代码无法呈现真实事物的地方加入进来：智能体自己在开放档案馆（Wikimedia Commons、Internet Archive、NASA、各家博物馆）中找到的影像和照片，以及来自 Pixabay 的图库照片和视频（用你的免费密钥，只问一次），每一项都会连同授权登记并注明出处。声音方面，工具包推荐使用录制的配乐和现成的音效（免费的 CC0 素材库）；完全合成的声音是你可以选择的一个选项。你也可以加入自己的影像、照片和录音。如果你自己接入了图像或视频生成器（Higgsfield、fal 或其他），智能体只会在你要求时把它作为最后手段使用；它从不主动推荐。人脸在特写中以风格化或剪影的方式呈现效果最好。

**每部影片都要输入 API 密钥吗？** 不用。第一次需要旁白时输入一次即可：智能体会在你的文本编辑器中打开密钥文件，里面有一行空的 `GEMINI_API_KEY=`；把密钥粘贴在 `=` 后面，保存并关闭（或者在终端中运行 `python3 tools/keys.py set GEMINI_API_KEY`，输入时不会显示）。之后的每部影片都会使用它。你放在旧影片 `.env` 中的密钥，可以用 `keys.py import` 迁移过去。密钥绝不会进入影片文件夹或代码仓库。

**怎么知道它能做什么？** 直接问：“你能做什么？”（"neler yapabilirsin?"）。你会得到一份简短的菜单：短片、广告或产品视频、为你的歌做的音乐视频、像某个参考视频的影片、剪辑你自己的素材、用已保存的格式做新片、浏览各种风格。或者直接说出你想要什么（“为这首歌做一支音乐视频”）；智能体会选择合适的路线。

**该选哪种模式？** 想今天就拿到成片或需要频繁发布时，选快速模式；某一部作品必须做到最好时，选电影模式。智能体会根据你的目标推荐一种。

**做一部影片要多久？** 在快速模式中，30 秒的影片只需一次简短的会话：几个问题、一份方案、两个场景供你查看、一版快速草稿，然后是最终渲染（每一步几秒到几分钟）。在电影模式中，30 秒的影片通常需要几次会话：访谈和路线图几分钟，剧本和风格帧一次坐下来搞定，而在较新的 GPU 上渲染 30 秒影片只需几分钟。大部分时间花在你的意见上，而这正是重点所在。

**需要强大的 GPU 吗？** 任何较新的 Mac（Apple 芯片）或显卡驱动正常的 PC 就足够了。智能体会在开始时检查这一点（`capture.mjs --probe`）。如果无头 Chrome 中没有 GPU，渲染会退回到 CPU：用来测试没问题，渲染整部影片就太慢了。

**可以用我自己的参考吗？** 可以：把图片放进 `refs/`，把链接或带时间点的电影名写进 `refs/links.txt`。受版权保护的参考只用于氛围，绝不会出现在画面中。

**我的影片可以商用吗（广告、客户项目、可变现的频道）？** 就工具包而言，可以。它提供或找到的每款字体都采用允许商用的授权，无需在画面或简介中做任何标注（SIL OFL、Apache、MIT、Ubuntu Font Licence、CC0）；字体用于画面中，从不作为文件出售或分享。有四款精选字体来自 Fontshare（ITF Free Font License）：同样可免费商用，但需要你自己下载，且绝不能把文件转给他人；工具包会把所有字体文件排除在 git 之外。智能体找到的参考只用于氛围和形态；图像或声音只有在授权允许时才会进入影片，并登记在 `LICENSES.csv` 中。你自己的标志、品牌字体、影像和歌曲由你自行负责。开放的音乐和图像：工具包只采用公有领域、CC0 和 CC BY 素材，图像还包括 CC BY-SA（音乐优先 CC0），会记录每一项的授权，并在每部成片旁写好可放进视频简介的致谢；发布前请核对素材的来源页面，并把致谢文件与影片放在一起（如果 CC BY 音轨遭到 YouTube Content ID 声明，它就是你的回应依据）。发布影片的人对其授权负责；工具包按原样提供（MIT 许可证）。以上不构成法律建议。

**致谢写在哪里？** 写在视频的简介（YouTube）或帖子的文案（Instagram、TikTok、X）里，不要放在画面上。每部成片旁都会留下一个 `<title>-credits.txt`：原样粘贴即可。公有领域和 CC0 素材无需写明（文件里仍会简要列出）；CC BY 和 CC BY-SA 素材需要写上对应的那一行，文件中已附好授权链接。如果某个平台标记了某段音轨或某张图片，这个文件也就是你的回应依据。

**我的影片会存到哪里？** 存到你启动智能体时所在的文件夹：如果它是空的或只放着影片，每部影片会在那里拥有自己的子文件夹；否则（你的主文件夹、桌面、某个代码项目），智能体会在那里建一个 `Films` 文件夹，把所有影片都放进去。智能体会告诉你路径。下次在同一位置启动智能体，说“继续”就会按名称列出你的影片。 如果你没有选择文件夹就开始（Claude 应用里没有文件夹的对话），影片会存到你主文件夹里的影片文件夹，智能体会把对话移到这部影片的文件夹里，这样静帧、音乐和样片都能在对话中显示。

**我的影片在哪？需要 git 吗？** 成片会以 `<title>.mp4` 的形式复制到你的影片文件夹中，智能体会给你这个路径；你需要的只有这个文件。你完全不必碰 git：如果装了 git，智能体会为影片的文本文件保留一份本地历史（这样改坏了可以撤销）。不会上传任何东西，视频也不在其中。

**我喜欢某部影片，下一部能用同样的格式吗？** 可以。在成片之后说“保存格式”（"formatı kaydet"）；下次说“同样的格式”（"aynı formatta"）。风格、字体、声音、摄像风格和节奏都会保留，只会问你创意，场景和文字则为新创意重新创作。格式保存在你的电脑上（`~/.cinecode/formats`）。

**一部影片要用多少 token，怎么查看？** 一部影片就是一段很长的对话，智能体在其中写代码、渲染和检查：一部 30–60 秒的快速模式影片通常需要 100–250 步。每一步都会重新读取整个对话；其中大部分来自缓存，费用很低，但随着对话增长，每一步也会变大。所以当某个步骤完成、对话已经变长时，工具包会建议在新对话中继续；不会丢失任何东西，因为影片存在于它的文件之中。在影片文件夹中运行 `python3 tools/usage.py` 可以查看每个对话的 token 用量（Claude Code）。每个对话开头还会载入所有已安装技能的简短描述，以及所有已连接插件和连接器的工具定义（技能的完整说明只在使用时才加载）；关掉影片用不到的那些，每一步都会更便宜。

**支持哪些语言？** 智能体会用你的语言回复。除非你要求，否则字幕默认关闭（最多两种语言，上下叠放）。

**能离线使用吗？** 渲染、混音和各项检查都可以离线进行，快速模式起始模板（Canvas 2D、Web Audio）也一样；搜索需要联网（参考、音乐、首次下载字体和风格，之后会被缓存）。three.js 场景需要联网一次来获取库（或使用本地副本，见 `references/looks.md` §6）；`starter/index.html` 什么都不需要。

## 测试

在工具包文件夹中运行 `python3 -m unittest discover -s tests`；在前面加上 `CINECODE_BROWSER_TESTS=1` 即可运行真实的 Chrome 和 ffmpeg 测试。测试套件还会在每次推送时于 Windows（有和没有 Git 与 bash 两种情况）和 Ubuntu 上运行。如果遇到问题，请在 GitHub 上反馈。

## 致谢

由 Sarp Yıldız（[@sarpstar](https://github.com/sarpstar)）与 Claude 一起，在 Claude Code 和 Cursor 中制作。MIT 许可证，见 [LICENSE](LICENSE)。
基于 [three.js](https://github.com/mrdoob/three.js)（MIT）和 [pmndrs/postprocessing](https://github.com/pmndrs/postprocessing)（Zlib）构建，二者在渲染时加载，不随包分发。
部分想法受 [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)（MIT）启发。
角色工具包（`references/characters.md`）受 John Heibel 的 [ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) 启发；陈词滥调与色彩检查受对 [yihui-dev/awesome-opus5-5-videos](https://github.com/yihui-dev/awesome-opus5-5-videos) 中影片的研究启发。仅借鉴想法：未包含二者的任何代码、提示词或画面。
节拍网格方法，以及关于音乐视频、转场音效和动态文字的经验，遵循 [tuzhechen2005/opus-video-skills](https://github.com/tuzhechen2005/opus-video-skills)（MIT），并为本工具包重新编写。
风格库（`styles/`）即 LemoLab 的 [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) 中的风格配方（MIT，`styles/LICENSE-lemo-opuscar`），固定在某一次提交；其演示影片和引擎仅提供链接，不包含在内。`vox-explainer` 配方是工具包自己的；其镜头类型和审看经验遵循 [charlie947/motion-graphics-skills](https://github.com/charlie947/motion-graphics-skills)（MIT）。
以下内容同样为本工具包重新编写，均为 MIT：产品片镜头目录参照 [AbubakrChan/product-launch-motion](https://github.com/AbubakrChan/product-launch-motion)；节拍类型和剪辑理由参照 [cth9191/animate](https://github.com/cth9191/animate)；剪辑接缝规则、单帧跳变与循环检查、只在物体运动处加运动模糊、无声一句话测试以及社交平台封面帧参照 [howseen-ai/claude-motion-design](https://github.com/howseen-ai/claude-motion-design)；光线与镜头词汇参照 [showheyohtaki/motion-prompt](https://github.com/showheyohtaki/motion-prompt)。
运动原则（`references/motion.md`）借鉴了 [LottieFiles/motion-design-skill](https://github.com/LottieFiles/motion-design-skill)（MIT）和 [whaleyxbt/claude-motion](https://github.com/whaleyxbt/claude-motion)（MIT）的想法；UI 主视觉镜头语法（`references/craft.md` §8）借鉴了 [1weiho/cinematic-shot](https://github.com/1weiho/cinematic-shot)（MIT）的想法；逐帧精确的节奏借鉴了 [cth9191/animate](https://github.com/cth9191/animate)（MIT）；素材剪辑（`references/footage-edit.md`）中的停顿与重录阈值和逐词计时节拍借鉴了 [nateherkai/herk-edit-kit](https://github.com/nateherkai/herk-edit-kit)（MIT），随语音计时的图形密度借鉴了 [Barty-Bart/motion-graphics](https://github.com/Barty-Bart/motion-graphics)（MIT）。录制的乐器音色（`scripts/samples.py`）是 CC0 的 [Versilian Community Sample Library](https://github.com/sgossner/VCSL)，由 [Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15)（MIT）打包，按需获取，不随包分发；配方 `line-boil`、`liquid-motion`、`shape-morph`、`sticker-explainer` 和 `variety-captions` 以及评审团检查遵循其风格说明和审看流程，并为本工具包重新编写。对影片文字的检查（`scripts/words_check.py`）遵循 [blader/humanizer](https://github.com/blader/humanizer)（MIT）的模式类别和维基百科的 [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)，并配有土耳其语对应规则。除 lemo-opuscar 配方（依其 MIT 许可证收录）外，全部用我们自己的话写成；未复制任何代码或文字。可选字体来自 [Fontsource](https://fontsource.org)（代码为 MIT；每款字体保留各自的许可证，大多为 SIL OFL 1.1），在渲染时加载。`fonts.py` 在运行时读取 [Fontsource API](https://fontsource.org/docs/api) 和 [google/fonts](https://github.com/google/fonts) 的公开标签列表；二者均不随包分发。
录制的乐器音色均为 CC0：[Versilian Community Sample Library](https://github.com/sgossner/VCSL) 和 [Versilian Studios Chamber Orchestra 2 Community Edition](https://github.com/sgossner/VSCO-2-CE)，只在影片用到时分小块获取。
现成音效来自 [Kenney](https://kenney.nl) 的音频包（CC0），在影片首次需要时下载一次。
“环境要求”中推荐的免费土耳其语语音：EMA Lightning（Canberk Aslan）、VoxCPM2 Türkçe ses tasarımı（alexturkey）和 Ahenk（Özgür Güler）；感谢它们的作者。
代码仓库：[github.com/sarpstar/cinecode](https://github.com/sarpstar/cinecode)

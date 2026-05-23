---
name: website-to-video-with-script
description: 将网站转换为带文案的视频。每张幻灯片自动生成旁白文案，视频中同步显示字幕。基于 website-to-ppt-video 增强版。
---

# Website to Video with Script

将任意网站转换为带文案旁白的专业视频。每张幻灯片自动生成文案，视频中同步显示字幕。

## 与 website-to-ppt-video 的区别

| 特性 | website-to-ppt-video | website-to-video-with-script |
|------|---------------------|------------------------------|
| HTML PPT | ✅ | ✅ |
| MP4 视频 | ✅ | ✅ |
| 文案生成 | ❌ | ✅ 自动为每页生成旁白 |
| 字幕显示 | ❌ | ✅ 视频中显示字幕 |
| 文案文件 | ❌ | ✅ 输出 script.md |

## 使用方式

```bash
# 基础用法
/website-to-video-with-script https://example.com

# 指定文案风格
/website-to-video-with-script https://example.com --script-style professional

# 指定字幕位置
/website-to-video-with-script https://example.com --subtitle-position bottom

# 只生成文案，不渲染视频
/website-to-video-with-script https://example.com --script-only
```

## 详细流程

### Step 0: 检查依赖 ⛔ BLOCKING

```bash
which bun || echo "需要安装 bun"
npx hyperframes --help || echo "需要安装 hyperframes"
ffmpeg -version || echo "需要安装 FFmpeg"
```

### Step 1: 抓取网站内容

```bash
bun ~/.claude/skills/baoyu-url-to-markdown/scripts/vendor/baoyu-fetch/src/cli.ts \
  <URL> --output source.md --headless
```

### Step 2: 生成 HTML PPT + 文案

基于抓取的内容，同时生成：
1. **HTML PPT** - Reveal.js 格式演示文稿
2. **文案脚本** - 每张幻灯片的旁白文案

**文案生成规则**：
- 封面页：简短开场白（5-10字）
- 内容页：核心要点阐述（30-50字）
- 结束页：总结+行动号召（20-30字）

**文案风格**：

| 风格 | 说明 | 适用场景 |
|------|------|----------|
| `professional` | 专业正式 | 商务汇报、产品介绍 |
| `casual` | 轻松口语 | 社交媒体、知识分享 |
| `storytelling` | 故事化 | 品牌宣传、案例分享 |
| `educational` | 教育科普 | 教程、培训材料 |

### Step 3: 渲染带字幕的视频

使用 Hyperframes 渲染视频，字幕作为叠加层显示在每张幻灯片上。

**字幕样式**：

| 位置 | 说明 |
|------|------|
| `bottom` | 底部居中（默认） |
| `top` | 顶部居中 |
| `overlay` | 半透明覆盖层 |

**字幕动画**：
- 淡入显示
- 与幻灯片切换同步
- 支持多行文案

## 输出文件

```
{output-dir}/
├── source.md              # 网站内容
├── script.md              # 文案脚本（可独立使用）
├── presentation.html      # HTML PPT
└── video-project/
    ├── index.html         # 视频合成文件（含字幕）
    └── output.mp4         # 最终视频
```

## 文案脚本格式

```markdown
# 视频文案脚本

## P1 - 封面
**时间**: 0-5秒
**文案**: GitHub 最流行的十大 Skill，带你了解 Claude Code 生态全景。

## P2 - 概览
**时间**: 5-15秒
**文案**: 目前 SkillsMP 已有超过 70 万技能，最高安装量达 41.8 万，生态正在爆发式增长。

## P3 - Top 1-3
**时间**: 15-25秒
**文案**: 排名前三的是 Anthropic 官方技能集合、Vercel 的技能搜索引擎，以及 React 最佳实践。

...
```

## 参数选项

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--output` | 输出目录名 | 基于网站标题 |
| `--slides` | 幻灯片数量 | 8-12 |
| `--duration` | 每张幻灯片时长 | 10秒 |
| `--cover-duration` | 封面时长 | 5秒 |
| `--script-style` | 文案风格 | professional |
| `--subtitle-position` | 字幕位置 | bottom |
| `--subtitle-font-size` | 字幕字号 | 24px |
| `--script-only` | 只生成文案 | false |
| `--no-subtitle` | 不显示字幕 | false |
| `--style` | 视觉风格 | default |
| `--theme` | 配色主题 | blue |

## 文案风格详情

### professional（专业正式）
```
封面：欢迎观看本期内容，今天我们将深入探讨...
内容：首先，让我们来看第一个关键要点...
结束：感谢观看，如需了解更多信息，请访问...
```

### casual（轻松口语）
```
封面：嘿！今天来聊聊一个超火的话题...
内容：第一个要说的就是...
结束：好啦，今天就到这里，记得点赞关注哦！
```

### storytelling（故事化）
```
封面：在 AI 时代，有一个故事正在上演...
内容：故事要从这里说起...
结束：这个故事还在继续，你准备好了吗？
```

### educational（教育科普）
```
封面：本节课程将讲解...
内容：第一个知识点是...
结束：本节要点回顾：1...2...3...
```

## 示例

### 示例 1: 知识图谱网站

```bash
/website-to-video-with-script https://ghoulvspol.github.io/bank-knowledge-graph/
```

输出：
- 12 张幻灯片 + 12 段文案
- 带字幕的视频

### 示例 2: AI 投资网站

```bash
/website-to-video-with-script https://ghoulvspol.github.io/ai-stocks-site/ --script-style casual
```

输出：
- 9 张幻灯片 + 9 段口语化文案
- 轻松风格的视频

### 示例 3: 微信文章

```bash
/website-to-video-with-script https://mp.weixin.qq.com/s/xxx --script-style storytelling
```

输出：
- 故事化文案
- 叙事风格视频

## 技术实现

### 字幕叠加层

```html
<div class="subtitle-overlay clip" data-start="5" data-duration="10" data-track-index="10">
  <div class="subtitle-text">
    这里是字幕文案内容
  </div>
</div>
```

### 字幕样式

```css
.subtitle-overlay {
  position: absolute;
  bottom: 60px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 100;
  pointer-events: none;
}

.subtitle-text {
  background: rgba(0, 0, 0, 0.7);
  color: #fff;
  padding: 12px 24px;
  border-radius: 8px;
  font-size: 24px;
  max-width: 80%;
  text-align: center;
  line-height: 1.5;
}
```

### GSAP 动画

```javascript
// 字幕淡入
tl.from(".subtitle-text", { opacity: 0, y: 20, duration: 0.5 });

// 字幕淡出
tl.to(".subtitle-text", { opacity: 0, y: -20, duration: 0.5 });
```

## 工作流程图

```
网站 URL
    ↓
[Step 1] 抓取网站内容
    ↓
[Step 2] 生成 HTML PPT + 文案脚本
    ↓
[Step 3] 合成带字幕的视频
    ↓
MP4 文件 + script.md
```

## 常见问题

### Q: 文案太长怎么办？

A: 使用 `--script-style casual` 生成更简洁的文案，或手动编辑 `script.md`。

### Q: 字幕遮挡内容？

A: 使用 `--subtitle-position top` 将字幕移到顶部，或调整 `--subtitle-font-size`。

### Q: 如何自定义文案？

A: 编辑 `script.md` 文件后重新渲染视频。

### Q: 支持 TTS 语音吗？

A: 当前版本仅支持字幕显示，TTS 功能开发中。

## 相关技能

- `website-to-ppt-video` - 基础版（无文案）
- `baoyu-url-to-markdown` - 网站抓取
- `baoyu-imagine` - 图片生成
- `hyperframes` - 视频渲染

## 更新日志

### v1.0.0 (2026-05-23)
- 基于 website-to-ppt-video 增强
- 新增文案自动生成
- 新增字幕叠加显示
- 支持 4 种文案风格

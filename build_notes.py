#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成单页 HTML 笔记：扫描所有 */notes/*.md，输出 index.html。
以后新增笔记只需写新的 .md，再运行：python build_notes.py
"""

import re
from collections import OrderedDict
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
OUTPUT = ROOT / "index.html"
NOTES_GLOB = "**/notes/*.md"

MD_EXTENSIONS = ["tables", "fenced_code", "sane_lists"]


def list_notes():
    """返回 [(phase 目录名, md 路径), ...]，按相对路径排序保证稳定。"""
    notes = []
    for md in sorted(ROOT.glob(NOTES_GLOB)):
        rel = md.relative_to(ROOT)
        phase = rel.parts[0] if len(rel.parts) > 1 else ""
        notes.append((phase, md))
    return notes


def extract_title(text):
    """取首个一级标题作为笔记标题。"""
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else "未命名笔记"


def build_sidebar(notes, titles):
    """按 phase 分组生成左侧目录 HTML。"""
    groups = OrderedDict()
    for i, (phase, _) in enumerate(notes):
        groups.setdefault(phase, []).append((i, titles[i]))

    parts = []
    for phase, items in groups.items():
        parts.append('<div class="nav-group">')
        parts.append(f'<div class="nav-group-title">{phase}</div>')
        for idx, title in items:
            parts.append(f'<a class="nav-link" href="#note-{idx}">{title}</a>')
        parts.append("</div>")
    return "\n".join(parts)


def main():
    notes = list_notes()
    titles = []
    sections = []
    for i, (_, md) in enumerate(notes):
        text = md.read_text(encoding="utf-8")
        titles.append(extract_title(text))
        body = markdown.markdown(text, extensions=MD_EXTENSIONS)
        sections.append(f'<section class="note" id="note-{i}">\n{body}\n</section>')

    sidebar = build_sidebar(notes, titles)
    content = "\n\n".join(sections)

    html = TEMPLATE.replace("$SIDEBAR$", sidebar)
    html = html.replace("$CONTENT$", content)
    html = html.replace("$COUNT$", f"{len(notes)} 篇笔记")

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"已生成 {OUTPUT}（{len(notes)} 篇笔记）")


TEMPLATE = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>嵌入式算法学习笔记</title>
<style>
:root {
  --bg: #f6f7f9;
  --panel: #ffffff;
  --border: #e5e7eb;
  --text: #1f2937;
  --muted: #6b7280;
  --accent: #4f46e5;
  --accent-soft: #eef2ff;
  --code-bg: #f1f5f9;
  --warn-bg: #fffbeb;
  --warn-border: #f59e0b;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: -apple-system, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
  color: var(--text);
  background: var(--bg);
  line-height: 1.75;
}

/* ===== 侧边栏 ===== */
.sidebar {
  position: fixed;
  top: 0; left: 0; bottom: 0;
  width: 270px;
  background: var(--panel);
  border-right: 1px solid var(--border);
  overflow-y: auto;
  padding: 24px 16px;
}
.sidebar h1 {
  font-size: 17px;
  margin: 0 0 4px;
  color: var(--accent);
}
.sidebar .count {
  font-size: 12px;
  color: var(--muted);
  margin: 0 0 20px;
}
.nav-group { margin-bottom: 18px; }
.nav-group-title {
  font-size: 13px;
  font-weight: 600;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: .03em;
  margin-bottom: 6px;
  padding: 0 8px;
}
.nav-link {
  display: block;
  padding: 6px 8px;
  font-size: 14px;
  color: var(--text);
  text-decoration: none;
  border-radius: 6px;
}
.nav-link:hover { background: var(--accent-soft); color: var(--accent); }

/* ===== 内容区 ===== */
.content {
  margin-left: 270px;
  padding: 40px 48px 80px;
  max-width: 960px;
}
.note {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 32px 40px;
  margin-bottom: 28px;
}
.note h1 {
  margin-top: 0;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border);
  font-size: 24px;
}
.note h2 { font-size: 20px; margin-top: 28px; }
.note h3 { font-size: 16px; margin-top: 22px; color: var(--accent); }

/* ===== 代码块与行内代码 ===== */
pre {
  background: var(--code-bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px 16px;
  overflow-x: auto;
  font-size: 13.5px;
  line-height: 1.6;
}
pre code { font-family: "SFMono-Regular", Consolas, "Courier New", monospace; }
:not(pre) > code {
  background: var(--code-bg);
  padding: 2px 6px;
  border-radius: 4px;
  font-family: "SFMono-Regular", Consolas, "Courier New", monospace;
  font-size: 0.9em;
}

/* ===== 表格 ===== */
table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 14px; }
th, td { border: 1px solid var(--border); padding: 8px 12px; text-align: left; }
th { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
tr:nth-child(even) td { background: #fafafa; }

/* ===== 引用块（重点/警告） ===== */
blockquote {
  margin: 16px 0;
  padding: 10px 16px;
  background: var(--warn-bg);
  border-left: 4px solid var(--warn-border);
  border-radius: 0 8px 8px 0;
}
blockquote p { margin: 0; }

/* ===== 响应式 ===== */
@media (max-width: 768px) {
  .sidebar { position: static; width: auto; border-right: none; border-bottom: 1px solid var(--border); }
  .content { margin-left: 0; padding: 20px 16px; }
  .note { padding: 20px; }
}
</style>
</head>
<body>
<aside class="sidebar">
  <h1>嵌入式算法学习笔记</h1>
  <p class="count">$COUNT$</p>
$SIDEBAR$
</aside>
<main class="content">
$CONTENT$
</main>
</body>
</html>
"""


if __name__ == "__main__":
    main()

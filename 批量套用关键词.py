from pathlib import Path
import re

BASE = Path(__file__).parent
KEYWORD_FILE = BASE / "关键词.txt"

keywords = [x.strip() for x in KEYWORD_FILE.read_text(encoding="utf-8").splitlines() if x.strip()]
files = sorted(BASE.glob("wechat-*.md"))

if not keywords:
    raise SystemExit("错误：关键词.txt 为空，请一行一个关键词填写。")

for i, path in enumerate(files):
    text = path.read_text(encoding="utf-8")
    kw = keywords[i % len(keywords)]

    # 1. 同步替换所有【旧关键词】
    text = re.sub(r'【[^】]*】', f'【{kw}】', text)

    # 2. 同步替换正文小标题中的关键词（仅针对本模板的三个小标题）
    text = re.sub(r'(?m)^<h2>一、.*?常见情况</h2>$',
                  f'<h2>一、{kw}常见情况</h2>', text)
    text = re.sub(r'(?m)^<h2>二、.*?使用技巧</h2>$',
                  f'<h2>二、{kw}使用技巧</h2>', text)
    text = re.sub(r'(?m)^<h2>三、.*?注意事项</h2>$',
                  f'<h2>三、{kw}注意事项</h2>', text)

    # 3. 同步替换正文第一段主题关键词
    text = re.sub(r'(?m)^<p>围绕“.*?”这一主题，',
                  f'<p>围绕“{kw}”这一主题，', text)

    path.write_text(text, encoding="utf-8")

print(f"完成：{len(files)}篇文章，使用{len(keywords)}个关键词循环处理。")
print("每篇文章的 title、H1、正文小标题和主题段落已同步。")

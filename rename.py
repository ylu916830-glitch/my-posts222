import os
import re

count = 0
for filename in os.listdir('.'):
    # 只处理 md 文件，跳过 py 脚本
    if filename.endswith('.md'):
        file_path = os.path.join('.', filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # 1. 如果存在 --- 开头的 Front Matter 区块，剔除其中的 title、date、draft 行
            def clean_frontmatter(match):
                block = match.group(1)
                lines = block.splitlines()
                new_lines = []
                for line in lines:
                    # 匹配并过滤 title:、date:、draft: 开头的配置行
                    if re.match(r'^\s*(title|date|draft)\s*:', line, re.IGNORECASE):
                        continue
                    new_lines.append(line)
                return '---\n' + '\n'.join(new_lines) + '\n---'

            # 替换 --- 包裹的 Front Matter
            content = re.sub(r'^---\s*\n(.*?)\n---\s*\n', clean_frontmatter, content, flags=re.DOTALL)

            # 2. 删除正文中单独出现的 # 标题 或 标题: / 日期: / 草稿: / title: / date: / draft: 文本行
            lines = content.splitlines()
            cleaned_lines = []
            for line in lines:
                # 过滤 # 开头的标题行
                if re.match(r'^\s*#+\s+', line):
                    continue
                # 过滤单独出现的“标题:”、“日期:”、“草稿:”或“title:”、“date:”、“draft:”等行
                if re.match(r'^\s*(标题|日期|草稿|title|date|draft)\s*[:：]', line, re.IGNORECASE):
                    continue
                cleaned_lines.append(line)

            new_content = '\n'.join(cleaned_lines).lstrip()

            # 保存修改后的文件
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1

        except Exception as e:
            print(f"处理文件 {filename} 失败: {e}")

print(f"清理完成！已成功处理 {count} 篇文章正文。")
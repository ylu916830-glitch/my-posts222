import os
import re

for filename in os.listdir('.'):
    # 跳过 py 脚本和非 md 文件
    if filename.endswith('.md'):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            title = None
            # 逐行寻找第一行非空的文字作为标题
            for line in lines:
                line_str = line.strip()
                if line_str:
                    # 过滤开头的 # 号、--- 符号或 title: 标签
                    clean_line = re.sub(r'^(#+\s*|title:\s*|---\s*)', '', line_str, flags=re.IGNORECASE).strip()
                    if clean_line and clean_line != '---':
                        title = clean_line
                        break
            
            if title:
                # 过滤文件名中的非法字符
                clean_title = re.sub(r'[\\/:*?"<>|]', '', title)
                new_filename = f"{clean_title}.md"
                
                if new_filename != filename:
                    os.rename(filename, new_filename)
                    print(f"成功重命名: {filename} -> {new_filename}")
        except Exception as e:
            print(f"处理 {filename} 失败: {e}")

print("重命名处理完成！")
import os
import re

# 遍历当前目录下的所有 .md 文件
for filename in os.listdir('.'):
    if filename.endswith('.md'):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取文章的第一行标题（匹配 # 开头的标题）
            match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            if match:
                title = match.group(1).strip()
                # 去除文件名中的非法特殊字符
                clean_title = re.sub(r'[\\/:*?"<>|]', '', title)
                new_filename = f"{clean_title}.md"
                
                # 执行重命名
                if new_filename != filename:
                    os.rename(filename, new_filename)
                    print(f"已重命名: {filename} -> {new_filename}")
        except Exception as e:
            print(f"处理文件 {filename} 时出错: {e}")

print("所有文件重命名完成！")
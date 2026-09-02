import os
import re

for filename in os.listdir('.'):
    if filename.endswith('.md'):
        try:
            # 去掉文件名里的【和】符号
            new_filename = filename.replace('【', '').replace('】', '')
            
            if new_filename != filename:
                os.rename(filename, new_filename)
                print(f"已去括号: {filename} -> {new_filename}")
        except Exception as e:
            print(f"处理 {filename} 失败: {e}")

print("所有文件名中的【】符号已全部去除！")
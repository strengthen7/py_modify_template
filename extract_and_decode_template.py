# -*- coding: utf-8 -*-

import base64
import re
import sys


def extract_and_decode_template(input_path, output_path):
    with open(input_path, 'r') as template_file:
        # 读取模板文件内容
        template_content = template_file.read()

        # 使用正则表达式提取被 () 包裹的内容
        matches = re.findall(r'\((.*?)\)', template_content)
        if matches:
            with open(output_path, 'w') as output_file:
                for match in matches:
                    # Base64 解码提取的内容
                    decoded_content = base64.b64decode(match).decode("GBK")

                    # 将解码后的内容写入新文件
                    output_file.write(decoded_content + '\n')
        else:
            print("No matches found.")


if __name__ == "__main__":
    # 获取模板文件路径和输出文件路径
    sys_input_path = sys.argv[1]
    sys_output_path = sys.argv[2]

    # 提取并解码模板文件中被 () 包裹的内容并写入新文件
    extract_and_decode_template(sys_input_path, sys_output_path)

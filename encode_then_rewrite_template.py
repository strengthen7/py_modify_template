# -*- coding: utf-8 -*-


import base64
import sys


def encode_file(file_path):
    with open(file_path, 'rb') as file:
        # 读取文件内容
        file_content = file.read()
        # 使用base64编码,返回编码后的内容
        return base64.b64encode(file_content)


def replace_and_write_template(replacement, template_path, output_path, placeholder):
    with open(template_path, 'r') as template_file:
        # 读取模板文件内容
        template_content = template_file.read()

        # 替换占位符
        replaced_content = template_content.replace(placeholder, replacement)

        # 将替换后的内容写入新文件
        with open(output_path, 'w') as output_file:
            output_file.write(replaced_content)


if __name__ == "__main__":
    # 模板文件路径
    template_path = 'template.txt'
    # 占位符名称
    placeholder = '{BASE64_CONTENT}'

    # base64 编码文件
    encoded_content = encode_file(sys.argv[1])
    # 替换模板文件中的占位符并写入新文件
    replace_and_write_template(encoded_content.decode("GBK"), template_path, sys.argv[2], placeholder)

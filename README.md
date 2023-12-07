# py_modify_template

You can specify the format of the template file yourself and declare placeholders in the file.
</br>
You can use a combination of the following files or just use one of them alone.
## encode_then_rewrite_template.py

+ introduction: base64 encode the source file and then replace the placeholders in the template file with the encoded
  content
+ how-to-use: python encode_then_rewrite_template.py input.txt output.txt

## extract_and_decode_template.py

+ introduction: extracts the contents of () and writes it to a new file using base64 decoding
+ how-to-use: python extract_and_decode_template.py output.txt new_output.txt
  

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import base64

# 将图片转换成base64编码，并写入到文本文件
# 运行后可以打开base64.txt文件
# 全选然后复制
# 有两种方式可以将base64编码的图片加入到markdown
#     1. 直接加入，在要插入图片的位置输入，这是基础用法，一般编码很长很长，所以很影响编写时的体验
#        ![avatar](data:image/png;base64,此处是在base64.txt文件内复制的内容)
#     2. 高级用法，分两步
#        首先在要插入图片的位置输入![avatar][tagName]
#        然后在文章末尾输入[tagName]:data:image/png;base64,此处是在base64.txt文件内复制的内容

# 2021/06/23 yuankuosheng 亲测有效

f = open("4.png", 'rb')  # 二进制方式打开图文件
ls_f = base64.b64encode(f.read())  # 读取文件内容，转换为base64编码
f.close()

str_base64 = str(ls_f)  # 将格式转换为字符串

# 将编码写入到文本文件
f = open("base64.txt", 'w')

# str_base64包含前缀"b'"和后缀"'"
# 在添加到markdown时是不需要上面的前缀和后缀的
f.write(str_base64[2:-1])  # 将编码以字符串的形式写入到文件

f.close()

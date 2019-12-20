#!/usr/bin/env python
# -*- coding:utf-8 -*-
#写入w 先清空文件，后写入内容 a 文件末尾追加内容b
# f = open("D:\\software2\\python\\1911a\\songsong.txt","w",encoding="utf-8")
# #写入内容 用write  参数为字符串类型
# f.write("你好,世界\n")
#写入内容，参数为list类型
# f.writelines(["淞\n","dtgfsgf\n","54545454\n"])
# f.close()

#读取内容
# f = open("songsong.txt","r",encoding="utf-8")
# c = f.read()
# print(c)
# f.close()

#f = open("test.txt","r",encoding="utf-8")
#c = f.read()
#print(c)
#f.close()
#lines=f.readlines
#print(lines)
# with open("songsong.txt","r",encoding="utf-8")as f:
#     c = f.read()
#     print(c)
class product():
    size="6寸"
    def __init__(self,color):
        self.color=color

    def call(self):
        print("有一个未接电话")
    def send_message(self):
        print("有一条信息")
# phone1 = product("白色")
# print(phone1.color)
# print(phone1.size)
# phone1.call()
#
# phone1 = product("黑色")
# print(phone1.color)
# print(phone1.size)
# phone1.send_message()

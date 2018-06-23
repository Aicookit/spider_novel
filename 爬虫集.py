#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@qq.com
@software: garner
@file: 爬虫集.py
@time: 2018/5/29/029 21:42
@desc:
'''
#0.轻松获取一个网页源代码
# import urllib.request
# response=urllib.request.urlopen('https://www.fliggy.com')
# text=response.read().decode('utf-8')
# print(text)
# print(type(text))

#1.判断超时异常
# import urllib.request
# import urllib.error
# import socket
#
# try:
#     response=urllib.request.urlopen('https://www.fliggy.com',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

#2.Request类，这里不是resquest方法
#Request(url,data=None,headers={},orgin_req_host=None,unverfiable=False,method=None)可以传更多参数，更有实际用处。
# import urllib.request
# request=urllib.request.Request('https://www.fliggy.com')
# response=urllib.request.urlopen(request)
# text=response.read().decode('utf-8')
# print(text)

#豆瓣小测
import urllib.request
# 1.def now_movie():
#     response=urllib.request.urlopen(url)
#     text=response.read().decode('utf-8')
#     print(text)
#2.第三方库requests
# import requests
# def now_movie():
#     url = 'https://movie.douban.com/'
#     response=requests.get(url)
#     print(response.cookies)
#     print(response.status_code)
#     print(response.text)

# if __name__ == '__main__':
#     now_movie()
#2.1 请求网页头部（headers）等信息#
# import requests
# url='http://httpbin.org/get'
# req=requests.get(url)
# print(req.text)
# print(type(req.text))   #str类型，但是是json格式的，想要得到字典类型，
# print(req.json())     #就使用json()方法
# print(type(req.json()))
# import requests
# from bs4 import BeautifulSoup
# url='http://news.sina.com.cn/photo/rel/csjsy07/399/'
# req=requests.get(url)
# req.encoding=req.apparent_encoding      #抛出异常，看网页是否接收
# text=req.text
# soup=BeautifulSoup(text,'html.parser')
# list=soup.find_all('img',{'class':'b1'})
# for i in list:
#     i=i['src']
#     # print(i)
#     f=[]
#html中的图片：<img src="http://image2.sina.com.cn/dy/c/p/2007-01-18/" \
#          "U1565P1T1D12074859F21DT20070118220227_sw160.JPG" class="b1">
# 然后怎么保存这些图片呢？把它们放进电脑进行储存?据说很简单
#     file=open('E:\英雄.txt','w',encoding='utf-8')
#     file.write(i)
# 现在还不知道怎么批量保存图片，下次来（！还没成功！）
# params参数、关键词
# #再来一次
###正则表达式演练：
# import re
# content='Hello 1234567 World_This is a Regex Demo'
# print(len(content))
# result=re.match('^Hello\s(\d+)\sW',content)
# print(result)                   #得到匹配的字符串
# print(result.group())           #输出完整的匹配结果，括号内默认为0
# print(result.group(1))          #输出（）内包含的匹配结果
# print(result.span())            #能够获取匹配的长度
###万能正则式演示
# import re
# content='Hello 1234567 World_This is a Regex Demo'
# # # result=re.match('^Hello.*Demo$',content)        # .*为贪婪模式
# # # print(result)
# # # print(result.group())
# # # print(result.span())
# # result=re.match('^He.*(\d+)\sW',content)
# # print(result.group())
# # print(result.group(1))   #结果只能匹配到 7 ，因为.*要尽可能多的匹配，\d+ 至少匹配到一个数字
# result=re.match('^He.*?(\d+)\sW',content)
# print(result.group())
# print(result.group(1))
#对于末尾的匹配,非贪婪和贪婪模式的区别
#如：我想要This is a Regex Demo
# import re
# content='Hello 1234567 World_This is a Regex Demo'
# result=re.match('^He.*?World_(.*?)',content)  #这里使用非贪婪模式就不能获得末尾的This is Regex Demo
# print(result.group())
# print(result.group(1))
# result=re.match('^He.*?World_(.*)',content)     #贪婪模式.*能尽可能多的匹配，所以就能得到我们想要的
# print(result.group())
# print(result.group(1))


# ###下面来看看 有换行符的怎么匹配，re.S为修饰符
# #想获得http://image2.sina.com.cn/dy/c/p/2007-01-18/
# import re
# content='<img src="http://image2.sina.com.cn/dy/c/p/2007-01-18/" \
#          "U1565P1T1D12074859F21DT20070118220227_sw160.JPG" class="b1">'
# result=re.match('^<img\ssrc="(.*?)".*?.JPG',content ,re.S)
# print(result)                   #得到你匹配的所有
# print(result.group(1))          #得到你匹配所以中的（）括号内的
###正则re的第二个方法search(),更方便，可以从字符串任意位置进行匹配，
###而不必像match()方法那样只能从开头开始匹配，下面改一下字符串试一下
###获取World_This is a Regex Demo为例
# import re
# content='Welcome,Hello 1234567 World_This is a Regex Demo'
# # result=re.match('Hello.*?World_(.*)',content)
# # print(result.group())                       #结果显示None
# result=re.search('Hello.*?World_(.*)',content)
# print(result.group())
# print(result.group(1))                         #这里就可以显示结果了
###去除匹配sub()方法
import re
content='abcde'
result=re.sub('ab|cd','',content)
print(result)strip













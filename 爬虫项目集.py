#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@qq.com
@software: garner
@file: 爬虫项目集.py
@time: 2018/5/30/030 18:31
@desc:
'''
#项目一（初级）：爬取王者荣耀英雄图片并保存文件E:
# import os
# import re
# import requests
# url="http://pvp.qq.com/web201605/herolist.shtml"
# headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0)"
#                           " Gecko/20100101 Firefox/59.0"
#             }
# rep=requests.get(url,headers)
# text=rep.content.decode('gbk')
# # print(text)
# content=re.compile('<a href=.*?><img\ssrc="(.*?)".*?>(.*?)</a>',re.S)
# results=re.findall(content,text)
# print(type(results))
# for result in results:
#
#         path="E:\王者英雄"
#         if not os.path.exists(path):
#             os.makedirs(path)
#         file=path+'/'+result[1]+'.png'
#         with open(file,'w')as f:
#             f.write(result[0])
#             f.close() ##成功爬取并已保存！存在的问题：图片不能打开，说文件格式不对或已破损。
##需要改进成面向对象的形式
# url='http://lol.qq.com/web201310/info-heros.shtml'
# headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
# compile=<li><a href="info-defail.shtml?id=Aatrox" title="暗裔剑魔 亚托克斯"><img src="http://ossweb-img.qq.com/images/lol/img/champion/Aatrox.png" alt="暗裔剑魔 亚托克斯"><p>暗裔剑魔</p><span class="sbg"><i class="commspr commico-search"></i></span></a></li>
#目标：获取英雄图片和称号，称号建立成文文件夹，图片保存在文件夹之内
import os
import re
import requests
import gzip
class Hero_Spider(object):
    def __init__(self):
        self.base_url='http://lol.qq.com/'
    def get_content(self):
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        req=requests.get(self.base_url+'web201310/info-heros.shtml',headers)
        text=req.content.decode('gbk')

        pattern=re.compile('<img src="(.*?)"\salt="(.*?)">',re.S)
        results=re.findall(pattern,text)

    def saveFile(self,down_url):
        path='E:\撸啊撸'
        if not os.path.exists(path):
            os.makedirs(path)
        data=requests.get(down_url[1],stream=True)
        file="path+'/'+down_url[0]+'.png'"
        with open(file,'wb')as f:
            f.write(down_url[0])
            f.close()

if __name__ == '__main__':
    a=Hero_Spider()
    a.get_content()
    a.get_content()






#!/usr/bin/env python3
# encoding: utf-8
from urllib import request
import re
import os

class TwoDogSpider(object):

    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.start='/104/'
        self.param='104326/'
        self.list=[]
        self.file_path='F:\SpidersWord\二狗的人生.txt'
    def get_page(self):
        url='http://www.shuge.net/html'+self.start+self.param
        req=request.Request(url,headers=self.headers)
        response=request.urlopen(req)
        page=response.read().decode('utf-8')
        return page

    def get_info(self):
        page=self.get_page()
        content=re.sub('<dt>.*?正文|</dt>|<dd>|</dd>','',page)
        result=re.findall('<a style="" href="(.*?)">(.*?)</a>',content,re.S)

        for item in result:
            self.list.append([item[0],item[1]])

    def write_in(self):
        print('开始抓取文件。。。')
        file=open(self.file_path,'w',encoding='utf-8')
        try:
            for item in self.list:
                file.write('文章章节：'+item[1]+'\r\n')
                file.write('文章内容地址：'+item[0]+'\r\n')
            print('文件写入完毕！')
        except Exception as e:
            print(e)
        finally:
            file.close()

    def main(self):
        print('爬虫爬去二狗的人生正式开始囖！')
        self.get_info()
        self.write_in()
        print('这个爬虫就爬完了，请下次再来唷！')
twodogsSpider=TwoDogSpider()
twodogsSpider.main()
###################################################################################2
#保存入数据库
from urllib import request
import re
import pymysql

class TwoDogSpider(object):

    def __init__(self):
        self.headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        self.start='/104/'
        self.param='104326/'
        self.list=[]
        self.file_path='F:\SpidersWord'
    def get_page(self):
        url='http://www.shuge.net/html'+self.start+self.param
        req=request.Request(url,headers=self.headers)
        response=request.urlopen(req)
        page=response.read().decode('utf-8')
        return page

    def get_info(self):
        page=self.get_page()
        content=re.sub('<dt>.*?正文|</dt>|<dd>|</dd>','',page)
        result=re.findall('<a style="" href="(.*?)">(.*?)</a>',content,re.S)

        for item in result:
            self.list.append([item[0],item[1]])


    def insert_into_mysql(self):
        root='root'
        password='123456'
        db=pymysql.connect("localhost",root,password,'mydatabase1',charset='utf8')
        print('连接上了')
        cursor=db.cursor()

        insert_str="insert into twodogs(title,story)values('%s','%s')"
        try:
            for item in self.list:
                insert_sql = insert_str % (item[1], item[0])
                if cursor.execute(insert_sql):
                    db.commit()
                    print('成功插入')
                else:
                    print('插入失败')
        except Exception as e:
            print(e)

    def main(self):
        print('爬虫爬去二狗的人生正式开始囖！')
        self.get_info()
        self.insert_into_mysql()
        print('这个爬虫爬完了，请下次再来唷！')
twodogsSpider=TwoDogSpider()
twodogsSpider.main()







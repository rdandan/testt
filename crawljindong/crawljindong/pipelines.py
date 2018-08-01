# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CrawljindongPipeline(object):
    def process_item(self, item, spider):
        return item

import MySQLdb
import MySQLdb.cursors
from  urllib import request
import requests
import re
import redis

class Writedb():
    def __init__(self):
        # 连接数据库
        self.conn = MySQLdb.connect('localhost', 'root', '12345', 'python77', charset='utf8', use_unicode=True)
        self.mycursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql="insert into jd_scrapy(pname,price,commit_t,shop) VALUES ('"+item['pname']+"','"+item['price']+"','"+item['commit']+"','"+item['shop']+"')"
        self.mycursor.execute(sql)
        self.conn.commit()


class Getpname():
    def __init__(self):
        # 连接数据库
        self.conn = MySQLdb.connect('localhost', 'root', '12345', 'python77', charset='utf8', use_unicode=True)
        self.mycursor = self.conn.cursor()
        con_pool = redis.ConnectionPool(host='127.0.0.1', port=6379,password='12345')
        self.r = redis.Redis(connection_pool=con_pool)

    def getname(self):
        sql = "SELECT pname FROM jd_scrapy"
        self.mycursor.execute(sql)
        # self.conn.commit()
        random=self.mycursor.fetchall()
        for i in random:
            if '华为'in i[0]:
                self.r.hincrby('phone','huawei',1)
            elif '荣耀' in i[0]:
                self.r.hincrby('phone', 'huawei', 1)
            elif '小米' in i[0]:
                self.r.hincrby('phone','xiaomi', 1)
            elif 'iPhone'in i[0]:
                self.r.hincrby('phone','iphone',1)
            elif 'Apple'in i[0]:
                self.r.hincrby('phone','iphone',1)
            elif'vivo'in i[0]:
                self.r.hincrby('phone','vivo',1)
            elif'OPPO'in i[0]:
                self.r.hincrby('phone','oppo',1)
            elif'魅族'in i[0]:
                self.r.hincrby('phone','meizu', 1)
            else:
                self.r.hincrby('phone','qita', 1)
        # print(random)

    def show(self):
        return self.r.hgetall('phone')

if __name__ == '__main__':
    a=Getpname()
    a.getname()
    print(a.show())

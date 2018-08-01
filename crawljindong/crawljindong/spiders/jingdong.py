# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from crawljindong.items import *
'''
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from selenium import webdriver
from  my0722homework.items import JdItem
import pymysql
import redis
import re




class JdSpider(CrawlSpider):
    name = 'jd'
    allowed_domains = ['jd.com']
    # start_urls = ['http://jd.com/']
    start_urls = ['https://list.jd.com/list.html?cat=9987,653,655&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main']

    rules = (
        Rule(LinkExtractor(allow=r'&sort=sort_rank_asc&trans=1&JL=6_0_0'), callback='parse_item', follow=True),
    )



    # def dbpymysql(self,describe1,comment,price,shopname):
    #     print('进入数据库了')
    #     print(describe1,comment,price,shopname)
    #     conn = pymysql.connect(host="localhost", port=3306, user="root", password="liuzhiyu", db="python77",
    #                            charset="utf8")
    #     cursor = conn.cursor()
    #     sql = "insert into phone(describe1,comment,price,shopname) values(%s,%s,%s,%s)"
    #     cursor.execute(sql,(describe1,comment,price,shopname))
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #
    # def dbredis(self,name,comment):
    #     connpool = redis.ConnectionPool(host='127.0.0.1', password='123456', port=6379)
    #     r = redis.Redis(connection_pool=connpool)
    #     r.set(name, comment)
        # r.hset('phone',name,comment)
        # if '万' in comment:
        #     num=int(re.findall('(.*?)万',comment))
        #     print('评论数:',num)




    def parse_item(self, response):
        driver=webdriver.Chrome()
        html=driver.get(response.url)
        # print('responseresponseresponseresponseresponseresponse',response.url)
        i = {}
        # '''
        # //a[@target='_blank']/em 手机描述   //strong[@class="J_price"]/i
        #
        # '''
        # describe=driver.find_elements_by_xpath('//li[@class="gl-item"]/div/div[4]/a/em')
        # des=[d.text for d in describe]
        # # print(len(des))
        # # print('desdesdesdesdes:',des)
'''
class JingdongSpider(CrawlSpider):
    name = 'jingdong'
    allowed_domains = ['list.jd.com']
    start_urls = ['http://list.jd.com/list.html?cat=9987,653,655/&page=1']
    driver = webdriver.Firefox()
    driver.get('https://list.jd.com/list.html?cat=9987,653,655&page=1')
    num = 1
    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), callback='parse', follow=True),
        #https://list.jd.com/list.html?cat=9987,653,655&page=2&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main
        #/list.html?cat=9987,653,655&page=2&sort=sort_rank_asc&trans=1&JL=6_0_0
        #http://list.jd.com/list.html?cat=9987,653,655&page=3&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=6#J_main
        # Rule(LinkExtractor(allow=(r'page=\d+.*?'),callback='parse',follow=True)
        #http://list.jd.com/list.html?cat=9987,653,655&page=2&sort=sort_rank_asc&trans=1&JL=6_0_0&ms=6#J_main
    )

    def parse(self, response):
        content_list = self.driver.find_elements_by_xpath('//ul[@class="gl-warp clearfix"]/li[@class="gl-item"]')
        pname = response.xpath('//a[@target="_blank"]/em/text()').extract()
        for i, j in zip(content_list, pname):
            # print(i.text)
            j = j.replace(' ', '')
            j = j.replace('\n', '')
            content = JDItem()
            content['pname'] = j
            content['price'] = i.find_element_by_xpath(".//div[@class='p-price']").text
            # content['title'] = i.find_element_by_xpath('.//div[@class="p-name p-name-type3"]').text
            content['commit'] = i.find_element_by_xpath(".//div[@class='p-commit']/strong/a").text
            content['shop'] = i.find_element_by_xpath(".//div[@class='p-shop']").text

            print(content)
            yield content
            # list.append(content)
        next_url = self.driver.find_elements_by_xpath("//a[@class='pn-next']")
        next_url = next_url[0] if len(next_url) > 0 else None
        if next_url is not None:
            next_url.click()
            self.num += 1
            # yield Req(url=next_url, callback=self.parse, dont_filter=True)
            # print(num)
'''
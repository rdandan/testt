# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawljindongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class JDItem(scrapy.Item):
    pname=scrapy.Field() #scrapy特殊方法 域
    price = scrapy.Field()
    commit = scrapy.Field()
    shop = scrapy.Field()



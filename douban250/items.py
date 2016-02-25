# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Douban250Item1(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 电影名
    rank = scrapy.Field()   # 电影排名
    link = scrapy.Field()   # 电影链接
    content = scrapy.Field()  # 电影简介

class Douban250Item2(scrapy.Item):
    url = scrapy.Field()  #
    content = scrapy.Field()  # 电影简介
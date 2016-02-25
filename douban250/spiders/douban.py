# -*- coding: utf-8 -*-
from urlparse import urljoin

import scrapy
from douban250.items import Douban250Item1, Douban250Item2


class DouBan(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):  # 获取各个主页信息
        block = response.css('.grid_view li .item')
        for info in block:
            item = Douban250Item()  # fuck,漏了Item
            item['title'] = info.css('.pic a img::attr(alt)').extract()  # 漏了img会导致电影名读不出来
            item['rank'] = info.css('.pic em::text').extract()
            item['link'] = info.css('.pic a::attr(href)').extract()
            yield item
            url = info.css('.pic a::attr(href)').extract()[0]  # url已经出来了
            # print '@@'*20
            # print url
            yield scrapy.Request(url, callback=self.parse_movie)

        next_page = response.css('.paginator .next a::attr(href)')
        if next_page:  # 如果有下一页继续采用parse_main去处理
            url = response.urljoin(next_page[0].extract())
            # print '###'*30
            yield scrapy.Request(url, self.parse)  # 所以要返回parse_main函数去去处理

    def parse_movie(self, response):  # 获取各个电影简介，爬出的结构不对，可以通过每个电影的详细页是否有url链接去判断
        movie = response.css('#link-report')
        for info in movie:
            # print '$$$'*30
            item = Douban250Item2()
            item['content'] = info.css('span[property]::text').extract()[0].strip('\n ')
            yield item





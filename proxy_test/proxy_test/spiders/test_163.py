# -*- coding: utf-8 -*-
import scrapy


class Test163Spider(scrapy.Spider):
    name = 'test_163'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        print(response.text)

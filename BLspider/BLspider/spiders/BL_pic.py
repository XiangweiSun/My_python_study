# -*- coding: utf-8 -*-

import scrapy
from BLspider.items import BlspiderItem

class BlPicSpider(scrapy.Spider):

    name = 'BL_pic'
    allowed_domains = ['www.beautyleg.com']

    BASE_URL = 'http://www.beautyleg.com/photo/show.php?no='
    start_index = 51
    MAX_index = 100

    start_urls = [BASE_URL + str(start_index)]


    def parse(self, response):

        if self.start_index > 100:
            return

        img_urls = response.xpath('/html/body/table[2]//a/@href').extract()
        item = BlspiderItem()

        for img in img_urls:
            item['IMG_URL'] = img
            yield item

        self.start_index += 1
        URL = 'http://www.beautyleg.com/photo/show.php?no=' + str(self.start_index)

        yield scrapy.Request(URL, callback = self.parse)
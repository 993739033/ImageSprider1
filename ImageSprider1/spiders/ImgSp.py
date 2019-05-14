import json

import scrapy
from ImageSprider1.items import ImgSprider


class ImgSp(scrapy.Spider):
    name = "ImgSprider"
    allowed_domains = ["unsplash.com"]

    def start_requests(self):
        for i in range(1, 4):
            url = 'https://unsplash.com/napi/photos?per_page=12&page=' + str(i)
            req = scrapy.Request(url=url, callback=self.parse)
            yield req

    def parse(self, response):
        item = ImgSprider()
        req = response.text
        html = json.loads(req)
        for e in html:
            item["img_url"] = e["urls"]["small"]
            item["img_title"] = e["id"]
            print(item["img_url"])
            yield item
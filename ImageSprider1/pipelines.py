# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import time

class Imagesprider1Pipeline(object):
    def process_item(self, item, spider):
        return item

class Img_Down(object):
    def process_item(self, item, spider):
        req =requests.get(url=item["img_url"])
        # 用时间函数当随机名称
        x = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        file_url =r"C:/Users/gjt66/Desktop/临时下载文件/"+item["img_title"]+x+".jpg"
        print("download>>>>")
        with open(file_url,"wb") as f:
            f.write(req.content)

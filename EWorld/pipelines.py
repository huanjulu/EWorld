# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
from scrapy import log

from scrapy.exceptions import DropItem

class EworldPipeline(object):
    def process_item(self, item, spider):

        self.collection.insert(dict(item))
        return item

    def __init__(self) -> None:
        # connection = pymongo.MongoClient(
        #     settings['MONGODB_SERVER'],
        #     settings['MONGODB_PORT']
        # )
        # db = connection[settings['MONGODB_DB']]
        # self.collection = db[settings['MONGODB_COLLECTION']]
        client = pymongo.MongoClient(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = client[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]






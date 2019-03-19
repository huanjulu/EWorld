# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EworldItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    world = scrapy.Field()
    definition = scrapy.Field()
    pronunciation = scrapy.Field()


pass


class CategoryBookItem(scrapy.Item):
    book_image = scrapy.Field()
    book_name = scrapy.Field()
    world_number = scrapy.Field()
    author = scrapy.Field()
    book_url = scrapy.Field()
pass

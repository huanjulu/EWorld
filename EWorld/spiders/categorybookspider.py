import scrapy

from EWorld.items import EworldItem
from EWorld.items import CategoryBookItem
import random
from scrapy import Request
from scrapy.selector import Selector


class CategoryBookSpider(scrapy.Spider):
    name = "categorybook"
    start_urls = [
        'https://www.shanbay.com/wordbook/category/20/'
    ]

    allowed_domains = ["https://shanbay.com"]

    def duplicateNoneString(self, list):
        list = [x.strip() for x in list if x.strip()]
        return list

    pass

    def parse_each_category(self, response):
        pass

    pass

    def parse(self, response):
        print(response.url)
        allbooks = []

        # Test
        row = response.xpath('//div[contains(@class, "wordbook-basic-info span")]')[0]
        # row = random.choice(list)
        itemBook = CategoryBookItem()
        itemBook['book_name'] = row.xpath('.//div[contains(@class, "wordbook-title")]/a/text()')[0].extract()
        authorlist = row.xpath('.//div[contains(@class, "wordbook-owner")]/text()').extract()
        itemBook['author'] = self.duplicateNoneString(authorlist)[0]
        numberlist = row.xpath('.//div[contains(@class, "wordbook-count")]/text()').extract()
        itemBook['world_number'] = self.duplicateNoneString(numberlist)[0]
        itemBook['book_url'] = self.allowed_domains[0] + row.xpath(
            '..//div[contains(@class, "wordbook-cover span thumbnail")]/a/@href')[0].extract()
        allbooks.append(itemBook)
        for book in allbooks:
            print(book['book_url'])
            yield scrapy.Request(url=book['book_url'], meta={"item_1": book}, dont_filter=True,
                                 callback=self.parse_book_unit)

        # for row in response.xpath('//div[contains(@class, "wordbook-basic-info span")]'):
        #     itemBook = CategoryBookItem()
        #     itemBook['book_name'] = row.xpath('.//div[contains(@class, "wordbook-title")]/a/text()')[0].extract()
        #     authorlist = row.xpath('.//div[contains(@class, "wordbook-owner")]/text()').extract()
        #     itemBook['author'] = self.duplicateNoneString(authorlist)[0]
        #     numberlist = row.xpath('.//div[contains(@class, "wordbook-count")]/text()').extract()
        #     itemBook['world_number'] = self.duplicateNoneString(numberlist)[0]
        #     itemBook['book_url'] = self.allowed_domains[0] + row.xpath(
        #         '..//div[contains(@class, "wordbook-cover span thumbnail")]/a/@href')[0].extract()
        #     allbooks.append(itemBook)
        # for book in allbooks:
        #     print(book['book_url'])
        #     yield scrapy.Request(url=book['book_url'], meta={"item_1": book}, dont_filter=True,
        #                          callback=self.parse_book_unit)

    def parse_book_unit(self, response):

        print('---------------------------------------   xpath each unit    -------------------')
        worldlist = response.xpath('//td[contains (@class, "wordbook-wordlist-name")]/a/@href')
        allUnits = []
        for unit in worldlist:
            allUnits.append(self.allowed_domains[0] + unit.extract())
        for unit in allUnits:
            yield scrapy.Request(url=unit, meta={"item_1": unit}, dont_filter=True,
                                 callback=self.parse_unit_page)

    # for i in range(1, 10):
    #     url = 'https://www.shanbay.com/wordlist/202/16306/?page=%s' % i
    #     yield Request(url)
    def parse_unit_page(self, response):
        each_unit_url = response.meta['item_1']
        print('---------------------------------------   each_unit_url    -------------------')
        try:
            for i in range(1, 15):
                url = each_unit_url + "?page=%s" % i
                yield scrapy.Request(url=url, dont_filter=True,
                                     callback=self.parse_detail_page)
        except Exception as i:
            print(i)

    def parse_detail_page(self, response):
        worldLists = response.xpath('//tr[contains(@class,"row")]')
        for each in worldLists:
            item = EworldItem()
            item['world'] = each.xpath('td[contains(@class,"span2")]/strong/text()')[0].extract()
            item['definition'] = each.xpath('td[contains(@class,"span10")]/text()')[0].extract()
            item['pronunciation'] = 'NULL'
            print(item)
            yield item
        pass

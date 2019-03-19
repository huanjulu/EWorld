import scrapy

from EWorld.items import EworldItem
from scrapy import Request
from scrapy.selector import Selector


class WorldSpider(scrapy.Spider):
    name = "shanbay"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
    }
    allowed_domains = ["shanbay.com"]

    def start_requests(self):
        pages = []
        for i in range(1, 10):
            url = 'https://www.shanbay.com/wordlist/202/16306/?page=%s' % i
            yield Request(url)

    def parse(self, response):
        worldLists = response.xpath('//tr[contains(@class,"row")]')
        for each in worldLists:
            item = EworldItem()
            item['world'] = each.xpath('td[contains(@class,"span2")]/strong/text()')[0].extract()
            item['definition'] = each.xpath('td[contains(@class,"span10")]/text()')[0].extract()
            item['pronunciation'] = 'NULL'
            yield item
        pass

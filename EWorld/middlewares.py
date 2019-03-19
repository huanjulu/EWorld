# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
# from .porxy import PROXIES
from .agent import AGENTS

class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent



# class CustomHttpProxyMiddleware(object):
#
#
#     def process_request(self, request, spider):
#         p = random.choice(PROXIES)
#         try:
#             request.meta['proxy'] = 'http://%s' % p['ip_port']
#         except Exception as e:
#             print("Error" + e.args)


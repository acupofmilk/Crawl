# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from ..items import KuaidailiItem


class GetIpSpider(scrapy.Spider):
    name = 'get_ip'
    allowed_domains = ['www.kuaidaili.com/free']
    def start_requests(self):
        prefix_url = 'https://www.kuaidaili.com/free/inha/'
        for i in range(1,4):    # 爬取前三页
            url = prefix_url + str(i)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        html = response.text
        soup = BeautifulSoup(html, "html5lib")
        nodes = soup.select('tbody > tr')
        item = KuaidailiItem()

        for node in nodes:
            data = node('td')
            item['IP'] = data[0].get_text()
            item['Port'] = data[1].get_text()
            item['Anonymity'] = data[2].get_text()
            item['Type'] = data[3].get_text()
            yield item



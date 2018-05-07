#coding=utf-8
import scrapy
from tutorial.items import TutorialItem
class czuSpider(scrapy.Spider):
    name = "czu"
    allowed_domains = ["czu.cn"]
    start_urls = [
        "http://www.czu.cn/6/list1.htm"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul[@class="wp_article_list"]/li/div/span[@class="Article_Title"]'):
            item = TutorialItem()
            item['title'] = sel.xpath('a/@title').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item

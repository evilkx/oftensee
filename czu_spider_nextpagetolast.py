#coding=utf-8                                           //使输出json文档中文输出正常，不是ascii格式
import scrapy
from scrapy.http import Request
from tutorial.items import TutorialItem
class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["czu.cn"]
    start_urls = [
        "http://www.czu.cn/6/list1.htm"
    ]
    url = "http://www.czu.cn"
    def parse(self, response):
        for sel in response.xpath('//ul[@class="wp_article_list"]/li/div/span[@class="Article_Title"]'):
            item = TutorialItem()
            item['title'] = sel.xpath('a/@title').extract()
            item['link'] = sel.xpath('a/@href').extract()
            yield item

                                                                            // 翻页爬取
        nextlink = response.xpath('//*[@id="wp_paging_w1205"]/ul/li/a[@class="next"]/@href').extract()
        print("##############")
        print(nextlink)
        print("##############")
        if nextlink:
            link = nextlink[0]
            print("##############")
            print(self.url + link)
            print("##############")

            yield Request(self.url + link, callback=self.parse)

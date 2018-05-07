import scrapy


class TutorialItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    pass

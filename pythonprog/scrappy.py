import scrapy

class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
      for sel in response.xpath('//ul/li'):
         title = sel.xpath('a/text()').extract()
         link = sel.xpath('a/@href').extract()
         desc = sel.xpath('text()').extract()
         print (title,link,desc)
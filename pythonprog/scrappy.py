import scrapy

class PostSpider(scrapy.Spider):
  name="PostSpider"
  allowed_domains=["medium.com"]
  start_url=["https://medium.com/search?q="]
  
  def parse(self, response):
    #for post in response.xpath():
    for post in response.css():
      yield {
        #these should be appended or assigned to be determined
      'creator':response.xpath().text() 
        'title':response.xpath().text()
        'details':response.xpath().text()
        'blogContent':response.xpath().text()
        'tags':response.xpath().text()
        'responses':response.xpath().text()
        # creator = response.css().get()
        # title = response.css().get()
        # details = response.css().get()
        # blogContent = response.css().get()
        # tags = response.xpath().css().get()
        # responses = response.css().get()
      }
   """ blogsToCrawl = response.css().get();
    if blogsToCrawl is not None:
      blogsToCrawl = response.urljoin(blogsToCrawl)
      yield scrapy.Request(blogsToCrawl, callback=self.parse)"""
    for href in response.css(''):
      yield response.follow(href, callback=self.parse)

    #     "/html/body/div[1]/div/div[3]/article/div/section/div/div/div[2]/div/div/div[1]/div[2]/div/div/span/a/h4"
    #   "/html/body/div[1]/div/div[3]/article/div/section/div[1]/div/div[2]/div/div/div[1]/div[2]/div/div/span/div/span/a"
    #   "/html/body/div[1]/div/div[3]/article/div/section[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div/span/a/h4"
    #   "/html/body/div[1]/div/div[3]/article/div/section/div/div/div/div/div/div[1]/div[2]/div/div/span/div/span/a"
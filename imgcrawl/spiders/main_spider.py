import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor

from imgcrawl.items import Image, Link


class MainSpider(CrawlSpider):
  name = "main"
  allowed_domains = ["www.rainforestpartnership.org", "filmsfortheforest.org"] 
  start_urls = [
    "http://www.rainforestpartnership.org",
    "http://filmsfortheforest.org"
  ]

  rules = (Rule(LinkExtractor(allow=(".*")), callback="parse_item", follow=True),)

  def parse_item(self, response):
    self.log('Crawling %s' % response.url)
    sel = Selector(response)
    images = sel.xpath('//img')
    items = []
    for image in images:
      item = Image()
      item['parent_page'] = response.url
      item['src'] = image.select('@src').extract()
      items.append(item)

    return items
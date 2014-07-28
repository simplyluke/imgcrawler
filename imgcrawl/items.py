# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class Image(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # image
    parent_page = Field()
    src = Field()

class Link(Item):
  link = Field()
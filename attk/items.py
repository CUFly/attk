# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AttkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Id = scrapy.Field()
    sub_tech = scrapy.Field()
    tactic = scrapy.Field()
    platform = scrapy.Field()
    data_source = scrapy.Field()
    require_network = scrapy.Field()
    version = scrapy.Field()
    created_data = scrapy.Field()
    last_modify_data = scrapy.Field()

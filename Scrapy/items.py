# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonkindleItem(scrapy.Item):
    # define the fields for your item here like:
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_rating = scrapy.Field()
    book_reviews = scrapy.Field()
    pass

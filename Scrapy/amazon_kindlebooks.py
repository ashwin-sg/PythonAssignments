import scrapy
from ..items import AmazonkindleItem

class AmazonKindlebooksSpider(scrapy.Spider):
    name = 'amazon_kindlebooks'
    page_number = 2
    start_urls = ['https://www.amazon.in/s?bbn=1634753031&rh=n%3A1634753031%2Cp_n_publication_date%3A2814697031&dc&qid=1612283318&rnid=2814695031&ref=lp_1634753031_nr_p_n_publication_date_1']

    def parse(self, response):
        items = AmazonkindleItem()

        book_name = response.css('.a-color-base.a-text-normal::text').extract()
        book_author = response.css('.a-size-base+ .a-size-base').css('::text').extract()
        book_rating = response.css('.aok-align-bottom').css('::text').extract()
        book_reviews = response.css('.a-size-small .a-size-base').css('::text').extract()

        items['book_name'] = book_name
        items['book_author'] = book_author
        items['book_rating'] = book_rating
        items['book_reviews'] = book_reviews


        yield items

        next_page = 'https://www.amazon.in/s?i=digital-text&bbn=1634753031&rh=n%3A1634753031%2Cp_n_publication_date%3A2814697031&dc&page=' + str(AmazonKindlebooksSpider.page_number) + '&qid=1617875666&rnid=2814695031&ref=sr_pg_2'
        if AmazonKindlebooksSpider.page_number <= 400:
            AmazonKindlebooksSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        pass

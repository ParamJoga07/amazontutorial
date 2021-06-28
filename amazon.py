import scrapy
from ..items import AmazonTutorialItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_no = int(input("enter the pages you want to scrap:"))
    print()
    i = 1
    while i <= page_no:
        start_urls = ['https://www.amazon.in/s?k=laptops' + str(i)]

        def parse(self, response):
            items = AmazonTutorialItem()
            all_laptops_amazon = response.css(".sg-col-12-of-20")

            for amazon in all_laptops_amazon:
                laptop_name = amazon.css('.a-size-medium::text').extract()
                laptop_price = amazon.css('.a-price-whole::text').extract()

                items['laptop_name'] = laptop_name
                items['laptop_price'] = laptop_price

                yield items

        i = i + 1

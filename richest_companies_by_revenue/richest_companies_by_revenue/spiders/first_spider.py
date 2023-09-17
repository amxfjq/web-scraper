import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"]

    def parse(self, response):
        pass

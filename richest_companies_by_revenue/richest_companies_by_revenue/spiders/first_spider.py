import scrapy


class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"]

    def parse(self, response):
        xxx = response.css('tbody tr')[2:-15]
        list_of_companies_and_info = xxx.css('tr')
        for i in list_of_companies_and_info:
            yield{
                'rank': i.css('th::text').get().strip(),
                'company': i.css('td a::text')[0].get(),
                'industry': i.css('td a::text')[1].get(),
                'revenue(in millions)': i.css('td')[2].css('td::text').get().strip(),
                'profit(in millions)': i.css('td')[3].css('td::text').get().strip(),
                'employees': i.css('td')[4].css('td::text').get().strip(),
                'headquarters': i.css('td')[5].css('td::text').get().strip(),
                'state owned': i.css('td')[6].attrib['data-sort-value']

            }
            
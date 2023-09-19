import scrapy
from richest_companies_by_revenue.items import CompanyInfo
class FirstSpiderSpider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue"]

    def parse(self, response):
        details = CompanyInfo()
        #long_shot = []
        xxx = response.css('tbody tr')[2:-15]
        list_of_companies_and_info = xxx.css('tr')
        for i in list_of_companies_and_info:
            details['rank'] = i.css('th::text').get().strip(),
            details['company'] = i.css('td a::text')[0].get(),
            details['company info'] = i.css('a::attr(href)').get(),
            details['industry'] = i.css('td a::text')[1].get(),
            details['revenue_in_millions'] = i.css('td')[2].css('td::text').get().strip(),
            details['profit_in_millions'] = i.css('td')[3].css('td::text').get().strip(),
            details['employees'] = i.css('td')[4].css('td::text').get().strip(),
            details['headquarters'] = i.css('td')[5].css('td::text').get().strip(),
            details['state owned'] = i.css('td')[6].attrib['data-sort-value']

            #long_shot.append(i.css('a::attr(href)').get())

            yield CompanyInfo

'''        for i in long_shot:
            actual_url = 'https://en.wikipedia.org/' + i
            yield response.follow(actual_url, callback=self.parse_company_info)

    def parse_company_info(self, response):
        i = response.css('table.infobox.vcard tbody tr td')
        yield{
            'company_name': response.css('table.infobox.vcard caption::text').get(),
            'company_type': i.css('td.infobox-data.category a::text').get(),
            'website': i.css('span.url a::attr(href)').get()
        }'''
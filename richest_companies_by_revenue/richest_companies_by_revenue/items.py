# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RichestCompaniesByRevenueItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class CompanyInfo(scrapy.Item):
    rank = scrapy.Field()
    company = scrapy.Field()
    industry = scrapy.Field()
    revenue_in_millions = scrapy.Field()
    profit_in_millions = scrapy.Field()
    employees = scrapy.Field()
    headquarters = scrapy.Field()
    state_owned = scrapy.Field()
    company_name = scrapy.Field()
    company_type = scrapy.Field()
    website = scrapy.Field()
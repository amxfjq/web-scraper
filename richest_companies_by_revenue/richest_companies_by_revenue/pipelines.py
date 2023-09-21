# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from richest_companies_by_revenue.items import CompanyInfo, ExtraInfo
from itemadapter import ItemAdapter
#import mysql.connector

class RichestCompaniesByRevenuePipeline:
    def process_item(self, item, spider):
        if isinstance(item, CompanyInfo):
            adapter = ItemAdapter(item)
            value = adapter.get('company_info')
            adapter['company_info'] = 'https://en.wikipedia.org' + value
        elif isinstance(item, ExtraInfo):
            pass

        return item
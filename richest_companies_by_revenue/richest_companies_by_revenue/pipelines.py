# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from richest_companies_by_revenue.items import CompanyInfo, ExtraInfo
from itemadapter import ItemAdapter
import mysql.connector

class RichestCompaniesByRevenuePipeline:
    def process_item(self, item, spider):
        if isinstance(item, CompanyInfo):
            adapter = ItemAdapter(item)
            value = adapter.get('company_info')
            adapter['company_info'] = 'https://en.wikipedia.org' + value
        elif isinstance(item, ExtraInfo):
            pass

        return item

class SaveToMySQLPipeline:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = 'localhost'
            user = 'amxfjq'
            password = 'readysetgo'
            database = 'companies'
        )

        self.cur = self.conn.cursor()

        self.cur.execute('''
                         CREATE TABLE IF NOT EXISTS companies(
                         id int NOT NULL auto_incrememnt,
                         rank INTEGER,
                         company VARCHAR(255),
                         company_info VARCHAR(255),
                         industry VARCHAR(255),
                         revenue_in_millions DECIMAL,
                         profit_in_millions DECIMAL,
                         employees INTEGER,
                         headquarters VARCHAR(255),
                         state_owned text,
                         company_name text,
                         company_type text,
                         website VARCHAR(255),
                         PRIMARY KEY (id)
        )''')
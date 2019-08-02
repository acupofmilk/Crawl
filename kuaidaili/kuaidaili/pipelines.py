# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class KuaidailiPipeline(object):
    def open_spider(self, sipder):
        self.connection = pymysql.connect(
            user = 'root',
            password = 'zhou',
            database = 'python',
            charset = 'utf8'
        )
        self.cur = self.connection.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO kuaidaili(IP,Port,Anonymity,Type) values(item['IP'],item['Port'],item['Anonymity'],item['Type'])"
        self.cur.execute(sql)
        self.connection.commit()
        return item

    def close_spider(self,spider):
        self.cur.close()
        self.connection.close()

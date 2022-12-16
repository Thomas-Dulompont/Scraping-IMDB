# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
from itemadapter import ItemAdapter


class FilmScrapingPipeline:

    collection_name = "Film"

    def open_spider(self, spider):
        self.client = MongoClient("mongodb://localhost:27017")
        db = self.client["Scraping"]

        self.film = db[self.collection_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.film.insert_one(dict(item))
        return item


class SerieScrapingPipeline:

    collection_name = "Serie"

    def open_spider(self, spider):
        self.client = MongoClient("mongodb://localhost:27017")
        db = self.client["Scraping"]

        self.serie = db[self.collection_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.serie.insert_one(dict(item))
        return item

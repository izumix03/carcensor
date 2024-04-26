# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sqlite3

# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


class CarcensorPipeline:
    _db = None

    @classmethod
    def get_database(cls):
        cls._db = sqlite3.connect(os.path.join(os.getcwd(), "carsensor.db"))

        cursor = cls._db.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS carsensor (\
                id INTEGER PRIMARY KEY AUTOINCREMENT,\
                url TEXT,\
                brand_name TEXT,\
                model_name TEXT\
            );"
        )
        return cls._db

    def process_item(self, item, spider):
        self.save_car(item)
        return item

    def save_car(self, item):
        if self.find_car(item["url"]):
            return

        db = self.get_database()
        db.execute(
            "INSERT INTO carsensor (url, brand_name, model_name) VALUES (?, ?, ?)",
            (item["url"], item["brand_name"], item["model_name"]),
        )
        db.commit()

    def find_car(self, url):
        db = self.get_database()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM carsensor WHERE url = ?", (url,))
        return cursor.fetchone()

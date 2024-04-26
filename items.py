# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CarcensorCar(scrapy.Item):
    url = scrapy.Field()
    brand_name = scrapy.Field()
    # sub_title = e.g. 10xs 電動スライド/衝突軽減/TV/ETC/カメラ (ブルーメタリック)
    model_name = scrapy.Field()
    # # 支払い総額
    # total_price = scrapy.Field()
    # # 本体価格
    # base_price = scrapy.Field()
    # # 年式
    # model_year = scrapy.Field()
    # # 走行距離
    # mileage = scrapy.Field()
    # # 修復歴
    # repair_history = scrapy.Field()
    # # 法定整備
    # legal_maintenance = scrapy.Field()
    # # 車検
    # vehicle_inspection = scrapy.Field()
    # # 地域
    # region = scrapy.Field()
    # # 保証
    # guarantee = scrapy.Field()

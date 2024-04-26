import re
import unicodedata

import scrapy

from ..items import CarcensorCar


class CarsensorCarSpiderSpider(scrapy.Spider):
    name = "carsensor_car_spider"
    allowed_domains = ["www.carsensor.net"]
    start_urls = ["https://www.carsensor.net/usedcar/tokyo/index.html"]

    def parse(self, response):
        # 車の台数
        car_count = response.xpath("/html/body/div[1]/div[3]/div[1]/div[1]/p/text()")
        print(car_count.extract_first())

        # 車の情報
        for car in response.css(".carListWrap .js_listTableCassette"):
            yield CarcensorCar(
                url=car.css(".cassetteMain__title a::attr(href)").extract_first(),
                brand_name=car.css("div.cassetteMain__carInfoContainer > p:nth-child(2)::text").extract_first().strip(),
                model_name=unicodedata.normalize("NFKD", car.css(".cassetteMain__title a::text").extract_first()).split(" ")[0],
            )

        if response.css("div.pager__btn > button.btnFunc.pager__btn__next:disabled").extract_first() is not None:
            return

        # 今のページから次のページを計算
        index_page_str = response.request.url.split("/")[-1]
        index_page = re.sub(r"\D", "", index_page_str)
        if index_page == "":
            yield scrapy.Request(response.urljoin(f"/usedcar/tokyo/index2.html"))
        else:
            yield scrapy.Request(response.urljoin(f"/usedcar/tokyo/index{int(index_page) + 1}.html"))

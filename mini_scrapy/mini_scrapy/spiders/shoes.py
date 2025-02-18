import json
from pathlib import Path
from typing import Iterable

import scrapy
from requests import request
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from scrapy_playwright.page import PageMethod
from selenium import webdriver

# # Options for browse
# options = webdriver.ChromeOptions()
# # options.add_argument('--headless')
#
# # Create a browser
# driver = webdriver.Chrome(options=options)

class ShoesSpider(scrapy.Spider):
    name = "shoes"
    # allowed_domains = ["www.nike.com"]
    # start_urls = ["https://www.scrapingcourse.com/javascript-rendering"]
    start_urls = ["https://www.academy.com/p/nike-womens-court-legacy-next-nature-shoes"]
    # driver = webdriver.Chrome(options=options)

    # def __init__(self):
    #     self.driver.get('https://www.scrapingcourse.com/javascript-rendering')

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response, **kwargs):
        name_section = response.css('[data-auid="PDP_ProductName"]')
        price_section = response.css('.nowPrice')
        rating_section = response.css('span.ratingAvg')
        reviews_section = response.css('button.ratingCount')
        default_colour_section = response.css('[data-auid="PDP-title"] div:last-child > span span:last-child')
        colors_section = response.css('div#swatch-drawer-content button')

        colours_list = []
        for colour in colors_section:
            colours_list.append(colour.attrib['aria-label'])

        yield {
            'name': name_section.css('::text').extract(),
            'price': price_section.css('::text').extract(),
            'colour': default_colour_section.css('::text').extract(),
            'reviews_count': reviews_section.css('::text').extract(),
            'reviews_score': rating_section.css('::text').extract(),
            'availableColours': colours_list,
        }

        # for review in reviews_section:
        #     yield {
        #         'review': review.attrib['aria-label'],
        #     }

        # 'response' contains the page as seen by the browser
        # self.driver.get(response.url)
        # res = response.replace(body=self.driver.page_source)
        # rating_data = driver.find_elements(By.CLASS_NAME, 'product-info')
        # names = response.css('.product-info span.product-name')
        # names_result = []
        # for name in names:
        #     yield {
        #         'name': name.css('::text').extract()
        #     }
        #     curr_name = name.css('::text').extract()
        #     names_result.append(curr_name)
        #
        # prices = response.css('.product-info span.product-price')
        #
        # prices_result = []
        # for price in prices:
        #     yield {
        #         'price': price.css('::text').extract(),
        #         'price2': price.attrib['data-content']
        #     }
        #     curr_price = price.css('::text').extract()
        #     prices_result.append(curr_price)
        #
        # print(names_result, prices_result)


# if __name__ == "__main__":
#     process = CrawlerProcess()
#     process.crawl(ShoesSpider)
#     process.start()

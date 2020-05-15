# -*- coding: utf-8 -*-
# https://docs.scrapy.org/en/latest/topics/spiders.html
import scrapy
from ..items import {{ cookiecutter.object_prefix }}Item


class {{ cookiecutter.object_prefix }}Spider(scrapy.Spider):
    name = '{{cookiecutter.project_name}}'
    allowed_domains = ['{{cookiecutter.domain}}']
    start_urls = ['{{cookiecutter.protocol}}://{{cookiecutter.domain}}']

    def parse(self, response):
        yield {'title': response.xpath('//title')}
        next_page_url = response.xpath('//a[@class="next" and not(contains(@class, "disabled"))]/@href')
        if next_page_url:
            yield response.follow(next_page_url, self.parse)

# -*- coding: utf-8 -*-
import scrapy
from ..items import {{ cookiecutter.object_prefix }}Item


class {{ cookiecutter.object_prefix }}Spider(scrapy.Spider):
    name = '{{cookiecutter.projcet_name}}'
    allowed_domains = ['{{cookiecutter.domain}}']
    start_urls = ['{{cookiecutter.protocol}}://{{cookiecutter.domain}}']

    def parse(self, response):
        pass

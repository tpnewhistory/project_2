# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class CarfaxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	name = scrapy.Field()
	price = scrapy.Field()
	mileage = scrapy.Field()
	location = scrapy.Field()
	ext_color = scrapy.Field()
	int_color = scrapy.Field()
	drive_type = scrapy.Field()
	transmission = scrapy.Field()
	body_style = scrapy.Field()
	engine = scrapy.Field()
	fuel = scrapy.Field()
	mpg_cty_hwy = scrapy.Field()
	VIN = scrapy.Field()

	accident = scrapy.Field()
	damage = scrapy.Field()
	one_owner = scrapy.Field()
	service = scrapy.Field()
	personal = scrapy.Field()



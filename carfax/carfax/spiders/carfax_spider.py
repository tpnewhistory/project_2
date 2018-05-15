import csv
from scrapy import Spider, Request
from carfax.items import CarfaxItem 

class CarfaxSpider(Spider):
	name = 'carfax_spider'
	allowed_urls = ['https://www.carfax.com/']
	start_urls = ['https://www.carfax.com/']

	def parse(self, response):
		car_urls = open('/Users/Tony/carfax/car_urls_listed.csv', 'r')
		dat = car_urls.readlines()
		for vinname in dat:
			url = 'https://www.carfax.com/vehicle/' + vinname
			yield Request(url = url, callback = self.parse_page)

		car_urls.close()

	def parse_page(self, response):

		name = response.xpath('//*[@id="_automation_test_VDP_h1"]/text()').extract_first()
		price = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[1]/td/text()').extract_first()
		mileage = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[2]/td/text()').extract_first()
		location = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[3]/td/text()').extract_first()
		ext_color = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[4]/td/text()').extract_first()
		int_color = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[5]/td/text()').extract_first()
		drive_type = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[6]/td/text()').extract_first()
		transmission = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[7]/td/text()').extract_first()
		body_style = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[8]/td/text()').extract_first()
		engine = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[9]/td/text()').extract_first()
		fuel = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[10]/td/text()').extract_first()
		mpg_cty_hwy = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[11]/td/text()').extract_first()
		VIN = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[1]/table/tbody/tr[12]/td/text()').extract_first()

		accident = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[5]/div[1]/div/text()').extract_first()
		damage = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[5]/div[2]/div/text()').extract_first()
		one_owner = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[5]/div[3]/div/text()').extract_first()
		service = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[5]/div[4]/div/text()').extract_first()
		personal = response.xpath('//*[@id="react-app"]/div[1]/div/div/div[2]/div[1]/div/div/div[2]/section[3]/div/div[1]/div[3]/div/div/div[2]/div[5]/div[5]/div/text()').extract_first()

		item = CarfaxItem()
		item['name'] = name
		item['price'] = price
		item['mileage'] = mileage
		item['location'] = location
		item['ext_color'] = ext_color
		item['int_color'] = int_color
		item['drive_type'] = drive_type
		item['transmission'] = transmission
		item['body_style'] = body_style
		item['engine'] = engine
		item['fuel'] = fuel
		item['mpg_cty_hwy'] = mpg_cty_hwy
		item['VIN'] = VIN

		item['accident'] = accident
		item['damage'] = damage
		item['one_owner'] = one_owner
		item['service'] = service
		item['personal'] = personal

		yield item
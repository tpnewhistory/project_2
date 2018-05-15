from selenium import webdriver
import selenium
import time
from selenium.webdriver.support.ui import Select

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome()
# Go to the page that we want to scrape
driver.get("https://www.carfax.com/")

# Click review button to go to the review section
used_car_button = driver.find_element_by_xpath('//a[@class="hero__button button--green"]')
used_car_button.click()

body_type_and_price_tab = driver.find_element_by_xpath('//a[@href="#bodyTypePanel"]')
body_type_and_price_tab.click()

price_range = driver.find_element_by_xpath('//select[@name="priceMax"]')
price_value = driver.find_element_by_xpath('//option[@value="15000"]')
price_value.click()

zip_code = driver.find_element_by_xpath('//input[@name="zip"]')
zip_code.send_keys('10027')

entries_button = driver.find_element_by_xpath('//button[@class="button large search-submit primary-green float-right  "]')
entries_button.click()

time.sleep(10)
results_button = driver.find_element_by_xpath('//button[@class="button large primary-green"]')
results_button.click()

vin_list = []

while True:
	try:
		for num in range(1,26):
			vin_list.append(driver.find_element_by_xpath('//article[{}]/div[2]/a'.format(num)).get_attribute('href'))

		time.sleep(10)
		next_page_button = driver.find_element_by_xpath('//li[@class="next"]')
		next_page_button.click()
		
	except: 
		driver.close()
		break

print(len(vin_list))

vin_list = str(vin_list)

f = open('car_urls2.csv', 'w')
f.write(vin_list)
f.close()

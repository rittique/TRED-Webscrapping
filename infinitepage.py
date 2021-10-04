from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get("https://www.tred.com/buy?body_style=&amp;distance=50&amp;exterior_color_id=&amp;make=&amp;miles_max=100000&amp;miles_min=0&amp;model=&amp;page_size=24&amp;price_max=100000&amp;price_min=0&amp;query=&amp;requestingPage=buy&amp;sort=desc&amp;sort_field=updated&amp;status=active&amp;year_end=2022&amp;year_start=1998&amp;zip=")
radius = driver.find_element_by_css_selector("select.form-control") 
zip_code = driver.find_element_by_css_selector("input.form-control")

radius.send_keys("300 mi.")
zip_code.send_keys("90001")
zip_code.send_keys(Keys.RETURN)

time.sleep(10) 


"""
previous_height = driver.execute_script('return document.body.scrollHeight')

while True:
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

	time.sleep(3)

	new_height = driver.execute_script('return document.body.scrollHeight')
	if new_height == previous_height:
		break
	previous_height = new_height

main_list = driver.find_elements_by_class_name("inventory grid car-item gutter-0 row")

for content in main_list:
    car_name = content.find_element_by_xpath('//*[@id="cars"]/div/div/div[1]/div/div[1]/div/div/div/a/div[2]/h5')
    price = content.find_element_by_class_name('//*[@id="cars"]/div/div/div[1]/div/div[1]/div/div/div/a/div[2]/h6[2]/span/span')
    #vehical_summary = content.find_element_by_xpath('')
    #options

    print(f"Car Name: {car_name}, price: {price}")

"""

item = driver.find_element_by_class_name('progressive-background-image')
item.click()

try:
	wait = WebDriverWait(driver, 10)
	price = wait.until(
    	EC.presence_of_element_located((By.XPATH, '//*[@id="header-box"]/div/div/div[2]/div/div/h2'))
    )
	print(price) 

except:
	print("Error!")

#try:

"""
price = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "price-box no-arrow"))
)
name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "bigger small-top-margin visible-xs"))
)
summary = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "summary-table"))
)
options = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "options-table"))
)
print(f"Name: {name}, Price: {price}, Summary: {summary}, Options: {options}")
#except:
 #   driver.quit()
"""

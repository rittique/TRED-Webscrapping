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


main = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory grid car-item gutter-0 row"))
)

content_list = main.find_elements_by_class_name("info")

for content in content_list:
    car_name = content.find_element_by_tag_name("h5")
    year = content.find_element_by_class_name("year pull-left")
    price = content.find_element_by_class_name("price text-right")

    print(f"Car Name: {car_name}, year: {year}, price: {price}")
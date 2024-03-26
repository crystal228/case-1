from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome()
driver.set_window_size(1920,1080)
driver.get("http://demo.stocrm.ru")
login_form = driver.find_element(By.CSS_SELECTOR, "[type = Text]").send_keys("")
password_form = driver.find_element(By.CSS_SELECTOR, "[type = Password]").send_keys("")
button = driver.find_element(By.CSS_SELECTOR, "div.square_button_wrapper").click()
#offer_create = driver.find_element(By.CSS_SELECTOR, "square_button_wrapper.middle_size_dark_blue")
offer_create = driver.find_element(By.CLASS_NAME, "add_card_column_button")
time.sleep(5)
if offer_create is None:
   print("Элемент не найден")
else:
   print("Элемент найден")
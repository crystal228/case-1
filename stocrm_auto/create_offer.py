from selenium import webdriver
import time
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options)
driver.set_window_size(1920,1080)
driver.get("http://demo.stocrm.ru")
login_form = driver.find_element(By.CSS_SELECTOR, "[type = Text]").send_keys("p")
password_form = driver.find_element(By.CSS_SELECTOR, "[type = Password]").send_keys("CLG")
button = driver.find_element(By.CSS_SELECTOR, "div.square_button_wrapper").click()
driver.implicitly_wait(10)
offer_create_1 = driver.find_element(By.ID, 'add_card_column_button_hint').click()
time.sleep(5) 
if offer_create is None:
   print("Элемент не найден")
else:
   print("Элемент найден")
   
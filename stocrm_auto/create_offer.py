from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Настройка опций Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--disable-notifications")

# Инициализация драйвера Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_window_size(1920, 1080)

# Открытие указанного URL
driver.get("http://demo.stocrm.ru")

# Вход на сайт
driver.find_element(By.CSS_SELECTOR, "[type='Text']").send_keys("pavel_d@demo.ru")
driver.find_element(By.CSS_SELECTOR, "[type='Password']").send_keys("CLGmL6ZN!")
driver.find_element(By.CSS_SELECTOR, "div.square_button_wrapper").click()

# Ожидание загрузки следующей страницы
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'add_card_column_button_hint')))

# Создание нового предложения
driver.find_element(By.ID, 'add_card_column_button_hint').click()
driver.find_element(By.CSS_SELECTOR, 'input.small').send_keys("89091002442")
driver.find_element(By.CSS_SELECTOR, 'div.middle:nth-child(2)').click()

# Выбор первого элемента из поиска
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.search_item:nth-child(1)')))
driver.find_element(By.CSS_SELECTOR, 'div.search_item:nth-child(1)').click()

# Ожидание видимости кнопки для добавления нового предложения и нажатие на неё
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'square_button_wrapper.button_main')))
driver.find_element(By.CLASS_NAME, 'square_button_wrapper.button_main').click()
time.sleep(7)
# Инициализация ActionChains
action = ActionChains(driver)

# Двойной клик на первую сделку
offer_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.first_clumn > div:nth-child(2) > div:nth-child(1) > div:nth-child(1)')))
action.double_click(offer_element).perform()

# вы ахуенен
time.sleep(10)

# Закрытие драйвера
driver.quit()
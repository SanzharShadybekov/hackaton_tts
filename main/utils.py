from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


base_url = 'https://translate.yandex.ru/?source_lang=ru&target_lang=ky'
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Запуск Chrome в режиме без головы
# chrome_options.add_argument("--no-sandbox")  # Режим без песочницы
# chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--disable-gpu")

service = Service('/usr/local/bin/chromedriver')

def get_page_html_selenium(data, url=base_url):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, 'fakearea-container'))
    )

    input_element = driver.find_element(By.CSS_SELECTOR, '.textinput')
    input_element.send_keys(data)

    sleep(1)

    res_text = driver.find_element(By.CSS_SELECTOR, '.translation')
    res = res_text.text

    driver.quit()
    return res


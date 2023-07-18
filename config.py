from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time


def scrap_screen_shots():
    s = Service("E:/Web Scrapping/Automated Product Screenshots/Chrome Driver/chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.get('https://www.nike.com')
    time.sleep(6)
    driver.find_element(by=By.XPATH,
                        value="""/html/body/div[3]/div/div[3]/header/div/div[1]/div[2]/div/div/div[1]/div/div/button[2]""").click()
    element = driver.find_element(by=By.XPATH,
                                  value="""/html/body/div[3]/div/div[3]/header/div/div[1]/div[2]/div/div/div[1]/div/div/input""")
    element.send_keys('men shoe')
    element.send_keys(Keys.ENTER)
    counter = 0
    while True:
        time.sleep(1)
        link = f"E:/Web Scrapping/selenium/SS/nike_{counter}.png"
        driver.save_screenshot(link)
        counter += 1
        height = driver.execute_script("return document.body.scrollHeight")
        # print(f'Height:\t{height}')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        # print(f'New Height:\t{new_height}')
        if height == new_height:
            break
    time.sleep(2)

from selenium import webdriver
import selenium.common.exceptions as exc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
options.add_argument("--disable-blink-features=AutomationControlled")
# options.headless = True

s = Service(executable_path="/path/chromedriver")
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.binance.com/ru-UA/my/wallet/account/payment/send")
time.sleep(10)

try:
    while True:
        time.sleep(60)
        
        # //*[@id="__APP"]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div/form/div[1]/button[1]
        
        otpravit = driver.find_element(By.CLASS_NAME, 'btn-text css-ioe039').click
        
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
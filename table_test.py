import time
import win32api

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/tables")
    rows1 = driver.find_elements(By.CSS_SELECTOR)

finally:
    driver.quit()
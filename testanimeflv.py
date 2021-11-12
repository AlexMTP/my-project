import time
import win32api

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

try:
    driver.get("https://www3.animeflv.net/")
    link_serie = driver.find_element(By.ID,"")

    win32api.MessageBox(0,'Nuevo episodio', 'Alerta')
finally:
    time.sleep(10)
    driver.quit()



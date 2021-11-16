import time
import win32api

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox1= driver.find_element(By.CSS_SELECTOR,"#checkboxes > input[type=checkbox]:nth-child(1)")
checkbox2= driver.find_element(By.CSS_SELECTOR,"#checkboxes > input[type=checkbox]:nth-child(3)")

def marcar_checks(check1, check2):

    if check1:
        if checkbox1.is_selected():
            print(True)




try:
    marcar_checks(True, True)
    win32api.MessageBox(0, 'Clickando checkboxes', 'true y true')

    marcar_checks(True, False)
    win32api.MessageBox(0, 'Clickando checkboxes', 'true y false')

    marcar_checks(False, True)
    win32api.MessageBox(0, 'Clickando checkboxes', 'false y true')

    marcar_checks(False, False)
    win32api.MessageBox(0, 'clickando checkboxes', 'false y false')


finally:
    time.sleep(5)
    driver.quit()


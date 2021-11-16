import unittest
import time
import win32api

from selenium import webdriver
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def test_something(self):
        driver = webdriver.Chrome()
        driver.get("https://python.org")
        self.assertEqual(driver.title, "Welcome to Python.org")
        driver.quit()


if __name__ == '__main__':
    unittest.main()

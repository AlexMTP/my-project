from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('chrome is up')
def step_impl(context):
    context.driver = webdriver.Chrome()
    time.sleep(3)


@when('user gets page')
def step_impl(context):
    context.driver.get("https://python.org")
    time.sleep(3)


@then('the title is correct')
def step_impl(context):
    assert context.driver.title == "Welcome to Python.org"
    context.driver.quit()


@given('chrome rising')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('the user gets animeflv page')
def step_impl(context):
    context.driver.get("https://www3.animeflv.net/")


@When('the user clicks one peace link')
def step_impl(context):
    link_series = context.driver.find_element(By.CSS_SELECTOR, "#mCSB_1_container > ul > li:nth-child(1) > a")
    link_series.click()


@then('the last episode is the 999th')
def step_impl(context):
    link_episodio = context.driver.find_element(By.CSS_SELECTOR,"#episodeList > li:nth-child(2) > a > p")
    assert link_episodio.text == "Episodio 999"
    context.driver.quit()

import time
from telnetlib import EC


from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

@then('Tap on Generate API key button')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[2]/div/nav/ul[2]/li/div/span/span[2]').click()
    time.sleep(2)

@then('clicks on Generate New API key')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[1]/div/button/h6').click()
    time.sleep(2)

@then('Enter Name')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="formName"]').send_keys('Automated User')
    time.sleep(2)

@then('Enter Description')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="formDescription"]').send_keys('Automated testing user API')
    time.sleep(3)

@then('clicks on submit button')
def step_impl(context):
     context.driver.find_element("xpath", '/html/body/div[3]/div/div/div/div/form/div[3]/button[2]').click()
     time.sleep(4)

@then('See the success message')
def step_impl(context):
    text = context.driver.find_element("xpath", '//body/div[@id="__next"]/div[1]/div[2]/div[1]/div[3]/div[2]').text
    print(text)
    assert text == "Key Generated Successfully"
    time.sleep(6)

@then('open delete popup')
def step_impl(context):
    context.driver.find_element("xpath", '//body/div[@id="__next"]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div['
                                         '2]/div[1]/div[1]/span[1]/span[1]/img[1]').click()
    time.sleep(3)

@then('click on delete button')
def step_impl(context):
    context.driver.find_element("xpath", '/html[1]/body[1]/div[3]/div[1]/div[1]/div[1]/div[1]/button[2]').click()
    time.sleep(3)

@then('See the delete msg')
def step_impl(context):
    text = context.driver.find_element("xpath", '//body/div[@id="__next"]/div[1]/div[2]/div[1]/div[3]/div[2]').text
    print(text)
    assert text == "Deleted Successfully"
    time.sleep(6)

@then('click on eye icon')
def step_impl(context):
    context.driver.find_element("xpath", '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/span[1]/span[1]/img[1]').click()
    time.sleep(4)

@then('Tap on Copy icon')
def step_impl(context):
    context.driver.find_element("xpath", '//body/div[@id="__next"]/div[1]/div[2]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/span[2]/span[1]/img[1]').click()
    time.sleep(4)


@then('See the copy success msg')
def step_impl(context):
    text = context.driver.find_element("xpath", '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]').text
    print(text)
    assert text == "Text Copied"
    time.sleep(6)
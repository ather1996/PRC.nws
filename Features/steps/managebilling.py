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


@When('Tap on Account')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[2]/div/nav/ul[3]/li/div/span').click()
    time.sleep(6)


@then('Tap on manage billing')
def step_impl(context):
    context.driver.find_element("xpath",
                                '//*[@id="__next"]/div/div[2]/div/div[2]/div/nav/ul[3]/ul/li[2]/div/span/span').click()
    time.sleep(6)


@then('Add new payment method')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[1]/div/button/h6').click()
    time.sleep(6)


@then('Add card name')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="formName"] ').send_keys('automated user')
    time.sleep(6)


@then('Add card number')
def step_impl(context):
    context.driver.switch_to.frame(context.driver.find_element(By.CSS_SELECTOR,
                                                               "body > div.fade.modal.show > div > div > div > div.undefined > form > div:nth-child(2) > div > div > div > iframe"))
    time.sleep(4)
    context.driver.find_element("xpath", '//*[@id="root"]/form/span[2]/div/div[2]/span/input').send_keys(
        '4000056655665556')
    context.driver.switch_to.default_content()


@then('Add expiration date')
def step_impl(context):
    wait = WebDriverWait(context.driver, 5)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > "
                                                                           "div > div.undefined > form > "
                                                                           "div.PaymentFormModal_payment-fields__5LY83 > div > div > div.pl-0.col > div > div > div > div > div > div > iframe")))
    context.driver.find_element("name", 'exp-date').send_keys('12/25')
    context.driver.switch_to.default_content()
    time.sleep(6)


@then('Add cvc')
def step_impl(context):
    wait = WebDriverWait(context.driver, 5)
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "body > div.fade.modal.show > div > div > div > div.undefined > form > div.PaymentFormModal_payment-fields__5LY83 > div > div > div.pr-0.col > div > div > div > div > iframe")))
    context.driver.find_element("name", 'cvc').send_keys('123')
    context.driver.switch_to.default_content()
    time.sleep(6)

@then('Tap on Add card button')
def step_impl(context):
    context.driver.find_element("xpath", ' /html/body/div[3]/div/div/div/div[2]/form/div[5]/button[2]').click()
    time.sleep(6)

@then('See the add card success msg')
def step_impl(context):
    text = context.driver.find_element("xpath", '//div[@id="1"]').text
    print(text)
    assert text == "Card Created Successfully."
    time.sleep(6)

@then('click on delete icon')
def step_impl(context):
    dynamicElement = context.driver.find_elements("xpath", '//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[2]/div[4]/span/span/img')
    if len(dynamicElement) != 0:
        assert True
    else:
        print(dynamicElement)
        assert False
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[2]/div[4]/span/span/img').click()
    time.sleep(6)

@then('clicks on delete button')
def step_impl(context):
    context.driver.find_element("xpath", ' /html/body/div[3]/div/div/div[2]/div/button[2]').click()
    time.sleep(4)

@then('See the card delete success msg')
def step_impl(context):
    text = context.driver.find_element("xpath", '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]').text
    print(text)
    assert text == "Card Removed Successfully."
    time.sleep(6)


@then('set as default')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[2]/div[4]/div/div[2]/div/span').click()
    time.sleep(4)

@then('click on submit')
def step_impl(context):
    context.driver.find_element("xpath", '/html/body/div[3]/div/div/div/div/form/div/button[2]').click()
    time.sleep(4)

@then('See the default success msg')
def step_impl(context):
    text = context.driver.find_element("xpath", '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]').text
    print(text)
    assert text == "Default Card Updated Successfully."
    time.sleep(6)


@then('Tap on Invoice')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,800);")
    time.sleep(3)
    context.driver.find_element("xpath", '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[5]/a[1]').click()
    time.sleep(6)







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


@given('user is on support us page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.get('https://dev.prc.news/support')
    context.driver.implicitly_wait(20)


@then('Enter First name')
def step_impl(context):
    context.driver.find_element("xpath",
                                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[1]/input[1]').send_keys(
        'automate')
    time.sleep(3)


@then('Enter Last name')
def step_impl(context):
    context.driver.find_element("xpath",
                                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[2]/input[1]').send_keys(
        'user')
    time.sleep(3)


@then('Enter email address')
def step_impl(context):
    context.driver.find_element("xpath",
                                ' /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[3]/input[1]').send_keys(
        'automateduser@yopmail.com')
    time.sleep(3)


@then('Enter Phone no.')
def step_impl(context):
    context.driver.find_element("xpath",
                                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[4]/input[1]').send_keys(
        '1234567890')
    time.sleep(3)


@then('Enter company name')
def step_impl(context):
    context.driver.find_element("xpath",
                                '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[5]/input[1]').send_keys(
        'testing')
    time.sleep(3)


@then('Enter your message')
def step_impl(context):
    context.driver.find_element("xpath",
                                ' /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/div[6]/textarea[1]').send_keys(
        'This is for testing purpose')
    time.sleep(3)

@then('Tap on submit button')
def step_impl(context):
    context.driver.find_element("xpath", ' /html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/form[1]/button[1]').click()
    time.sleep(3)

@then('user should navigate to the Thank you page')
def step_impl(context):
    text = context.driver.find_element("xpath", '//p[contains(text(),"Thank you for contacting us. We have received '
                                                'your")]').text
    print(text)
    assert text == "Thank you for contacting us. We have received your contact information and will be in touch soon!"
    time.sleep(6)



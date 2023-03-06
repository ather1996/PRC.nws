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



@given('user is on login page')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.maximize_window()
    context.driver.get('https://dev.prc.news/login')
    context.driver.implicitly_wait(20)


@when('User enters valid credentials')
def step_impl(context):
  context.driver.find_element("id", "floatingInput").send_keys('ather@yopmail.com')
  context.driver.find_element("id", "floatingPassword").send_keys('Admin0101!')
time.sleep(4)


@when('Clicks login')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div/div/div[2]/div[1]/form/button').click()
    time.sleep(4)

@when('user should navigate to PRC.News dashboard')
def step_impl(context):
    text = context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[2]/div/nav/ul[1]/li/div/span/span[2]').text
    assert text == "Dashboard"
    time.sleep(3)

@when('Open Account dropdown')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[2]/div/nav/ul[3]/li/div').click()
    time.sleep(3)

@then('Clicks on Manage Profile')
def step_impl(context):
    context.driver.find_element("xpath", ' //*[@id="__next"]/div/div[2]/div/div[2]/div/nav/ul[3]/ul/li[1]/div/span/span ').click()
    time.sleep(3)

@then('Clicks on Edit Profile')
def step_impl(context):
    context.driver.find_element("xpath", ' //*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div/div/div[1]/div/button ').click()
    time.sleep(3)

@then('Edit Fields')
def step_impl(context):
    context.driver.find_element("xpath", ' /html/body/div/div/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/form/div[1]/div/input ').clear()
    time.sleep(4)
    context.driver.find_element("xpath", ' /html/body/div/div/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/form/div[1]/div/input ').send_keys('Automated')
    context.driver.find_element("xpath", '/html/body/div/div/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/form/div[2]/div/input').clear()
    time.sleep(4)
    context.driver.find_element("xpath", ' /html/body/div/div/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/form/div[2]/div/input').send_keys('user')
    context.driver.find_element("xpath",
                                '/html/body/div/div/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/form/div[3]/div/input').clear()
    time.sleep(2)
    context.driver.find_element("xpath", ' /html/body/div/div/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/form/div[3]/div/input').send_keys('1234567890')


@then('tap on save button')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[3]/div[1]/div[1]/div/div[3]/form/div[4]/button[2]').click()
    time.sleep(6)


@then('sign in method')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/form/div[1]/button').click()
    context.driver.find_element("xpath", '//*[@id="email"]').clear()
    time.sleep(4)

@then('enter new email')
def step_impl(context):
    context.driver.find_element("xpath", ' //*[@id="email"]').send_keys('Newemail@gmail.com')
    time.sleep(2)

@then('clicks on cancel button')
def step_impl(context):
    context.driver.find_element("xpath", ' //button[contains(text(),"Cancel")]').click()
    time.sleep(2)

@then('click on reset password')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="__next"]/div/div[2]/div/div[3]/div[2]/div[1]/div/div[2]/form/div[2]/button').click()
    time.sleep(2)

@then ('enter current password')
def step_impl(context):
    context.driver.find_element("xpath", '//*[@id="oldpassword"]').send_keys('Admin0101!')
    time.sleep(2)

@then('enter new password')
def step_impl(context):
    context.driver.execute_script("window.scrollTo(0,800);")
    time.sleep(3)
    context.driver.find_element("xpath", ' //*[@id="newpassword"]').send_keys('admin@123')
    time.sleep(2)

@then('enter confirm password')
def step_impl(context):
    context.driver.find_element("xpath", ' //*[@id="confirmpassword"]').send_keys('admin@123')
    time.sleep(2)

@then('click on cancel password')
def step_impl(context):
    context.driver.find_element("xpath", '/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/form[1]/form[1]/div[1]/div[4]/button[2]').click()
    time.sleep(4)


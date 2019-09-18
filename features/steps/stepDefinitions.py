from behave import given, when, then
from utils import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


@given(u'I get information from this API "{api_url}"')
def get_info_from_api(context, api_url):
    context.pet_names = get_info_api(api_url)
    assert (len(context.pet_names)>0)


@when(u'then I search each pet in "{search_engine}"')
def search_results_in_browser(context, search_engine):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    driver = webdriver.Chrome(executable_path="C:\\Users\\sergio.esteban\\Downloads\\chromedriver_win32\\chromedriver.exe", port=9515, chrome_options=options)
    for pet_name in context.pet_names:
        driver.get('https://www.google.com')
        elem = driver.find_element_by_name("q")
        time.sleep(3)
        elem.send_keys(pet_name)
        elem.send_keys(Keys.RETURN)
        time.sleep(3)


@then(u'I see the first result in the results page')
def open_results_page(context):
    pass


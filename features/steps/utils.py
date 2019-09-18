import json
from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import requests

def get_info_api(api_url):
    names = []
    response = requests.get(api_url)
    assert (response.status_code == 200)
    jsonBody = json.loads(response.content)
    for group in jsonBody:
        for key in group:
            names.append(group[key]['name'])

    return names

def set_browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    driver = webdriver.Chrome(executable_path="chrome_driver\\chromedriver.exe", port=9515, chrome_options=options)
    return driver

def search_element(pet_name, driver, search_engine_url):
    driver.get(search_engine_url)
    elem = driver.find_element_by_name("q")
    time.sleep(3)
    elem.send_keys(pet_name)
    elem.send_keys(Keys.RETURN)
    time.sleep(3)
from behave import given, when, then
from utils import *


@given(u'I get information from this API "{api_url}"')
def get_info_from_api(context, api_url):
    context.pet_names = get_info_api(api_url)
    assert (len(context.pet_names)>0)


@when(u'then I search each pet in "{search_engine}"')
def search_results_in_browser(context, search_engine):
    driver = set_browser()
    if search_engine == "google":
        search_engine_url = "https://www.google.com"
    elif search_engine == "bing":
        search_engine_url = "https://www.bing.com"
    for pet_name in context.pet_names:
        search_element(pet_name, driver, search_engine_url)
        

@then(u'I see the first result in the results page')
def open_results_page(context):
    pass


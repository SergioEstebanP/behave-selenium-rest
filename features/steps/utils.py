import json
from typing import List

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

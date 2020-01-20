#!/usr/bin/env python
import requests
import json
from contrasena import api_key

headers = {'X-Auth-Token': api_key}
url = "https://api.football-data.org/v2/"
parameters = {
    "matchday":"19"
}
response = requests.get(url+"competitions/PL/",headers=headers,params=parameters)


print(response.status_code)
print(response)

if response.status_code == 200:
    print(json.loads(response.content.decode('utf-8')))
else:
    pass
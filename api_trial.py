#!/usr/bin/env python
import requests
import json
from .contrasena import api_key

print(api_key)

response = requests.get("https://api.football-data.org/v2/competitions/PL/matches")
headers = {'X-Auth-Token': api_key}
print(response.status_code)
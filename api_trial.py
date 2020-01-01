#!/usr/bin/env python
import requests
import json
from contrasena import api_key

headers = {'X-Auth-Token': api_key}

response = requests.get("https://api.football-data.org/v2/competitions/PL/matches",headers=headers)

print(response.status_code)
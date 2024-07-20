# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://yoshobanta-153.atlassian.net/rest/api/3/project"

API_TOKEN= ""

auth = HTTPBasicAuth("", API_TOKEN )

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output= json.loads(response.text)
name= output[1]["name"]
print(name)
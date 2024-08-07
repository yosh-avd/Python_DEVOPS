# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://yoshobanta-153.atlassian.net/rest/api/3/issue"

API_TOKEN= "ATATT3xFfGF0IGqeLg3v9NyYi6oSV_PcPbiGSwtDBk_WW1Wi5gd82fYQE4z2W-TlDMfoGz95nAZyrWSOC_UpVMN_N5INZsZbY3JJf4P64yU8xYfSzGlBDUZCHAV3sK8oILX54olNTkv4ZOUHsI6XBPS-EBhERsUWdQjmwWF9_dOMGTziN3i0xa8=465D9C74"

auth = HTTPBasicAuth("garnaikyosh@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {

    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },

    "issuetype": {
      "id": "10007"
    },
    
    "project": {
      "key": "MAH"
    },

    "summary": "My First JIRA Ticket",
   
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createjira', methods=['POST'])
def createjira():

    url = "https://yoshobanta-153.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF0BURcokdoDtUbIbqvZodVsKvbS8kpv6vydQsP-2rlckbuaLi2t8e_PZ_60-4BlPlsLEK0YGikg3XjuKvDopWCmeJU9xqb79PTT3vqn1zVILE51qBc8KBwo4c4IJsKqc0jP4lXF3vUH87byuaGjXNoWUYGsLVgh2FMuR8TrNuSQnY=D01996FD"
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
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "MAH"
        },
        "issuetype": {
            "id": "10007"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )

    webhook = request.get_json()

    required_output = webhook['comment']['body']

    if (required_output  == '/jira'):
                response = requests.request(
                "POST",
                url,
                data=payload,
                headers=headers,
                auth=auth
                )

                return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

    else:
                print("Jira issue will be created if comment include /jira")
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)

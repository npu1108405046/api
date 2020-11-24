import requests
import json
import jwt
import time

url = "http://127.0.0.1:8000/users"
vaild_token = jwt.encode({"user_id":'123','timestamp':int(time.time())},
'password', algorithm='HS256').decode('utf-8')
payload="{\"user_id\":\"123\"}"
headers = {
  'auth': vaild_token,
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)
print(data)
import requests

url = "http://5b74423ea5837400141908c3.mockapi.io/Demo"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)

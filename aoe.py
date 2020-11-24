import requests

url = "https://age-of-empires-2-api.herokuapp.com/api/v1/units"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)

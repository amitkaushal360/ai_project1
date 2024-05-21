import requests

response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':"which chutney is perfect"}})

print(response.json()['output']['content'])
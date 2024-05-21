import requests

response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':"provide receipe of cutlet"}})

print(response.json()['output']['content'])
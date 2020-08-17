import requests
import json
from fastapi import FastAPI, HTTPException

test = FastAPI()
url = " http://localhost:3000/Books"

@test.get(url)
async def get_all_data():
    response = requests.get(url)
    print(response.content)

@test.get(url)
async def get_specific_data():
    response = requests.get(url, {'id': 15})
    print(response.content)

@test.post(url)
async def add_new_book():
    file = open('/Users/anilyavuz6176gmail.com/Desktop/TrendyolApi/newBooks.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)


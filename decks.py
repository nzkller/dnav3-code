import requests
from pprint import pprint
import time

i = 0

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"

querystring = {"deck_count":"6"}

headers = {
    'Cache-Control': "no-cache",
    'Postman-Token': "2f173ba1-10b3-4750-b499-dbf083901e7f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

pprint(response.text)

deck = response.json()
deck_id = deck['deck_id']
print(deck_id)

url2 = "https://deckofcardsapi.com/api/deck/"

url3 = deck_id

url4 = url2 + url3 + "/draw"

print(url4)

querystring = {"count":"10"}

headers2 = {
    'Cache-Control': "no-cache",
    'Postman-Token': "f5a11c4c-499c-456d-b9e6-a9c1fb012250"
    }

while i < 5:
	response2 = requests.request("GET", url4, headers=headers2, params=querystring)

	pprint(response2.text)

	time.sleep(5)

	i = i + 1

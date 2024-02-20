import apikey
import requests

headers = {
    'X-CMC_PRO_API_KEY' : apikey.key,
    'Accepts' : 'application/json',
    'Accept-Encoding': 'deflate, gzip'
}

params = {
    'start' : '1',
    'limit' : '5',
    'convert': 'USD'
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/historical'


data = requests.get(url, params = params, headers = headers ).json()['data']

for coins in data:
    if(coins['symbol'] == 'BTC'):
        print(coins['symbol'],coins['quote']['USD']['price'])
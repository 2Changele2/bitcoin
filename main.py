import requests
import time


def cotizacion():
    r = requests.get("https://api.coinbase.com/v2/exchange-rates?currency=BTC")
    print(type(r))
    print(r.json()['data']['rates']['EUR'])


while(True):
    cotizacion()
    time.sleep(15)

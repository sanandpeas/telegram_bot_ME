import aiohttp
import json
import time

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
trait_ = {}
mint_url = 'qM45orhAePbFUg3ZcapsyHiSPs8YUGtk1Jv5fo4jeqL'
url = 'https://magiceden.io/marketplace/bvdcat'
hr = UserAgent()
mint_addresses = []

offset = 0
size = 20

while True:
    time.sleep(5)

    response = requests.get(url=f'https://api-mainnet.magiceden.dev/v2/collections/bvdcat/listings?offset=0&limit=20',
                            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                                     "Accept": "application/json, text/plain, */*",
                                     "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                                     "Sec-Fetch-Dest": "empty",
                                     "Sec-Fetch-Mode": "cors",
                                     "Sec-Fetch-Site": "same-site",
                                     "Pragma": "no-cache",
                                     "Cache-Control": "no-cache"})
    data = response.json()
    items = len(data)

    for i in data:
        mint_addresses.append(i['tokenMint'])

    for adr in range(len(mint_addresses)):
        response1 = requests.get(url='https://api-mainnet.magiceden.dev/rpc/getNFTByMintAddress/'+mint_addresses[adr],
                                 headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                                          "Accept": "application/json, text/plain, */*",
                                          "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                                          "Sec-Fetch-Dest": "empty",
                                          "Sec-Fetch-Mode": "cors",
                                          "Sec-Fetch-Site": "same-site",
                                          "Pragma": "no-cache",
                                          "Cache-Control": "no-cache"})
        result = response1.json()
        for trait in result['results']['attributes']:
            trait_[trait['trait_type']] = trait['value']

        if int(result['results']['price']) < 2 : #and trait_.get('Glasses') == 'None'
            print(trait_)
            print('https://magiceden.io/item-details/'+result['results']['mintAddress']+'?name='+result['results']['attributes'][0]['value'])
            print(result['results']['img'])
            print(result['results']['collectionTitle'])
            print(result['results']['price'])







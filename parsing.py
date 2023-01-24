import asyncio
import urllib.request
from urllib.request import urlopen

from urllib.request import Request, urlopen
from urllib.error import HTTPError

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
mint_address = []



response = requests.get(url='https://api-mainnet.magiceden.dev/v2/collections/bvdcat/listings?offset=0&limit=20',
                        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                                 "Accept": "application/json, text/plain, */*",
                                 "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                                 "Sec-Fetch-Dest": "empty",
                                 "Sec-Fetch-Mode": "cors",
                                 "Sec-Fetch-Site": "same-site",
                                 "Pragma": "no-cache",
                                 "Cache-Control": "no-cache"})
data = response.json()
for i in data:
    mint_address.append(i['tokenMint'])


for i in range(20):
    response1 = requests.get(url='https://api-mainnet.magiceden.dev/rpc/getNFTByMintAddress/'+mint_address[i],
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
    if int(result['results']['price']) < 3 and trait_.get('Head') == 'None':

        print(trait_)

        # ссылка
        print('https://magiceden.io/item-details/'+result['results']['mintAddress']+'?name='+result['results']['attributes'][0]['value'])
        # Название коллекции
        print(result['results']['img'])
        print(result['results']['collectionTitle'])
        #цена
        print(result['results']['price'])
    else:
        print('False')


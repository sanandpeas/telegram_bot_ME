import json
import time

from bs4 import BeautifulSoup
import requests



def get_data():
    trait_ = {}
    collection = 'bvdcat'
    mint_addresses = []
    price = 2
    results = []
    count = 0
    traitGet = 'Eyes'
    while True:
        response = requests.get(url=f'https://api-mainnet.magiceden.dev/v2/collections/{collection}/listings?offset=0&limit=20',
                                headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
                                         "Accept": "application/json, text/plain, */*",
                                         "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                                         "Sec-Fetch-Dest": "empty",
                                         "Sec-Fetch-Mode": "cors",
                                         "Sec-Fetch-Site": "same-site",
                                         "Pragma": "no-cache",
                                         "Cache-Control": "no-cache"})
        data = response.json()

        mint_addresses.clear()
        for i in data:
            mint_addresses.append(i['tokenMint'])

        for adr in range(len(mint_addresses)):
            count += 1
            print(count)
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
            trait_.clear()
            for trait in result['results']['attributes']:
                trait_[trait['trait_type']] = trait['value']

            if float(result['results']['price']) < float(f'{price}') and trait_.get(traitGet) == 'Lazy':
                results.append({'link on site': 'https://magiceden.io/item-details/'+result['results']['mintAddress']+'?name='+result['results']['attributes'][0]['value'],

                                'Title':result['results']['title'],
                                'Trait': traitGet+': '+trait_.get(traitGet),
                               'Collection': result['results']['collectionTitle'],
                               'Price':result['results']['price']
                })
                print(trait_)
                print('https://magiceden.io/item-details/'+result['results']['mintAddress']+'?name='+result['results']['attributes'][0]['value'])
                print(result['results']['title'])
                print(result['results']['collectionTitle'])
                print(result['results']['price'])

        if count == 20:
            with open('result.json','w') as file:
                json.dump(results,file,indent=4,ensure_ascii=False)
            break

if __name__ == '__main__':
    get_data()


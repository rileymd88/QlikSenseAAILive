import requests
import json

cookies = {
    'client': 'qlik',
    '_ga': 'GA1.2.2101023541.1530713274',
    'GloboBalancerSSL': '377628170.48129.0000',
    '_gid': 'GA1.2.145639894.1546590051',
    'JSESSIONID': '6FC4CB55608F3BA224B62C66782B13D6',
}

headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': '*/*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.globoforce.net/store/',
}

response = requests.get('https://www.globoforce.net/microsites/login/userSessionAuthToken', headers=headers, cookies=cookies)

tokResponse = response.json()
token = tokResponse['token']


cookies = {
    '_ga': 'GA1.2.2101023541.1530713274',
    'GloboBalancerSSL': '377628170.48129.0000',
    '_gid': 'GA1.2.145639894.1546590051',
    'JSESSIONID': '6FC4CB55608F3BA224B62C66782B13D6',
}

headers = {
    'Pragma': 'no-cache',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en',
    'Authorization': 'Bearer ' + token,
    'client': 'qlik',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'Referer': 'https://www.globoforce.net/store/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'lang': 'eng',
}

params = (
    ('category', 'ELECT__HEADP'),
    ('page', '4'),
    ('limit', '128'),
)

response = requests.get('https://www.globoforce.net/ec-api/V1/countries/79/products', headers=headers, params=params, cookies=cookies)
print(response)
jsonResponse = response.json()
products = jsonResponse['products']
print(products)
""" for p in products:
    print(p['id'], p['title'], p['price'], p['fx'], p['image'], p['category'], p['brand']) """
    

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.globoforce.net/ec-api/V1/countries/79/products?category=ELECT__HEADP&page=1&limit=48', headers=headers, cookies=cookies)

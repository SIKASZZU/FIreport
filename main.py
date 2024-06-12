""" unnecessary right now

# import pandas as pd

# crypto_data = {'Name': [], 'Price': []}

# def add_to_dataframe(name, price):
#     crypto_data['Name'].append(name)
#     crypto_data['Price'].append(price)
#     df = pd.DataFrame(crypto_data)
#     print(df)


"""




import requests
from bs4 import BeautifulSoup

from currency_converter import CurrencyConverter
c = CurrencyConverter()


#=================== USER INPUT ===================#  
user_euro = True
user_BTC_amount = 0.00290389  # AMOUNT OF USER'S ASSETS
user_STOCK_name = int
user_STOCK_amount = int


#=================== CRYPTO ===================#  

def fetch_price_crypto(name):
    url = 'https://api.coingecko.com/api/v3/simple/price?ids=' + name + '&vs_currencies=usd'

    print('url', url)
    response = requests.get(url)
    price_data = response.json()
    
    return price_data[name]['usd']  # returns value

BTC_price = fetch_price_crypto('bitcoin')  # USD

# PRICE OF USER'S ASSETS
user_BTC_price = user_BTC_amount * BTC_price

### *** *** *** CONVERT *** *** *** ### 
if user_euro != True:
    CURRENCY_TAG = 'USD'

else:
    dollar_to_eur = c.convert(1, 'USD', 'EUR')
    BTC_price      *= dollar_to_eur
    user_BTC_price *= dollar_to_eur
    CURRENCY_TAG = 'EUR'

### *** *** *** PRINT *** *** *** ### 
print('')
print(f'BTC: {BTC_price}{CURRENCY_TAG} || USER: {user_BTC_price}{CURRENCY_TAG}')  # EUR

#=================== STOCK ===================#  

def fetch_price_stock():
    url = 'https://markets.ft.com/data/funds/tearsheet/charts?s=SE0014261764:EUR'
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Failed to retrieve webpage, status code: {response.status_code}"
    
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find(class_="mod-ui-data-list__value")
    
    if not price_element:
        return "Price element not found"

    return price_element.get_text(strip=True)

# Fetch and print the stock price
print(fetch_price_stock())


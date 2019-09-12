#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

# Legacy address format
legacy_address = {
    # ---请修改钱包名称和钱包地址，以下为例子
    'A': '169BgJcHBFnnagWwzK5PemC7nYjc3EbMov',
    'B': '1N47gZghj55dF569cSrtkZLTaP8bdfHBbs',
    'C': '1AcpaEcJACmAEniQ1QfeLEGR986b9Bff5Y',
}

# ---请修改钱包名称，以下为例子
wallet_names = ['A', 'B', 'C']

sum_balance = 0

for name in wallet_names:
    # use blockchair explore

    # 1. download html code
    url_head = 'https://blockchair.com/bitcoin-sv/address/'
    url = url_head + legacy_address[name]
    content = requests.get(url).text

    # 2. use BeautifulSoup to analyze html
    bs = BeautifulSoup(content, 'html.parser')
    elem = bs.select('div[class="col-9 block__info pr-0 text-right"] \
                     > span')[0].text

    # 3. format output
    new_elem = elem.replace(',', '')
    sum_balance += float(new_elem)
    print('%s : %s' % (name, new_elem))

print('sum of bsv in wallets: %f' % sum_balance)

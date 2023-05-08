#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyfiglet import Figlet
import mmh3
import requests
import codecs
import sys
import urllib3

# urllib3'ün "InsecureRequestWarning" uyarısını devre dışı bırakır
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Favicon yazısını ASCII sanatı olarak oluşturur ve yazdırır
f = Figlet(font='slant')
print(f.renderText('favicon.py'))

# Hoşgeldiniz mesajını yazdırır
print('Hello, Welcome to the Favicon Hash Scanner by Ali Baykara')
# https://gist.github.com/yehgdotnet/b9dfc618108d2f05845c4d8e28c5fc6a

# İsteği gönderir ve favicon içeriğini base64 olarak kodlar
response = requests.get(sys.argv[1], verify=False)
favicon = codecs.encode(response.content, 'base64')

# MMH3 algoritmasını kullanarak favicon hash değerini hesaplar
hash = mmh3.hash(favicon)

# Shodan sorgusunu yazdırır
print('\nShodan search query: http.favicon.hash:' + str(hash))


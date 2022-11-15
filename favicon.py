#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('favicon.py'))

print('Hello Welcome Favicon Hash Scanner Ali Baykara')
#https://gist.github.com/yehgdotnet/b9dfc618108d2f05845c4d8e28c5fc6a

import mmh3
import requests
import codecs
import sys

response = requests.get(sys.argv[1],verify=False)
favicon = codecs.encode(response.content, 'base64')
hash = mmh3.hash(favicon)
print('\nShodan search query: http.favicon.hash:'+str(hash))

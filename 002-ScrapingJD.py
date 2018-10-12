#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
题目要求：
        爬取一个京东商品的详情页。
'''

import requests

url = "https://item.jd.com/7842699.html"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print( url + " 爬取失败。")

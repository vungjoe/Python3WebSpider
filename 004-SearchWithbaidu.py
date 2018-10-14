#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
题目要求：
	百度、360等搜索引擎通过关键词进行搜索
'''

import requests

keyword = "Python"
kv = {'wd':keyword}

try:
    r = requests.get("https://www.baidu.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败。")

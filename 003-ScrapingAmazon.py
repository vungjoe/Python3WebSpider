#!/usr/bin/python3
# -*- coding:utf-8 -*-

'''
题目要求：
	亚马逊网站设置了 User-Agent ，所以要通过修改 User-Agent 来跨国网站的拦截。
'''

import requests

url = "https://www.amazon.cn/gp/product/B07GGG5BQZ/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=merchandised-search-2&pf_rd_r=CHDJDJRB5JPNP2QA3XSR&pf_rd_r=CHDJDJRB5JPNP2QA3XSR&pf_rd_t=101&pf_rd_p=bd80b4a1-1eb3-4753-89e4-7f96382ebfa4&pf_rd_p=bd80b4a1-1eb3-4753-89e4-7f96382ebfa4&pf_rd_i=658413051"
kv = {'user-agent':'Mozilla/5.0'}

try:
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print(url + " 爬取失败。")

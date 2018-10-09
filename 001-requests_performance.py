#!/usr/bin/python3

import requests,time

for i in range(1,101):
    start = time.perf_counter()
    url = "https://www.baidu.com"
    r = requests.get(url)
    during = time.perf_counter() - start
    print("The time scrapying "+ url + " is " + "{:.2f}".format(during) +"s.")
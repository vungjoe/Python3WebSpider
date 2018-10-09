#!/usr/bin/python3
# -*- coding:utf-8 -*-

# author: vungjoe
# version: 0.1

'''
 题目要求：

尽管 Requests 库功能很友好、开发简单（其实除了import外只需一行主要代码），但其性能
与专业爬虫相比还是有一定差距的。请编写一个小程序，“任意”找个url，测试一下成功爬取100次
网页的时间。（某些网站对于连续爬取页面将采取屏蔽IP的策略，所以，要避开这类网站。）
请回复代码，并给出url及在自己机器上的运行时间。
'''

import requests,time

for i in range(1,101):
    start = time.perf_counter()
    url = "https://www.baidu.com"
    r = requests.get(url)
    during = time.perf_counter() - start
    print("The time scrapying "+ url + " is " + "{:.2f}".format(during) +"s.")
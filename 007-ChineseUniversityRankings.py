'''
爬取软科中国最好大学排名2018，网址http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html
要求输出排名、学校名称、分数。
	- 本例给出的是爬取静态网页
	- 
'''

import requests
from bs4 import BeautifulSoup
import bs4

# 从网络上获取大学排名网页内容

def getHTMLText(url):
	try:
		r = requests.get(url,timeout = 30)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ""

# 提取网页内容中的信息到合适的数据结构

def fillUnivList(ulist,html):
	soup = BeautifulSoup(html,"html.parser")
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[3].string])
	pass

# 利用数据结构展示并输出结果

def printUnivList(ulist,num):
	print("{:^10}\t{:^6}\t{:^10}".format("排名","大学名称","分数"))
	for i in range(num):
		u = ulist[i]
		print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
	print("Suc" + str(num))

def main():
	uinfo = []
	url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2018.html"
	html = getHTMLText(url)
	fillUnivList(uinfo,html)
	printUnivList(uinfo,20) # 排名前20的大学
main()

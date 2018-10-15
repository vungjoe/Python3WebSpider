import requests

url = 'http://m.ip138.com/ip.asp?ip='
ip = '114.114.114.114'
try:
    r = requests.get(url + ip)
    r.raise_for_status
    r.encoding = r.apparent_encoding
    print(r.text[:500])
except:
    print("爬取失败")
    

# -*- coding:utf-8 -*-

import requests
import os

url = 'https://www.nationalgeographic.com/content/dam/photography/rights-exempt/photos-of-the-week/181012-potw/01-potw-181012.adapt.885.1.jpg'
root = 'D:/230 - nationalgeographic/'
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
        print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')

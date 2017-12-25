'''
获取bing首页过去14天的背景图
'''
import requests
from urllib.request import urlretrieve
import time
import os

img_urls = []
for i in [0, 7]:
    timestamp = int(time.time() * 1000)
    url = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=%s&n=10&nc=%s&pid=hp&video=1&og=1' % (i, timestamp)
    r = requests.get(url)
    images = r.json()['images']
    for img in images:
        img_urls.append(img['url'])

for img_url in set(img_urls):
    idx = img_url.rfind('/')
    filename = '/tmp/' + img_url[idx:]
    print("get img|url=%s,filename=%s" % (img_url, filename))
    if os.path.exists(filename):
        print("file already exist|filename=%s" % filename)
        continue
    urlretrieve('https://cn.bing.com' + img_url, filename)

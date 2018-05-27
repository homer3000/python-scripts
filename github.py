#!/usr/bin/python
# coding=utf8

import urllib2
import cjson
import csv
import sys


reload(sys)
sys.setdefaultencoding('utf8')

url = 'https://api.github.com/search/repositories?q=python&page=1&per_page=100&sort=stars&order=desc'

resp = urllib2.urlopen(url).read()
# print resp

items = cjson.decode(resp)['items']
with open('github_python_repositories.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'description', 'html_url'])
    for item in items:
        writer.writerow([item['name'], item['description'], item['html_url']])


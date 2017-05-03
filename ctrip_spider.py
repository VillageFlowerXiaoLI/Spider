# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json

'''
携程的游记根据地点区分

<div class="despop_box">

'''

req_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'you.ctrip.com',
    'Referer': 'http://you.ctrip.com/place/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36', }


# 获取游记url
def get_travels_url():
    url = 'http://you.ctrip.com/travels'

    page = requests.get(url=, headers=req_headers).content  # .decode('utf-8')

    data = etree.HTML(page.decode('utf-8'))

    travels_url = data.xpath('//div[@class="despop_box/*"]')

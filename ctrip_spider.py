# -*- coding: utf-8 -*-

import requests
from random import randint
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
# [国内，亚洲，欧洲，北美洲，大洋洲，其他州]
# 指定或不指定区域
# 返回游记url
def get_travels_url(area=None):
    req_url = 'http://you.ctrip.com/travels'

    page = requests.get(url=, headers=req_headers).content  # .decode('utf-8')

    data = etree.HTML(page.decode('utf-8'))

    url_info = data.xpath('//div[@class="despop_box"]//a')

    if area != None:
        # 存在要求的位置名称
        for url in url_info:
            if url.text == area:
                return 'you.ctrip.com' + url.xpath('@href')
    else:
        # 不存在要求，返回随机游记
        index = randint(0, len(url_info) - 1)
        return 'you.ctrip.com' + url_info[index].xpath('@herf')

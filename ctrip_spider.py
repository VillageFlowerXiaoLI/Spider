# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json

'''
携程的游记根据地点区分

<div class="despop_box">

'''

req_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'you.ctrip.com',
    'Referer': 'http://you.ctrip.com/place/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36',
    "Content-Type": "application/json;charset=UTF-8"}


# 获取游记url


def get_travels_url():
    url = 'http://you.ctrip.com/travels'

from ctrip_spider import get_travel
import requests
from random import randint
from lxml import etree
import sqlite3

'''
<div class="ctd_main_body">
游记正文
<a title="点击查看原图">
各个图片  一篇游记可能很多
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


def get_html_root():
    travel_url = get_travel()

    page = requests.get(travel_url, headers=req_headers).content

    return etree.HTML(page.decode('utf-8'))


data = get_html_root()


def get_title():
    global data

    title = data.xpath('//title/text()')[0]


def get_content():
    global data


# 只取前五十张图片的url
def get_img_urls():
    global data

    img_info = data.xpath('//a[@title="%s"]' % ('点击查看原图'.decode('utf-8')))
    img_list = []
    for i in range(max(50, len(img_info))):
        img_list.appnd(img_info[i].xpath('@herf')[0])

    img_urls = '_'.join(img_list)

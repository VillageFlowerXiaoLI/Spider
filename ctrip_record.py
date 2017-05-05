# -*- coding: utf-8 -*-

from ctrip_spider import get_travel
import requests
from random import randint
from lxml import etree
import sqlite3

db_path = '/Users/duxinlu/Desktop/dachuang2017/dachuang.db'

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


def connect_db():
    db = sqlite3.connect(db_path)

    return db


def get_html_root():
    travel_url = get_travel()

    page = requests.get(travel_url, headers=req_headers, timeout=15).content

    return etree.HTML(page.decode('utf-8'))


data = get_html_root()


def get_title():
    global data
    title = data.xpath('//title/text()')[0].split('-')[0].strip()

    return title


# 内容不好抓
def get_content():
    global data

    # < div class ="ctd_main_body" >

    content = ''

    content_info = data.xpath('//div[@class="ctd_main_body"]//p')

    for i in content_info:
        if i.text == None:
            continue
        else:
            content += i.text + '_'

    return content


# 只取前五十张图片的url
def get_img_urls():
    global data

    img_info = data.xpath('//a[@share-pic="1"]')

    img_list = []
    for i in range(0, min(20, len(img_info))):
        img_list.append(img_info[i].xpath('@href')[0])

    img_urls = '_'.join(img_list)

    return img_urls


if __name__ == '__main__':
    db = connect_db()

    title = get_title()
    content = get_content()
    img_urls = get_img_urls()

    db.execute('insert into spider_data values ("ctrip","%s","%s","%s","%s");'
               % (get_travel(), title, content, img_urls))
    db.commit()
    db.close()

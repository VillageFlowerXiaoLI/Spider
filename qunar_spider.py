# -*- coding: utf-8 -*-

import requests
from lxml import etree
from random import randint

req_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'travel.qunar.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36', }


def get_travels_url():
    req_url = 'http://travel.qunar.com/travelbook/list.htm?order=hot_heat'

    page = requests.get(req_url, headers=req_headers, timeout=15).content

    data = etree.HTML(page.decode('utf-8'))

    url_info = data.xpath('//a[@data-beacon="click_guild_des"]')

    index = randint(0, len(url_info) - 1)

    return url_info[index].xpath('@href')[0]


def get_area_travels_url():
    tmp_url = get_travels_url()
    req_url = 'http://' + tmp_url[2:35] + tmp_url[50:] + '/hot_heat/1.htm'

    page = requests.get(req_url, headers=req_headers, timeout=15).content

    data = etree.HTML(page.decode('utf-8'))

    url_info = data.xpath('//ul[@class="b_strategy_list "]/li/h2/a')

    index = randint(0, len(url_info) - 1)

    return 'http://travel.qunar.com' + url_info[index].xpath('@href')[0]


def get_travel():
    return get_area_travels_url()


if __name__ == '__main__':
    print get_travel()

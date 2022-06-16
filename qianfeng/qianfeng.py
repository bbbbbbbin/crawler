'''
Author: cn_lion
Date: 2022-06-10 10:47:52
LastEditTime: 2022-06-13 20:03:57
description: description your project
FilePath: \crawler\qianfeng.py
'''
# -*- coding: utf-8 -*-


import random
import re
import time
from bs4 import BeautifulSoup
import urllib3
from lxml import etree
import json
import requests
requests.packages.urllib3.disable_warnings()

def get_website(url):
    data = None
    proxy_support = urllib3.PoolManager()
    headers = ["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36", 
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36", 
    "Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1944.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36", 
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F", 
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.116 Safari/537.36 Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.10",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.517 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36", 
    "Mozilla/5.0 (X11; CrOS i686 4319.74.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1500.55 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36", 
    "Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", 
    "Mozilla/5.0 (X11; CrOS i686 3912.101.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36", 
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17", 
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1309.0 Safari/537.17", 
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15", 
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14"]
    random_header = random.choice(headers)
    headers = {"User-Agent":random_header}
    '''
    headers = {"User-Agent":random_header,
                "Cookie" : "buvid3=589E073E-6139-AA49-8B7C-E2340E377C0192020infoc; \
                            CURRENT_FNVAL=4048; b_lsid=21C5A10B5_1815CB54C75; \
                            _uuid=A8DED99C-3B103-6572-9FA7-24CDCAF517AD94444infoc; \
                            buvid4=6B414246-214A-42D7-A919-F21EFAB4D37593791-022061318-TuRjxQsJ8l+dwOeYJTO0BA%3D%3D; \
                            buvid_fp=31aecddedde11f48e694821fc5fad0a1; \
                            CURRENT_BLACKGAP=0; blackside_state=0; \
                            sid=l8zrje6t; \
                            rpdid=|(um||kJl|JY0J'uYlluu~)||; \
                            b_timer=%7B%22ffp%22%3A%7B%22333.788.fp.risk_589E073E%22%3A%221815CB553C3%22%2C%22333.999.fp.risk_589E073E%22%3A%221815CB571A2%22%7D%7D"}
    '''
    req = proxy_support.request(method='Get', url=url, headers=headers)
    if req.status != 200:
        print('错误连接代码：{}'.format(req.status))
        time.sleep(600)
        print(req.data.decode('utf-8'))
        return get_website(url)
    return req.data.decode('utf-8')


# 静态解析
def parse_html(html):
    data = None
    if html == None:
        return None
    soup = BeautifulSoup(html, 'html.parser')
    et = etree.HTML(html)
    pages = soup.find(attrs={'class':'be-pager-total'})
    info = et.xpath('//*[@id="submit-video-list"]')

    print(pages, info)


# api获取up主视频数以及各个视频简要信息
def dy_get(uid, pn, pns):
    # 用户UID
    mid = uid
    # 页数
    pn = pn
    # pubdate, click, stow
    # 视频排序方式
    order = 'pubdata'
    url = "https://api.bilibili.com/x/space/arc/search?mid={0}&tid=0&pn={1}&order={2}&jsonp=jsonp".format(mid, pn, order)
    data = get_website(url)
    data = json.loads(data)
    if pns == 1:
        return data['data']['page']['count']
    else:
        return data['data']


# 获取各视频分p情况以及cid
def get_cid(bv):
    url = "https://api.bilibili.com/x/player/pagelist?bvid={0}&jsonp=jsonp".format(bv)
    data = get_website(url)
    data = json.loads(data)
    return data['data']


# 获取博主粉丝数和关注数
def get_fans(uid):
    url = 'https://api.bilibili.com/x/relation/stat?vmid={0}&jsonp=jsonp'.format(uid)
    data = get_website(url)
    data = json.loads(data)
    return data['data']


# 获取博主用户信息
def get_info(uid):
    url = 'https://api.bilibili.com/x/space/acc/info?mid={0}&jsonp=jsonp'.format(uid)
    data = get_website(url)
    data = json.loads(data)
    return data


# 处理视频相关json信息
def parse_videodata(data, dict):
    num = len(dict)
    if data['list']['tlist'] == 'null':
        print('该页未找到视频：{}'.format(num))
        return dict
    else:
        '''
        整理获取到的数据
        av : av号
        bv : bv号
        title : 视频标题
        comment : 评论数
        plays : 播放数
        length : 时长
        time : 创建时间
        description : 视频简介
        pic : 视频封面
        p : 分p情况
            cid : cid号码
            title : 分p标题
            length : 分p时长
        '''
        
        for l in data['list']['vlist']:
            dict[num] = {}

            dict[num]['av'] = l['aid']
            dict[num]['bv'] = l['bvid']
            dict[num]['title'] = l['title']
            dict[num]['comment'] = l['comment']
            dict[num]['plays'] = l['play']
            dict[num]['length'] = l['length']
            dict[num]['time'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(l['created']))
            dict[num]['description'] = l['description']
            dict[num]['pic'] = l['pic']

            dict[num]['p'] = {}
            pcid = get_cid(l['bvid'])
            n = 1
            for d in pcid:
                dict[num]['p'][n] = {}
                dict[num]['p'][n]['cid'] = d['cid']
                dict[num]['p'][n]['title'] = d['part']
                dict[num]['p'][n]['length'] = d['duration']
                n += 1
            num += 1
        return dict


def parse_userdata(data, dict):
    num = len(dict)
    if data['code'] == 0:
        data = data['data']
        dict[num] = {}
        dict[num]['mid'] = data['mid']
        dict[num]['name'] = data['name']
        dict[num]['sex'] = data['sex']
        dict[num]['pic'] = data['face']
        dict[num]['sign'] = data['sign']
        fans = get_fans(data['mid'])
        dict[num]['fans'] = fans['follower']
        dict[num]['follow'] = fans['following']
    return dict


if __name__ == '__main__':
    # html = get_website('https://www.famulei.com/services/match/tournament_list.php')
    dict = {}
    '''
    uid = 146668655
    counts = dy_get(uid, 1, 1)
    for i in range(1, int(int(counts)/30)+2):
        data = dy_get(uid, i, 0)
        dict = parse_videodata(data, dict)
    print(dict)
    '''
    for i in range(1,10000):
       data = get_info(i)
       time.sleep(1)
       dict = parse_userdata(data, dict)
    print(dict) 

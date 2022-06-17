'''
Author: cn_lion
Date: 2022-06-16 14:25:04
LastEditTime: 2022-06-18 00:16:58
description: description your project
FilePath: \vscode\crawler\job_boss\job_boss.py
'''
# -*- coding: utf-8 -*-

import random
import re
import time
from bs4 import BeautifulSoup
import urllib3
import urllib
from lxml import etree
import json
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import pandas as pd
import pickle
requests.packages.urllib3.disable_warnings()


def get_website(url):
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
    req = proxy_support.request(method='Get', url=url, headers=headers)
    if req.status != 200:
        print('错误连接代码：{}'.format(req.status))
        # ime.sleep(600)
        return None
        # return get_website(url)
    return req.data.decode('utf-8')


def get_citydata():
    citycode_data = {}
    data = get_website('https://www.zhipin.com/wapi/zpgeek/common/data/citysites.json')
    data = json.loads(data)
    for i in data['zpData']:
        if i["name"] not in citycode_data:
            citycode_data[i['name']] = i['code']
    return citycode_data


def init_browser():
    browser = webdriver.Chrome('crawler\chromedriver.exe')
    browser.get("https://login.zhipin.com/")
    time.sleep(10)
    pickle.dump(browser.get_cookies(),open("cookies.pkl", 'wb'))
    browser.quit()
    return browser


def get_url(job,city,pages,citycode):
    url = 'https://www.zhipin.com/c{0}/?query={1}&page={2}'.format(citycode[city], urllib.parse.quote(job), pages)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
    options.add_argument('-ignore-certificate-errors')
    options.add_argument('-ignore -ssl-errors')
    # option.add_argument("headless")
    browser = webdriver.Chrome('crawler\chromedriver.exe',chrome_options=options)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    browser.get(url)
    for cookie in cookies:
        browser.add_cookie(cookie)
    
    time.sleep(random.randrange(3,8))
    data = browser.find_element(By.CLASS_NAME, 'job-list')
    data = data.get_attribute('innerHTML')
    browser.quit()
    return(data)


def parse_html(html,jobs):
    num = len(jobs)
    p1 = re.compile(r'</em>(?P<finance>.*?)<em class="vline"></em>(?P<people>.*?)</p>')
    p2 = re.compile(r'</em>(?P<finance>.*?)<em class="vline">')
    p3 = re.compile(r'</em>(?P<people>.*?)</p>')
    soup = BeautifulSoup(html,"html.parser")
    lists = soup.select('li')
    for i in lists:
        jobs[num] = {}
        jobs[num]['工作标题'] = i.select(".job-name > a ")[0].get('title')
        jobs[num]['工作链接'] = i.select(".job-name > a ")[0].get('href')
        jobs[num]['工作地点'] = i.select(".job-area")[0].text
        jobs[num]['薪资'] = i.select('.red')[0].text
        jobs[num]['年限'] = i.select('p')[0].text[:-2]
        jobs[num]['学历'] = i.select('p')[0].text[-2:]
        jobs[num]['公司名'] = i.select('.name > a')[0].text
        jobs[num]['公司链接'] = i.select('.name > a')[0].get('href')
        jobs[num]['公司行业'] = i.select('.false-link')[0].text
        if p2.search(str(i.select('p')[1])) == None:
            jobs[num]['融资情况'] = None
            jobs[num]['人数'] = p3.search(str(i.select('p')[1])).group('people')
        else:
            jobs[num]['融资情况'] = p1.search(str(i.select('p')[1])).group('finance')
            jobs[num]['人数'] = p1.search(str(i.select('p')[1])).group('people')
        jobs[num]['标签'] = [x.text for x in i.select('.tag-item')]
        jobs[num]['福利'] = i.select('.info-desc')[0].text
        num += 1
    return jobs


if __name__ == '__main__':
    browser = init_browser()
    citycode = get_citydata()
    job = '数据分析'
    city = '广州'
    jobs = {}
    for i in range(10):
        print("正在获取第{}页".format(i+1))
        data = get_url(job, city, i+1, citycode)
        print("正在解析第{}页".format(i+1))
        jobs = parse_html(data, jobs)
        i += 1
    print('获取数据完成，正在写入数据')
    data = pd.DataFrame(jobs).T
    data.to_csv('data_{0}_{1}.csv'.format(city, job))
    print('结束')

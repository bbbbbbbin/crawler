'''
Author: cn_lion
Date: 2022-06-20 21:03:21
LastEditTime: 2022-06-28 21:27:28
description: description your project
FilePath: \vscode\crawler\job_lagou\job_lagou.py
'''
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
import sys
import pickle
requests.packages.urllib3.disable_warnings()



def init_browser():
    browser = webdriver.Chrome('crawler\chromedriver.exe')
    browser.get("https://passport.lagou.com/login/login.html")
    time.sleep(10)
    pickle.dump(browser.get_cookies(),open("crawler\job_lagou\cookies.pkl", 'wb'))
    browser.quit()
    return browser


if __name__ == '__main__':
    # browser = init_browser()
    job,city = '爬虫','广州'

    # 初始化浏览器，可以对浏览器进行登陆操作等，最终保持浏览器处于第一页的页面
    url = 'https://www.lagou.com/wn/jobs?kd={0}&city={1}&pn=1'.format(urllib.parse.quote(job),urllib.parse.quote(city))
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
    options.add_argument('-ignore-certificate-errors')
    options.add_argument('-ignore -ssl-errors')
    browser = webdriver.Chrome('crawler/chromedriver.exe',options=options)
    browser.maximize_window()
    cookies = pickle.load(open("crawler/job_lagou/cookies.pkl", "rb"))
    browser.get(url)
    for cookie in cookies:
        browser.add_cookie(cookie)
    html = browser.find_element(By.ID, 'jobList')
    html = html.get_attribute('innerHTML')
    soup = BeautifulSoup(html, "html.parser")
    pages = len(soup(class_ = re.compile('^lg-pagination-item lg-pagination-item')))
    print('共{}页'.format(pages))
    waiter = input('回车继续\n')


    # 回车后开始获取数据，通过模拟鼠标悬浮，获取到更多的职位信息的悬浮框
    jobs = {}
    b = 1
    p = re.compile(r'\[(?P<area>.*?)\]')
    while(b <= pages):
        print('获取第{}页信息'.format(b))
        num = len(jobs)
        a = 1
        html = browser.find_element(By.ID, 'jobList')
        html = html.get_attribute('innerHTML')
        soup = BeautifulSoup(html, "html.parser")
        lists_top = soup(class_ = re.compile('^item-top'))
        lists_bottom = soup(class_ = re.compile('^item-bom'))
        time.sleep(2)
        browser.execute_script("window.scrollTo(0,0)")
        for i,j in zip(lists_top,lists_bottom):
            jobs[num] = {}
            # jobs[num]['工作标题'] = i(re.compile('^p-top'))[0].select('a')[0].text
            try:
                mouse1 = browser.find_element(By.XPATH, '//*[@id="jobList"]/div[1]/div[{0}]/div[1]/div[1]/div[1]/a'.format(a))
            except:
                continue
            ActionChains(browser).move_to_element(mouse1).perform()
            time.sleep(0.5)
            h = browser.find_element(By.ID, 'jobList')
            h = h.get_attribute('innerHTML')
            s = BeautifulSoup(h, "html.parser")
            f = s(class_ = re.compile('^job_detail'))
            if len(f) == 0:
                continue
            jobs[num]['工作标题'] = f[0](class_ = re.compile('^modal_title_text'))[0].select('span')[0].text
            jobs[num]['薪资'] = f[0](class_ = re.compile('^modal_title_text'))[0].select('span')[1].text
            jobs[num]['城市'] = f[0](class_ = re.compile('^modal_title_discription'))[0].select('span')[0].text
            jobs[num]['地区'] = p.search(str(i.select('a')[0])).group('area')
            jobs[num]['年限'] = f[0](class_ = re.compile('^modal_title_discription'))[0].select('span')[1].text
            jobs[num]['学历'] = f[0](class_ = re.compile('^modal_title_discription'))[0].select('span')[2].text
            jobs[num]['职限'] = f[0](class_ = re.compile('^modal_title_discription'))[0].select('span')[3].text
            jobs[num]['职位详情'] = f[0](class_ = re.compile('^job_discription'))[0](class_ = re.compile('^job_info'))[0].text
            jobs[num]['具体地点'] = f[0](class_ = re.compile('^job_discription'))[0](class_ = re.compile('^job_info'))[1].text
            jobs[num]['公司名字'] = i(class_ = re.compile('^company-name'))[0].text
            if len(i(class_ = re.compile('^industry'))) == 0:
                jobs[num]['公司情况'] = None
            else:
                jobs[num]['公司情况'] = i(class_ = re.compile('^industry'))[0].text
            jobs[num]['职位标签'] = []
            for k in j.select('div')[0].select('span'):
                jobs[num]['职位标签'].append(k.text)
            jobs[num]['公司标签'] = j.select('div')[1].text
            browser.execute_script("window.scrollTo(0,{})".format(a*80))
            a += 1
            num += 1
        b+=1
        # 点击下一页
        try:
            browser.find_element(By.CLASS_NAME, 'lg-pagination-next').click()
        except:
            continue

    data = pd.DataFrame(jobs).T
    data.to_csv('crawler/job_lagou/lougou_data_{0}_{1}.csv'.format(city, job))
    browser.quit()
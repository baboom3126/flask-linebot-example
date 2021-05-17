# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup		#匯入套件
import requests		#將套件匯入
from selenium import webdriver

url = 'https://www.cwb.gov.tw/V8/C/'    #要下載的檔案或網站來源
driver = webdriver.Chrome('YOUR_CHROMEDRIVER_PATH')
driver.get(url)

html = driver.page_source

#driver.close()

sp = BeautifulSoup(html, 'html.parser')
low = sp.find_all(class_="low")
height = sp.find_all(class_="height")
for i in range(0,3):
    print(low[i].text,height[i].text)

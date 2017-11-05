
# coding: utf-8

# In[ ]:

from selenium import webdriver
import time
import os
import csv

#環境設定
chrome_path=os.getcwd()
chrome_path+="\\chromedriver.exe"

n=int(input("開啟帳號數量"))
url=input("直播URL")

#with open('F.csv', 'r', newline='', encoding='utf-8') as csvfile: 
f=open("3.txt",'r',newline="")
l=[]
for i in f:
    l.append(i.split())
    
#填入帳密表單!!
email_list=[]
pass_list=[]

#瀏覽器自動化開啟
web=[]
for i in range(n):
    web.append("")
    web[i] = webdriver.Chrome(chrome_path)
    web[i].get(url)
    web[i].set_window_position(0,0) #瀏覽器位置
    web[i].set_window_size(200,200) #瀏覽器大小
    email_input = web[i].find_element_by_id("email")
    email_input.send_keys(l[i][0])
    pass_input = web[i].find_element_by_id("pass")
    pass_input.send_keys(l[i][1])
    web[i].find_element_by_id("loginbutton").click()
    web[i].get(url)



# coding: utf-8

# In[16]:

from selenium import webdriver
import time
import os

#環境設定
chrome_path=os.getcwd()
chrome_path+="\\chromedriver.exe"

n=int(input("開啟帳號數量"))
url=input("直播URL")

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
    web[i].set_window_size(700,700) #瀏覽器大小
    email_input = web[i].find_element_by_id("email")
    email_input.send_keys(email_list[i])
    pass_input = web[i].find_element_by_id("pass")
    pass_input.send_keys(pass_list[i])
    web[i].find_element_by_id("loginbutton").click()
    web[i].get(url)


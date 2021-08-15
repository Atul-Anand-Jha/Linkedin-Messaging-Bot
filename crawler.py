"""
# !pip install selenium 

# !pip install beautifulsoup4
"""
# This program will read users from the excel file and send them automated messages one by one.

import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
import time
from tqdm import tqdm
import pandas as pd
from selenium import webdriver

# replace with Linkedin Username / Password
uname = 'abc123@gmail.com'
passwd = 'xxxyyyZZZ321abc'


file = pd.read_excel("./targets_list.xlsx")
target_names = file['username'].values
target_urlLinks = file["link"].values
print(target_names)


browser = webdriver.Chrome(executable_path="./chromedriver_linux64/chromedriver")

browser.get('https://www.linkedin.com/login')

elementID = browser.find_element_by_id('username')
elementID.send_keys(uname)
elementID = browser.find_element_by_id('password')
elementID.send_keys(passwd)
elementID.submit()

for name, fullLink, i in zip(target_names, target_urlLinks, tqdm(range(len(target_names)))):
	browser.implicitly_wait(2)
	target_name = name.split()[0]
	browser.get(fullLink)
	browser.implicitly_wait(2)
	message_body = f"Hi {target_name},\n\nI hope this message finds you well.\nI am sending this message just to test it for the educational purposes.\n\nPlease, Don't Use it for any un-ethical purposes. Otherwise, You LI profile could be permanently deleted.\n\nPlease, visit this link : https://kaggle.com/atulanandjha/.\n\nShow some love with your upvotes, and leave your precious feedback in the comment section.\nStay tuned.\n\nThanks,\n-Atul"
	browser.find_element_by_class_name("message-anywhere-button").click()
	browser.find_element_by_class_name('msg-form__contenteditable').send_keys(message_body)
	browser.find_element_by_class_name("msg-form__send-button").click()
	browser.implicitly_wait(2)
	browser.switch_to.active_element
	browser.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]").click()
	browser.implicitly_wait(1)

print("Successfully sent messages to all {len(target_names)} targets. !!!")

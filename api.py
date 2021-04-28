import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random

def get_likes_page(browser,link_fb):
    json_data_like_page = open('like_page.json', 'a+')
    #browser = webdriver.Chrome(executable_path="../chromedriver_win32/chromedriver88.exe")
    #link = str(link_fb) +  "/likes"
    browser.get(link_fb)
    like_data = {}
    like_data['Link user'] = link_fb
    pages = []
    #scroll to load data
    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        sleep(random.randint(1,3))
        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    a_tag = browser.find_elements_by_class_name("gpro0wi8")
    print(len(a_tag))
    for a in a_tag:
        link = a.get_attribute('href')
        print(link)
        pages.append(link)
    like_data['Liked Pages'] = pages
    json.dump(like_data, json_data_like_page)
    json_data_like_page.write("\n")
    json_data_like_page.close()
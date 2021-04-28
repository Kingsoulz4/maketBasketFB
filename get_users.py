from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from selenium.webdriver.chrome.options import Options
import json
import api
    

# Pass popup notifation
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
} )
# define webdriver variable 
browser = webdriver.Chrome(chrome_options=option,executable_path="../chromedriver_win32/chromedriver88.exe")
browser.get("http://facebook.com")
sleep(random.randint(1, 5))
#login to Facebook
email_box = browser.find_element_by_id("email")
sleep(random.randint(1, 5))
email_box.send_keys("kingsoulz4e@gmail.com")
password_box = browser.find_element_by_id("pass")
sleep(random.randint(1, 5))
password_box.send_keys("Playgamenow")
sleep(random.randint(1, 5))
password_box.send_keys(Keys.ENTER)
sleep(random.randint(5, 8))

#crawler
fb_data = open('datafb.json', 'w+')
sleep(1)
browser.get("https://www.facebook.com/groups/hoinguoidammenhiepanh/members")
sleep(random.randint(2,8))

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

#Get data    
mem_element = browser.find_elements_by_class_name("nc684nl6")
users = []
for m in mem_element:
    data = {}
    mem = m.find_elements_by_css_selector("*")
    if(len(mem)==1):
        link_fb = mem[0].get_attribute('href')
        full_name = mem[0].text 
        if link_fb != None:
            data['Name'] = full_name
            data['Link Facebook'] = link_fb
            users.append(link_fb)
            json.dump(data, fb_data)
            fb_data.write("\n")
            #api.get_likes_page(browser,str(link_fb)+"/likes")
# Stand 10 second
fb_data.close()
sleep(20)
#Close browser
#browser.close()
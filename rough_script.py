# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 01:22:22 2021

@author: preet
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# configuring chrome driver for brave browser
# skip the binary_location if running on chrome
options = Options()
# options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = "C:/Users/zeels/Desktop/projects/walmart_scraper/chromedriver.exe"
browser = webdriver.Chrome(  executable_path = driver_path)

# get our product url
url = "https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-\
    Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365"
browser.get(url)

# trying to execute a class name selection
element_class1=browser.find_elements_by_class_name("w_Cl")
print(element_class1)
"""
Action Chains Class helps us simulate complex browser actions like scrolling\
to a certain location of a webpage, doubleclicks, etc.
"""
from selenium.webdriver import ActionChains
action_chains = ActionChains(browser)
action_chains.pause(5)
action_chains.move_by_offset(0, 1000)
action_chains.move_by_offset(0, -1000)

# Use the explicit wait method till our browser page loads the button beforeshowing an error

from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
max_duration = 10
try:
    wait_element = WebDriverWait(browser, max_duration).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='item-review-section']/div[2]/a[1]")       
    ))
except TimeoutException as e:
    print('Loading Exceeds Delay Time')
else:
    print(wait_element.get_attribute('innerHTML'))

# get the params to scroll to 'see all reviws' button
element =  browser.find_element_by_xpath("id='item-review-section']/div[2]/a[1]")
# element = browser.find_element_by_class_name('w_Cr no-underline ba br-pill pa1 pl3 pr3 items-center b f6 tl mr2')
print(element)


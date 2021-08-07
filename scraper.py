# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 01:42:22 2021

@author: preet
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException

"""
# configuring chrome driver for brave browser
# skip the binary_location if running on chrome
options = Options()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
browser = webdriver.Chrome(options= options, executable_path = driver_path)
"""

driver_path = "C:/Users/zeels/Desktop/projects/walmart_scraper/chromedriver.exe"
browser = webdriver.Chrome(  executable_path = driver_path)

# get our product url
url = "https://www.walmart.com/ip/Clorox-Disinfecting-Wipes-225-Count-\
    Value-Pack-Crisp-Lemon-and-Fresh-Scent-3-Pack-75-Count-Each/14898365"
browser.get(url)

browser.implicitly_wait(5)
element = browser.find_element_by_xpath('//*[@id="customer-reviews-header"]/div[2]/div/div[3]/a[2]/span')
# element =  browser.find_element_by_xpath('//*[@id="customer-reviews-header"]/div[2]/div/div[3]/a[2]/span')
print(element)

# scroll to desired element, the code works just fine without scrolling too
# element.location
# element.size

"""
Action Chains Class helps us simulate complex browser actions like scrolling\
to a certain location of a webpage, doubleclicks, etc.
"""

from selenium.webdriver import ActionChains
action_chains = ActionChains(browser)
# action_chains.move_to_element_with_offset(element, 0, 10*element.size['height']).perform()
browser.implicitly_wait(5)
action_chains.click(element).perform()
product_id = browser.current_url.split('/')[-1]
print(product_id)

# select newest first from the dropdown
from selenium.webdriver.support.ui import Select
element_dropdown_exchange = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div[5]/div/div[2]/div/div[2]/div/div[2]/select')
selection_exchange = Select(element_dropdown_exchange)
selection_exchange.select_by_visible_text('newest to oldest')

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

review_data = pd.DataFrame(columns=['Review date', 'Reviewer name', 'Review title', 'Review body', 'Ratings'])
primary_url=browser.current_url
for j in range(1,30):
    browser.get(primary_url+"&page="+str(j))
    response = browser.page_source
    soup = BeautifulSoup(response, 'lxml')
    date=[]
    name=[]
    title=[]
    reviews=[]
    rating=[]
    [date.append(i.text) for i in soup.findAll("div",{'class':"review-date"})]    
    [name.append(i.text) for i in soup.findAll("div",{'class':"review-user"})]
    # [title.append(i.text) for i in soup.findAll("h3",{'itemprop':"name"})]
    [reviews.append(i.text) for i in soup.findAll("div",{'class':"review-body"})]
    [rating.append(i.find("span",{'class':"visuallyhidden seo-avg-rating"}).text)\
     for i in soup.findAll("div",{'class':"review-heading"})]
    """
    Our reviews has missing values for title in several number of entries,
    so we need to modify our rule for the titles
    """
    
    for i in soup.findAll("div",{'class':"review-heading"}):
        title_present = bool(len(i.findAll("h3")))
        if (title_present):
            title.append(i.find("h3").text)
        else :
            title.append(np.nan)
    rev={'Review date':date, 'Reviewer name':name, 'Review title':title,\
         'Review body':reviews, 'Ratings':rating}
    
    review_data= review_data.append(pd.DataFrame.from_dict(rev), ignore_index=True)
# review_data
review_data['Reviewer name'] = review_data['Reviewer name'].str.replace('Reviewed by ','')
review_data['Review date'] = review_data['Review date'].str.replace('Verified purchase','')
review_data['Review date'] = pd.to_datetime(review_data['Review date'])
review_data = review_data.set_index(['Review date'])
review_data= review_data[review_data.index > pd.to_datetime('2020-12-01')]
review_data.to_csv('output.csv')
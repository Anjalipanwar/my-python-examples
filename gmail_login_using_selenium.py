# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:36:22 2016

@author: Anjali Panwar
"""
# Gmail Login using Selenium in Firefox

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#driver = webdriver.Ie() 
driver = webdriver.Firefox()

driver.get("https://accounts.google.com")

time.sleep(5)

email = driver.find_element_by_name('Email')
email.send_keys('your gmail email id')
email.send_keys(Keys.RETURN)

time.sleep(5)

pwrd = driver.find_element_by_name('Passwd')
pwrd.send_keys('your password')
pwrd.send_keys(Keys.RETURN)

time.sleep(15)

driver.close()
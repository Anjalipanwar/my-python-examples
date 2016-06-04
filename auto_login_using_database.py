# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:53:03 2016

@author: Anjali Panwar
"""

# Reads email id's and password's reside in DB and writes the success and failure in excel.

'''
NOTE : 

SERVER = ec2-50-157-100-000.compute-1.amazonaws.com 
DATABSE = Testdatabse
UID = anjali
PWD = password
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyodbc
import time 
import xlwt

wb = xlwt.Workbook()
sheet1= wb.add_sheet('Report') 

connection = pyodbc.connect('DRIVER={SQL Server}; SERVER= your server name; DATABASE= your databse name ; UID= your user id/name ;PWD=password')
cursor = connection.cursor()

sql_data = []

cursor.execute("SELECT * FROM Table Name")
data = cursor.fetchall()
 
sql_data = data
cursor.close()
connection.close()

for i in range(0,len(sql_data)):
          
        driver = webdriver.Firefox()
        driver.get("https://accounts.google.com")
        time.sleep(2)
    
        try:
            username = driver.find_element_by_name('Email')
        #        username.send_keys(str(list_data[0].value))
            username.send_keys(sql_data[i][5])        
            username.send_keys(Keys.RETURN)
        
            time.sleep(2)
            username = driver.find_element_by_name('Passwd')
        #    username.send_keys(str(list_data[1].value))
            username.send_keys(sql_data[i][6])    
            username.send_keys(Keys.RETURN)
           # print 'Success--> ', list_data[0].value
            
            time.sleep(5)
            logout = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/a")
            logout.send_keys(Keys.RETURN)
                
            signout = driver.find_element_by_id('gb_71')
            signout.send_keys(Keys.RETURN)
            print 'Working'
    
            sheet1.write(i,2,'Successfull')
            
        except:
            
             pass
             sheet1.write(i,2,'Failure')
             wb.save('D:/loginDB_report.xls')
             time.sleep(5)
        driver.close()

    
        

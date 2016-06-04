# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:53:03 2016

@author: Anjali Panwar
"""

#Imports data from database and write it into excel


'''
NOTE :

SERVER = ec2-50-157-000-000.compute-1.amazonaws.com
DATABSE = Testdatabse
PWD = password

'''
import pyodbc
import xlwt

wb = xlwt.Workbook()
sheet1= wb.add_sheet('Report') 

connection = pyodbc.connect('DRIVER={SQL Server}; SERVER= your sever path; DATABASE= your database name; UID=sa;PWD= your password')
cursor = connection.cursor()

cursor.execute("SELECT * FROM table name")
data = cursor.fetchall()
data_list  =[]

data_list = data

print data_list
cursor.close()
connection.close() 

for i in range(0,len(data_list)):
    for j in range(0,len(data_list[i])):
        sheet1.write(i,j,data_list[i][j])
wb.save('D:/excel_report.xls')


    
        

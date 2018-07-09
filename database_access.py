# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 18:34:30 2016

@author: Anjali Panwar
"""

import MySQLdb
import sys

'''
NOTE:  Example Input

host = ec2-54-000-139-333.compute-1.amazonaws.com
user = anjali
passwd = password
port = 1000

'''

connection = MySQLdb.connect (host = "Place your server id here as mentioned above", 
user = "a", passwd = "1234", db = "TestDB", port = 1000)

cursor = connection.cursor ()
cursor.execute ("select Col1, Col2 from TableName")
data = cursor.fetchall()

for row in cursor.fetchall():
    print row
    
cursor.close()
connection.close()

sys.exit()

    

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 12:24:13 2016

@author: Anjali Panwar
"""

# This script fetches the data written in a cell from excel 


import xlrd

#Open and read excel
work_book = xlrd.open_workbook('D:/samplefile.xlsx')

#Print number of sheets
#print work_book.nsheets()

#Print sheet name
print "Sheet Name : " , work_book.sheet_names()

#Get the first work sheet
first_sheet = work_book.sheet_by_index(0)

#Read a row
print "Row data : " , first_sheet.row_values(0)

#Read a cell
cell = first_sheet.cell(0,0)
print "Cell : " , cell
print "Cell Value : " , cell.value

#Read a row slice 
first_sheet.row_slice(rowx=1, start_colx=0, end_colx=3)

#Print all data of excel
for i in xrange(0,first_sheet.nrows):
    cells = first_sheet.row_slice(rowx=i, start_colx=0, end_colx=first_sheet.ncols)
    for cell in cells:
       print cell.value
       

for i in xrange(0,first_sheet.nrows):
    list = [first_sheet.row_slice(rowx=i, start_colx=0, end_colx=first_sheet.ncols)]
    print list







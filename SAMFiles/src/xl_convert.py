#--------------------------------------------------
# Title : xl_convert 
#--------------------------------------------------
#--------------------------------------------------
# Author   |  Date             |  Notes
#--------------------------------------------------
# antleypk | 10 - AUG - 2018   | Created
#--------------------------------------------------
#--------------------------------------------------

import xlrd
import csv
import os

#converts American Ninja Warrior .xlsx to anowh.csv

def csv_from_excel():
    wb = xlrd.open_workbook('ninja_data/American Ninja Warrior Obstacle History.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('ninja_data/anwoh.csv', 'w')
    wr = csv.writer(your_csv_file, quoting = csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))
    
    your_csv_file.close()




csv_from_excel()


import xlrd

book = xlrd.open_workbook("SOWC 2014 Stat Tables_Table 9.xlsx")

for sheet in book.sheets():
    print sheet.name

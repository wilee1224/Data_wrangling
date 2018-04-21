import xlrd

book = xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')
sheet = book.sheet_by_name('Table 9 ')

# for sheet in book.sheet():
# print sheet.nrows
count = 0
data = {}

for i in xrange(sheet.nrows):
    if count < 20:
        if i >= 14:
            row = sheet.row_values(i)
            country = row[1]
            data[country] = {}
    count += 1

print data
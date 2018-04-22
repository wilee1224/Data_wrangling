import xlrd

book = xlrd.open_workbook('SOWC 2014 Stat Tables_Table 9.xlsx')
sheet = book.sheet_by_name('Table 9 ')

# for sheet in book.sheet():
# print sheet.nrows

data = {}

for i in xrange(14, sheet.nrows):
    row = sheet.row_values(i)
    country = row[1]

    data[country] = {
        'child_labor' : {
            'total' : [row[4], row[5]],
            'male' : [row[6], row[7]],
            'female' : [row[8], row[9]],
        },
        'child_marriage' : {
            'marriage_by_15' : [row[10], row[11]],
            'marriage_by_18' : [row[12], row[13]],
        }
    }

print data['Afghanistan']

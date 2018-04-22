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
            'total' : [],
            'male' : [],
            'female' : [],
        },
        'child_marriage' : {
            'marriage_by_15' : [],
            'marriage_by_18' : [],
        }
    }

print data['Afghanistan']

import xlrd


excel1 = xlrd.open_workbook("1.xls")
excel2 = xlrd.open_workbook("2.xls")
excel3 = xlrd.open_workbook("3.xls")
sheet1 = excel1.sheet_by_name("Mysheet")
sheet2 = excel2.sheet_by_name("Sheet1")
sheet3 = excel3.sheet_by_name("Sheet1")
data1 = []
data2 = []
data3 = []
for i in range(sheet1.nrows):
    dat = sheet1.row_values(i)[0]
    data1.append(dat)

for i in range(sheet2.nrows):
    dat = sheet2.row_values(i)[0]
    data2.append(dat)

for i in range(sheet3.nrows):
    dat = sheet3.row_values(i)[0]
    data3.append(dat)


for i in range(len(data2)):
    if(data2[i] not in data1):
        data2.append(data2[i])
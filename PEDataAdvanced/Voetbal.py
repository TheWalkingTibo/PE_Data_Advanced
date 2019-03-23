import xlrd

file = "voetbal.xlsx"
workbook = xlrd.open_workbook(file)

sheet = workbook.sheet_by_index(0)
#print(sheet.cell_value(0, 0))
#print(sheet.nrows)

for kolom in range(sheet.ncols):
    print(sheet.cell_value(0, kolom), end="\t\t")


#datum1 = datetime.strptime()
#datum2 = datetime.strptime();

#print(random_date(d1, d2))

#files Used: https://www.youtube.com/watch?v=p0DNcTnreuY

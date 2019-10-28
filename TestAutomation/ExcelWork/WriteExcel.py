import openpyxl

wk = openpyxl.Workbook()
print(wk.active.title)
sh = wk.active
sh.title="HelloTestingWorld"
print(sh.title)

# Second Sheet is created
wk.create_sheet(title="TestingW")
sh1= wk['TestingW']
sh1['A3']="8585635"

# Remove sheet
wk.remove(wk['HelloTestingWorld'])

sh['A4'].value="www.thetestingworld.com"
wk.save("C:\\Users\\geefu\\OneDrive\\Documents\\PySheet.xlsx")
import xlsxwriter
import time
import keyboard

test = 0
uid = 2333
time = str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
name = str(uid)+' '+time+".xlsx"
workbook = xlsxwriter.Workbook(str(name))
worksheet = workbook.add_worksheet(str(uid))
worksheet.write(0,0,'0.0')
worksheet.write(1,0,'1.0')
worksheet.write(0,1,'0.1')
workbook.close()

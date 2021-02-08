import keyboard
import requests
import time
import xlsxwriter

l = 0
tn = str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
print("""

███████╗ ███████╗ ███╗   ██╗ ██████╗ 
██╔══██╗ ██╔════╝ ████╗  ██║ ██╔══██╗
██████╔╝ █████╗   ██╔██╗ ██║ ██████╔╝
██╔══██╗ ██╔══╝   ██║╚██╗██║ ██╔══██╗
██████╔╝ ██║      ██║ ╚████║ ██║  ██║
╚═════╝  ╚═╝      ╚═╝  ╚═══╝ ╚═╝  ╚═╝
                                                                   
""") #这个是用 http://patorjk.com/software/taag/ 做的
uid = int(input('输入你的B站UID:'))
t = int(input('输入刷新时间间隔:'))
print('按住E键终止记录(按下时间取决于你设置的时间间隔)')
name = str(uid)+' '+tn+".xlsx"
save = 1
workbook = xlsxwriter.Workbook(str(name))
worksheet = workbook.add_worksheet(str(uid))
url = 'https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % (uid)
while True:
    s = requests.get(url)
    ti = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(ti, "丨",s.json()["data"]["follower"])
    r = str((s.json()['data']['follower']))
    worksheet.write(l,0,ti)
    worksheet.write(l,1,r)
    l = l+1
    try:
        if keyboard.is_pressed('e'):
            workbook.close()
            print('终止记录')
            break
        if str(time.strftime("%H:%M", time.localtime())) == '00:00':
            if save == 0:
                save = 1
                workbool.close()
                name = str(uid)+' '+tn+".xlsx"
                workbook = xlsxwriter.Workbook(str(name))
                worksheet = workbook.add_worksheet(str(uid))
                pass
            pass
        if str(time.strftime("%H:%M", time.localtime())) == '00:01':
            save = 0 
            pass
        else:
            pass
    except:
        workbook.close()
        print('程序遇到问题终止,结果已保存')
        break
    time.sleep(t)
pass

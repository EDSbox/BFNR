import requests
import time

uid = int(input('输入你的B站UID:'))
t = int(input('输入刷新时间间隔:'))
url = 'https://api.bilibili.com/x/relation/stat?vmid=%s&jsonp=jsonp' % (uid)
while (0 == 0):
    a = ''
    s = requests.get(url)
    for __count in range(((129 - 7 * len(str((s.json()['data']['follower'])))) - 1)):
        a = (a + ' ')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), "丨",s.json()["data"]["follower"])
    r = str((s.json()['data']['follower']))
    L1 = a #从这里开始全都是数显的东西
    L2 = a
    L3 = a
    L4 = a
    L5 = a
    for i in range(0, len(r)):
        if (str(r[i]) == str('0')):
            L1 = str((L1 + '██████ '))
            L2 = str((L2 + '██  ██ '))
            L3 = str((L3 + '██  ██ '))
            L4 = str((L4 + '██  ██ '))
            L5 = str((L5 + '██████ '))
        if (str(r[i]) == str('1')):
            L1 = str((L1 + '  ██   '))
            L2 = str((L2 + '████   '))
            L3 = str((L3 + '  ██   '))
            L4 = str((L4 + '  ██   '))
            L5 = str((L5 + '██████ '))
        if (str(r[i]) == str('2')):
            L1 = str((L1 + '██████ '))
            L2 = str((L2 + '    ██ '))
            L3 = str((L3 + '██████ '))
            L4 = str((L4 + '██     '))
            L5 = str((L5 + '██████ '))
        if (str(r[i]) == str('3')):
            L1 = str((L1 + '██████ '))
            L2 = str((L2 + '    ██ '))
            L3 = str((L3 + '██████ '))
            L4 = str((L4 + '    ██ '))
            L5 = str((L5 + '██████ '))
        if (str(r[i]) == str('4')):
            L1 = str((L1 + '██  ██ '))
            L2 = str((L2 + '██  ██ '))
            L3 = str((L3 + '██████ '))
            L4 = str((L4 + '    ██ '))
            L5 = str((L5 + '    ██ '))
        if (str(r[i]) == str('5')):
            L1 = str((L1 + '██████ '))
            L2 = str((L2 + '██     '))
            L3 = str((L3 + '██████ '))
            L4 = str((L4 + '    ██ '))
            L5 = str((L5 + '██████ '))
        if (str(r[i]) == str('6')):
            L1 = str((L1 + '██████ '))
            L2 = str((L2 + '██     '))
            L3 = str((L3 + '██████ '))
            L4 = str((L4 + '██  ██ '))
            L5 = str((L5 + '██████ '))
        if (str(r[i]) == str('7')):
            L1 = str((L1 + '██████ '))
            L2 = str((L2 + '    ██ '))
            L3 = str((L3 + '    ██ '))
            L4 = str((L4 + '    ██ '))
            L5 = str((L5 + '    ██ '))
        if (str(r[i]) == str('8')):
            L1 = str((L1 + '██████ '))
            L2 = str((L2 + '██  ██ '))
            L3 = str((L3 + '██████ '))
            L4 = str((L4 + '██  ██ '))
            L5 = str((L5 + '██████ '))
        if (str(r[i]) == str('9')):
            L1 = str((L1 + '██████ '))
            L2 = str((L2 + '██  ██ '))
            L3 = str((L3 + '██████ '))
            L4 = str((L4 + '    ██ '))
            L5 = str((L5 + '    ██ '))
        if (str(r[i]) == str('-')):
            L1 = str((L1 + '       '))
            L2 = str((L2 + '       '))
            L3 = str((L3 + '██████ '))
            L4 = str((L4 + '       '))
            L5 = str((L5 + '       '))
        if (str(r[i]) == str(':')):
            L1 = str((L1 + '       '))
            L2 = str((L2 + '  ██   '))
            L3 = str((L3 + '       '))
            L4 = str((L4 + '  ██   '))
            L5 = str((L5 + '       '))
        if (str(r[i]) == str('丨')):
            L1 = str((L1 + '  ██   '))
            L2 = str((L2 + '  ██   '))
            L3 = str((L3 + '  ██   '))
            L4 = str((L4 + '  ██   '))
            L5 = str((L5 + '  ██   '))
        if (str(r[i]) == str(' ')):
            L1 = str((L1 + '       '))
            L2 = str((L2 + '       '))
            L3 = str((L3 + '       '))
            L4 = str((L4 + '       '))
            L5 = str((L5 + '       '))
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print(L1)
    print(L2)
    print(L3)
    print(L4)
    print(L5)
    print('')
    print('')
    print('')
    print('')
    print('')
    time.sleep(t)
pass

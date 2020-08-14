    for __count in range(((129 - 7 * len(str((s.json()['data']['follower'])))) - 1)):
        a = (a + ' ')#这个好像是一个计算屏幕宽度使数显居中的算法
    L1 = a
    L2 = a
    L3 = a
    L4 = a
    L5 = a
    for i in range(0, len(r)):#输入变量为r
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
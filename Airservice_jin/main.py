from internet import*
loopFlag = 1

def printMenu():
    print("*******************************************************")
    print("          실시간 항공운항 서비스입니다.")
    print("*******************************************************")
    print("                      Menu")
    print("          시간대별 국내선 검색: S")
    print("          시간대별 국제선 검색: L")
    print ("          공항별 국내선 검색: H")
    print("          정기 국내선 스케쥴 검색: A")
    print("======================Menu======================")

def launcherFunction(menu):
    if menu == 'S':
        timesearch()
    elif menu == 'A':
        airline()
    elif menu == 'L':
        oversea()
    elif menu == 'H':
        line()
    elif menu == 'T':
        schd()
    else:
        print("error : unknow menu key")

##### run #####
while (loopFlag > 0):
    printMenu()
    menuKey = str(input('select menu :'))
    launcherFunction(menuKey)
else:
    print("Thank you! Good Bye")




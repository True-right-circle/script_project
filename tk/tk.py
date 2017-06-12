from tkinter import *
from tkinter import font
import tkinter.messagebox
from internet import *


g_Tk = Tk()
g_Tk.geometry("700x650+750+200")
DataList = []

def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[항공정보 서비스 app]")
    MainText.pack()
    MainText.place(x=200)


def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=430, y=50)

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=15, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "공항 코드")
    SearchListBox.insert(2, "시간별 국내선")
    SearchListBox.insert(3, "시간별 국제선")
    SearchListBox.insert(4, "공항별 국내선")
    SearchListBox.insert(5, "정기 국내선")
    SearchListBox.pack()
    SearchListBox.place(x=230, y=50)

    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    TimeText=Label(g_Tk,text='시간입력(0000~2400)',font=TempFont)
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    TimeText.place(x=10,y=120)
    InputLabel.place(x=230, y=115)

def InitInputLabel2():
    global InputLabel2
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    PortText=Label(g_Tk,text='출발 공항코드입력',font=TempFont)
    InputLabel2 = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='ridge')
    InputLabel2.pack()
    PortText.place(x=10,y=170)
    InputLabel2.place(x=230, y=170)

def InitInputLabel3():
    global InputLabel3
    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    ArriText = Label(g_Tk, text='도착 공항코드입력', font=TempFont)
    InputLabel3 = Entry(g_Tk, font=TempFont, width=26, borderwidth=12, relief='ridge')
    InputLabel3.pack()
    ArriText.place(x=10, y=230)
    InputLabel3.place(x=230, y=230)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=550, y=120)

def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)  # ?댁쟾 異쒕젰 ?띿뒪??紐⑤몢 ??젣
    iSearchIndex = SearchListBox.curselection()[0]  # 由ъ뒪?몃컯???몃뜳??媛?몄삤湲?
    t=InputLabel.get()
    a=InputLabel2.get()

    if iSearchIndex==0:
        RenderText.insert(INSERT, "=============공항코드 정보=================")
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "김포 = GMP 김해 = PUS  대구 = TAE  제주 = CJU  \n광주 = KWJ 청주 = CJJ  포항 = KPO")
        RenderText.insert(INSERT, "  울산 = USN  \n진주 = HIN 원주 = WJU  양양 = YNY  여수 = RSU  \n목포 = MPK 군산 = KUV  무안 = MWX")
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, "==========================================")
    if iSearchIndex == 1:  # ?꾩꽌愿
        key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
        url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + "&schStTime=" + t + '&schEdTime=2400&schLineType=D'
        data = urllib.request.urlopen(url).read()
        # d = str(data,"utf-8")
        root = etree.fromstring(data)
        for child in root.iter("item"):
            airlin = child.find('airlineKorean').text
            start = child.find('boardingKor').text
            end = child.find('arrivedKor').text
            stime = child.find('std').text

            RenderText.insert(INSERT,'항공사 = ' + airlin +
                  '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
            RenderText.insert(INSERT,'\n')
            RenderText.insert(INSERT,'=================================================')
            RenderText.insert(INSERT,'\n')
            '''
        res = str(input("예약 하시겠습니까?  (Y/N)"))
        if res == 'Y':
            print('=======================================================')
            print('아시아나 = A  대한항공 = K  이스타항공 = E  제주항공 = J \n진에어항공 = JI  티웨이항공 = T  에어부산 = B')
            print('=======================================================')
            l = str(input("항공사를 선택하세요: "))
            if l == 'A':
                newurl = 'http://flyasiana.com/CW/ko/booking/bookingMain.do'
                return webbrowser.open_new(newurl)
            if l == 'K':
                newurl = 'https://kr.koreanair.com/korea/ko.html'
                return webbrowser.open_new(newurl)
            if l == 'E':
                newurl = 'https://www.eastarjet.com/newstar/PGWBA00001'
                return webbrowser.open_new(newurl)
            if l == 'J':
                newurl = 'https://www.jejuair.net/jejuair/com/jeju/ibe/availInit.do'
                return webbrowser.open_new(newurl)
            if l == 'JI':
                newurl = 'https://www.jinair.com/RSV/RSV_ScheduleSelect.aspx'
                return webbrowser.open_new(newurl)
            if l == 'T':
                newurl = 'https://www.twayair.com/main.do'
                return webbrowser.open_new(newurl)
            if l == 'B':
                newurl = 'https://www.airbusan.com/content/individual/'
                return webbrowser.open_new(newurl)
                '''
    elif iSearchIndex == 2:  # 紐⑤쾾?뚯떇
        key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
        url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + "&schStTime=" + t + '&schEdTime=2400&schLineType=I'
        data = urllib.request.urlopen(url).read()
        # d = str(data,"utf-8")
        root = etree.fromstring(data)

        RenderText.insert(INSERT,"          운항정보")
        RenderText.insert(INSERT,'\n')
        '''
        for child in root.iter("response"):
            no = child.find('totalCount')
            if (no == None):
                RenderText.insert(INSERT,"\n          해당 지역은 운행 정보가 없습니다.\n")
        '''
        for child in root.iter("item"):
            airlin = child.find('airlineKorean').text
            start = child.find('boardingKor').text
            end = child.find('arrivedKor').text
            stime = child.find('std').text

            RenderText.insert(INSERT,'항공사 = ' + airlin +
                  '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
            RenderText.insert(INSERT,'\n')
            RenderText.insert(INSERT,'=================================================')
            RenderText.insert(INSERT,'\n')

    elif iSearchIndex == 3:  # 留덉폆

        key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
        url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + \
              "&schStTime=" + t + '&schEdTime=2400&schLineType=D&schAirCode=' + a
        data = urllib.request.urlopen(url).read()
        # d = str(data,"utf-8")
        root = etree.fromstring(data)
        for child in root.iter("item"):
            airlin = child.find('airlineKorean').text
            start = child.find('boardingKor').text
            end = child.find('arrivedKor').text
            stime = child.find('std').text

            RenderText.insert(INSERT,'항공사 = ' + airlin +
                  '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
            RenderText.insert(INSERT,'\n')
            RenderText.insert(INSERT,'=================================================')
            RenderText.insert(INSERT,'\n')
            '''
            res = str(input("예약 하시겠습니까?  (Y/N)"))
            if res == 'Y':
                print('=======================================================')
                print('아시아나 = A  대한항공 = K  이스타항공 = E  제주항공 = J \n진에어항공 = JI  티웨이항공 = T  에어부산 = B')
                print('=======================================================')
                l = str(input("항공사를 선택하세요: "))
                if l == 'A':
                    newurl = 'http://flyasiana.com/CW/ko/booking/bookingMain.do'
                    return webbrowser.open_new(newurl)
                if l == 'K':
                    newurl = 'https://kr.koreanair.com/korea/ko.html'
                    return webbrowser.open_new(newurl)
                if l == 'E':
                    newurl = 'https://www.eastarjet.com/newstar/PGWBA00001'
                    return webbrowser.open_new(newurl)
                if l == 'J':
                    newurl = 'https://www.jejuair.net/jejuair/com/jeju/ibe/availInit.do'
                    return webbrowser.open_new(newurl)
                if l == 'JI':
                    newurl = 'https://www.jinair.com/RSV/RSV_ScheduleSelect.aspx'
                    return webbrowser.open_new(newurl)
                if l == 'T':
                    newurl = 'https://www.twayair.com/main.do'
                    return webbrowser.open_new(newurl)
                if l == 'B':
                    newurl = 'https://www.airbusan.com/content/individual/'
                    return webbrowser.open_new(newurl)

    elif iSearchIndex == 4:
        InitInputLabel3()
        key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
        url = 'http://openapi.airport.co.kr/service/rest/FlightScheduleList/getDflightScheduleList?ServiceKey=' + key + "&schDeptCityCode=" + a + "&schArrvCityCode=" +f
        data = urllib.request.urlopen(url).read()
        # d = str(data,"utf-8")
        root = etree.fromstring(data)
        for child in root.iter("item"):
            airlin = child.find('airlineKorean').text
            start = child.find('boardingKor').text
            end = child.find('arrivedKor').text
            stime = child.find('std').text

            RenderText.insert(INSERT, '항공사 = ' + airlin +
                              '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
            RenderText.insert(INSERT, '\n')
            RenderText.insert(INSERT, '=================================================')
            RenderText.insert(INSERT, '\n')

    RenderText.configure(state='disabled')
    '''



def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=230, y=230)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


InitTopText()
InitSearchListBox()
InitInputLabel()
InitInputLabel2()
InitSearchButton()
InitRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()
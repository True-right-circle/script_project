from tkinter import *
from tkinter import font
import tkinter.messagebox
from internet import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser

g_Tk = Tk()
g_Tk.geometry("470x650+750+200")
g_Tk.title('실시간 항공 운항 서비스')
g_Tk.resizable(width=TRUE, height=TRUE);
DataList = []


def mail(info):
    body=info
    from_addr = 'wlsdndnjs@gmail.com'
    msg=MIMEMultipart('alternative')
    msg['From'] = from_addr
    msg['To'] = InputMailLabel.get()
    msg['Subject'] = '요청하신 항공운항 정보입니다'     # 제목
    msg.attach(MIMEText(body, 'plain', 'utf-8')) # 내용 인코딩

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("forgamecapstone@gmail.com", "wlsdndnjs12")
        server.sendmail(from_addr, InputMailLabel.get(), msg.as_string())
        server.quit()
    except BaseException as e:
        print("failed to send mail", str(e))

def InitTopText():
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[실시간 항공운항 검색 서비스 app]")
    MainText.pack()
    MainText.place(x=70)


def InitAirPortButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    PortButton = Button(g_Tk, font = TempFont, text="공항코드 \n& \n항공사 사이트 주소",  command=PortButtonAction,width=20,height=5)
    PortButton.pack()
    PortButton.place(x=20, y=120)

def PortButtonAction():
    p_Tk = Tk()
    p_Tk.geometry("650x350")
    p_Tk.title("공항코드 및 항공사 주소")

    global RenderText1

    TempFont = font.Font(p_Tk, size=15, weight="bold", family='Consolas')
    porttext=Label(p_Tk,font=TempFont,text="[공항코드 및 항공사 주소]")
    porttext.pack()
    porttext.place(x=160)
    RenderText1 = Text(p_Tk, width=80, height=20, borderwidth=12, relief='ridge')
    RenderText1.pack()
    RenderText1.place(x=30, y=40)

    RenderText1.configure(state='disabled')
    RenderText1.configure(state='normal')
    RenderText1.delete(0.0, END)
    RenderText1.insert(INSERT, "=============공항코드 정보========================")
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, "김포 = GMP 김해 = PUS  대구 = TAE  제주 = CJU  \n광주 = KWJ 청주 = CJJ  포항 = KPO")
    RenderText1.insert(INSERT, "  울산 = USN  \n진주 = HIN 원주 = WJU  양양 = YNY  여수 = RSU  \n목포 = MPK 군산 = KUV  무안 = MWX")
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, "==================================================\n")
    RenderText1.insert(INSERT, "아시아나 항공 : http://flyasiana.com/CW/ko/booking/bookingMain.do")
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, "대한항공 : https://kr.koreanair.com/korea/ko.html")
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, "제주항공 : https://www.jejuair.net/jejuair/com/jeju/ibe/availInit.do")
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, "진에어항공 : https://www.jinair.com/RSV/RSV_ScheduleSelect.aspx")
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, "티웨이항공 : https://www.twayair.com/main.do")
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, "에어부산 : https://www.airbusan.com/content/individual/")
    RenderText1.insert(INSERT, '\n')
    RenderText1.insert(INSERT, '\n')

def InitSearchTimeButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchTimeButton = Button(g_Tk, font = TempFont, text="시간대별 국내선 검색",  command=STButtonAction,width=20,height=5)
    SearchTimeButton.pack()
    SearchTimeButton.place(x=20, y=250)

def STButtonAction():
    global InputLabel
    global InputMailLabel
    s_Tk=Tk()
    s_Tk.title("시간대별 국내선 검색")
    s_Tk.geometry("400x650")
    TempFont = font.Font(s_Tk, size=13, weight='bold', family='Consolas')
    TimeText = Label(s_Tk, text='시간입력(0000~2400)', font=TempFont)
    MailText= Label(s_Tk,text='메일주소입력',font=TempFont)
    InputLabel = Entry(s_Tk, font=TempFont, width=7, borderwidth=10, relief='ridge')
    InputMailLabel=Entry(s_Tk,font=TempFont,width=16,borderwidth=10,relief='ridge')
    InputLabel.pack()
    InputMailLabel.pack()
    TimeText.place(x=20, y=60)
    MailText.place(x=20,y=510)
    InputLabel.place(x=200, y=50)
    InputMailLabel.place(x=130,y=500)

    Search = Button(s_Tk, font=TempFont, text="검색", command=SearchAction)
    Search.pack()
    Search.place(x=300, y=55)

    mailb = Button(s_Tk, font=TempFont, text="보내기", command=Searchtimen)
    mailb.pack()
    mailb.place(x=300, y=505)

    global RenderText

    RenderTextScrollbar = Scrollbar(s_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=100, y=200)

    TempFont = font.Font(s_Tk, size=10, family='Consolas')
    RenderText = Text(s_Tk, width=45, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=20, y=100)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

def Searchtimen():
    t = InputLabel.get()
    key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + "&schStTime=" + t + '&schEdTime=2400&schLineType=D'
    data = urllib.request.urlopen(url).read()
    # d = str(data,"utf-8")
    root = etree.fromstring(data)
    b = '요청하신 정보입니다\n'

    for child in root.iter("item"):
        airlin = child.find('airlineKorean').text
        start = child.find('boardingKor').text
        end = child.find('arrivedKor').text
        stime = child.find('std').text

        a = '항공사=' + airlin + '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end + \
            '\n=======================================================\n'

        b += a
    mail(b)

def SearchAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    t=InputLabel.get()
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

        RenderText.insert(INSERT, '항공사 = ' + airlin +
                          '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, '=============================================')
        RenderText.insert(INSERT, '\n')


def searchoversee():
    b = InputLabel2.get()
    key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + "&schStTime=" + b + '&schEdTime=2400&schLineType=I'
    data = urllib.request.urlopen(url).read()
    # d = str(data,"utf-8")
    c = "요청하신 정보입니다\n"
    root = etree.fromstring(data)

    RenderText.insert(INSERT, "          운항정보")
    RenderText.insert(INSERT, '\n')

    for child in root.iter("item"):
        airlin = child.find('airlineKorean').text
        start = child.find('boardingKor').text
        end = child.find('arrivedKor').text
        stime = child.find('std').text

        a = '항공사=' + airlin + '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end + \
            '\n=======================================================\n'

        c += a
    mail(c)

def InitSearchBroadTimeButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchBroadTimeButton = Button(g_Tk, font = TempFont, text="시간대별 국제선 검색",  command=SBTButtonAction,width=20,height=5)
    SearchBroadTimeButton.pack()
    SearchBroadTimeButton.place(x=250, y=250)

def SBTButtonAction():
    global InputMailLabel
    global InputLabel2
    b_Tk = Tk()
    b_Tk.title("국제선 검색")
    b_Tk.geometry("400x650")
    TempFont = font.Font(b_Tk, size=13, weight='bold', family='Consolas')
    TimeText = Label(b_Tk, text='시간입력(0000~2400)', font=TempFont)
    MailText = Label(b_Tk, text='메일주소입력', font=TempFont)
    InputLabel2 = Entry(b_Tk, font=TempFont, width=7, borderwidth=10, relief='ridge')
    InputMailLabel = Entry(b_Tk, font=TempFont, width=16, borderwidth=10, relief='ridge')
    InputLabel2.pack()
    TimeText.place(x=20, y=60)
    MailText.place(x=15, y=510)
    InputLabel2.place(x=200, y=50)
    InputMailLabel.place(x=130, y=500)

    Search = Button(b_Tk, font=TempFont, text="검색", command=SearchBroadAction)
    Search.pack()
    Search.place(x=300, y=55)

    mailb = Button(b_Tk, font=TempFont, text="보내기", command=searchoversee)
    mailb.pack()
    mailb.place(x=300, y=505)


    global RenderText

    RenderTextScrollbar = Scrollbar(b_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=100, y=200)

    TempFont = font.Font(b_Tk, size=10, family='Consolas')
    RenderText = Text(b_Tk, width=45, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=20, y=100)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

def SearchBroadAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    b = InputLabel2.get()
    key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + "&schStTime=" + b + '&schEdTime=2400&schLineType=I'
    data = urllib.request.urlopen(url).read()
    # d = str(data,"utf-8")
    root = etree.fromstring(data)

    RenderText.insert(INSERT, "          운항정보")
    RenderText.insert(INSERT, '\n')

    for child in root.iter("item"):
        airlin = child.find('airlineKorean').text
        start = child.find('boardingKor').text
        end = child.find('arrivedKor').text
        stime = child.find('std').text



        RenderText.insert(INSERT, '항공사 = ' + airlin +
                          '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
        RenderText.insert(INSERT, '\n')
        RenderText.insert(INSERT, '=============================================')
        RenderText.insert(INSERT, '\n')

def InitSearchPortButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchPortButton = Button(g_Tk, font = TempFont, text="공항별 검색",  command=SPButtonAction,width=20,height=5)
    SearchPortButton.pack()
    SearchPortButton.place(x=20, y=400)


def SPButtonAction():
    global  InputMailLabel
    global InputLabel3
    global InputLabel4
    sp_Tk = Tk()
    sp_Tk.title("공항별 운항정보 검색")
    sp_Tk.geometry("400x800")
    TempFont = font.Font(sp_Tk, size=13, weight='bold', family='Consolas')
    TimeText = Label(sp_Tk, text='시간입력(0000~2400)', font=TempFont)
    LineText=Label(sp_Tk,text="공항코드입력",font=TempFont)
    MailText = Label(sp_Tk, text='메일주소입력', font=TempFont)
    InputLabel3 = Entry(sp_Tk, font=TempFont, width=7, borderwidth=10, relief='ridge')
    InputLabel4=Entry(sp_Tk,font=TempFont,width=7,borderwidth=10,relief='ridge')
    InputMailLabel = Entry(sp_Tk, font=TempFont, width=16, borderwidth=10, relief='ridge')
    InputLabel3.pack()
    InputLabel4.pack()
    TimeText.place(x=20, y=60)
    LineText.place(x=20,y=120)
    MailText.place(x=20, y=610)
    InputLabel3.place(x=200, y=60)
    InputLabel4.place(x=200,y=120)
    InputMailLabel.place(x=130, y=600)

    Search = Button(sp_Tk, font=TempFont, text="검색", command=SearchLineAction)
    Search.pack()
    Search.place(x=300, y=55)

    mailb = Button(sp_Tk, font=TempFont, text="보내기", command=Station)
    mailb.pack()
    mailb.place(x=300, y=605)


    global RenderText

    RenderTextScrollbar = Scrollbar(sp_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=100, y=200)

    TempFont = font.Font(sp_Tk, size=10, family='Consolas')
    RenderText = Text(sp_Tk, width=45, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=20, y=200)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

def SearchLineAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    t = InputLabel3.get()
    p=InputLabel4.get()

    key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + \
          "&schStTime=" + t + '&schEdTime=2400&schLineType=D&schAirCode=' + p
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
        RenderText.insert(INSERT, '=============================================')
        RenderText.insert(INSERT, '\n')


def Station():
    t = InputLabel3.get()
    p=InputLabel4.get()

    key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + \
          "&schStTime=" + t + '&schEdTime=2400&schLineType=D&schAirCode=' + p
    data = urllib.request.urlopen(url).read()
    b = "요청하신 자료입니다\n"
    # d = str(data,"utf-8")
    root = etree.fromstring(data)
    for child in root.iter("item"):
        airlin = child.find('airlineKorean').text
        start = child.find('boardingKor').text
        end = child.find('arrivedKor').text
        stime = child.find('std').text

        a = '항공사=' + airlin + '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end + \
            '\n=======================================================\n'

        b += a
    mail(b)

def InitSearchRegularButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchRegularButton = Button(g_Tk, font = TempFont, text="정기 스케줄 검색",  command=SRButtonAction,width=20,height=5)
    SearchRegularButton.pack()
    SearchRegularButton.place(x=250, y=400)

def SRButtonAction():
    global InputLabel5
    global InputLabel6
    global InputMailLabel
    r_Tk = Tk()
    r_Tk.geometry("400x600")
    r_Tk.title("정지운행 정보 검색")
    TempFont = font.Font(r_Tk, size=13, weight='bold', family='Consolas')
    TimeText = Label(r_Tk, text='출발공항코드', font=TempFont)
    LineText = Label(r_Tk, text="도착공항코드", font=TempFont)
    InputLabel5 = Entry(r_Tk, font=TempFont, width=7, borderwidth=10, relief='ridge')
    InputLabel6 = Entry(r_Tk, font=TempFont, width=7, borderwidth=10, relief='ridge')
    InputLabel5.pack()
    InputLabel6.pack()
    TimeText.place(x=20, y=60)
    LineText.place(x=20, y=120)
    InputLabel5.place(x=150, y=60)
    InputLabel6.place(x=150, y=120)

    Search = Button(r_Tk, font=TempFont, text="검색", command=SearchRLAction)
    Search.pack()
    Search.place(x=300, y=55)

    global RenderText

    RenderTextScrollbar = Scrollbar(r_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=100, y=200)

    TempFont = font.Font(r_Tk, size=10, family='Consolas')
    RenderText = Text(r_Tk, width=45, height=27, borderwidth=12, relief='ridge',
                      yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=20, y=200)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')

def SearchRLAction():
    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)
    RenderText.insert(INSERT, '해당 서비스가 종료되었습니다 죄송합니다')
    """
    a = InputLabel5.get()
    d = InputLabel6.get()
    key = 'Mpb2vh%2FkiADe0I%2B1mVP0MlW8TwXVBb%2Fbgi1yBrX36Yx4v6wDVgmaRZk9%2BvYNyh8%2FvSGbyx5tGExltmd9wfN%2FbQ%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightScheduleList/getDflightScheduleList?ServiceKey=' + key + "&schDeptCityCode=" + d + "&schArrvCityCode=" + a
    data = urllib.request.urlopen(url).read()
    # d = str(data,"utf-8")
    root = etree.fromstring(data)
    for child in root.iter("item"):
        airlin = child.find('airlineKorean').text
        start = child.find('startcity').text
        end = child.find('arrivalcity').text
        stime = child.find('domesticStartTime').text
        endtime = child.find("domesticArrivalTime").text

        mon = child.find("domesticMon").text
        tue = child.find("domesticTue").text
        wnd = child.find("domesticWed").text
        thus = child.find("domesticThu").text
        fri = child.find("domesticFri").text
        sat = child.find("domesticSat").text
        sun = child.find("domesticSun").text


       # RenderText.insert(INSERT, '항공사 = ' + airlin +
       #                  '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
       #RenderText.insert(INSERT,"Y = 이용가능 / N = 이용 불가능")
       #RenderText.insert(INSERT,
       #     "월요일 " + mon + "  " + "화요일 " + tue + "  " + "수요일 " + wnd + "  " + "목요일 " + thus + '\n' + "금요일 " + fri + "  " + "토요일 " + sat + "  " + "일요일 " + sun)
       """

def MapButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchPortButton = Button(g_Tk, font = TempFont, text="공항 위치 보기",  command=showimage,width=20,height=5)
    SearchPortButton.pack()
    SearchPortButton.place(x=250, y=120)

def showimage():
    global InputLabel7
    win = Tk()
    win.geometry("400x400")
    win.title("공항 지도 보기")
    TempFont = font.Font(win, size=13, weight='bold', family='Consolas')
    TimeText = Label(win, text='국내 공항 입력', font=TempFont)
    InputLabel7 = Entry(win, font=TempFont, width=10, borderwidth=10, relief='ridge')
    InputLabel7.pack()
    InputLabel7.place(x=180, y=65)
    TimeText.place(x=50, y=74)

    Search = Button(win, font=TempFont, text="검색", command=naver)
    Search.pack()
    Search.place(x=300, y=65)

    global RenderText2

    RenderText2 = Text(win, width=30, height=10, borderwidth=12, relief='ridge')
    RenderText2.pack()
    RenderText2.place(x=80, y=150)

    RenderText2.configure(state='disabled')
    RenderText2.configure(state='normal')
    RenderText2.delete(0.0, END)
    RenderText2.insert(INSERT, "========입력 공항 예시========")
    RenderText2.insert(INSERT, '\n')
    RenderText2.insert(INSERT, "김포  김해   대구   제주   \n광주  청주   포항 ")
    RenderText2.insert(INSERT, "  울산   \n진주  원주   양양   여수   \n목포  군산   무안 ")
    RenderText2.insert(INSERT, '\n')


def naver():
    rocation=InputLabel7.get()
    newurl = 'http://map.naver.com/?query='+rocation+'공항&type=SITE_1&siteOrder='
    return webbrowser.open_new(newurl)





InitTopText()
InitAirPortButton()
InitSearchTimeButton()
InitSearchBroadTimeButton()
InitSearchRegularButton()
InitSearchPortButton()
MapButton()


#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()
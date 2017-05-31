from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import xml.etree.ElementTree as etree
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def timesearch():
    time=input("시간대를 입력하세요(24시간 기준)")
    key='%2F3AEJBd1vcRO0ErsjC7gmLUi7WvMGdMrwgY86vbDyWsWun98FtVFl%2BJehIVuPPi%2B0jn7MSpRFMRQc00IUp11vg%3D%3D'
    url='http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey='+key+ "&schStTime="+time+'&schEdTime=2400&schLineType=D'
    data = urllib.request.urlopen(url).read()
    b = time+"시의 국내 운항정보 입니다.\n=======================================================\n"
    root=etree.fromstring(data)
    for child in root.iter("item"):
        airlin=child.find('airlineKorean').text
        start=child.find('boardingKor').text
        end=child.find('arrivedKor').text
        stime=child.find('std').text

        a = '항공사=' + airlin + '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end + \
            '\n=======================================================\n'

        b += a
    print(b)
    select = input("항공 정보를 메일로 보내시겠습니까? Y/N")
    if (select == 'Y'):
        mail(b)
    else:
        print("이용해 주셔서 감사합니다")

def airline():
    print("=============공항코드 정보=================")
    print("김포 = GMP 김해 = PUS  대구 = TAE  제주 = CJU  \n광주 = KWJ  청주 = CJJ  포항 = KPO")
    print("울산 = USN  진주 = HIN 원주 = WJU  양양 = YNY \n여수 = RSU  목포 = MPK  군산 = KUV  무안 = MWX")
    print("==========================================")
    start=input("출발공항 코드 입력 :")
    end=input("도착공항 코드 입력 : ")
    key='%2F3AEJBd1vcRO0ErsjC7gmLUi7WvMGdMrwgY86vbDyWsWun98FtVFl%2BJehIVuPPi%2B0jn7MSpRFMRQc00IUp11vg%3D%3D'
    url='http://openapi.airport.co.kr/service/rest/FlightScheduleList/getDflightScheduleList?ServiceKey='+key+ "&schDeptCityCode="+start+"&schArrvCityCode="+end
    data = urllib.request.urlopen(url).read()
    root=etree.fromstring(data)
    b = '입력하신 공항의 운항정보입니다.\n=======================================================\n'

    for child in root.iter("item"):
        airlin=child.find('airlineKorean').text
        start=child.find('startcity').text
        end=child.find('arrivalcity').text
        stime=child.find('domesticStartTime').text
        endtime=child.find("domesticArrivalTime").text

        mon = child.find("domesticMon").text
        tue = child.find("domesticTue").text
        wnd = child.find("domesticWed").text
        thus = child.find("domesticThu").text
        fri = child.find("domesticFri").text
        sat = child.find("domesticSat").text
        sun = child.find("domesticSun").text

        a = '항공사 = '+airlin +'\n출발시간 = '+stime+'\n도착시간 = '+endtime+'\n출발공항 = '+start+'\n도착공항 =' +end+\
            "\nY = 이용가능 / N = 이용 불가능"+"\n월요일 "+mon+"  "+"화요일 "+tue+"  "+"수요일 "+wnd+"  "+"목요일 "+thus+''                                                                                                                                                                                    '\n'+"금요일 "+fri+"  "+"토요일 "+sat+"  "+"일요일 "+sun\
            +"\n=======================================================\n"

        b += a
    print(b)
    select = input("항공 정보를 메일로 보내시겠습니까? Y/N")
    if (select == 'Y'):
        mail(b)
    else:
        print("이용해 주셔서 감사합니다")

def oversea():
    time=input("시간대를 입력하세요(24시간 기준)")
    key='%2F3AEJBd1vcRO0ErsjC7gmLUi7WvMGdMrwgY86vbDyWsWun98FtVFl%2BJehIVuPPi%2B0jn7MSpRFMRQc00IUp11vg%3D%3D'
    url='http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey='+key+ "&schStTime="+time+'&schEdTime=2400&schLineType=I'
    data = urllib.request.urlopen(url).read()
    #d = str(data,"utf-8")
    root=etree.fromstring(data)
    b = time + "시의 국제 운항정보 입니다.\n=======================================================\n"


    for child in root.iter("item"):
        airlin=child.find('airlineKorean').text
        start=child.find('boardingKor').text
        end=child.find('arrivedKor').text
        stime=child.find('std').text

        a = '항공사=' + airlin + '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end + \
            '\n=======================================================\n'

        b += a
    print(b)
    select = input("항공 정보를 메일로 보내시겠습니까? Y/N")
    if (select == 'Y'):
        mail(b)
    else:
        print("이용해 주셔서 감사합니다")

def line():
    print("=============공항코드 정보=================")
    print("김포 = GMP 김해 = PUS  대구 = TAE  제주 = CJU  \n광주 = KWJ  청주 = CJJ  포항 = KPO")
    print("울산 = USN  진주 = HIN 원주 = WJU  양양 = YNY \n여수 = RSU  목포 = MPK  군산 = KUV  무안 = MWX")
    print("==========================================")


    code = input("공항 코드를 입력하세요 : ")
    time = input("시간대를 입력하세요 : ")
    key = '%2F3AEJBd1vcRO0ErsjC7gmLUi7WvMGdMrwgY86vbDyWsWun98FtVFl%2BJehIVuPPi%2B0jn7MSpRFMRQc00IUp11vg%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + \
          "&schStTime=" + time + '&schEdTime=2400&schLineType=D&schAirCode='+code
    data = urllib.request.urlopen(url).read()
    b='입력하신 공항간의 정기운항 정보입니다.\n=======================================================\n'

    # d = str(data,"utf-8")
    root = etree.fromstring(data)
    for child in root.iter("item"):
        airlin = child.find('airlineKorean').text
        start = child.find('boardingKor').text
        end = child.find('arrivedKor').text
        stime = child.find('std').text
        
        
        a='항공사='+airlin+'\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end+\
          '\n=======================================================\n'

        b+=a
    print(b)
    select =input("항공 정보를 메일로 보내시겠습니까? Y/N")
    if(select=='Y'):
        mail(b)
    else:
        print("이용해 주셔서 감사합니다")


def mail(info):
    body=info
    gmail_user=input("구글 계정 ID :")
    gmail_pw=input('구글 계정 pass : ')
    from_addr = 'wlsdndnjs@gmail.com'
    to_addr=input("보낼 이메일 주소")
    msg=MIMEMultipart('alternative')
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = '요청하신 항공운항 정보입니다'     # 제목
    msg.attach(MIMEText(body, 'plain', 'utf-8')) # 내용 인코딩

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pw)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print('메일을 성공적으로 발송했습니다.')
    except BaseException as e:
        print("메일 발송에 실패했습니다.", str(e))
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import xml.etree.ElementTree as etree

def timesearch():
    time=input("시간대를 입력하세요")
    key='%2F3AEJBd1vcRO0ErsjC7gmLUi7WvMGdMrwgY86vbDyWsWun98FtVFl%2BJehIVuPPi%2B0jn7MSpRFMRQc00IUp11vg%3D%3D'
    url='http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey='+key+ "&schStTime="+time+'&schEdTime=2400&schLineType=D'
    data = urllib.request.urlopen(url).read()
    #d = str(data,"utf-8")
    root=etree.fromstring(data)
    for child in root.iter("item"):
        airlin=child.find('airlineKorean').text
        start=child.find('boardingKor').text
        end=child.find('arrivedKor').text
        stime=child.find('std').text

        print('항공사 = '+airlin +
              '\n출발시간 = '+stime+'\n출발공항 = '+start+'\n도착공항 = '+end)
        print('=======================================================')

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
    #d = str(data,"utf-8")
    root=etree.fromstring(data)
    print("          운항정보")

    for child in root.iter("response"):
        no=child.find('totalCount')
        if(no==None):

            print("\n          해당 지역은 운행 정보가 없습니다.\n")

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
        print('항공사 = '+airlin +
              '\n출발시간 = '+stime+'\n도착시간 = '+endtime+'\n출발공항 = '+start+'\n도착공항 = '+end)
        print("Y = 이용가능 / N = 이용 불가능")
        print("월요일 "+mon+"  "+"화요일 "+tue+"  "+"수요일 "+wnd+"  "+"목요일 "+thus+'\n'+"금요일 "+fri+"  "+"토요일 "+sat+"  "+"일요일 "+sun)
        print('=======================================================')

def oversea():
    time=input("시간대를 입력하세요")
    key='%2F3AEJBd1vcRO0ErsjC7gmLUi7WvMGdMrwgY86vbDyWsWun98FtVFl%2BJehIVuPPi%2B0jn7MSpRFMRQc00IUp11vg%3D%3D'
    url='http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey='+key+ "&schStTime="+time+'&schEdTime=2400&schLineType=I'
    data = urllib.request.urlopen(url).read()
    #d = str(data,"utf-8")
    root=etree.fromstring(data)

    print("          운항정보")

    for child in root.iter("response"):
        no = child.find('totalCount')
        if (no == None):
            print("\n          해당 지역은 운행 정보가 없습니다.\n")

    for child in root.iter("item"):
        airlin=child.find('airlineKorean').text
        start=child.find('boardingKor').text
        end=child.find('arrivedKor').text
        stime=child.find('std').text

        print('항공사 = '+airlin +
              '\n출발시간 = '+stime+'\n출발공항 = '+start+'\n도착공항 = '+end)
        print('=======================================================')

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
    # d = str(data,"utf-8")
    root = etree.fromstring(data)
    for child in root.iter("item"):
        airlin = child.find('airlineKorean').text
        start = child.find('boardingKor').text
        end = child.find('arrivedKor').text
        stime = child.find('std').text

        print('항공사 = ' + airlin +
              '\n출발시간 = ' + stime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
        print('=======================================================')


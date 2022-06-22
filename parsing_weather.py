import requests
import datetime
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()

def weather() : 

    weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?"
    service_key = os.environ.get('SERVICE_KEY')
    
    today = datetime.today()
    today_date =  today.strftime("%Y%m%d")  # 20220527 형식으로 변환
    base_date = today_date                  # 기본 날짜는 현재 날짜
    yesterday_date = date.today() - timedelta(days=1)
    time = datetime.now()
    # 시간에 따른 basetime 설정
    if  time.hour < 2 or (time.hour == 2 and time.minute <= 10): # 0시~2시 10분 사이
        base_date = yesterday_date # 기준 날짜/시간 : 어제 날짜 23시
        base_time = "2300"
    elif time.hour < 5 or (time.hour == 5 and time.minute <= 10): 
        base_time = "0200"
    elif time.hour<8 or (time.hour == 8 and time.minute <= 10): # 5시 11분~8시 10분 사이
        base_time = "0500"
    elif time.hour <= 11 or time.minute <= 10: # 8시 11분~11시 10분 사이
        base_time = "0800"
    elif time.hour < 14 or (time.hour == 14 and time.minute <= 10): # 11시 11분~14시 10분 사이
        base_time = "1100"
    elif time.hour < 17 or (time.hour == 17 and time.minute <= 10): # 14시 11분~17시 10분 사이
        base_time = "1400"
    elif time.hour < 20 or (time.hour == 20 and time.minute <= 10): # 17시 11분~20시 10분 사이
        base_time = "1700" 
    elif time.hour < 23 or (time.hour == 23 and time.minute <= 10): # 20시 11분~23시 10분 사이
        base_time = "2000"
    else: # 23시 11분~23시 59분
        base_time = "2300"
    
    # 대연동의 위도, 경도 (기상청 기준) 설정
    nx = "98"
    ny = "75"

    payload = f"serviceKey={service_key}&dataType=json&base_date={base_date}&" +\
        f"base_time={base_time}&nx={nx}&ny={ny}"

    res = requests.get(weather_url + payload)
    print(base_date, base_time)
    items = res.json().get('response').get('body').get('items')
    data = dict()
    data['date'] = base_date

    weather_data = dict()
    for item in items['item']:
        # 기온
        if item['category'] == 'TMP':
            weather_data['tmp'] = item['fcstValue']
        
        # 기상상태
        if item['category'] == 'PTY':
            
            weather_code = item['fcstValue']
            
            if weather_code == '1':
                weather_state = 'rain'
            elif weather_code == '2':
                weather_state = 'rain'
            elif weather_code == '3':
                weather_state = 'snow'
            elif weather_code == '4':
                weather_state = 'shower'
            else:
                weather_state = 'clear'
            
            weather_data['code'] = weather_code
            weather_data['state'] = weather_state

    data['weather'] = weather_data

    return weather_data['state'], weather_data['tmp']


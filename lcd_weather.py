from parsing_weather import weather
from lcd import lcdprint
import asyncio
from led import hot_led_off, hot_led_on, rain_led_off, rain_led_on

async def lcd_weather():
    weather_cond, weather_tmp = weather()
    
    lcdprint(weather_cond, weather_tmp)
    if weather_cond != 'clear' :                # 강수 알림
        rain_led_on()  
    else :
        rain_led_off()
    if int(weather_tmp) >= 30 :                 # 30도 이상 고온 경보
        hot_led_on()
    else :
        hot_led_off()
    
    await asyncio.sleep(60)
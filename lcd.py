from time import time_ns
import Adafruit_CharLCD as LCD
import asyncio

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def lcdprint(weather_state, weather_tmp) :
    lcd.set_cursor(0, 0)
    lcd.message(f"today: {weather_state} / {weather_tmp}")
    
async def lcdtimer(t):
    lcd.set_cursor(0, 1)
    lcd.message(t)
    await asyncio.sleep(60)

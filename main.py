import RPi.GPIO as GPIO
import sys
import time
from lcd import lcdtimer
from display_weather import display_weather
import asyncio

async def main() :
    while(1) :       
        t1 = asyncio.create_task(display_weather())
        now_time = time.strftime(f"%H%M")
        t2 = asyncio.create_task(lcdtimer(now_time))
        await t1
        await t2

if __name__ == "__main__" :
    try :
        asyncio.run(main())
    except KeyboardInterrupt :
        GPIO.cleanup()
        sys.exit(0)
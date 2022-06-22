import RPi.GPIO as GPIO

led_blue = 21
led_red = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_blue, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)

GPIO.output(led_blue, GPIO.LOW)
GPIO.output(led_red, GPIO.LOW)

def rain_led_on() :
    GPIO.output(led_blue, GPIO.HIGH)

def rain_led_off() :
    GPIO.output(led_blue, GPIO.LOW)

def hot_led_on() :
    GPIO.output(led_red, GPIO.HIGH)

def hot_led_off() :
    GPIO.output(led_red, GPIO.LOW)



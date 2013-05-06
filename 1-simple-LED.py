import RPi.GPIO as GPIO
import time

PIN_LED_RED=18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LED_RED, GPIO.OUT)
GPIO.output(PIN_LED_RED, True)
time.sleep(100)
GPIO.output(PIN_LED_RED, False)

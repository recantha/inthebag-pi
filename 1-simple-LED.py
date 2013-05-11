import RPi.GPIO as GPIO
import time

PIN_LED_GREEN=7
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LED_GREEN, GPIO.OUT)
GPIO.output(PIN_LED_GREEN, True)
time.sleep(5)
GPIO.output(PIN_LED_GREEN, False)

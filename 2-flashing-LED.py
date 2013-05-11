import RPi.GPIO as GPIO
import time

PIN_LED_GREEN=7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LED_GREEN, GPIO.OUT)

print "Press Ctrl-C to quit. Try and do it when the light is off!"

while True:
	GPIO.output(PIN_LED_GREEN, True)
	time.sleep(0.3)
	GPIO.output(PIN_LED_GREEN, False)
	time.sleep(0.3)

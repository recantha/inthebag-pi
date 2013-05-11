import RPi.GPIO as GPIO
import time

PIN_LED_RED=13
PIN_LED_YELLOW=11
PIN_LED_GREEN=7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LED_RED, GPIO.OUT)
GPIO.setup(PIN_LED_YELLOW, GPIO.OUT)
GPIO.setup(PIN_LED_GREEN, GPIO.OUT)

print "Press Ctrl-C to quit."

while True:
	GPIO.output(PIN_LED_RED, False)
	GPIO.output(PIN_LED_YELLOW, False)
	GPIO.output(PIN_LED_GREEN, True)
	time.sleep(3)
	GPIO.output(PIN_LED_GREEN, False)
	GPIO.output(PIN_LED_YELLOW, True)
	time.sleep(0.5)
	GPIO.output(PIN_LED_YELLOW, False)
	time.sleep(0.5)
	GPIO.output(PIN_LED_YELLOW, True)
	time.sleep(0.5)
	GPIO.output(PIN_LED_YELLOW, False)
	time.sleep(0.5)
	GPIO.output(PIN_LED_YELLOW, True)
	time.sleep(0.5)
	GPIO.output(PIN_LED_YELLOW, False)
	time.sleep(0.5)
	GPIO.output(PIN_LED_YELLOW, True)
	time.sleep(0.5)
	GPIO.output(PIN_LED_YELLOW, False)
	GPIO.output(PIN_LED_RED, True)
	time.sleep(3)
	GPIO.output(PIN_LED_YELLOW, True)
	time.sleep(1.5)

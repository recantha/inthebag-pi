import RPi.GPIO as GPIO
import time

PIN_SWITCH=12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_SWITCH, GPIO.IN)

while True:
	if(GPIO.input(PIN_SWITCH) == 0):
		print("Switch pressed (down)")
	else:
		print("Switch up")
	time.sleep(0.5)

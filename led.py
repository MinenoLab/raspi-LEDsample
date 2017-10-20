import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED = 11

GPIO.setup(LED, GPIO.OUT)

for i in range(3):
    GPIO.output(LED, GPIO.HIGH)
    time.sleep(1)

    GPIO.output(LED, GPIO.LOW)
    time.sleep(1)

GPIO.cleanup()

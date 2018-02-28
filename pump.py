import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
en=21
in1=20
in2=16

GPIO.setup(en,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)

GPIO.output(en,GPIO.HIGH)
GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)
time.sleep(6)
GPIO.output(en,GPIO.LOW)

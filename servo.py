import time
import RPi.GPIO as GPIO
from moisture import *
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
def servoinit():
     GPIO.setup(24, GPIO.OUT)                  
       
def servodown():
     pwm=GPIO.PWM(24,100)
     pwm.start(8.5)     
     pwm.ChangeDutyCycle(8.5)
     time.sleep(0.8)
def servoup():
     pwm=GPIO.PWM(24,100)
     pwm.start(1.5)
     pwm.ChangeDutyCycle(1.5)
     time.sleep(0.8)
if(__name__=='__main__'):
     servoinit()
     servodown()
     time.sleep(1)
     print(moisture())
     servoup()
     time.sleep(1)
        
     GPIO.cleanup()

import RPi.GPIO as GPIO
# programming the GPIO by BCM pin numbers
from program import *
from moisture import *
from weather import *
from servo import *
#Import time library
import time 


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 26
en=21
in1=20
in2=16

GPIO.setup(en,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)                  
GPIO.setup(ECHO,GPIO.IN) 

def motor_init():
	GPIO.setup(25,GPIO.OUT) #enable no.4
	GPIO.setup(8,GPIO.OUT)  #forward
	GPIO.setup(7,GPIO.OUT)  #backward

	GPIO.setup(10,GPIO.OUT) #enable no. 3
	GPIO.setup(9,GPIO.OUT) #backward
	GPIO.setup(11,GPIO.OUT) #forward

	GPIO.setup(18,GPIO.OUT) #enable no. 2
	GPIO.setup(14,GPIO.OUT) #backward
	GPIO.setup(27,GPIO.OUT) #forward

	GPIO.setup(17,GPIO.OUT) #enable no. 1
	GPIO.setup(22,GPIO.OUT) #backward
	GPIO.setup(15,GPIO.OUT) #forward
def backward():
	GPIO.output(17,GPIO.HIGH) #enable	
	GPIO.output(18,GPIO.HIGH) #enable
	GPIO.output(25,GPIO.HIGH) #enable
	GPIO.output(10,GPIO.HIGH) #enable
	GPIO.output(27,GPIO.LOW)
	GPIO.output(14,GPIO.HIGH)
	GPIO.output(9,GPIO.LOW) 
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(7,GPIO.LOW)  
	GPIO.output(8,GPIO.HIGH)
	GPIO.output(22,GPIO.HIGH)
	GPIO.output(15,GPIO.LOW)
	print('forward')
def forward():
	GPIO.output(17,GPIO.HIGH) #enable
	GPIO.output(18,GPIO.HIGH) #enable
	GPIO.output(25,GPIO.HIGH) #enable
	GPIO.output(10,GPIO.HIGH) #enable
	GPIO.output(8,GPIO.LOW) 
	GPIO.output(7,GPIO.HIGH)
	GPIO.output(9,GPIO.HIGH)
	GPIO.output(11,GPIO.LOW)
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(14,GPIO.LOW)
	GPIO.output(22,GPIO.LOW)
	print('backward')
def left():
	GPIO.output(17,GPIO.LOW) #enable
	GPIO.output(18,GPIO.HIGH) #enable
	GPIO.output(25,GPIO.HIGH) #enable
	GPIO.output(10,GPIO.LOW) #enable
	GPIO.output(14,GPIO.LOW)
	GPIO.output(15,GPIO.HIGH)
	GPIO.output(8,GPIO.LOW)
	GPIO.output(7,GPIO.HIGH)
	print('right')
def right():
	GPIO.output(17,GPIO.HIGH) #enable
	GPIO.output(18,GPIO.LOW) #enable
	GPIO.output(25,GPIO.LOW) #enable
	GPIO.output(10,GPIO.HIGH) #enable
	GPIO.output(11,GPIO.LOW) 
	GPIO.output(9,GPIO.HIGH) 
	GPIO.output(27,GPIO.HIGH)
	GPIO.output(22,GPIO.LOW)
	print('left')
def stop():
	GPIO.output(17,GPIO.LOW)
	GPIO.output(25,GPIO.LOW) 
	GPIO.output(10,GPIO.LOW) 
	GPIO.output(18,GPIO.LOW) 
	print('stop')
motor_init()
stop()
count=0
x=weather()
servoinit()
print(x)
if(x==False):
        print('will not water as it rained yesterday or it may rain today or tomorrow')
else:
        x=0
        while True:
         avgDistance=0
         for i in range(2):
          GPIO.output(TRIG, False)                 #Set TRIG as LOW
          time.sleep(0.1)                                   #Delay
          GPIO.output(TRIG, True)                  #Set TRIG as HIGH
          time.sleep(0.00001)                           #Delay of 0.00001 seconds
          GPIO.output(TRIG, False)                 #Set TRIG as LOW
          while GPIO.input(ECHO)==0:              #Check whether the ECHO is LOW
               pulse_start = time.time()             
          pulse_start = time.time()
          while GPIO.input(ECHO)==1:
                pulse_end = time.time()        
          pulse_end = time.time()
          pulse_duration = pulse_end - pulse_start #time to get back the pulse to sensor
          distance = pulse_duration * 17150        #Multiply pulse duration by 17150 (34300/2) to get distance
          distance = round(distance,2)
          avgDistance=avgDistance+distance
         avgDistance=avgDistance/2
         print avgDistance
         flag=0
         if avgDistance < 30 :      #Check whether the distance is within 30 cm range
            count=count+1
            stop()
            time.sleep(0.5)
            hs=start()
            if(hs):
                time.sleep(1)
                servodown()
                time.sleep(1)
                s=moisture()
                if(s):
                  time.sleep(1)
                  GPIO.output(en,GPIO.HIGH)
                  GPIO.output(in1,GPIO.HIGH)
                  GPIO.output(in2,GPIO.LOW)
                  time.sleep(3)
                  GPIO.output(en,GPIO.LOW)

                time.sleep(1)
                servoup()
            
            if (count%3 ==1) & (flag==0):
             left()
             time.sleep(2)
             flag=1
            else:
             right()
             time.sleep(1)
             flag=0
            
            stop()
            time.sleep(1)
         else:
            y=0
            stop()
            time.sleep(0.3)
            forward()
            time.sleep(0.2)
            stop()
            flag=0
         x=x+1
        stop()
        GPIO.cleanup()

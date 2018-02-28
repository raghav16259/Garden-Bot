import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

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
if(__name__=='__main__'):
	motor_init()
	i=0
	while(i<1):
                sleep(0.3)
                forward()
                sleep(1)
                stop()
                i=i+1
	GPIO.cleanup()

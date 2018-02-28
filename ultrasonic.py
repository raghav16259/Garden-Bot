
import RPi.GPIO as GPIO
import time
#Import time library
def distance():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	TRIG = 23
	ECHO = 26
	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)
        
 

	GPIO.output(TRIG, False)
	time.sleep(2)
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	while GPIO.input(ECHO)==0:
        	pulse_start = time.time()
	pulse_start = time.time()
  
	while GPIO.input(ECHO)==1:
		pulse_end = time.time()
	pulse_end = time.time()
  
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
        
	return distance
	
if(__name__=='__main__'):
	d=distance()
	print(d)
        GPIO.cleanup()

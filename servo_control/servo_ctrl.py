import RPi.GPIO as GPIO
import time
#Red is positive, brown is ground and orange is PWD

#SG90 expects 5 Hz ecery 0.2 seconds

# Set gpio numbering mode
GPIO.setmode(GPIO.BOARD)
 
 
#Set pin 11 as an output, and set servo1 as pin 11 as PWD
 
GPIO.setup(11,GPIO.OUT)
servo1= GPIO.PWM(11,50)  ## 11 IS PIN and 50 = 50 Hz pulse
 
#start PVM    running, but with vlaue of zero(pulse off)
 
servo1.start(0)
print("Waiting fot 2 seconds")
time.sleep(2)

#Lets move the sevo

print("Rotating 180 degree in 10 steps")


#Define variable duty
duty = 2

#Loop for the duty values from 2 to 12(0 to 180 Degree)
# while duty <= 12:
    # servo1.ChangeDutyCycle(duty)
    # time.sleep(1)
    # duty = duty + 1 
    
# To avoid the jitter
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1 
    
    
# Wait for couple of seconds
time.sleep(2)

#Turn back to 90 degree
print("Turining back to 90 Degre4ee for 2 seconds ")
servo1.ChangeDutyCycle(7)
time.sleep(1.5)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)
#time.sleep(2)

##Turn back to zero
print("turn back to zero Degree")
servo1.ChangeDutyCycle(2)
time.sleep(0.3)
servo1.ChangeDutyCycle(0)
time.sleep(0.7)
#time.sleep(1)
servo1.ChangeDutyCycle(0)

##Cleanup at the end
servo1.stop()
GPIO.cleanup()
print("Good Bye")

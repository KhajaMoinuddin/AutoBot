import RPi.GPIO as GPIO
import time
from termcolor import colored
#Red is positive, brown is ground and orange is PWD

#SG90 expects 5 Hz ecery 0.2 seconds
class Servo:
  servo1=7
  def __init__(self,pin):
    # Set gpio numbering mode
    #print("Servo:"pin)
    GPIO.setmode(GPIO.BOARD)
    #Set pin 11 as an output, and set servo1 as pin 11 as PWD
    GPIO.setup(pin,GPIO.OUT)
    self.servo1= GPIO.PWM(pin,50)  ## 11 IS PIN and 50 = 50 Hz pulse
    self.duty = 2
    self.servo1.start(0)

  def move_servo_10_step(self):
    #start PVM    running, but with vlaue of zero(pulse off)
    #self.servo1.start(0)
    print(colored("Waiting fot 2 seconds",'yellow'))
    time.sleep(2)
    #Lets move the sevo
    print(colored("Rotating 180 degree in 10 steps",'yellow'))
    #Define variable duty
    #duty = 2

    #Loop for the duty values from 2 to 12(0 to 180 Degree)
    # while duty <= 12:
        # servo1.ChangeDutyCycle(duty)
        # time.sleep(1)
        # duty = duty + 1

    # To avoid the jitter
    while self.duty <= 12:
        self.servo1.ChangeDutyCycle(self.duty)
        time.sleep(0.3)
        self.servo1.ChangeDutyCycle(0)
        time.sleep(0.7)
        self.duty = self.duty + 1

  def turn_back_90_degree(self):
    # Wait for couple of seconds
    #time.sleep(2)

    #Turn back to 90 degree
    print(colored("Turining back to 90 Degre4ee for 2 seconds "),'yellow')
    self.servo1.ChangeDutyCycle(7)
    time.sleep(0.3)
    self.servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    #time.sleep(2)

  def turn_back_to_zero_degree(self):
    ##Turn back to zero
    print("turn back to zero Degree")
    self.servo1.ChangeDutyCycle(2)
    time.sleep(0.3)
    self.servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    #time.sleep(1)
    #self.servo1.ChangeDutyCycle(0)


  def turn_back_to_Forty_Five_degree(self):
    ##Turn back to zero
    print(colored("turn back to zero Degree",'yellow'))
    self.servo1.ChangeDutyCycle(4.5)
    time.sleep(0.3)
    self.servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    #time.sleep(1)
    #self.servo1.ChangeDutyCycle(0)
    
  def turn_back_to_135_degree(self):
    ##Turn back to zero
    print(colored("turn back to zero Degree",'yellow'))
    self.servo1.ChangeDutyCycle(9.5)
    time.sleep(0.3)
    self.servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    #time.sleep(1)
    #self.servo1.ChangeDutyCycle(0)
    
  def turn_back_to_180_degree(self):
    ##Turn back to zero
    print(colored("turn back to zero Degree","yellow"))
    self.servo1.ChangeDutyCycle(12)
    time.sleep(0.3)
    self.servo1.ChangeDutyCycle(0)
    time.sleep(0.7)
    #time.sleep(1)
    #self.servo1.ChangeDutyCycle(0)
    
  def SetAngle(angle):
    duty = angle / 18 + 2
    GPIO.output(03, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(03, False)
    pwm.ChangeDutyCycle(0)

  def __del__(self):
    ##Cleanup at the end
    self.servo1.stop()
    GPIO.cleanup()
    print(colored('Servo:Good Bye', 'yellow'))


if __name__ =="__main__":
  servo = Servo(8)
  servo.move_servo_10_step()
  servo.turn_back_90_degree()
  servo.turn_back_to_zero_degree()
  del servo



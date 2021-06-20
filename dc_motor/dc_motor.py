import RPi.GPIO as GPIO
from datetime import time

class DC_Motor:
  def __init__(self,pin1,pin2,pin_enable):
    GPIO.setmode(GPIO.BOARD)
    self.pin1 = pin1
    self.pin2 = pin2
    self.pin_enable = pin_enable
    GPIO.setup(self.pin1, GPIO.OUT)
    GPIO.setup(self.pin2, GPIO.OUT)
    GPIO.setup(self.pin_enable, GPIO.OUT)
    self.pwm=GPIO.PWM(self.pin_enable, 100)
    self.pwm.start(0)
    
  def speed_low(self):
    self.pwm=GPIO.PWM(self.pin_enable, 25)

  def speed_midium(self):
    self.pwm=GPIO.PWM(self.pin_enable, 50)

  def speed_high(self):
    self.pwm=GPIO.PWM(self.pin_enable, 75)
    
   
  def forward(self,fwd_seconds):
    #So, for now, we're going to write a code that runs forward at 50% power for 2 seconds, then runs backward at 75% power for 3 seconds.
    #First, to set the direction to forward write
    
    GPIO.output(self.pin1, True)
    GPIO.output(self.pin2, False)
    #Now, we're going to set the PWM duty to 50%. Write
    
    pwm.ChangeDutyCycle(50)
    #then turn on the Enable pin
    
    GPIO.output(self.pin_enable, True)
    #then put the code to sleep for 2 seconds so the motor runs
    
    #sleep(2)
    sleep(fwd_seconds)
    #now turn off the Enable pin    
    GPIO.output(self.pin_enable, False)
  
  def Reverse(self,rev_Seconds):
    #then reverse the inputs to set it to reverse

    GPIO.output(self.pin1, False)
    GPIO.output(self.pin2, True)
    #Then change the PWM duty to 75%
    
    pwm.ChangeDutyCycle(75)
    #then turn the enable back on
    
    GPIO.output(self.pin_enable, True)
    #put the code to sleep for 3 seconds
    
    #sleep(3)
    sleep(rev_Seconds)
    
    #then turn the enable pin back off    
    GPIO.output(self.pin_enable, False)
    
  def __del__(self):
    self.pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
  dc_motor1 = DC_Motor(03,05,07)
  dc_motor1.forward(2)
  dc_motor1.reverse(3)
  del dc_motor1


import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

GPIO.cleanup()

Forward=37
Backward=38
sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)

def forward(x):
  GPIO.output(Forward, GPIO.HIGH)
  print("Moving Forward")
  time.sleep(x)
  GPIO.output(Forward, GPIO.LOW)

def reverse(x):
  GPIO.output(Backward, GPIO.HIGH)
  print("Moving Backward")
  time.sleep(x)
  GPIO.output(Backward, GPIO.LOW)

while (1):
  print("Forward 5 sec\n")
  forward(5)
  print("Reverse 5 sec\n")
  reverse(5)
  GPIO.cleanup()
  break

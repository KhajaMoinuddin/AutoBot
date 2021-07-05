import RPi.GPIO as GPIO
import time

class UltraSonic_Sensor:
    TRIG = 38
    ECHO = 37
    
    def __init__(self, T, E):
        self.TRIG = T
        self.ECHO = E
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.TRIG,GPIO.OUT)
        GPIO.setup(self.ECHO,GPIO.IN)
        GPIO.output(self.TRIG, False)
        
    def get_distance(self):
        try:    
           GPIO.output(self.TRIG, True)
           time.sleep(0.00001)
           GPIO.output(self.TRIG, False)

           while GPIO.input(self.ECHO)==0:
              pulse_start = time.time()

           while GPIO.input(self.ECHO)==1:
              pulse_end = time.time()

           pulse_duration = pulse_end - pulse_start

           distance = pulse_duration * 17150

           distance = round(distance+1.15, 2)
           return distance
           # if distance<=20 and distance>=5:
              # print "distance:",distance,"cm"
              # #i=1
              
           # if distance>20 and i==1:
              # print "place the object...."
              # i=0
           # time.sleep(2)

        except KeyboardInterrupt:            
                GPIO.cleanup()
    
    def __del__(self):
        try:
            GPIO.cleanup()
        except:
            pass
 
if __name__=='__main__':
    TRIG = 38
    ECHO = 37
    ultrasonic_sensor_object = UltraSonic_Sensor(TRIG,ECHO)
    distance = ultrasonic_sensor_object.get_distance()
    print("distance:",distance,"cm")


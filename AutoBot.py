import sys
import time
import RPi.GPIO as GPIO
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/pi/AutoBot/servo_control')
sys.path.insert(1, '/home/pi/AutoBot/ultrasonic')
sys.path.insert(1, '/home/pi/AutoBot/dc_motor')

from servo_ctrl1_class import Servo
from ultrasonic_class import UltraSonic_Sensor
from dc_motor_class import DC_Motor

class AutoBot:
    servo_object=""
    ultrasonic_sensor_object = ""
    dc_motor_left_object = ""
    dc_motor_right_object = ""
    
    def __init__(self,servo_input_pin,T_pin,E_pin,Dc_left_1_pin,Dc_left_2_pin,Dc_left_enable_pin,Dc_right_1_pin,Dc_right_2_pin,Dc_right_enable_pin):
        print("Constructor called")
        self.servo_object = Servo(servo_input_pin)
        self.ultrasonic_sensor_object = UltraSonic_Sensor(T_pin,E_pin)        
        ####Dc Motor Left Initalization
        self.dc_motor_left_object = DC_Motor(Dc_left_1_pin,Dc_left_2_pin,Dc_left_enable_pin)        
        ####Dc Motor Right Initalization
        self.dc_motor_right_object = DC_Motor(Dc_right_1_pin,Dc_right_2_pin,Dc_right_enable_pin)       
        

    def __del__(self):
        print("Distructor called")
        self.servo_object.turn_back_to_zero_degree()
	
    
    def automatic(self):
        print("Automatic Mode")
        #self.servo_object.tun_back_90_degree()
        #self.servo_object.turn_back_to_zero_degree()      
        # self.servo_object.move_servo_10_step()
        # self.servo_object.turn_back_to_zero_degree()
        self.servo_object.turn_back_90_degree()
        d_zero = self.ultrasonic_sensor_object.get_distance()
        print("Duistance at zero Degree:",d_zero,"Cm")

        try: 
            #Infine Loop
            while(True):
                self.servo_object.turn_back_90_degree()
                d_ninty = self.ultrasonic_sensor_object.get_distance()
                print("Duistance at zero Degree:",d_ninty,"Cm")
                if(d_ninty>50):
                    print("DC Motor Move Forward")
                    self.forward_1_second()
                    d_ninty = self.ultrasonic_sensor_object.get_distance()
                else:
                    ##180 Degree is Left 
                    ##0 Degree is Right
                    self.servo_object.turn_back_to_Forty_Five_degree()
                    d = self.ultrasonic_sensor_object.get_distance()
                    print("Duistance at 45 Degree:",d,"Cm")
                    
                    if(d >50):
                        print("DC Motor Turn Right 45 Degree")
                        self.steer_45_degree_right()
                    else:
                        self.servo_object.turn_back_to_zero_degree()
                        d = self.ultrasonic_sensor_object.get_distance()
                        print("Duistance at 0 Degree:",d,"Cm")
                        if (d > 50):
                            print("DC Motor Turn Hard Right 0 Degree")
                            self.steer_0_degree_right()
                        else:
                            self.servo_object.turn_back_to_135_degree()
                            d = self.ultrasonic_sensor_object.get_distance()
                            print("Duistance at 135 Degree:",d,"Cm")
                            if (d > 50):
                                print("DC Motor Turn left 135 Degree")  
                                self.steer_135_degree_left()
                            else:
                                self.servo_object.turn_back_to_180_degree()
                                d = self.ultrasonic_sensor_object.get_distance()
                                print("Duistance at 180 Degree:",d,"Cm")
                                if (d > 50):
                                    print("DC Motor Turn Hard Left 180 Degree")    
                                else:
                                    ###Trake a U turn
                                    print("DC Motor Turn 180 Degree ")
                                    self.steer_270_degree_left()
                        
        except KeyboardInterrupt:
            print("Ending Autonomus Mode")
            self.servo_object.turn_back_to_zero_degree()
            GPIO.cleanup()
        self.servo_object.turn_back_to_zero_degree()
        
	#try:
            #while(1):
                
    def manual(self):
        print("Manual Mode")
        
        
    def start(self):
        print("Starting with Automatic mode, By Default")
        self.automatic()
        
        #self.forward_1_second()        
        self.reverse_1_second()        
        #self.steer_45_degree_right()  
        #self.steer_0_degree_right()  
        self.steer_270_degree_left()
        
    def stop(self):
        print("Stopping Autobot")
        self.servo_object.turn_back_to_zero_degree()
        
    def steer_45_degree_right(self):
        # seconds = 1
        print("Turn Right 45 degree")
        # ##We should turn at a slow speed
        # self.dc_motor_right_object.speed_low()
        # self.dc_motor_right_object.forward(seconds)   
        #self.dc_motor_left_object.set_pin_disable()        
        self.dc_motor_left_object.set_reverse_pin()
        self.dc_motor_right_object.set_forward_pin() 
        
        self.dc_motor_left_object.set_pin_enable()
        self.dc_motor_right_object.set_pin_enable()
        #self.dc_motor_left_object.set_pin_disable()  
        time.sleep(0.5)        
        self.dc_motor_left_object.set_pin_disable()
        self.dc_motor_right_object.set_pin_disable()  
        
    def steer_0_degree_right(self):
      # seconds = 1
        print("Turn Right 0 degree")
        # ##We should turn at a slow speed
        # self.dc_motor_right_object.speed_low()
        # self.dc_motor_right_object.forward(seconds)   
        #self.dc_motor_left_object.set_pin_disable()        
        self.dc_motor_left_object.set_reverse_pin()
        self.dc_motor_right_object.set_forward_pin() 
        
        self.dc_motor_left_object.set_pin_enable()
        self.dc_motor_right_object.set_pin_enable()
        #self.dc_motor_left_object.set_pin_disable()  
        time.sleep(1)        
        self.dc_motor_left_object.set_pin_disable()
        self.dc_motor_right_object.set_pin_disable()  
    
    def steer_135_degree_left(self):
        # seconds = 1
        print("Turn left 135 degree")
        # ##We should turn at a slow speed
        # self.dc_motor_right_object.speed_low()
        # self.dc_motor_right_object.forward(seconds)   
        #self.dc_motor_left_object.set_pin_disable()        
        self.dc_motor_left_object.set_forward_pin()
        self.dc_motor_right_object.set_reverse_pin() 
        
        self.dc_motor_left_object.set_pin_enable()
        self.dc_motor_right_object.set_pin_enable()
        #self.dc_motor_left_object.set_pin_disable()  
        time.sleep(0.5)        
        self.dc_motor_left_object.set_pin_disable()
        self.dc_motor_right_object.set_pin_disable()  
        
    def steer_180_degree_left(self):
        # seconds = 1
        print("Turn left 135 degree")
        # ##We should turn at a slow speed
        # self.dc_motor_right_object.speed_low()
        # self.dc_motor_right_object.forward(seconds)   
        #self.dc_motor_left_object.set_pin_disable()        
        self.dc_motor_left_object.set_forward_pin()
        self.dc_motor_right_object.set_reverse_pin() 
        
        self.dc_motor_left_object.set_pin_enable()
        self.dc_motor_right_object.set_pin_enable()
        #self.dc_motor_left_object.set_pin_disable()  
        time.sleep(1)        
        self.dc_motor_left_object.set_pin_disable()
        self.dc_motor_right_object.set_pin_disable()  
        
    def steer_270_degree_left(self):
        # seconds = 1
        print("Turn left 135 degree")
        # ##We should turn at a slow speed
        # self.dc_motor_right_object.speed_low()
        # self.dc_motor_right_object.forward(seconds)   
        #self.dc_motor_left_object.set_pin_disable()        
        self.dc_motor_left_object.set_forward_pin()
        self.dc_motor_right_object.set_reverse_pin() 
        
        self.dc_motor_left_object.set_pin_enable()
        self.dc_motor_right_object.set_pin_enable()
        #self.dc_motor_left_object.set_pin_disable()  
        time.sleep(1.5)        
        self.dc_motor_left_object.set_pin_disable()
        self.dc_motor_right_object.set_pin_disable()  
    
    def forward_1_second(self):
        print("Forward one second")
        #self.dc_motor_left_object.speed_low()
        #sef.dc_motor_right_object.speed_low()        
        self.dc_motor_left_object.set_forward_pin()
        self.dc_motor_right_object.set_forward_pin()        
        self.dc_motor_left_object.set_pin_enable()
        self.dc_motor_right_object.set_pin_enable()
        time.sleep(1)        
        self.dc_motor_left_object.set_pin_disable()
        self.dc_motor_right_object.set_pin_disable()      

        
    def reverse_1_second(self):
        #self.dc_motor_left_object.speed_low()
        #sef.dc_motor_right_object.speed_low()        
        self.dc_motor_left_object.set_reverse_pin()
        self.dc_motor_right_object.set_reverse_pin()        
        self.dc_motor_left_object.set_pin_enable()
        self.dc_motor_right_object.set_pin_enable()
        time.sleep(1)        
        self.dc_motor_left_object.set_pin_disable()
        self.dc_motor_right_object.set_pin_disable()    
        
if __name__ == "__main__":
    print("Starting AutoBot")
    ###Pin Number Servo 
    servo_pin = 8
    
    ###Pin Number Ultrasonic Sensor
    T_pin = 31
    E_pin = 32
    
    ###Pin Nuber Dc Left
    Dc_left_1_pin = 33
    Dc_left_2_pin = 35
    Dc_left_enable_pin = 37
    
    ###Pin Number Dc Right
    Dc_right_1_pin = 36
    Dc_right_2_pin = 38
    Dc_right_enable_pin = 40   
    
    bot = AutoBot(servo_pin,T_pin,E_pin,Dc_left_1_pin,Dc_left_2_pin,Dc_left_enable_pin,Dc_right_1_pin,Dc_right_2_pin,Dc_right_enable_pin)
    bot.start()
    #bot.manual()
    #bot.stop()

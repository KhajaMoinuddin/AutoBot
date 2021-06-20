import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/home/pi/Rover/servo_control')
sys.path.insert(1, '/home/pi/Rover/ultrasonic')

from servo_ctrl1_class import Servo
from ultrasonic_class import UltraSonic_Sensor



class AutoBot:
    servo_object=""
    ultrasonic_sensor_object = ""
    dc_motor1_object = ""
    dc_motor2_object = ""
    
    def __init__(self,servo_input_pin,T_pin,E_pin):
        print("Constructor called")
        self.servo_object = Servo(servo_input_pin)
        self.ultrasonic_sensor_object = UltraSonic_Sensor(T_pin,E_pin)

    def __del__(self):
        print("Distructor called")
        self.servo_object.turn_back_to_zero_degree()
	
    
    def automatic(self):
        print("Automatic Mode")
	#self.servo_object.tun_back_90_degree()
        self.servo_object.turn_back_to_zero_degree()      
        # self.servo_object.move_servo_10_step()
        # self.servo_object.turn_back_to_zero_degree()
        d_zero = self.ultrasonic_sensor_object.get_distance()
        print("Duistance at zero Degree:",d_zero,"Cm")

        try: 
            #Infine Loop
            while(True):
                self.servo_object.tun_back_90_degree()
                d_ninty = self.ultrasonic_sensor_object.get_distance()
                print("Duistance at zero Degree:",d_ninty,"Cm")
                if(d_ninty>30):
                    print("DC Motor Move Forward")
                    d_ninty = self.ultrasonic_sensor_object.get_distance()
                else:
                    ##180 Degree is Left 
                    ##0 Degree is Right
                    self.servo_object.turn_back_to_Forty_Five_degree()
                    d = self.ultrasonic_sensor_object.get_distance()
                    print("Duistance at 45 Degree:",d,"Cm")
                    if(d >30):
                        print("DC Motor Turn Right 45 Degree")
                    else:
                        self.servo_object.turn_back_to_zero_degree()
                        d = self.ultrasonic_sensor_object.get_distance()
                        print("Duistance at 0 Degree:",d,"Cm")
                        if (d > 30):
                            print("DC Motor Turn Hard Right 0 Degree")
                        else:
                            self.servo_object.turn_back_to_135_degree()
                            d = self.ultrasonic_sensor_object.get_distance()
                            print("Duistance at 135 Degree:",d,"Cm")
                            if (d > 30):
                                print("DC Motor Turn left 135 Degree")                       
                            else:
                                self.servo_object.turn_back_to_180_degree()
                                d = self.ultrasonic_sensor_object.get_distance()
                                print("Duistance at 180 Degree:",d,"Cm")
                                if (d > 30):
                                    print("DC Motor Turn Hard Left 180 Degree")    
                                else:
                                    ###Trake a U turn
                                    print("DC Motor Turn 180 Degree ")                                        
                        
        except KeyboardInterrupt:
             print("Ending Autonomus Mode")
        
        
        
        self.servo_object.turn_back_to_zero_degree()
	#try:
            #while(1):
                
    def manual(self):
        print("Manual Mode")
        
    def start(self):
        print("Starting with Automatic mode, By Default")
        self.automatic()
        
    def stop(self):
        print("Stopping Autobot")
        self.servo_object.turn_back_to_zero_degree()
        

        
if __name__ == "__main__":
    print("Starting AutoBot")
    servo_pin = 8
    T_pin = 37
    E_pin = 38
    bot = AutoBot(servo_pin,T_pin,E_pin)
    bot.start()
    bot.manual()
    bot.stop()

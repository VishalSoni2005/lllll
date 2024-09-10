import time
from gpiozero import LED

class LEDController:
    def __init__(self, a, b, c, d):
        # Initialize GPIO pins
        self.led1 = LED(a)
        self.led2 = LED(b)
        self.led3 = LED(c)
        self.led4 = LED(d)
        
    def on(self, signal_type=2):
        # Control LEDs based on signal type
        if signal_type == 0:  # Red signal
            self.led1.on()
            self.led2.off()
            self.led3.off()
            #self.led4.off()
        elif signal_type == 1:  # Yellow signal
            self.led1.off()
            self.led2.on()
            self.led3.off()
            #self.led4.off()
        elif signal_type == 2:  # Green signal
            self.led1.off()
            self.led2.off()
            self.led3.on()
            #self.led4.off()
        elif signal_type == 3:  # Emergency (blue) signal
            self.led1.off()
            self.led2.off()
            self.led3.off()
            #self.led4.on()
        else:  # Invalid input
            print("Wrong input...")
    
    def off(self):
        self.led1.on()
        self.led2.off()
        self.led3.off()
        #self.led4.off()
    
    def emer_on(self):
        # Turn on the emergency LED
        self.led4.on()
    
    def emer_off(self):
        # Turn off the emergency LED
        self.led4.off()
    
    def is_on(self):
        return self.led2.on()
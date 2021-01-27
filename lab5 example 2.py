from gpiozero import PWMLED
from time import sleep
import math
import time

led = PWMLED(21)
val=10/3
print(val)
led.value = 0  # off
while led.value<1:
    if led.value<=0.9:
        led.value+=0.1
    else:
        time.sleep(val)
        led.value = 0  # off
        
        
        
    

    
    
    

    
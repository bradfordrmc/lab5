from gpiozero import Button# importmodule LED
from gpiozero import LED # import module LED
from time import sleep
button = Button(2)
led =LED(17)

while True:
    if button.is_pressed:
        print("Pressed")
        led.on() # set the GPIO 17to high
    else:
        print("Released")
        led.off() # set the GPIO 17to low
        sleep(1)
#!/usr/bin/python3

# Flash LEDs Randomly using GPIO Pin Numbers.

# Breadboard Setup
# GND Pin 9 (Just north of GPIO 17)
# GND has a 220 Ohm resistor. 
# Green multicolor needs a 4.7 K Ohm resistor. Too bright.
# Yellow single color needs a 100 Ohm resistor.
# Blue multicolor needs a 100 Ohm resistor.

# Import Packages
import os
import RPi.GPIO as GPIO
import time
import random

# Clear the console screen
os.system('clear')

# Input number of desired flashes.
print ('How many flashes?')
print ('')
flashes = int(input())
print ('')

time.sleep(1)

# Blinking Function  
def blink(pin):  
    GPIO.output(pin,GPIO.HIGH)  
    time.sleep(0.1)  
    GPIO.output(pin,GPIO.LOW)  
    time.sleep(0.1)  
    return  

# Set to use Raspberry Pi board pin numbers.  
GPIO.setmode(GPIO.BOARD)  

# Set up GPIO Output Channels.  
GPIO.setup(7, GPIO.OUT)       # Yellow LED
GPIO.setup(11, GPIO.OUT)      # Red LED
GPIO.setup(13, GPIO.OUT)      # Green LED
GPIO.setup(15, GPIO.OUT)      # Blue LED

# Blink the the lights randomly for requested number of times.  
for i in range(1,flashes+1,1):
    random_color = random.randint(1,4)  
    if random_color == 1:
        print('Yellow ' + str(i))
        blink(7)
    elif random_color == 2:
        print('Red ' + str(i))
        blink(11)
    elif random_color == 3:
        print('Green ' + str(i))
        blink(13)
    elif random_color == 4:
        print('Blue ' + str(i))
        blink(15)
GPIO.cleanup() 

print ('')

# End comment.
if flashes == 1:
	print ('That was 1 flash!')
else:
	print ('That was ' + str(flashes) + ' flashes!')

print ('')
print ('')
print ('')

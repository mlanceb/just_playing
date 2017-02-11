#!/usr/bin/python3

# Flashing LED

# Breadboard Setup
# GND Pin 9 (Just north of GPIO 17)
# Resistors
# Negative (short lead) LED
# Positive (long lead) LED
# GPIO Pin 17


# Clear the console screen
import os
os.system('clear')

print ('How many flashes?')
flashes = int(input())

import RPi.GPIO as GPIO  
import time  

time.sleep(1)

# blinking function  
def blink(pin):  
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(0.1)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(0.1)  
        return  
# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
GPIO.setup(11, GPIO.OUT)  
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
# blink GPIO17 the requested number of times  
for i in range(0,flashes):  
        print('Red ' + str(i+1))
        blink(11)
        print('Green ' + str(i+1))
        blink(13)
        print('Blue ' + str(i+1))
        blink(15)
        print('Yellow ' + str(i+1))
        blink(7)
GPIO.cleanup() 

print ('')

print ('That was ' + str(flashes) + ' flashes!')

print ('')
print ('')
print ('')

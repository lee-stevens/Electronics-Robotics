#!/usr/bin/env python3
########################################################################
# Filename    : LightWater.py
# Description : Use LEDBar Graph(10 LED) 
# Author      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

ledPins = [11, 12, 13, 15, 16, 18, 22, 29, 31, 32]

def setup():    
    GPIO.setmode(GPIO.BOARD)        # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPins, GPIO.OUT)   # set all ledPins to OUTPUT mode
    GPIO.output(ledPins, GPIO.HIGH) # make all ledPins output HIGH level, turn off all led

def loop():
    while True:
        for pin in ledPins:
            GPIO.output(pin, GPIO.LOW)  
            time.sleep(0.03)
            GPIO.output(pin, GPIO.HIGH)
        for pin in ledPins[::-1]:
            GPIO.output(pin, GPIO.LOW)  
            time.sleep(0.2)
            GPIO.output(pin, GPIO.HIGH)

def destroy():
    GPIO.cleanup()                     # Release all GPIO

if __name__ == '__main__':     # Program entrance
    print ('Program is starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()


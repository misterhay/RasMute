#!/usr/bin/env python
from time import sleep
import os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# define the pins we're using
button1 = 4
LED = 7

# set up the pins
GPIO.setup(button1, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)

# turn on the LED
GPIO.output(LED, True)
# wait for half a second
sleep(0.5)
# turn off the LED
GPIO.output(LED, False)
# toggle the LED
GPIO.output(LED, not GPIO.input(4))

# set up some variable to read from the button
input = False
previousInput = True

# loop
while True:
 # read the button state to the variable input
 input = GPIO.input(button1)
 # make sure the button state isn't what it used to be
 if ((not previousInput) and input):
  print("button pushed")
 # copy the button state to the previousInput variable
 previousInput = input
 # wait to "debounce" the input
 sleep(0.05)

# clean things up
GPIO.cleanup()

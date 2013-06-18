#!/usr/bin/env python

# this requires the RPi.GPIO and pyOSC libraries

from time import sleep
#import threading
from OSC import OSCClient, OSCServer, OSCMessage
#import RPi.GPIO as GPIO

# declare the GPIO pins we're using
LED1 = 2
LED2 = 3
button1 = 4
button2 = 22

# variables for the previous button inputs
previousInput1 = False
previousInput2 = False

# set up the GPIO
'''GPIO.setmote(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)
# turning on the LEDs is like this:  GPIO.output(LED1, True)
'''
# set up the OSC client (for sending) and server (for receiving)
x32address = ('192.168.1.200', 10023)
client = OSCClient()
client.connect((x32address))
# not sure about these next three lines, check the syntax
#server = ThreadingOSCServer((x32address, 10023))
#server.timeout = 0
#run = True

# define the OSC addresses for the channels that we'll be controlling
#pulpit = '/ch/01/mix/on'
#lapel = '/ch/02/mix/on'
#mutegroup = '/config/mute/1'

# declare some varaibles for storing the current states of the mute groups
muteGroup1 = 0
muteGroup2 = 0
muteGroup3 = 0
muteGroup4 = [0, 1]
muteGroup5 = [0, 1]
muteGroup6 = [0, 1]

# add the message handlers for the channels we're controlling
#server.addDefaultHandlers()
#server.addMsgHandler('/config/mute', muteGroupHandler)
#server.addMsgHandler(pulpit, muteHandler1)
#server.addMsgHandler(lapel, muteHandler2)

# define a functions for toggling a mute groups
# channel is an integer between 1 and 6, state is 0 or 1 (off or on)
def toggleMuteGroup(channel, state):
 stringChannel = str(channel)
 muteAddress = '/config/mute/' + stringChannel
 msg = OSCMessage(muteAddress)
 msg.append(state)
 client.send(msg)
 print msg

button1State = 1

# check the state of the mute group, and set the value of the mute group accordingly
# also change the value of the corresponding LED
# in an infinte loop
while True:
 #button1State = GPIO.input(button1)
 if ((not previousInput1) and input1):
  # toggle the muteGroup1 variable between 0 and 1, %2 is right out
  muteGroup1 = (muteGroup1 + 1) %2
  toggleMuteGroup(1, muteGroup1)
  previousInput1 = input1
 elif button2State == 1:
  muteGroup1 = (muteGroup2 + 1) %2
  toggleMuteGroup(2, muteGroup2)
 # wait for a second before doing it again
 sleep(1)

def muteGroupHandler(addr, tags, stuff, source):
 if addr == '/config/mute/':
  print addr
  print tags
  print stuff
  print source

def main():
    st = threading.Thread(target = server.serve_forever)
    st.start()

main()

'''
#  check out this example of a threading OSC server https://code.google.com/p/osc-midi-bridge/wiki/OSC
# start the OSC server to receive messages from the X32
threadingServer = threading.Thread(target=server.serve_forever)
threadingServer.start()
'''

'''
# an infinite loop that checks if the button is pressed and if so toggles the mute channel
while True:
 input1 = GPIO.input(button1)
 if ((not previousInput1) and input1):
  #send an OSC message here to toggle the mute
  previousInput1 = input1
'''

'''
# sending an OSC mute
msg = OSCMessage('/ch/01/mix/on')
msg.append(0)
client.send(msg)
'''

# shut everything down
#threadingServer.join()
#server.close()
#GPIO.cleanup()

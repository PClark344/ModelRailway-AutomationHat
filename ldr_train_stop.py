#!/usr/bin/env python
# Paul Clark 11/02/2017
# Code to detect a train using Light Dependant Resistor
# from Pimoroni code for input for automation hat

import RPi.GPIO as GPIO

import time

import automationhat

threshold = 0.25

try:

    cnt = 0
    detectioncnt = 0    
    while True:
        # get relevant data from automation hat output
        s = str(automationhat.analog.read())
        slist = s.split()
        reldata = slist[5]
        numdata = reldata.replace('}','')
        finalnum = float(numdata)

        # first run do nothing. Second run record output voltage. Third run display
        if cnt == 0:
            print('Initialisation Run')
        elif cnt == 1:
            print('detector now calibrated')
            print('trainstop program running')
            startvalue = finalnum
            diff = 0
        else:
           diff = finalnum - startvalue
           #print('First value = ' + str(startvalue))
           #print('Current value = ' + str(finalnum))
           #print('Difference = ' + str(diff))

           # if detected for first time only switch relay
           if diff > abs(threshold):
              if detectioncnt == 0:
                 #print('Train detected')
                 automationhat.relay.one.toggle() # switch on relay
                 detectioncnt = detectioncnt + 1
              #else:
                 #print('train still at detector')
           else:
              if detectioncnt > 0:
                 #print('train has left detector')
                 automationhat.relay.one.toggle() # switch off relay
                 detectioncnt = 0
              #else:
                 #print('no train detected')
   
        cnt = cnt + 1
        time.sleep(0.01)

finally:  
    print("Cleaning up")
    GPIO.cleanup()

#!/usr/bin/env python
# Paul Clark 11/02/2017
# Code to detect a train using Light Dependant Resistor
# from Pimoroni code for input for automation hat

import RPi.GPIO as GPIO

import time

import automationhat

threshold = 2.0
delay = 12.0

def detect_train():
   cnt = 0    
   while True:
      # get relevant data from automation hat output
      s = str(automationhat.analog.read())
      slist = s.split()
      reldata = slist[5]
      numdata = reldata.replace('}','')
      finalnum = float(numdata)
      print('cnt = ' + str(cnt) + '  s = ' + str(s))

      if cnt == 0:
         print('Initialisation Run')
         cnt = cnt + 1
      elif cnt == 1:
         print('Still Initialising')
         cnt = cnt + 1
      elif cnt == 2:
         startvalue = finalnum
         diff = 0
         cnt = cnt + 1
      else:
         diff = finalnum - startvalue
         #print('First value = ' + str(startvalue))
         #print('Current value = ' + str(finalnum))
         #print('Difference = ' + str(diff))

         if diff > abs(threshold):
            print('Train detected')
            automationhat.output.two.off() # switch off amber
            automationhat.output.three.off() # switch off green
            automationhat.output.one.on() # show red
            time.sleep(delay)
            automationhat.output.one.off()# wsitch off red
            automationhat.output.two.on() # show amber
            time.sleep(delay)
            automationhat.output.two.off() # switch off amber
            automationhat.output.three.on() # show green
         else:
            print('No Train detected')
            automationhat.output.one.off()
            automationhat.output.two.off()
            automationhat.output.three.on() # show green

try:

   detect_train()

finally:  

    print("Cleaning up")
    GPIO.cleanup()

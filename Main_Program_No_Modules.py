#!/usr/bin/env python
# Main_Program
# Program reads files and runs modules to carry out:
# assignment of detectors, detection of trains, switching relays for sections 
# Paul Clark
# Version 1.0
# 08/06/2017

# import required libraries
import RPi.GPIO as GPIO
import time
import spidev
import random

# define variables
train_found = False
delay = 1
switch_on = True
ldr_channel = 0
threshold = 150 # ir value

#Create SPI
spi = spidev.SpiDev()
spi.open(0, 0)

# define definitions for subroutines

def readadc(adcnum):
    # read SPI data from the MCP3008, 8 channels in total
    if adcnum > 7 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

def assign_detectors(): # reads list/file of detectors locations on layout
    global detector_locs
    #detector_locs = ['LH FY Siding 1','LH FY Siding 2','LH FY Siding 3','Loop','Main','RH FY Siding 1','RH FY Siding 2','RH FY Siding 3']
    detector_locs = ['LH FY Siding 1']

    #random_number = random.randint(0,2)
    #print(random_number)
    #print(detector_locs[random_number])
    return

def initialise_detector(): # checks first value
    global ldr_channel
    global startvalue
    print("Initialising Detector for Channel " + str(ldr_channel))
    startvalue = 0
    ldr_value = readadc(ldr_channel)
    finalnum = ldr_value
    startvalue = finalnum
    return startvalue

def check_detector(): # checks value to see if train detected by a particular sensor
    ldr_value = readadc(ldr_channel)
    finalnum = ldr_value

    diff = finalnum - startvalue

    print('First value = ' + str(startvalue))
    print('Current value = ' + str(finalnum))
    print('Difference = ' + str(diff))

    if abs(diff) > abs(threshold):
        print('Train detected')
    else:
        print('No Train detected')    
    return

def sections_occupied():
    return

def sections_switch_logic():
    return

def switch_section(section_num,switch_on): # switches required relay on or off
    return


# Main Loop - Loops through each detector and checks if section is occupied
try:


    assign_detectors()

    cnt = 0    
    diff = 0

    
    while True:
        if cnt == 0:
            ldr_channel = 0
            for item in detector_locs:
                print(item)
                initialise_detector()
                ldr_channel = ldr_channel + 1
        else:
            ldr_channel = 0
            for item in detector_locs:
                print(item)
                check_detector()
                ldr_channel = ldr_channel + 1            

        cnt = cnt + 1
        time.sleep(delay)


except IOError:
    print("Cannot open file")

finally:  
    print("Cleaning up")
    GPIO.cleanup()
    

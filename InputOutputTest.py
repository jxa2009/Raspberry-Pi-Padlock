#written by Jason Au
#last updated 1/13/2019
#File that will test multiple functionalities of the GPIO for the Raspberry Pi 3 Model B for bigger project

import RPi.GPIO as GPIO
from time import sleep


#General setup
GPIO.setmode(GPIO.BOARD)
ledPin = 12
switchPin = 11

buttonPin =15

GPIO.setup(ledPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



#GPIO pin labelling is according to GPIO.setmode(GPIO.BOARD), not BCM
#GPIO PINS THAT CAN BE USED: 7 11 13 15 18 22 29 31 33 35 37 32 36 38 40 

#GPIO PINS CURRENTLY USING : Input: 16
#                          : Output: 12
#

#Tests the switch and reads if its open or closed
#If the swithc is closed then it will output voltage to pin 12 which has an led connected to it
#if the swithc is open then it will emit not voltage and the led connected to pin 12 will turn off
def readSwitchTest():
    try:
        while True:
            switchState = GPIO.input(switchPin)
            if switchState == False:
                print("Closed")
                GPIO.output(ledPin,1)
                sleep(3)
            else:
                print("Open")
                GPIO.output(ledPin,0)
                sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
def buttonSwitchTest():
    try:
        while True:
            print(GPIO.input(buttonPin))
            GPIO.output(ledPin, GPIO.input(buttonPin))
            sleep(3)
    except KeyboardInterrupt:
        GPIO.cleanup()
            
#initalize the dictionary of inputs
def dictInit():
    input = {}
    input[1] = True
    input[2] = True
    input[3] = True
    input[4] = True
    input[Active] = True
    return input

#This function will test that multiple switches can be used and if the inputs can all be detected
#Will be used eventaully to emit an output based on multiple inputs of the switch
#The way the padlock will work is that all the inputs must be put in and then the Switch 10 must be closed 

#testMultiSwitch HAS NOT HAD THE OTHER SWITCHES SETUP YET REMEMBER TO DO SO
def testMultiSwitch():
    inputs = dictInit()
    switchActive = GPIO.input(switchActivate) #switchActive will be switch 10 on the dip switch and will only start reading inputs if it is closed. If it is not then nothing will happen
    if inputs[Active] == False: # if the switch is closed
        print("switchActive (Switch 10) is closed")

print("start")
GPIO.setwarnings(False)
buttonSwitchTest()

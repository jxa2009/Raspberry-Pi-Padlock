# This file will be for the Raspberry Pi lock program
# Jason Au
# 1/14/2019
# Will primarily focus on implementing interrupts with the raspberry pi to make the overall function more efficient


# Do setup as usual


# def callback_handle(channel):
#   #This is what to do when the event is called
#   print("Call back handle called")


#GPIO.add_event_detect(CHANNEL, GPIO.FALLING, callback=callback_handle,
#                      bouncetime=300)  # CHANNEL needs to be replaced with a value
# whatever callback is equal to is the function
# that will execute when the event is detected
# bouncetime is the amount of time to where another input
# will be ignored
# whenever the requirements for the event_detect is activated, the current code being executed will be ignored and proceed to be executed

# actual code to do program ----
from time import sleep
from QueueClass import Queue
import RPi.GPIO as GPIO
from time import sleep
from sendmail import send_mail
MAX_SIZE = 4
CHANNELTOINPUT = {}  # dictionary associating the channel with its input value
CHANNEL1 = 7
CHANNEL2 = 11
CHANNEL3 = 13
CHANNEL4 = 15
ledPin = 12
# Pins to use for buttons : Pin 7, Pin 11, Pin 13, Pin 15
queue = Queue(MAX_SIZE)  # global queue to hold the input buttons

#Sets up the gpio pins for the buttons for input and output

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(CHANNEL1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(CHANNEL2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(CHANNEL3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(CHANNEL4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(ledPin,GPIO.OUT)
# Initalizes the queue that will represent the buttons the user must push to "successfully" open/ turn on led
def initMasterQueue():
    masterQueue = Queue(MAX_SIZE)
    i = 0
    while i < 4:
        masterQueue.enqueue(int(input("Enter a master key code input (1-4): ")))
        i +=1
    return masterQueue


# Interrupt handler for when a button is pushed
# interrupts the current line of code to execute
def callback_handle(channel):
    
    if queue.size() >= 4:  # if more than 4 inputs has been added to the current queue list, dequeue one
        queue.dequeue()
    queue.enqueue(CHANNELTOINPUT[channel])
    print("Button " + str(CHANNELTOINPUT[channel]) + " has been pushed. The current inputs are " )
    queue.printQueue()

# initalize the interrupts to the dictionary and add the events to be detect
def initalizeInterrupts():
    CHANNELTOINPUT[CHANNEL1] = 1  # each buttons channel value is added to a dictionary as a key`
    CHANNELTOINPUT[CHANNEL2] = 2  # assigned a value 1-4 to simulate separate buttons
    CHANNELTOINPUT[CHANNEL3] = 3
    CHANNELTOINPUT[CHANNEL4] = 4

    GPIO.add_event_detect(CHANNEL1, GPIO.FALLING, callback=callback_handle, bouncetime=150)  # channel = GPIO pin
    GPIO.add_event_detect(CHANNEL2, GPIO.FALLING, callback=callback_handle,
                          bouncetime=300)  # gpio falling = falling edge of the button
    GPIO.add_event_detect(CHANNEL3, GPIO.FALLING, callback=callback_handle,
                          bouncetime=300)  # callback = the function to be called on detection
    GPIO.add_event_detect(CHANNEL4, GPIO.FALLING, callback=callback_handle,
                          bouncetime=300)  # bouncetime = deadtime on being able to add another input


def main():
    setup()
    initalizeInterrupts()
    masterQueue = initMasterQueue()
    GPIO.output(ledPin,GPIO.LOW) #set it to low on start up
    
    while True:
        
        
        if queue.getQueue() == masterQueue.getQueue():  # if the last 4 inputs inputted by the buttons are equal to the master key
            GPIO.output(ledPin, GPIO.HIGH)
            send_mail()
            queue.dequeue()
            queue.dequeue()
            queue.dequeue()
            queue.dequeue()
        else:
            GPIO.output(ledPin,GPIO.LOW)
            
main()
import RPi.GPIO as GPIO
import time

ledPin = 11    # define ledPin

def setup():
  GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering i.e., GPIO 17 is pin 11
  GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
  GPIO.output(ledPin, GPIO.LOW)  # make the ledPin's output LOW level 
  print ('using pin%d'%ledPin)

def mainLoop():
  while True:
    GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
    print ('led turned on >>>')     # print information on terminal
    time.sleep(1)                   # Wait for 1 second
    GPIO.output(ledPin, GPIO.LOW)   # make ledPin output LOW level to turn off led
    print ('led turned off <<<')
    time.sleep(1)                   # Wait for 1 second

def destroy():
  GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':
  print ('Starting Project, please use ctrl+c to end at any point\n')
  setup()
  try:
    mainLoop()
  except KeyboardInterrupt:   # Press ctrl-c to end the program.
    destroy()
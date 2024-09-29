import RPi.GPIO as GPIO
import time
from libraries.ADCDevice import ADCDevice, PCF8591, ADS7830

adc = ADCDevice() # Define an ADCDevice class object
ledPin = 11    # define ledPin

def setup():
  setupLeds()
  setupAdc()

def setupLeds():
  GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering i.e., GPIO 17 is pin 11
  GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
  GPIO.output(ledPin, GPIO.LOW)  # make the ledPin's output LOW level 
  print ('using pin%d'%ledPin)


def setupAdc():
  global adc
  if(adc.detectI2C(0x48)): # Detect the pcf8591.
    adc = PCF8591()
  elif(adc.detectI2C(0x4b)): # Detect the ads7830
    adc = ADS7830()

def mainLoop():
  while True:
    loopLeds()
    loopAdc()

def loopLeds():
  GPIO.output(ledPin, GPIO.HIGH)  # make ledPin output HIGH level to turn on led
  print ('led turned on >>>')     # print information on terminal
  time.sleep(1)
  GPIO.output(ledPin, GPIO.LOW)   # make ledPin output LOW level to turn off led
  print ('led turned off <<<')
  time.sleep(1)

def loopAdc():
  value = adc.analogRead(0)    # read the ADC value of channel 0
  voltage = value / 255.0 * 3.3  # calculate the voltage value
  print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
  time.sleep(0.1)

def destroy():
  GPIO.cleanup()                      # Release all GPIO
  adc.close()

if __name__ == '__main__':
  print ('Starting Project, please use ctrl+c to end at any point\n')
  setup()
  try:
    mainLoop()
  except KeyboardInterrupt:   # Press ctrl-c to end the program.
    destroy()
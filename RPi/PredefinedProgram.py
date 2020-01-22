#from playsound import playsound
 
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import os
import time
 
state = 0
f = open("Data.txt", "w+")
f.write("white, SISMA")
f.close()
 
########################################################################
 
#Input and output pins setup
 
########################################################################
 
 
GPIO.setmode(GPIO.BCM)
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
 
########################################################################
 
#Predefined Program Button SetUp 
 
########################################################################
 
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
 
########################################################################
 
#Knobes Configurations and Functions
 
########################################################################
 
# define GPIO pins with variables a_pin and b_pin
a_pin = 18
b_pin = 23
 
# create discharge function for reading capacitor data
def discharge():
   GPIO.setup(a_pin, GPIO.IN)
   GPIO.setup(b_pin, GPIO.OUT)
   GPIO.output(b_pin, False)
   time.sleep(0.005)
 
# create time function for capturing analog count value
def charge_time():
   GPIO.setup(b_pin, GPIO.IN)
   GPIO.setup(a_pin, GPIO.OUT)
   count = 0
   GPIO.output(a_pin, True)
   #print("Inside the charge time function")
   while not GPIO.input(b_pin):
       count = count +1
   return count
 
def analog_read():
   discharge()
   return charge_time()
 
 
########################################################################
 
#Internal Sensor Setup and functions
 
########################################################################
def readInternalTemp():
   tempFile = open("/sys/bus/w1/devices/28-0119137d6016/w1_slave")
   tempText = tempFile.read()
   tempFile.close()
   result = tempText.split("\n")[1].split(" ")[9]
   tempCelsius = float(result[2:])
   tempCelsius = tempCelsius/1000
   return tempCelsius
 
 
while(True):
   #Waiting to select the pre-defined program
   if (state == 0 and GPIO.input(15) == 1):
       f = open("Data.txt", "w+")
       f.write("grey, chicken")
       f.close()
       os.system("mpg321 ~/Desktop/TechChallenge/Audio/Sisma/Aufnahme_1.mp3")
       state = 1
       time.sleep(1.5)
  
   #print("Inside the while loop")
   #Tell the user to select the Auto Mode
   if (state == 1):
       f = open("Data.txt", "w+")
       f.write("grey, Select Auto")
       f.close()
       os.system("mpg321 ~/Desktop/TechChallenge/Audio/Sisma/Aufnahme_2.mp3")
       state = 2
       time.sleep(2)
      
   #Upon change in the Knobe
   #print(analog_read())
   if (state == 2 and analog_read() <= 20):
       f = open("Data.txt", "w+")
       f.write("grey, Started")
       f.close()
       os.system("mpg321 ~/Desktop/TechChallenge/Audio/Sisma/Aufnahme_3.mp3")
       state = 3
       time.sleep(2)
      
      
   internalTemp = int(readInternalTemp())
   #Read the internal Temperature of the food and display it to the end user
   if (state == 3):     
       print("Current internal Temperature is : " + str(internalTemp) + " C")
       f = open("Data.txt", "w+")
       f.write("green, " + str(internalTemp) + " C")
       f.close()
       time.sleep(1)
      
       if (internalTemp >= 35):
           state = 4
      
   #the food is ready, Notify the user that the food is ready
   if (state == 4):
       f = open("Data.txt", "w+")
       f.write("yellow, Ready soon")
       f.close()
       os.system("mpg321 ~/Desktop/TechChallenge/Audio/Sisma/Aufnahme_4.mp3")
       state = 5
       time.sleep(1.5)
      
   if (state == 5):     
       print("Current internal Temperature is : " + str(internalTemp) + " C")
       f = open("Data.txt", "w+")
       f.write("yellow, " + str(internalTemp) + " C")
       f.close()
       time.sleep(1)
      
       if (internalTemp >= 40):
           state = 6
  
   #the food is ready, Notify the user that the food is ready
   if (state == 6):
       f = open("Data.txt", "w+")
       f.write("red, Enjoy")
       f.close()
       os.system("mpg321 ~/Desktop/TechChallenge/Audio/Sisma/Aufnahme_5.mp3")
       state = 7
       time.sleep(10)
      
  
   #Food is collected, now the system starts again
   if (state == 7):
       f = open("Data.txt", "w+")
       f.write("white, SISMA")
       f.close()
       time.sleep(3)
       state = 0
  
   time.sleep(0.05)
  
GPIO.cleanup() # Clean up


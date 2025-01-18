#!/usr/bin/python

# Import required libraries
import time
import RPi.GPIO as GPIO# Library for Raspberry Pi GPIO control
import time
import os,sys
from urllib.parse import urlparse # For handling URLs if needed in future
import paho.mqtt.client as paho # MQTT library for IoT communication
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import drivers # LCD display driver
from time import sleep
from datetime import datetime  # For handling date and time

# Initialize the LCD display
display = drivers.Lcd()

# Define GPIO pins for parking slot sensors
slot1_Sensor = 13# Sensor for parking slot 1
slot2_Sensor = 15# Sensor for parking slot 2

# Set up GPIO pins as input
GPIO.setup(slot1_Sensor, GPIO.IN) 
GPIO.setup(slot2_Sensor, GPIO.IN) 


# Display welcome message on LCD
display.lcd_display_string("welcome ",1)
time.sleep(0.5)
display.lcd_display_string("Car Parking ",1)
display.lcd_display_string("System ",2)
time.sleep(0.5)
display.lcd_clear()  # Clear the LCD display

# Infinite loop to continuously check parking slot status
while 1:
 # Read sensor input status
  slot1_status = GPIO.input(slot1_Sensor)
  time.sleep(0.1)
  slot2_status = GPIO.input(slot2_Sensor)
  time.sleep(0.1)


    # Check if slot 1 is occupied or free
  if (slot1_status == False):  # If sensor detects a vehicle
   display.lcd_display_string("Slot1 Parked  ",1)
   time.sleep(0.1)
  else:
    display.lcd_display_string("Slot1 Free  ",1)
    time.sleep(0.1)
    
      # Check if slot 2 is occupied or free
  if (slot2_status == False): # If sensor detects a vehicle
   display.lcd_display_string("Slot2 Parked  ",2)
   time.sleep(0.1)
  else:
    display.lcd_display_string("Slot2 Free  ",2)
    time.sleep(0.1)




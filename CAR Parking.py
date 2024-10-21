#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import time
import os,sys
from urllib.parse import urlparse
import paho.mqtt.client as paho
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
import drivers
from time import sleep
from datetime import datetime
display = drivers.Lcd()



slot1_Sensor = 13
slot2_Sensor = 15

GPIO.setup(slot1_Sensor, GPIO.IN) 
GPIO.setup(slot2_Sensor, GPIO.IN) 



display.lcd_display_string("welcome ",1)
time.sleep(0.5)
display.lcd_display_string("Car Parking ",1)
display.lcd_display_string("System ",2)
time.sleep(0.5)
display.lcd_clear()

while 1:
  # Print out results
  slot1_status = GPIO.input(slot1_Sensor)
  time.sleep(0.1)
  slot2_status = GPIO.input(slot2_Sensor)
  time.sleep(0.1)
  if (slot1_status == False):
   display.lcd_display_string("Slot1 Parked  ",1)
   time.sleep(0.1)
  else:
    display.lcd_display_string("Slot1 Free  ",1)
    time.sleep(0.1)
    
  if (slot2_status == False):
   display.lcd_display_string("Slot2 Parked  ",2)
   time.sleep(0.1)
  else:
    display.lcd_display_string("Slot2 Free  ",2)
    time.sleep(0.1)

  #/ i am happy mehatab


#!/usr/bin/python
import time;  
import serial;

#Send "o\n" to trigger the MCU to send a power on command.

ser = serial.Serial('/dev/tty.usbmodem1a1221')

alarmMin = 1
alarmHour = 7

while 1:
	time.sleep(5) #don't do stuff for a while
	x = time.localtime()
	print x #print to debug
	if x[3] == alarmHour:
		if x[4] == alarmMin:
			ser.write("o\n")#send this string and the microcontroller handles the rest
		



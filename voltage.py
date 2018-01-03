#!/usr/bin/env python

import os
import sys
import threading
import serial
import time
import math
import select

ser = serial.Serial(
	port='/dev/ttyACM1',
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)

ser.isOpen()

while 1 :
	os.system('cls' if os.name == 'nt' else 'clear')
	ser.flushInput()
	ser.write('b' + '\r\n')
	out = ''
	while ser.inWaiting() > 0:
		out += ser.read(1)
	if out != '':
		a = out
		b = a.split("\r\n")
		print 'Press Enter to stop read voltage'
		if 8 < len(b):
			for i in range(0,7):
				x = float(b[i][8:])
				vol = 3.3*(x/4096.0)
				vol1 = math.ceil(vol*1000)/1000
				print "voltage = " + str(vol1)
		else:
			print 'Error when get value from MCu'
	if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
		line = raw_input()
		break
	time.sleep(0.05)
	#time.sleep(1)

ser.close()

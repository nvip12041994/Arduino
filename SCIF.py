#!/usr/bin/python

import threading
import serial
import sys
import time
import re
import datetime
from time import sleep

_waited_time_out = 20;  # if there is no data transferring, waitln() will break after time_out seconds.
#-------------------- global variables -------------------#
CStr_Expect = ''
_input_str = ''
_bytes_to_read = 0
_matched_result = 0
_start_time = time.time()
_serial = ''


global PASSED, FAILED
FAILED=1
PASSED=0
time_out=45

class serial_thread(threading.Thread):
    def __init__(self,com,has_print=1):
        threading.Thread.__init__(self)
        self.port_name=''
        self.has_print=has_print
        self.daemon=True
        self.port_err=False
        self.pause=False
        self.serial = serial.Serial()
        self.buff=''
        if self.config(com)==False:
            exit(1)

    def config(self,com):
        self.serial.baudrate = 115200
        self.serial.port = com
        self.serial.stopbits = serial.STOPBITS_ONE
        self.serial.xonxoff = 0
        self.serial.timeout = 60

        try:
            self.serial.open()
            self.port_err = False
            return True
        except:
            print 'cannot open port %s'% self.port_name
            self.port_err=True
            return False

    def output_str(self,_input_str):
        if self.has_print==0:
            return 0
        for i in _input_str:
            sys.stdout.write(i)
            sys.stdout.flush()
            if i == '\n':
                # sys.stdout.write('[' + datetime.datetime.now().strftime("%a %b %d %H:%M:%S.%f %Y") + '] ')
                sys.stdout.flush()

    def run(self):
        if (self.serial.isOpen()):
            _bytes_to_read = self.serial.inWaiting()
            self.serial.read(_bytes_to_read)
            if self.port_err:
                return 1;

        while self.serial.isOpen():
            _bytes_to_read = self.serial.inWaiting()
            if _bytes_to_read:
                    data=self.serial.read(_bytes_to_read)
                    self.output_str(data)
                    self.buff =self.buff+data
                    if len(self.buff)>512:
                        self.buff=self.buff[12:]



            sleep(0.1)

    def send(self,str,time=0,board_name="root@salvator-x:~#"):
        sleep(0.5)
        self.buff=""
        self.serial.write('\n')
        i=0
        for i in range(1, 10):
            if (self.buff.find(board_name)>-1):
                break
            else:
                sleep(1)

        else:
            #print "Time out command"
            return FAILED

        sleep(0.1)
        for i in str:
            self.serial.write(i)
            sleep(time)
        self.serial.write('\r')
        return PASSED

    def func_fail(self):
        #print "Test case Failed !!!"
        self.serial.close()
        exit(0)

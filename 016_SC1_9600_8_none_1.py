#!/usr/bin/python
import serial
from time import sleep
import sys
import SCIF as scif
import subprocess

FAILED=1
PASSED=0

if __name__ == '__main__':
    com0=scif.serial_thread("/dev/ttyUSB1", 1)
    com1=scif.serial_thread("/dev/pts/29", 1)

    com0.start()
    com1.start()
	
    while True:
        sleep(10)

    #try_process=0
    #com0.buff=""
    #com0.serial.write('\n')
    #while True:
    #    if (com0.buff.find('login')>-1):
    #        com0.serial.write('root')
    #        com0.serial.write('\r')
    #        break
    #    if (com0.buff.find('root@salvator-x:~#')>-1):
    #        #com0.send('',0.1)
    #        break
    #    #com0.send('\n', 0.1)
    #    try_process = try_process + 1
    #    sleep(1)
    #    if (try_process > scif.time_out):
    #        print "Cannot find root@salvator-x:~#"
    #        com0.serial.close()
    #        com1.serial.close()
    #        exit(0)
    #
    #if (com0.send('zcat /proc/config.gz | grep SERIAL_SH_SCI_DMA',0.05)==FAILED):
    #    print "\n\nCommand zcat Failed!\n"
    #    com0.serial.close()
    #    com1.serial.close()
    #    exit(0)
    #sleep(0.5)
    #if (com0.buff.find('SERIAL_SH_SCI_DMA=y') > -1):
    #    print "\n\nCONFIG FAILURE !!!\n"
    #    com0.serial.close()
    #    com1.serial.close()
    #    exit(0)
    #sleep(1)
    #
    #com0.send('stty -F /dev/ttySC1 speed 9600 cs8 -cstopb', 0.05)
    #sleep(1)
    #com0.send('cat /dev/ttySC1',0.05)
    #sleep(1)
    ##cmd = "echo abcd > /dev/ttyUSB0"
    ##subprocess.call(cmd, shell=True)
    ##sleep(1)
    #
    #print "\n\nStart On Host"
    #print "stty -F /dev/ttyUSB1 speed 9600 cs8 -cstopb"
    #print "cat file_1mb.dat > /dev/ttyUSB1"
    #subprocess.call("stty -F /dev/ttyUSB1 speed 9600 cs8 -cstopb", shell=True)
    #print "End On Host \n"
    #sleep(0.5)
    #subprocess.call("cat file_100kb.dat > /dev/ttyUSB1", shell=True)
    #
    #sleep(10)
    #com0.serial.write(chr(3))
    #sleep(1)
    #if (com0.send('') == FAILED):
    #    try_process = 0
    #    while try_process < 1200:
    #        if (com0.buff.find('[<ffff') > -1):
    #            break
    #        sleep(0.1)
    #        try_process = try_process + 1
    #
    #    print "\n\nError !!!\n"
    #    com0.serial.close()
    #    com1.serial.close()
    #    exit(0)
    #
    #sleep(0.5)
    #com0.serial.close()
    #com1.serial.close()
    #
    #sleep(0.5)
    #print "\n\nSuccess !!!\n"
    exit(0)

    #com0.join()


















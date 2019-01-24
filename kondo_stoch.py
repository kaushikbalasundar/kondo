#!/usr/bin/env/python
import serial
import time
import struct
import array
import numpy

com = serial.Serial()
com.port = '/dev/ttySAC0'
com.baudrate = 115200
com.bytesize = 8
com.parity =serial.PARITY_EVEN
com.stopbits =1
com.timeout = 0.1
com.open()
buff  = bytearray(3)
temp_ = bytearray(2)

def setSpd(ID,spd):
    speed = spd
    while 1:
        buff[0] = 0xC0 + ID;      
        buff[1] = 0x02;  
        buff[2] = speed
        com.write(buff)
        buf_read = com.read(6)
        if(len(buf_read)==6):
	        temp_[0] = ord(buff_read[4])
	        temp_[1] = ord(buff_read[5])
	        val = temp_[1](temp_[0] << 7)
	        print "%d" %(val)

def setPos(ID,pos):
    target_angle = pos
    while 1: 
        buff[0] = 0x80 + ID
        buff[1] = (target_angle >> 7) & 0x7f
        buff[2] = target_angle & 0x7f
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp_[1](temp_[0] << 7)
        print "%d" %(val)

def setStrc(ID,strc):
    while 1: 
        buff[0] = 0xC0 + ID
        buff[1] = 0x01;
        buff[2] = strc
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp_[1](temp_[0] << 7)
        print "%d" %(val)

def setCurlim(ID,curlim):
    while 1: 
        buff[0] = 0xC0 + ID
        buff[1] = 0x03;
        buff[2] = curlim
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp_[1](temp_[0] << 7)
        print "%d" %(val)


def setFree(ID,curlim):
    while 1: 
        buff[0] = 0x80 + ID
        buff[1] = 0;
        buff[2] = 0;
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp_[1](temp_[0] << 7)
        print "%d" %(val)

def settemp(ID,templim):
    while 1: 
        buff[0] = 0xC0 + ID
        buff[1] = 0x04;
        buff[2] = templim
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp_[1](temp_[0] << 7)
        print "%d" %(val)

def getStrc(ID):
    while 1: 
        buff[0] = 0xA0 + ID
        buff[1] = 0x01;
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp[2]
        print "%d" %(val)

def getSpd(ID):
    while 1: 
        buff[0] = 0xA0 + ID
        buff[1] = 0x02;
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp_[1](temp_[0] << 7)
        print "%d" %(val)

def getStrc(ID):
    while 1: 
        buff[0] = 0xA0 + ID
        buff[1] = 0x03;
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp[2]
        print "%d" %(val)

def getTemp(ID,templim):
    while 1: 
        buff[0] = 0xA0 + ID
        buff[1] = 0x04;
        buff[2] = templim
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp[2]
        print "%d" %(val)

def getPos(ID,templim):
    while 1: 
        buff[0] = 0xA0 + ID
        buff[1] = 0x05;
        buff[2] = templim
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp[2]
        print "%d" %(val)

def getStrc(ID,templim):
    while 1: 
        buff[0] = 0xA0 + ID
        buff[1] = 0x01;
        buff[2] = templim
        com.write(buff)
        buf_read = com.read(6)
    if(len(buf_read)==6):
        temp_[0] = ord(buff_read[4])
        temp_[1] = ord(buff_read[5])
        val = temp[2]
        print "%d" %(val)

time.sleep(10)
 

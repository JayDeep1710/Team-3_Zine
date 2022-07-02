import serial
import struct
import time

arduino = serial.Serial('COM6', 9600)


arduino.write(struct.pack('>BB', 45, 90))

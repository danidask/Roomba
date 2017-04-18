#!/usr/bin/python

import os
import serial  # pyserial

# SISTEMA_OPERATIVO = os.uname()[3]
# print(SISTEMA_OPERATIVO)
# if SISTEMA_OPERATIVO.find("Ubuntu") > 0:
#     ser = serial.Serial('/dev/rfcomm3', 115200)
# else:
#     print("Otros sitemas operativos aun no contemplados")
#     quit()
# ser.open()
# print(ser.is_open)

class Roomba:
    serie = None

    def __init__(self, puerto):
        self.serie = serial.Serial(puerto, 115200)

    def control(self):
        self.serie.write(chr(128))  # Start
        self.serie.write(chr(131))  # Safe mode
        return

    def mover(self):
        self.serie.write(chr(145))  # Drive Direct (-500 a 500 mm/s)
        self.serie.write(chr(0))  # Right velocity high byte
        self.serie.write(chr(200))  # Right velocity low byte
        self.serie.write(chr(0))  # Left velocity high byte
        self.serie.write(chr(200))  # Left velocity low byte
        return

    def parar(self):
        self.serie.write(chr(173))  # Stop
        return

    def apagar(self):
        self.serie.write(chr(133))  # Power down
        return

# ser.write(chr(143))  # Seek Dock
# ser.write(chr(143))  # Seek Dock

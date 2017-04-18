#!/usr/bin/python

from Roomba import Roomba

puerto = '/dev/rfcomm3'
robot = Roomba(puerto)

entrada = raw_input("intro para empezar")

robot.control()
robot.mover()

entrada = raw_input("intro para parar")

robot.parar()
robot.apagar()



quit()


bucle = True
while bucle:
    entrada = raw_input("->")
    if entrada == "":
        bucle = False
    else:
        # print(entrada)
        ser.write(chr(49))
    tempstr = ""
    while ser.in_waiting > 0:
        tempstr += ser.read_all()
        print(tempstr)

# ser.close()
print("FIN")



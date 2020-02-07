#!/usr//bin/python3

import sys

if len(sys.argv) > 4 or len(sys.argv) != 4:
    print("Introduce una operacion y un operando")
    sys.exit(1)

operation = sys.argv[1]
operand1 =  int(sys.argv[2])
operand2 =  int(sys.argv[3])

if operation == "add":
    print("El resultado es: "+ str(operand1 + operand2))
if operation == "sub":
    print("El resultado es: "+ str(operand1 - operand2))
if operation == "mul":
    print("El resultado es: "+ str(operand1 * operand2))
if operation == "div":
    print("El resultado es: "+ str(operand1 / operand2))

#!/usr//bin/python3

import sys

if len(sys.argv) != 4:
    print("Introduce una operacion y dos operandos")
    sys.exit(1)

operation = sys.argv[1]
operand1 =  int(sys.argv[2])
operand2 =  int(sys.argv[3])

if operation == "add":
    result = operand1 + operand2
if operation == "sub":
    result = operand1 - operand2
if operation == "mul":
    result = operand1 * operand2
if operation == "div":
    result = operand1 / operand2

print("El resultado es: "+ str(result))

#!/usr//bin/python3

import sys

if len(sys.argv) != 4:
    print("Introduce una operacion y dos operandos")
    sys.exit(1)

operation = sys.argv[1]
try:
    operand1 =  int(sys.argv[2])
    operand2 =  int(sys.argv[3])
except ValueError:
    print("Introduce un operando valido")
    sys.exit(1)

if operation == "add":
    result = operand1 + operand2
elif operation == "sub":
    result = operand1 - operand2
elif operation == "mul":
    result = operand1 * operand2
elif operation == "div":
    result = operand1 / operand2
else:
    print("Introduce una operacion: add, sub, mul o div")
    sys.exit(1)

print("El resultado es: "+ str(result))

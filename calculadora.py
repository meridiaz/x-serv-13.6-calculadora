#!/usr//bin/python3


import sys

operation = sys.argv[1]
operand1 =  int(sys.argv[2])
operand2 =  int(sys.argv[3])

def add(operand1, operand2):
    return operand1 + operand2

def sub(operand1, operand2):
    return operand1 - operand2

def mul(operand1, operand2):
    return operand1 * operand2

def div(operand1, operand2):
    return operand1 / operand2

if operation == "add":
    print("El resultado es: "+ str(add(operand1, operand2)))
    #llamo a sumar
if operation == "sub":
    print("El resultado es: "+ str(sub(operand1, operand2)))
    #llamo a restar
if operation == "mul":
    print("El resultado es: "+ str(mul(operand1, operand2)))
    #llamo a mul
if operation == "div":
    print("El resultado es: "+ str(div(operand1, operand2)))
    #llamo a dividir

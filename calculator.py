#!/usr/bin/env python 
while True:

    first_number = input("Please enter your first number: ")

    operator = input("Please enter operator: ")

    second_number = input("Please enter your second number: ")

    def addition(first_number, second_number):
    
        num1 = int(first_number)
        num2 = int(second_number)
        print(num1 + num2)
        return

    def subtract(first_number, second_number):
    
        num1 = int(first_number)
        num2 = int(second_number)
        print(num1 - num2)
        return

    def multiply(first_number, second_number):
    
        num1 = int(first_number)
        num2 = int(second_number)
        print(num1 * num2)
        return
        
    def divide(first_number, second_number):
    
        num1 = int(first_number)
        num2 = int(second_number)
        print(num1 / num2)
        return

        

    if operator == '+':
        addition(first_number, second_number)

    if operator == '-':
        subtract(first_number, second_number)

    if operator == '*':
        multiply(first_number, second_number)

    if operator == '/':
        if second_number == '0':
            print("Cannot divide by 0")
        else:
            divide(first_number, second_number)

    else: 
        print("Please enter a valid operator ")

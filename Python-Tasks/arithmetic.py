# TASK 1 - BASIC ARITHMETIC OPERATIONS 
def arithmetic_operations():
    x = int(input("Enter the first number:"))
    y=  int(input("Enter the second number:"))
    
    addition= x+y
    subtraction=x-y
    multiplication=x*y
    division=None
    
    if y != 0:
        division= x/y
    
    print("\n Addition of two numbers:",addition)
    print("Subtraction of two numbers:",subtraction)
    print("Multiplication of two numbers:",multiplication)
    
    if division is not None:
        print("Division of two numbers:",division)
    else:
        print("ERROR! Cannot divide by zero")
    
    
arithmetic_operations()

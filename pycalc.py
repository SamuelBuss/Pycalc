def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: You cannot divide by zero."
    return a / b
equation = input("Enter your equation: ")
equation = equation.split()
print(equation[0])
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
if len(equation) != 3:
    print("Error: Please enter an equation in the format: number operator number")
    exit()
a = equation[0]
operator = equation[1]
b = equation[2]
if operator not in ['+', '-', '*', '/']:
    print("Error: Unsupported operator. Please use one of +, -, *, /.")
    exit()
if operator == '+':
    result = addition(float(a), float(b))
elif operator == '-':
    result = subtraction(float(a), float(b))
elif operator == '*':
    result = multiplication(float(a), float(b))
elif operator == '/':
    result = division(float(a), float(b))
print("Result:", result)
exit()

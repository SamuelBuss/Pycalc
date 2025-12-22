def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divisionrem(a, b):
    return a // b
equation = input("Enter your equation: ")
equation = equation.split()
if len(equation) != 3:
    print("Error: Please enter an equation in the format: number operator number")
    exit()
a = float(equation[0])
operator = equation[1]
b = float(equation[2])
if b == 0 and operator == '/':
    print("Error: Division by zero is not allowed.")
    exit()
if operator not in ['+', '-', '*', '/']:
    print("Error: Unsupported operator. Please use one of +, -, *, /.")
    exit()
if a % b != 0 and operator == '/':
    remainder = int(a % b)
else:
    remainder = ""
if operator == '+':
    result = addition(a, b)
elif operator == '-':
    result = subtraction(a, b)
elif operator == '*':
    result = multiplication(a, b)
elif operator == '/':
    if a % b == 0:
        result = divisionrem(a, b)
        print("Result:", int(result))
        exit()
    print("Result:", int(divisionrem(a, b)), "Remainder:", remainder)
    exit()
print("Result:", float(result))
exit()
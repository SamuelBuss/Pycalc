# Simple command-line calculator
# Ask the user whether they want to see the remainder for division operations
remainderoption = input("Do you want to see the remainder for division operations? (yes/no): ").strip().lower()
# Validate yes/no input
if remainderoption not in ['yes', 'no']:
    print("Error: Please answer with 'yes' or 'no'.")
    exit()
# Convert to t/f for easier checks later
if remainderoption == 'no':
    remainderoption = False
else:
    remainderoption = True

# --- arithmetic helpers ---
def addition(a, b):
    """Return the sum of a and b"""
    return a + b

def subtraction(a, b):
    """Return the difference a - b"""
    return a - b

def multiplication(a, b):
    """Return the product of a and b"""
    return a * b

def division(a, b):
    """Return floating-point division a / b"""
    return a / b

def divisionrem(a, b):
    """Return integer division (floor division) a // b"""
    return a // b

# --- parse input ---
# Expected input format: number operator number (e.g., "10 / 3")
equation = input("Enter your equation: ")
equation = equation.split()
if len(equation) != 3:
    print("Error: Please enter an equation in the format: number operator number")
    exit()

# Convert input list to float variables
a = float(equation[0])
operator = equation[1]
b = float(equation[2])

# Validate operator and check for division by zero
if b == 0 and operator == '/':
    print("Error: Division by zero is not allowed.")
    exit()
if operator not in ['+', '-', '*', '/']:
    print("Error: Unsupported operator. Please use one of +, -, *, /.")
    exit()

# Determine remainder when doing division (if applicable)
if a % b != 0 and operator == '/':
    remainder = int(a % b)
else:
    remainder = ""

# Perform the chosen operation
if operator == '+':
    result = addition(a, b)
elif operator == '-':
    result = subtraction(a, b)
elif operator == '*':
    result = multiplication(a, b)
elif operator == '/' and remainderoption == False:
    # User doesn't want remainder: perform floating-point division
    result = division(a, b)

# If user requested remainder, show integer division result and remainder
if remainderoption == True and operator == "/":
    if a % b == 0:
        # Exact division: show integer result (no remainder)
        result = divisionrem(a, b)
        print("Result:", int(result))
        exit()
    # Show result and remainder separately
    print("Result:", int(divisionrem(a, b)))
    print("Remainder:", remainder)
    exit()

# Default: print the (floating-point) result
print("Result:", float(result))
exit()
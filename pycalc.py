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

def format_number(x):
    """Format numbers for display: show integers without trailing .0"""
    # For floats that are whole numbers, return as int
    if isinstance(x, float):
        if x.is_integer():
            return int(x)
        return x
    return x

# --- parse input ---
# Expected input format: number operator number (e.g., "10 / 3")
equation = input("Enter your equation: ")
equation = equation.split()
# Validate input lenght
if len(equation) != 3:
    print("Error: Please enter an equation in the format: number operator number")
    exit()

# Errors for wrong input
# Validate that the first and third elements are numbers (support floats and negatives)
operator = equation[1]
try:
    a = float(equation[0])
    b = float(equation[2])
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()
# Validate division by zero
if b == 0 and operator == '/':
    print("Error: Division by zero is not allowed.")
    exit()
# Validate operator
if operator not in ['+', '-', '*', '/']:
    print("Error: Unsupported operator. Please use one of +, -, *, /.")
    exit()
# Determine remainder when doing division (if applicable)
if operator == '/' and a % b != 0:
    remainder = a % b
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
        print("Result:", format_number(result))
        exit()
    # Show result and remainder separately
    print("Result:", format_number(divisionrem(a, b)))
    print("Remainder:", format_number(remainder))
    exit()

# Default: print the result with clean formatting
print("Result:", format_number(result))
exit()
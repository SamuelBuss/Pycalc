from time import sleep
import configparser
from pathlib import Path
import re
import math

# Project settings file (INI) - created only at runtime
SETTINGS_PATH = Path(__file__).parent / "settings.ini"
config = configparser.ConfigParser()
if SETTINGS_PATH.exists():
    config.read(SETTINGS_PATH)
    try:
        intro_enabled = config.getboolean("settings", "introduction", fallback=True)
    except Exception:
        intro_enabled = True
else:
    # First run: default to True, create file when user changes it
    intro_enabled = True

# Show the introduction only when enabled
if intro_enabled:
    print("Welcome to my simple python calculator!")
    sleep(2)
    print("You can perform addition (+), subtraction (-), multiplication (*), and division (/).")
    sleep(2)
    print("Please enter your equation in the format: number operator number (e.g., 10 / 3)")
    sleep(1)

    # Ask whether to show it next time; if user says no, save setting
    ans = input("Do you wanna see the introduction next time? (Y/n) ").strip().lower()
    if ans in ("n", "no"):
        if not config.has_section("settings"):
            config["settings"] = {}
        config["settings"]["introduction"] = "false"
        with SETTINGS_PATH.open("w") as f:
            config.write(f)
else:
    # intro disabled; do nothing (skip intro)
    pass

# Ask the user whether they want to see the remainder for division operations
remainderoption = input("Do you want to see the remainder for division operations? (Y/n): ").strip().lower()
# Validate yes/no input
if remainderoption not in ['y', 'n', 'yes', 'no']:
    print("Error: Please answer with 'yes' or 'no'.")
    exit()
# Convert to t/f for easier checks later
if remainderoption in ['n', 'no']:
    remainderoption = False
else: 
    remainderoption = True

# --- mathematical constants ---
CONSTANTS = {
    'pi': math.pi,
    'e': math.e,
    'tau': math.tau,
    'phi': (1 + math.sqrt(5)) / 2,  # Golden ratio
}

# --- arithmetic helpers ---
def resolve_value(value_str):
    """Resolve a value: check if it's a constant name, otherwise parse as float"""
    if value_str.lower() in CONSTANTS:
        return CONSTANTS[value_str.lower()]
    try:
        return float(value_str)
    except ValueError:
        raise ValueError(f"'{value_str}' is not a valid number or constant")

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
equation = re.split(r'([+\-*/])', equation.strip())
# Remove empty strings and strip whitespace
equation = [p.strip() for p in equation if p.strip()]

# Handle negative numbers: if first part is '-' or '+', merge with next part
if len(equation) >= 2 and equation[0] in ['-', '+']:
    equation = [equation[0] + equation[1]] + equation[2:]

# Validate input length
if len(equation) != 3:
    print("Error: Please enter an equation in the format: number operator number")
    exit()
# Parse operands (handles both numbers and constants)
operator = equation[1]
try:
    a = resolve_value(equation[0])
    b = resolve_value(equation[2])
except ValueError as e:
    print(f"Error: {e}")
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
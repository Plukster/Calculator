
import sys

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

if len(sys.argv) != 4:
    print("Usage: python app.py <operator> <num1> <num2>")
    print("<operator>: add, subtract, or multiply")
    sys.exit(1)

operator = sys.argv[1]
num1 = float(sys.argv[2])
num2 = float(sys.argv[3])

if operator == "add":
    result = add(num1, num2)
elif operator == "subtract":
    result = subtract(num1, num2)
elif operator == "multiply":
    result = multiply(num1, num2)
else:
    print("Invalid operator. Please use 'add', 'subtract', or 'multiply'.")
    sys.exit(1)

print(f"The result is: {result}")

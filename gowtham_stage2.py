# Stage 2: Calculator with Result Check

# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Using if-elif-else
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
        exit()
    else:
        result = num1 / num2

else:
    print("Invalid operator")
    exit()

# Display result
print("Result =", result)

# Check result type
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")

#Taking in the numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Taking the operator from the user
operation = input("Enter an operation (+, -, *, /): ")

# Perform the given operation
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Math Error: Cannot divide by 0.")
else:
    print("Invalid operation. Please use +, -, *, or /.")

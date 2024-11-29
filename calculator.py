# Simple Calculator

def calculator():
    print("Welcome to the simple calculator!")

    # Prompt the user to input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Display operation choices
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Prompt the user to select an operation
    operation = input("Enter the number corresponding to your choice: ")

    # Perform the calculation
    if operation == "1":
        result = num1 + num2
        print(f"\nThe result of addition is: {result}")
    elif operation == "2":
        result = num1 - num2
        print(f"\nThe result of subtraction is: {result}")
    elif operation == "3":
        result = num1 * num2
        print(f"\nThe result of multiplication is: {result}")
    elif operation == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"\nThe result of division is: {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation choice. Please select a valid option.")

# Run the calculator
calculator()

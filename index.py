# Function for Addition
def add(x, y):
    return x + y

# Function for Subtraction
def subtract(x, y):
    return x - y

# Function for Multiplication
def multiply(x, y):
    return x * y

# Function for Division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to drive the program
def main():
    # Ask user for the first number
    num1 = float(input("Enter the first number: "))
    
    # Ask user for the second number
    num2 = float(input("Enter the second number: "))
    
    # Ask user for the operation
    operation = input("Enter operation (+, -, *, /): ")

    # Perform the operation based on user's input
    if operation == "+":
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif operation == "-":
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif operation == "*":
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif operation == "/":
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid operation! Please enter one of the following: +, -, *, /.")

# Run the main function
if __name__ == "__main__":
    main()

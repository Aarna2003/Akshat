# Simple Calculator

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "You can't divide by zero!"
    return num1 / num2

def calculator():
    print("Welcome to my calculator!")
    

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    

    print("\nWhat do you want to do?")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Pick a number (1, 2, 3, or 4): ")


    if choice == "1":
        result = add(num1, num2)
        print(f"The answer is: {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"The answer is: {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"The answer is: {result}")
    elif choice == "4":
        result = divide(num1, num2)
        print(f"The answer is: {result}")
    else:
        print("That wasn't a valid choice.")

if __name__ == "__main__":
    calculator()

print("Hello! Welcome to The Calculator App!")

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a/b

def exponent(a,b):
    return (a**b)

print("To begin, please enter an operator. (+,-,*,/,**)")

while True:
    choice = input("Enter Choice: ")

    if choice in ("+", "-", "*", "/","**"):
        try:
            number1 = float(input("Enter First Number: "))
            number2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue 
        
        if choice == "+":
            print(number1, "+", number2, "=", add(number1, number2))
        elif choice == "-":
            print(number1, "-", number2, "=", subtract(number1, number2))
        elif choice == "*":
            print(number1, "*", number2, "=", multiply(number1, number2))
        elif choice == "/":
            print(number1, "/", number2, "=", divide(number1, number2))
        elif choice == "**":
            print(number1, "^", number2, "=", exponent(number1, number2)) 

        next_calculation = input("Would you like to do another calculation? (y/n): ")
        if next_calculation == "n":
            break
    else:
        print("Invalid Input")
import time
from math import sqrt

# Function to perform basic calculations
def calc(a, b):
    try:
        choice = input("Choose the operation: +|-|*|/ ")
        if choice not in ("+", "-", "*", "/"):
            print("Error! Invalid operation.")
            return
        solution = eval(f'{a} {choice} {b}')
        print(f'The solution is: {solution}')
    except:
        print("Something went wrong! Please try again.")

# Function to solve equations
def eq_solver(a, b, c):
    choice = input("Choose the operation level: eq1/eq2 ")
    if choice.lower() == "eq1":
        if a == 0:
            if b == 0:
                print("Infinite solutions!")
            else:
                print("No solution")
        else:
            x = -b / a
            print("The result is:", round(x, 2))
    elif choice.lower() == "eq2":
        delta = (b * b) - (4 * a * c)
        if delta == 0:
            x = -b / (2 * a)
            print("There is one solution:", round(x, 2))
            shorthand = input("Do you want a shorthand for this expression? yes/no ")
            if shorthand == "yes":
                if x > 0:
                    short = f"{a}(x-{x})"
                    print("Shorthand is:", short)
                else:
                    short = f"{a}(x+{x})"
                    print("Shorthand is:", short)
        elif delta > 0:
            x1 = (-b - sqrt(delta)) / (2 * a)
            x2 = (-b + sqrt(delta)) / (2 * a)
            print("There are two solutions:")
            print("First one is:", round(x1, 2))
            print("Second one is:", round(x2, 2))
            shorthand = input("Do you want a shorthand for this expression? yes/no ")
            if shorthand == "yes":
                if x1 > 0 and x2 > 0:
                    short = f"{a}(x-{round(x1, 2)})(x-{round(x2, 2)})"
                    print("Shorthand is:", short)
                elif x1 > 0 and x2 < 0:
                    short = f"{a}(x-{round(x1, 2)})(x{round(x2, 2)})"
                    print("The shorthand is:", short)
                elif x1 < 0 and x2 > 0:
                    short = f"{a}(x{round(x1, 2)})(x-{round(x2, 2)})"
                    print("Shorthand is:", short)
                else:
                    short = f"{a}(x{round(x1, 2)})(x{round(x2, 2)})"
                    print("Shorthand is:", short)
        else:
            print("No real solutions.")

# Welcome message
print("Asalamo Alaykom! I hope you're enjoying here.")
time.sleep(3)
print("Welcome to my structured program")
time.sleep(1)
print("You can solve equations or perform calculations")
time.sleep(1)

# Get user's choice
options = input("Select your choice: calc/eq_solver ")

# Based on user's choice, proceed accordingly
if options.lower() == "calc":
    a, b = float(input("Enter the first value: ")), float(input("Enter the second value: "))
elif options.lower() == "eq_solver":
    number3_check = input('Do you need the third value? (yes/no) ')
    if number3_check.lower() == "yes":
        a,b,c = float(input("Enter the first value: ")), float(input("Enter the second value: ")),float(input("Enter the third value: "))
    else:
        pass
else:
    print("Wrong input! Please try again.")

# Perform calculations or equation solving based on the user's choice
if options.lower() == "calc":
    print("Starting calculation...")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    calc(a, b)
elif options.lower() == "eq_solver":
    print("Starting equation solving...")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    eq_solver(a, b, c)

# Retry option
retry = input("Do you want to try again? (yes/no) ")
if retry.lower() == "yes":
    print("Restarting in 3 seconds...")
    time.sleep(3)
    attempts = int(input("How many times do you want to retry? (integer value!) "))
    if attempts > 0:
        for retry in range(attempts):
            a, b, c = float(input("Enter the first value: ")), float(input("Enter the second value: ")), float(input("Enter the third value: "))
            options = input("Select your choice: calc/eq_solver ")
            if options.lower() == "calc":
                print("Starting calculation...")
                time.sleep(2)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                calc(a, b)
            elif options.lower() == "eq_solver":
                print("Starting equation solving...")
                time.sleep(2)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                eq_solver(a, b, c)
            else:
                print("Have a nice day")
        else:
            print("Have a nice day!")
    else:
        print("Negative numbers are unacceptable")
else:
    print("have a nice day")
    
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

#Function to solve system
def system_solving():
    time.sleep(1)
    
    print("enter the coefficient for the first equation: ")
    
    time.sleep(2)
    
    a1 = float(input("the first value: "))
    b1 = float(input("the second value: "))
    c1 = float(input("the third value: "))
    
    time.sleep(1)
    
    print("enter the coefficents for the second equation")
    
    time.sleep(2)
    
    a2 = float(input("the first value: "))
    b2 = float(input("the second value: "))
    c2 = float(input("the third value: "))

    delta = (a1*b2) - (b1*a2)
    delta_x = (c1*b2) - (b1*c2)
    delta_y = (a1*c2) - (c1*a2)

    if delta == 0 :
        if delta_x == delta_y == 0 :
            print("infinit solutions")
        else: 
            print("no solutions for this!")
    else:
        x = delta_x/delta
        y = delta_y/delta
        print ("x=",round(x,2),"and y=",round(y,2))
    method = input("do you want to see the method? ")
    
    if method == "yes" :
        print("here is the method")
        time.sleep(2)
        if b1 < 0 :
            print("your first equations is:",f'{a1}x  {b1}y = {c1}')
        else :
            print("your first equation is:",f'{a1}x + {b1}y = {c1}')
        time.sleep(1)
        if b2 < 0 :
            print("your second equation is:",f'{a2}x  {b2}y = {c2}')
        else:
            print("your second equation is:",f'{a2}x + {b2}y = {c2}')
        time.sleep(2)
        print("using Cramer's Rule to find x and y")
        time.sleep(2)
        print("delta =",f'({a1}*{b2}) - ({b1}*{a2}) = {round(delta,2)})')
        time.sleep(1)
        print("delta-x =",f'({c1}*{b2}-({b1}*{c2})) = {round(delta_x,2)}')
        time.sleep(1)
        print("delta-y =",f'({a1}*{c2})-({c1}*{a2}) = {round(delta_y,2)}')
        time.sleep(2)
        print("the final result:")
        time.sleep(1)
        print("x="f'{round(delta_x,2)}/{round(delta,2)} = {round(x,2)}')
        time.sleep(1)
        print("y=",f'{round(delta_y,2)}/{round(delta,2)} = {round(y,2)}')
    else:
        time.sleep(1)
        print("i hope you enjoying here!")
        return

# Welcome message
print("Asalamo Alaykom! I hope you're enjoying here.")
time.sleep(3)
print("Welcome to my structured program")
time.sleep(1)
print("You can solve equations and linear systems or perform calculations ")
time.sleep(1)

# Get user's choice
options = input("Select your choice: calc/eq_solver/sys_solver ")

# Based on user's choice, proceed accordingly
if options.lower() == "calc":
    a, b = float(input("Enter the first value: ")), float(input("Enter the second value: "))
elif options.lower() == "eq_solver":
    number3_check = input('Do you need the third value? (yes/no) ')
    if number3_check.lower() == "yes":
        a,b,c = float(input("Enter the first value: ")), float(input("Enter the second value: ")),float(input("Enter the third value: "))
    else:
        pass
elif options.lower()== "sys_solver" :
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

elif options.lower() == "sys_solver":
    print("Starting system solving...")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    system_solving()

# Retry option
retry = input("Do you want to try again? (yes/no) ")
if retry.lower() == "yes":
    print("Restarting in 3 seconds...")
    time.sleep(3)
    attempts = int(input("How many times do you want to retry? (integer value!) "))
    if attempts > 0:
        for retry in range(attempts):
            
            options = input("Select your choice: calc/eq_solver/sys_solver ")

            # Based on user's choice, proceed accordingly
            if options.lower() == "calc":
                a, b = float(input("Enter the first value: ")), float(input("Enter the second value: "))
            elif options.lower() == "eq_solver":
                number3_check = input('Do you need the third value? (yes/no) ')
                if number3_check.lower() == "yes":
                    a,b,c = float(input("Enter the first value: ")), float(input("Enter the second value: ")),float(input("Enter the third value: "))
                else:
                    pass
            elif options.lower()== "sys_solver" :
                pass 
            else:
                print("Wrong input! Please try again.")

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
            elif options.lower() == "sys_solver":
                print("Starting system solving...")
                time.sleep(2)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                system_solving()
            else:
                print("Have a nice day")
        else:
            print("Have a nice day!")
    else:
        print("Negative numbers are unacceptable")
else:
    print("have a nice day")
    
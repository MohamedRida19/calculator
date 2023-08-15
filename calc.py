import time
from math import sqrt
def calc(a,b):
    try:
        choice = input("chose the operation: +|-|*|/ ")
        valid_choice = ("+","-","*","/")
        if choice not in valid_choice:
            print("error! ")
            return
        expression = f'{a} {choice} {b}'
        solution = eval(expression)
        print(f'the expression is: {expression}')
        print(f'the solution is: {solution}')
    except:
        print("something wrong! try again pls")

def eq_solver(a,b,c):
    choice = input("chose the operation lvl: eq1/eq2 ")
    if choice.lower() == "eq1":
        if a==0 :
            if b==0:
                print("infinite results!")
            else:
                print("no result")
        else:
            x= -b/a
            print("the result is:",round(x,2))
    if choice.lower() == "eq2":
        delta = (b*b)-(4*a*c)
        if delta == 0:
            x = -b/2*a
            print ("there is one result:",round(x,2))
            shorthand=input("do you want a shorthand for this expression? yes/no ")
            if shorthand == "yes":
                if x > 0:
                    short = str(a)+"(x-"+str(x)+")"
                    print("shorthand is:",short)
                else :
                    short = a+"(x+"+str(x)+")"
                    print("shorthand is:",short)
        elif delta > 0 :
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            print ("there is two results:")
            print ("first one is:",round(x1,2))
            print("second one is:",round(x2,2))
            shorthand = input("do you want a shorhand for this expression? yes/no ")
            if shorthand == "yes":
                if x1 > 0 and x2 >0:
                    short = str(a)+"(x-"+str(round(x1,2))+")(x-"+str(round(x2,2))+")"
                    print("shorthand is:",round(short))
                elif x1 > 0 and x2 <0 :
                    short = str(a)+"(x-"+str(round(x1,2))+")(x"+str(round(x2,2))+")"
                    print("the shorthand is:",short)
                elif x1 < 0 and x2 >0 :
                    short = str(a)+"(x"+str(round(x1,2))+")(x-"+str(round(x2,2))+")"
                    print("shorthand is:",short)
                else:
                    short = str(a)+"(x"+str(round(x1,2))+")(x"+str(round(x2,2))+")" 
                    print("shorthand is:",short)              
        else:
            print("there is no results")

time.sleep(3)
print("Welcome to my structured program")
time.sleep(1)
print("You can solve equations or perform calculations")
time.sleep(1)
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

    retry = input("Do you want to try again? yes/no ")
    if retry.lower() == "yes":  # Corrected this line
        print("Restarting in 3 seconds...")
        time.sleep(3)
        a, b, c = float(input("Enter the first value: ")), float(input("Enter the second value: ")), float(input("Enter the third value: "))
        options = input("Select your choice: calc/eq_solver")
        if options.lower() == "calc":
            print("Starting calculation...")
            time.sleep(2)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            calc(a, b, c)
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
        print("Have a nice day")
    else:
        print("Have a nice day!")
else:
    print("Invalid choice. Have a nice day!")
import time
from math import sqrt
def calc(a,b):
    try:
        choice = input("Choose the operation: +|-|*|/ ")
        if choice not in ("+","-","*","/"):
            print("error! ")
            return
        solution = eval(f'{a} {choice} {b}')
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
                    short = f'{a}(x-{round(x,2)})'
                    print("shorthand is:",short)
                else :
                    short = f'{a}(x{round(x)})'
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
                    short = f"{a}(x-{round(x1,2)})(x-{round(x2,2)}) "
                    print("shorthand is:",round(short))
                elif x1 > 0 and x2 <0 :
                    short = f"{a}(x-{round(x1,2)})(x-{round(x2,2)}) "
                    print("the shorthand is:",short)
                elif x1 < 0 and x2 >0 :
                    short = f"{a}(x-{round(x1,2)})(x-{round(x2,2)}) "
                    print("shorthand is:",short)
                else:
                    short = f"{a}(x-{round(x1,2)})(x-{round(x2,2)}) "
                    print("shorthand is:",short)              
        else:
            print("there is no results")


print("Asalamo Alaykom! i hope you enjoying here")
time.sleep(3)
print("Welcome to my structured program")
time.sleep(1)
print("You can solve equations or perform calculations")
time.sleep(1)
options = input("Select your choice: calc/eq_solver ")
if options == "calc":
    a, b = float(input("Enter the first value: ")), float(input("Enter the second value: "))
elif options == eq_solver:
    number3_check = input('do you need the third value?')
    if number3_check == "yes" :
        c=float(input("Enter the third value: "))
        pass

    else:
        pass
else: 
    print("worng input! pls try again.")


if options.lower() == "calc":
    print("Starting calculation...")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    calc(a,b)


elif options.lower() == "eq_solver":
    print("Starting equation solving...")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    eq_solver(a,b,c)


retry = input("Do you want to try again? yes/no ")
if retry.lower() == "yes":  # Corrected this line
    print("Restarting in 3 seconds...")
    time.sleep(3)
    attempts = int(input("how many times do you want to retry: (int value!) "))
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
                calc(a,b)
                
                
            elif options.lower() == "eq_solver":
                print("Starting equation solving...")
                time.sleep(2)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                eq_solver(a,b,c)
                
            else:    
                print("Have a nice day")
        else:
            
            print("Have a nice day!")
    else:
        print("negative numbers unacceptable")
else: 
    print("have fun!")
    
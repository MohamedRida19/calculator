from math import sqrt
def calc(a,b):
    choice = input("chose the operation: +|-|*|/ ")
    if choice == "+":
        x= a+b
        print("the result is:",round(x,2))
    elif choice == "-":
        x= a-b
        print ("the result is:",round(x,2))
    elif choice == "*":
        x= a*b
        print("the result is:",round(x,2))
    elif choice == "/":
        x= a/b
        print ("the result is:",round(x,2))

def eq_solver(a,b,c):
    choice = input("chose the operation lvl: eq1/eq2")
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
            shorthand=input("do you want a shorthand for this expression? yes/no")
            if shorthand == "yes":
                if x > 0:
                    short = a("x-"+round(str(x),2))
                    print("shorthand is:",short)
                else :
                    short = a("x+"+round(str(x),2))
                    print("shorthand is:",short)
        elif delta > 0 :
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            print ("there is two results:")
            print ("first one is:",round(x1,2))
            print("second one is:",round(x2,2))
            shorthand = input("do you want a shorhand for this expression? yes/no")
            if shorthand == "yes":
                if x1 > 0 and x2 >0:
                    short = a("x-"+round(str(x1),2))("x-"+round(str(x2),2))
                    print("shorthand is:",round(short))
                elif x1 > 0 and x2 <0 :
                    short = a("x-"+round(str(x1),2))("x+"+round(str(x2,2)))
                    print("the shorthand is:",short)
                elif x1 < 0 and x2 >0 :
                    short = a("x+"+round(str(x1),2))("x-"+round(str(x2,2)))
                    print("shorthand is:",short)
                else:
                    short = a("x+"+round(str(x1),2))("x+"+round(str(x2,2))) 
                    print("shorthand is:",short)              
        else:
            print("there is no results")


        
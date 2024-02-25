import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Math Error! Divison by 0")
    else:
        return a/b

def power(num,p):
    return math.pow(num,p)

def root(num,r):
    if r==0:
        print("Math Error! Can't find root with 0 power!!!")
    else:
        return math.pow(num,1/r)

def LCM():
    #print()
    x=int(input("Enter total numbers to calculate LCM: " ))
    arr=[]
    for i in  range(x):
        data=int(input(f"Enter {i+1} number: "))
        arr.append(data)

    return math.lcm(*arr)

def Ceiling(x):
    return math.ceil(x)

def Floor(x):
    return math.floor(x)

def factorial(x):
    return math.factorial(x)



def showMenu():
    print("0.Exit\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Power(x^n)\n6.Root\n7.LCM\n8.Ceiling\n9.Floor\n10.Factorial")

    while True:
        choice = int(input("Enter your choice: "))



        if choice>0 and choice<=10:
            if choice in [1,2,3,4,5,6]:
                x=float(input("Enter num 1: "))
                y=float(input("Enter num 2: "))
                if choice==1:
                    print(f"{x} + {y}  = ",add(x,y))
                    break
                elif choice==2:
                    print(f"{x} - {y}  = ", subtract(x, y))
                    break
                elif choice==3:
                    print(f"{x} * {y}  = ", multiply(x, y))
                    break
                elif choice==4:
                    print(f"{x} / {y}  = ", divide(x, y))
                    break
                elif choice==5:
                    print(f"{x} ^ {y} = ", power(x, y))
                    break
                elif choice==6:
                    print(f"Root of {x} with power {y} = ", root(x, y))
                    break

            elif choice in [8,9]:
                num=float(input("Enter number: "))
                if choice==8:
                    print(f"{num} Ceiling= ",Ceiling(num))
                    break
                elif choice==9:
                    print(f"{num} Floor= ",Floor(num))
                    break


            else:
                if choice == 7:
                    print("LCM= ",LCM())
                    break
                elif choice==10:
                    x=int(input("Enter number: "))
                    print(f"{x}! = ",factorial(x))
                    break






print("\n--------------Calculator---------------\n")
while True:
    showMenu()




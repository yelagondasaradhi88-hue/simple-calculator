import math
num1= float(input("Enter 1st number : "))
operator = input("Enter operator (+, -, *, /, //, %, **, sqrt, abs): ")
if operator in ['sqrt', 'abs']:
    if operator=='sqrt':
        if num1<0:
            print("Cannot calculate square root of a negative number.")
        else:
            print(math.sqrt(num1))
    elif operator=="abs":
        print(abs(num1))
else:
    num2= float(input("Enter 2nd number : "))
    if operator =="+":
        print(num1+num2)
    elif operator == "-":
        print(num1-num2)
    elif operator =="*":
        print(num1*num2)
    elif operator=="/":
        if num2 !=0:
            print(round(num1/num2,3))
        else:
            print("Cannot divide by zero.")
            #print("cann't divisible by zero bue to zero is non zero number")
    elif operator =="//":
        if num2 !=0: 
            print(round(int(num1//num2),3))
        else:
            print("cann't divisible by zero")
    elif operator =="%":
        if num2!=0:
            print(round(num1%num2,3))
        else:
            print("cann't divisible by zero")  
    elif operator=='**':
        print(num1**num2)
    #square root

    elif operator=='%':
        print(num1%num2)
    else:
        print("invalid operator")    
    '''elif operator=='abs':
        print(abs(num1))
        print(abs(num2))
        print(abs(num1+num2))
    elif operator=='sqrt':
        print(math.sqrt(num1))
        print(math.sqrt(num2))
    '''

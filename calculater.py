x= int(input("Enter the first number: "))
y= int(input("Enter the second number: "))
s= input("Enter the operation you want to perform (+, -, *, /): ")


if s == "+":
    print(x+y)  
elif s == "-":
    print(x-y)
elif s == "*":
    print(x*y)
elif s == "/":
    if y != 0:
        print(x/y)
    else:
        print("Error: Division by zero is not allowed.")
else:    print("Invalid operation. Please enter one of +, -, *, or /.") 


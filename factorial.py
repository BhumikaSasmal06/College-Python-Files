def factorial(n):
    if n==0 or n==1:
        res = 1
    else: 
        res= n*factorial(n-1)
    return res

ch = "y"

while(ch == "y"):
    num = int(input("enter a number: "))
    result = factorial(num)
    print("factorial = ", result)
    ch = input("continue?(y/n):")
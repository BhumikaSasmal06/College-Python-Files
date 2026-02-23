#Write a program to Print a Message -"Welcome to Python Programming Lab"
print("Welcome to Python Programming Lab")


#Write a program to Read and Display User Name
name = input("Enter your name: ")
print("Your name is:", name)


#Write a program to Addition of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


#Write a program to Arithmetic Operations (Addition, Subtraction, Multiplication, Division)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)


#Write a program to Check the Number is Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


#Write a program to Check Positive, Negative or Zero
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#Write a program to Find Largest of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest =", a)
else:
    print("Largest =", b)


#Write a program to Find Largest of Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)


#Write a program to Reverse a Number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed Number =", reverse)


#Write a program to Sum of Digits of a Number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("Sum of digits =", sum)


#Write a program to Print First N Natural Numbers
n = int(input("Enter value of N: "))
for i in range(1, n + 1):
    print(i)
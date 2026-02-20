ch = "y"

while(ch == "y"):
    s = input("enter a word or number")
    if s == s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
    ch = input("continue? (y/n)")




def factorial(n):
    if n==0 or n==1:
        res = 1
    else: 
        res= n*factorial(n-1)
    return res

l = [1,2,3,4,5,6]
factorials = list(map(lambda x: factorial(x),l))
print(l)
print(factorials)
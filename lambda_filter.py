s = lambda n: n*n
print("square of 4: ", s(4))

s = lambda a,b: a+b
print("addition of 2 and 3: ", s(2,3))

s = lambda a,b: a if a>b else b
print("greater of 2 and 3: ", s(2,3))

s = lambda a,b,c: a if a>b and a>c else (b if b>a and b>c else c)
print("greater of 2,3,5 : ", s(2,5,3))

l = [0,5,10,12,15,16]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)
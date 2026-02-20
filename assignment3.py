#wap to create and display a list
L = [10,20,30,40,50]
for i in L:
    print(i, end = " ")    

#wap to find sum and avg of lsit of elements
sum = 0
for i in L:
    sum += i
avg = sum/len(L)    
print("\nsum:", sum, "\navg:", avg) 

#wap largest and smallest el in list
max=min=L[0]
for i in L:
    if i>max:
        max = i
    if i<min:
        min = i
print("\nmax:", max, "\nmin:", min) 

#wap reverse a list
print(L[::-1])

#searching num in list
x = 30
flag = 0
for i in range(0,len(L)-1):
    if L[i]==x:
        print("Number is found at index",i)
        flag=1
if flag==0:
    print("Number not found")
    
#create and display tuple
T = (10,20,30,40,50)
print("Tuple:")
for i in T:
    print(i, end = " ")  

#find len of tuple
count = 0
for i in T:
    count+=1
print("\nnumber of elements in tuple:",count)

#convert list to tuple
num = [1,2,3,4,5,6]
print(num)
tup = tuple(num)
print(tup)

#create and display a dictionary
d = {1:10,2:20,3:30,4:40}
print("dictionary:",d)

#add and update d element
d[5]=50 #add
d[2]=200 #update for key 2
print(d)

#delete d element
del d[2]
print(d)

#traverse d using loop
for key,value in d.items():
    print(key, ":", value)

#unique vowels
x = input("\nenter a word: ")
vowels = ["a", "e","i","o","u"]
temp = []
print("vowels:")
for i in x:
    if i.lower() in vowels and i not in temp:
        temp.append(i)
print(temp)

# all vowels from word
x = input("enter a word: ")
vowels = ["a", "e","i","o","u"]
print("vowels:")
for i in x:
    if i.lower() in vowels:
        print(i, end=" ")

#enter name and percentage in a dictionary  and display info in screen
ch = "y"
students = {}
while ch=="y":
      name = input("/nenter name:")  
      p = int(input("/nenter percentage"))
      students[name]=p
      ch = input("/ncontinue? (y/n)")
print(students)
#a) search marks using input
n = input("/nenter name to find: ")
flag = 0
for key in students:
    if key==n:
        print(key , ":" , students[key])
        flag = 1
        break
if flag == 0:
    print("student not found")

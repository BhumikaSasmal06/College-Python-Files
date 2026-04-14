print("Grading System\n===============================================")
class Grade:
    def __init__(self, m1, m2, m3, m4, m5, name):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4
        self.m5 = m5
        self.name = name

    def grade(self):
        total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        p = total / 5
        
        
        if p >= 90:
            g = "A"
        elif p >= 80:
            g = "B"
        elif p >= 70:
            g = "C"
        elif p >= 60:
            g = "D"
        elif p >= 50:
            g = "E"
        else:
            g = "F"
            
        print("Grade: ", g)


s1 = Grade(90, 90, 90, 90, 90, "Bhumika")
print("Name: ", s1.name)
s1.grade()
print("\n===============================================\nShopping Cart\n===============================================")
class ShoppingCart:
    def __init__(self):
        self.total = 0
        self.items = []
        
    def add(self,item,price):
        self.items.append(item)
        self.total+=price
    def show(self):
        print("Items: ", self.items, "\nTotal: ", self.total)
        
       
c1 = ShoppingCart()
c1.add("Pen",1000)
c1.add("book",50)
c1.show()

print("\n===============================================\nLibrary\n===============================================")
class Library:
    def __init__(self):
        self.books={"The Ninth House": True, "Harry Potter": False, "The Alchemist": True}
    def issue(self,bn):
        if self.books.get(bn) == True:
            self.books[bn] = False
            print(f"You Have Issued {bn}")
        else:
            print("Not Available")
            
    def returnb(self,bn):
        if bn in self.books:
            self.books=True
            print(f"You Have returned {bn}")
        else:
            print("Invalid operation")
            
lib = Library()
lib.issue("Harry Potter")
lib.issue("The Alchemist")
lib.returnb("The Alchemist")

print("\n===============================================\nRead File\n===============================================")
class ReadFiles:
    
    def __init__(self,f):
        self.file = f
    def rfile(self):
        f1= open(self.file,'r')
        content = f1.read()
        print(content)
        f1.close()
r = ReadFiles('demo.txt')
r.rfile()

print("\n===============================================\nBank\n===============================================")
class BankAccount:
    bank_name = "PyBank"
    owner = " "
    __balance= 0
    def __init__(self,name,bal):
        self.owner = name
        self.__balance=  bal

    def get_balance(self):
        print("Balance: ", self.__balance)
    def deposit(self,amount):
        if self.__balance > 0:
            self.__balance+= amount
            print("Deposit Successful!\nUpdated Balance:", self.__balance)
            print("---------------------------------------------")
    def withdraw(self,amount):
        if self.__balance>=amount:
            self.__balance -= amount
            print("Withdrawal successful! \nRemaining Balance: ", self.__balance)
            print("---------------------------------------------")
        else:
            print("Insufficient Balance!")
            print("---------------------------------------------")
    def __str__(self):
        print(f"Bank Name: {self.bank_name} \nAccount Owner: {self.owner} \nAccount Balance: {self.__balance}")
        print("---------------------------------------------")


acc = BankAccount("Bhumika", 1000)
acc2 = BankAccount("Mahul",100)
acc.deposit(1000)
acc.withdraw(500)
acc.__str__()
acc2.deposit(100)
acc2.withdraw(50)
acc2.__str__()

print("\n===============================================\nLogin\n===============================================")
class Login:
    def __init__(self):
        self.user = ""
        self.password= "123456"
    def signup(self,user,password):
        self.user=user
        self.password=password
        print(f"Signup Successful, Welcome {user}")
    def login(self,user,password):
        if self.user==user and self.password==password:
            print(f"Login Successful, Welcome Back {user}")
        else:
            print("Invalid Details")
acc = Login()
acc.signup("Bhumika","abcdef")
acc.login("Bhumika","abcdef")

        



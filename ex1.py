"""class Shape:
    def __init__(self,length,breadth):
        self._length=length
        self._breadth=breadth

    def displaysides(self):
        print("Length :",self._length)
        print("Breadth :",self._breadth)

class Rectangle(Shape):
    def __init__(self,length,breadth):
        Shape.__init__(self,length,breadth)

    def calculatearea(self):
        print("Area :",self._length * self._breadth)

n=int(input("Enter length :"))
m=int(input("Enter breadth :"))

      
obj=Rectangle(n,m)
obj.displaysides()
obj.calculatearea()"""

"""class cal:
    def add(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a-b
        elif a!=None:
            return a
d=cal()
print(d.add(1,2))
print(d.add(5,6,7))
print(d.add())"""

"""from abc import ABC , abstractmethod
class Car (ABC):
    @abstractmethod
    def mileage(self):
        pass
class Tesla (Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Renault (Car):
    def mileage(self):
        print("The mileage is 27kmph")


t=Tesla()
t.mileage()
r=Renault()
r.mileage()

x=Car()
x.mileage()"""

"""n=int(input("Enter numbre :"))
if(n%2==0):
    print(n," is even")
else:
    print(n," is odd")"""

"""n1=int(input("Enter numbre :"))
n2=int(input("Enter numbre :"))
n3=int(input("Enter numbre :"))
if(n1>n2):
    print(n1,"is greater")
elif(n2>n3):
    print(n2,"is greater")
elif(n3>n1):
    print(n3,"is greater")"""


"""p=int(input("Enter numbre :"))
t=int(input("Enter numbre :"))
r=int(input("Enter numbre :"))
si=(p*t*r)/100
print("Simple interest :",si)"""
"""ab=[44,23,789,56,11,8,4004,324]
largest=ab[0]
for x in ab:
    if(x>largest and largest>ab[0]):
        x=ab[0]
print(ab[2])"""

"""op="hello"
reverse=op[::-1]
print(reverse)"""
        

"""pal=input("Enter text :")
if(pal==pal[::-1]):
    print(pal,"is palindrome")
else:
    print(pal,"is not a palindrome")"""

"""n=int(input("Enter number :"))
a,b=0,1
for i in range(n):
    print(a,end="\n")
    a,b=b,b+a"""


"""str1=int(input("Enter text :"))
str2=int(input("Enter text :"))
if (sorted(str(str1)))==(sorted(str(str2))):
    print("Both strings are anagrams")
else:
    print("Both strings are not anagrams")"""

"""n=int(input("enter number :"))
for i in range(n):
    for j in range(n):
        if i == 0  or j==0 or i ==n-1 or j==n-1 or i==j or i==n-(j+1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()"""  

"""class Bank:
    def __init__(self):
        self.acc_num=12345
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(amount > self.balance):
            print("Insufficient Balance")
        else:
            self.balance-=amount
    def display_balance(self):
        print("Account Balance is =",self.balance)
user1=Bank()
user1.deposit(1000)
user1.display_balance()
user1.withdraw(2000)
user1.withdraw(500)
user1.display_balance()"""

"""n=int(input("Enter a number :"))
for row in range(1,n+1):
    for col in range(n+1,row,-1):
        print(col,end=" ")
    print()"""

"""class Bank:
    def __init__(self):
        self.acc_num=12345
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if(amount > self.balance):
            print("Insufficient Balance")
        else:
            self.balance-=amount
    def display_balance(self):
        print("Account Balance is =",self.balance)
user1=Bank()
user1.deposit(1000)
user1.display_balance()
user1.withdraw(2000)
user1.withdraw(500)
user1.display_balance()"""

"""class Book:
    def __init__(self):
        self.list1=["titanic","victory","ram","boll"]
    def display_book(self,name):
        self.name=list1
    def lend_book(self,book_name):
        if name in list1:
            book_name.remove(name)
        else:
            print("Book not found")
    def add_book(self,add):
        self.add=append(list1)

user1=Book()
user1.display_book("manju")"""


"""n=int(input("Enter number :"))
i=1
while i<=10:
    print(n*i)
    i+=1"""


"""def twosum(nums,target):
    lookup={}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff],i]
        lookup[num]=i
nums=[2,11,15,7]
target=9

print(twosum(nums,target))"""

"""num=[2,11,15,7,5,8,16,23,56]
target=23

for x in range(0,len(num)):
    for y in range(x+1,len(num)):
        if(num[x]+num[y] == target):
            print("[",x,y,"]")"""

"""n=int(input("Enter:"))
list1=[]
for i in range(n):
    item=int(input("Enter items :",i+1))
    list1.append(item)
print(list1)"""



"""list1 = []  
for i in range(3):
    item = int(input(f"Enter items {i+1} :"))  
    list1.append(item)  
print(list1)

list2 = []  
for i in range(3):
    item = int(input(f"Enter items {i+1} :"))  
    list2.append(item)  
print(list2)

print("Reversed list")
print(list1[::-1])
print(list2[::-1])

for x in range(0,len(list1)):
    r1=list1[x]
    print(r1)
for y in range(0,len(list2)):
    r2=list1[y]
    print(r2)
print(r1+r2)"""


"""list1=[4,5,8]
list2=[5,6,4]
total=[]
for x in range(3):
    total.append(list1[x]+list2[x])
print(total)"""


"""nums=[1,1,0,1,1,1,1,1,0,1,10,1,1,1]
count=0
max_count=0
for x in nums:
    if(x==1):
        count+=1
        if(count>max_count):
            max_count=count
    else:
        count=0
print(max_count)"""

"""for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i,"is multiplied by 3 n 5 FizzBuzz ")
        continue
    if i%3==0:
        print(i,"multiplied by 3 Fizz")
        continue
    if i%5==0:
        print(i,"multiplied by 5 Buzz")
        continue
    else:
        print(i)"""

"""str1=input("Enter text :")
str2=str1[::-1]
if str1==str2:
    print(str1," is a palindrome")
else:
    print(str1," is not a palindrome")"""

"""def is_palindrome(s):
    # Remove any spaces and convert the string to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Example usage
input_string = "malayalam"
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')"""

"""str1="A man a plan a canal Panama"
str1=str1.replace(" ","").lower()
print(str1)"""


"""def find_winning_party(n,votes):
    from collections import Counter
    counts=Counter(votes)
    majority=n//2+1
    for party, count in counts.items():
        if count>=majority:
            return party
    return -1
n=int(input("Enter number of votes :"))
votes=list(map(int,input("Enter the votes (space-separated):").split()))
print("the winning party is:",find_winning_party(n,votes) or "no party has a majority.")"""


"""def calculate_rounds(C, N):
    # Calculate the minimum number of rounds required
    rounds = (N + C - 1) // C
    return rounds

# Input: capacity of the ship (C) and number of people (N)
C = int(input("Enter the capacity of the ship: "))
N = int(input("Enter the number of people to be transported: "))

# Output: number of rounds required
print("The ship needs to make", calculate_rounds(C, N), "rounds.")"""





"""def rearrange_even_odd(arr):
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 != 0]
    return even + odd

# Input size of array
N = int(input())

# Input the array elements
arr = list(map(int, input()))

# Rearrange and print the result
result = rearrange_even_odd(arr)
print(*result)"""

"""def rearrange_even_odd(arr):
    even=[x for x in arr if x%2==0]
    odd=[x for x in arr if x%2!=0]
    return even + odd
n=int(input())

arr=list(map(int,input()))
result = rearrange_even_odd(arr)
print(*result)"""


"""def find_winning_party(n,votes):
    from collections import Counter
    counts=Counter(votes)
    majority=n//2+1
    for party, count in counts.items():
        if count>=majority:
            return party
    return -1
n=int(input("Enter number of votes :"))
votes=list(map(int,input("Enter the votes (space-separated):").split()))
print("the winning party is:",find_winning_party(n,votes) or "no party has a majority."""


    
"""item=int(input("1.apple\n2.orange\n3.banana\nEnter item :"))
if(item==1):
    print(f"Cost of apple is 30rs per kg")
    quantity=int(input("Enter quantity :"))
    if quantity==1:
        print(f"the total cost is {30*30*0.05} including tax")
    elif quantity==2:
        print(f"the total cost is {(30+30)*(30*2)*0.05} including tax")
    elif quantity==3:
        print(f"the total cost is {(30+30+30)*(30*3)*0.05} including tax")
    
elif(item==2):
    print("Cost of orange is 40rs per kg")
    quantity=int(input("Enter quantity :"))
    if quantity==1:
        print(f"the total cost is {40*40*0.05} including tax")
    elif quantity==2:
        print(f"the total cost is {(40+40)*(40*2)*0.05} including tax")
    elif quantity==3:
        print(f"the total cost is {(40+40+40)+ (40+40+40)*0.05} including tax")
   
elif(item==3):
    print("Cost of banana is 50rs per kg")
    quantity=int(input("Enter quantity :"))
    if quantity==1:
        print(f"the total cost is {50*50*0.05} including tax")
    elif quantity==2:
        print(f"the total cost is {(50+50)*(50*2)*0.05} including tax")
    elif quantity==3:
        print(f"the total cost is {(50+50+50)*(50*3)*0.05} including tax")"""

"""def billing_system(item_name,price_per_item,quantity):
    total_cost=price_per_item*quantity
    total_with_tax=total_cost+(total_cost*0.05)
    return item_name,total_with_tax

print(billing_system("Apple",3,5))
print(billing_system("Mango",3,5))
print(billing_system("Banana",3,5))"""


"""def seat_reservation(seat_type):
    if seat_type=='economy':
        print("the seat type is economy\nTotal cost for 1 seat $100")
    elif seat_type=='business':
        print("the seat type is business\nTotal cost for 1 seat $200")
    elif seat_type=='first-class':
        print("the seat type is first-class\nTotal cost for 1 seat $300")
    i=0
    
    return "booking finished"


seat=input("The available seats are\nBusiness\neconomy\nfirst class\nenter seat type :")
print(seat_reservation(seat))"""


def billing_system(cost):
    cost=cost+(cost*0.08)
    return cost

order=input("1.Pizza\n2.Burger\n3.Finger-chips\nEnter your order :")
if order=="Pizza":
    cost=20
elif order=="Burger":
    cost=30
elif order=="Finger-chips":
    cost=40
print("The total cost of your order is ",billing_system(cost))

























































































































































































































































































































































































































    





































































































































"""for i in range(2,50):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)



def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)"""

"""n=int(input("Enter number :"))
print(fact(n))
list1=[1,2,57,28,96,44,23]
list2=max(list1)
print("\nmax value is :",list2)
a=[4,6,8,5,2]
b=[12,9,3,8,1]
c=sorted(a)+sorted(b)
d=sorted(c)
print(d)"""


class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("stack is_empty")
    def peak(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("stack is_empty")
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items )
    def __str__(self):
        return str(self.items)

stack=Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.peak())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.is_empty())
try:
    stack.pop()
except IndexError as e:
    print(e)
























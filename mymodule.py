
"""queue=[]
queue.append(1)
queue.append(2)
queue.append(3)

print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print(queue)

if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")"""

"""class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"
    def is_empty(self):
        return len(self.items)==0
    def size(self):
        return len(self.items)
    def print_queue(self):
        print(self.items)
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.print_queue()
print(q.dequeue())
q.print_queue()"""

"""def remove_vowels(s):
    return ''.join(sorted(set(s), key=s.index))

# Example usage
input_string = "hello world"
result = remove_vowels(input_string)
print(result)

a='hello world'
b=''.join(sorted(set(a),key=a.index))
print(*b)"""


"""a='hello world'
b=sorted(set(a),key=a.index)
"""

"""def remove_vowels(s):
    vowels='aeiouAEIOU'
    return ''.join(char for char in s if char not in vowels)
a='hello world'
print(remove_vowels(a))"""


"""a=[1,2,3]
a=iter(a)
print(a)
print(next(a))
print(next(a))
print(next(a))"""


"""def hh():
    n=1
    yield n
    n+=11
    yield n
h=hh()
print(next(h))
print(next(h))"""


        
"""class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        if not self.head:
            self.head=Node(data)
        else:
            current=self.head
            while current.next:
                current=current.next
                
            current.next=Node(data)
    def print_list(self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
        print("ddd")
    def delete(self,data):
        if self.head is None:
            return
        current=self.head
        while current.next:
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
            if current.next.data==data:
                current.next=current.next.next
                return
            current=current.next
            
    def search(self,data):
        current=self.head
        while current:
            if current.data==data:
                return True
            current=current.next
        return False
l1=LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.insert(5)
l1.print_list()
print("search 3:",l1.search(3))
print("search 6:",l1.search(6))
l1.delete(4)
print("After deletion:")
l1.print_list()"""


"""def bubble_sort(arr):
    for n in range(len(arr)):
        for i in range(len(arr)-n-1):
            if arr[i]>arr[i+1]:
                temp=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                
arr=[39,12,18,85,72,10,2,18]
print("Unsorted list is:")
print(arr)
bubble_sort(arr)
print("Sorted list is :")
print(arr)"""

"""def mergeSort(arr):
    if len(arr)<=1:
        return arr

    mid = len(arr)//2
    leftHalf=arr[:mid]
    rightHalf=arr[mid:]

    sortedLeft=mergeSort(leftHalf)
    sortedRigth=mergeSort(rigthHalf)
    return merge(sortedLeft,sortedRigth)
def merge(left,rigth):
    result=[]
    i=j=0

    while i<len(left) and j<len(rigth):
        if left[i]<rigth[j]:
            result.append(left[i])
        else:
            result.append(rigth[j])
            j+=1

    result.extend(left[i:])
    result.extend(right[j:])
    print(i,j)
    result"""

"""row=10
for i in range(row):
    for j in range(i):
        print(i,end=" ")
    print(" ")"""


for i in range(6):
    for j in range(i):
        if i==














































































































































        
    

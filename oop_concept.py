# #oop concepts
# class Person:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def greet(self):
#         print(f"My name is {self.name} and id is {self.id}")
# persn=Person("Veeha",20)
# persn.greet()

# #inheritence
# class Student(Person):
#     def __init__(self,name,id,age):
#         super().__init__(name,id)
#         self.age=25
#     def stdInfo(self):
#         print(f"My name is {self.name} and id is {self.id} my age is {self.age}")
# std=Student("Abhi",2,25)
# std.stdInfo()

#lets write Multilevel inheritance and multiple inheritance to calculate
#area of different type of shapes

#data sturcture using oop
#perform stack and queue operation using classes
# class Stack: 
#     def __init__(self,list,insertele,n): 
#         self.list=list
#         self.insertele=insertele
#         self.n=n 
#     def push(self):
#         self.list.append(self.insertele)
#     def pop(self):
#         self.list.pop()
#         print(self.list)
# list1=[10,20]
# n=int(input("Enter the number of elements in the Stack: "))
# for i in range(0,n):
#     insertele=input("enter the element to be inserted in stack: ")
#     stackop=Stack(list1,insertele,n)
#     stackop.push()
# print(stackop.list)
# stackop.pop()

#queue
class Queue:
    def __init__(self,n,queue,insertele,front,rear):
        self.n=n
        self.queue=queue
        self.insertele=insertele
        self.front=front
        self.rear=rear
    def enqueue(self):
        self.queue.append(self.insertele)
    def dequeue(self):
        self.queue.pop(0)
        print(self.queue)
queue=[10,20]
n=int(input("Enter the number of elements in the Queue: "))
for i in range(0,n):
    insertele=input("enter the element to be inserted in Queue: ")
    queueop=Queue(n,queue,insertele,0,n-1)
    queueop.enqueue()
print(queueop.queue)
queueop.dequeue()
        
#linked list
# class Node:
#     def __init__(self,ndata):
#         self.ndata=ndata
#         self.next=None

# class SingleLL:
#     def __init__(self):
#         self.head=None
#     def append(self,data):
#         new_node=Node(data)
#         if not self.head:
#             self.head=new_node
#             return
#         current=self.head
#         while current.next:
#             current.next=new_node
#     def print_list(self):
#         current = self.head
#         while current:
#             print(f"Node data: {current.ndata}, Next pointer: {current.next}")
#             current = current.next
# ndata=input("enter the element: ")
# ll=SingleLL()
# ll.append(ndata)
# ll.print_list()


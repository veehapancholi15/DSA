# # #while loop
# # l=5
# # while l<=15:
# #     print(l)
# #     l-l+1

# # #if-elif-else
# # sub1 = int(input("Enter marks of the first subject: "))
# # sub2 = int(input("Enter marks of the second subject: "))
# # sub3 = int(input("Enter marks of the third subject: "))
# # sub4 = int(input("Enter marks of the fourth subject: "))
# # sub5 = int(input("Enter marks of the fifth subject: "))

# # total = sub1 + sub2 + sub3 + sub4 + sub5
# # percentage = int((total / 500) * 100)

# # print("Total Marks = ", total)
# # print("Percentage = ", percentage)
# # if percentage >= 90:
# #     print("Grade: A+")
# # elif percentage <= 80 and percentage >= 70:
# #     print("Grade: B")
# # elif percentage >= 60 and percentage >= 50:
# #     print("Grade: C")
# # elif percentage >= 40 and percentage >= 35:
# #     print("Passed the Exam")
# # else:
# #     print("Failed the Exam")
    
# #break&continue
# #wap using continue to print odd numbers from 1 to 10
# for n in range(1,10):
#     if n%2==0:
#         continue
#     else:
#         print(n)

# #enumerate example
# def find_char(string,ch):
#     indx=[i for i,c in enumerate(string) if c==ch]
#     cnt=len(indx)
#     print(f"Character {ch} is found {cnt} times at indexs {indx}")

# #array
# import array
# numbr=array.array('i',[10,20,30,40])
# numbr.append(50)
# numbr.extend([60,70,80])
# numbr.pop(2)
# numbr[3]=55
# li=numbr.tolist()
# #1d array convert into list in python 
# #for 2d array use numpy in python

# import numpy as np
# arr=np.array([4,7,3,1,5])
# arr=np.append(arr,[6])
# arr=np.delete(arr,2)
# sorted_arr=np.sort(arr)

#wap to perform stack operation using list
stack=[]
stack.append(10);stack.append(20);stack.append(30);stack.append(40);stack.append(50);stack.append(60)
print(f"stack elements are {stack}")
#pop
pop_element=stack.pop()
print(f"stack element after pop {stack}")
#peek
if stack:
    top_element=stack[-1]
    print(f"Top element is {top_element}")
#check stack is empty
is_empty=len(stack)==0
print(f"Is stack empty? {is_empty}")
# to define stack size
stack_size=len(stack)
print(f"Is stack size {stack_size}")
# Iterate stack
# to print rest of the elements
for el in reversed(stack):
    print(el,end="")

#Queue
from collections import deque
queue=deque()
queue.append(10);queue.append(20);queue.append(30);queue.append(40);queue.append(50);queue.append(60)
#remove element from front
del_ele=queue.popleft()
print(f"delete element from queue: {del_ele}")
#peek
#is empty
#get size
#iterate
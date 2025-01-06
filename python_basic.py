#variable and type function intro
name="Veeha"
age=20
height=5.1
is_programmer=True
print(f"Name : {name} | Type : ",type(name))

#operators
#arithmetic
num1=20;num2=30
print(f"{num1}+{num2}={num1+num2}")
print("hello"+"hi")

#conditional
if is_programmer:
    print("True")
else:
    print("False")

#loop
for i in range(1,6):
    print(f"{i}")

#list,tuple,dictionary,set
list_l=[10,20,30]
list_l[0]=32
list_l.append("abc")
print(list_l[:])
list_l.remove("abc")
list_l.remove(list_l[0])
print(list_l[:])

tuple_t=(10,20,30)
print(tuple_t[-1])

dict_d={"name":"veeha","age":20}

set_s={1,5,6}

#for 1d array
import array
number=array.array('i',[10,20,30])
print(number)
number.append(40)
number.pop(2)
print("Extended array ",number)

#queue
from collections import deque
qu=deque()
qu.append(1)
qu.append(11)
qu.append(111)
print("queue : ",qu)

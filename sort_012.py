# Create a calculator - Take input from the user
# a = 10
# b = 23
a = int (input("First Number is: "))
b = int (input("Second Number is: "))
print ( a + b)
#
a = int (input("First Number is: "))
b = int (input("Second Number is: "))
print ( a - b)

arr = [0, 1, 2, 0, 1, 2]
for i in range(len(arr)): 
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr)
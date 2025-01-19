#linear search 
def linear(arr,target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
    return -1
    
arr = [1,2,3,4,5]
target=3
print(linear(arr,target))

#binary search and search space
def binarySearch(arr,target):
    left,right=0,len(arr)-1
    while(left<=right):
        mid=(left+right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1

arr=[10,20,30,40,50,60]
target=50
print(binarySearch(arr,target))


#insertion sort
def insertSort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j -= 1
            arr[j+1]=key
    return arr

arr=[12,11,13,5,6]
print(insertSort(arr))

# def insertionSort(arr):
# 	n = len(arr) # Get the length of the array
	
# 	if n <= 1:
# 		return # If the array has 0 or 1 element, it is already sorted, so return

# 	for i in range(1, n): # Iterate over the array starting from the second element
# 		key = arr[i] # Store the current element as the key to be inserted in the right position
# 		j = i-1
# 		while j >= 0 and key < arr[j]: # Move elements greater than key one position ahead
# 			arr[j+1] = arr[j] # Shift elements to the right
# 			j -= 1
# 		arr[j+1] = key # Insert the key in the correct position

# # Sorting the array [12, 11, 13, 5, 6] using insertionSort
# arr = [12, 11, 13, 5, 6]
# insertionSort(arr)
# print(arr)


# #merge sort
# def mergeSrt(arr):
#     a = arr[len(arr)//2:]
#     b = arr[:len(arr)//2]
#     return a,b

# arr=[1,2,3,4,5,6]
# print(mergeSrt(arr))
#string character search
st=input("Enter the string: ")
starray=[]
for i in st:
    starray.append(i)
print(starray)
search=input("Enter the character you want to search: ")
count=0
for j in range(len(starray)):
    if j==search:
        print(f"match found: {j}")
        count=count+1
        print(f"count: {count}")
    elif j!=search:
        continue
    else:
        print(f"not found")

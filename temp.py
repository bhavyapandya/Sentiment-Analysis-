arr = [1,3,2,5,6]

i = 0

while i<len(arr)-1:

    if arr[i] >arr[i+1]:
        t = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = t
    
    i+=1

print(arr)
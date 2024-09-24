L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original List : ", L)

count = 0

for i in L:
    count = count + i
    
print("Sum = ", count)

avg = count/len(L)
print("average = ", avg)

L.sort()
print(L)

print("Smallest element is:", L[0])
print("Largest element is:", L[-1])
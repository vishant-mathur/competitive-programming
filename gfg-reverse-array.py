# https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in reversed(range (n)):
    temp = arr[i]
    arr.append(temp)
    arr.remove(temp)
print(arr)
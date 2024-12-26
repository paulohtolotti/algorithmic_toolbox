arr = [1, 4, 3, 6, 7, 0]
max_el = [0, 0]
max = 0
for i in range(len(arr)-2):
    for j in arr:
        if (arr[i]*j > max):
            max = arr[i]*j
            max_el[0] = arr[i]
            max_el[1] = j
print(f"Maximum product is {max}, and is produced by the elements {max_el}")

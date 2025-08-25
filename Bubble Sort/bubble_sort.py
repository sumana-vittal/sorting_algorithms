def bubble_sort(arr):
    if len(arr) <= 0:
        return
    if len(arr) == 1:
        return arr[0]

    for i in range(0, len(arr)):
        for j in range(len(arr)-1, i, -1):
            if arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr


print(bubble_sort([9,4,1,7,2,8]))

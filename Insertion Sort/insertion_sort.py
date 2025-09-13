def insertion_sort(arr):
    if len(arr) == 0:
        return arr

    for i in range(0, len(arr)):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

print(insertion_sort([8,2,4,9,3,6]))
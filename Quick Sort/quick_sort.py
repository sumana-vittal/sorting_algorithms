import random

def lomuto_sort(arr, start, end):
    if start >= end:
        return arr

    pivot = random.randint(start, end)
    arr[start], arr[pivot] = arr[pivot], arr[start]

    small = start
    for big in range(start+1, end+1):
        if arr[big] < arr[start]:
            small += 1
            arr[big], arr[small] = arr[small], arr[big]
    arr[start], arr[small] = arr[small], arr[start]

    lomuto_sort(arr, start, small)
    lomuto_sort(arr, small+1, end)

    return arr

def hoare_sort(arr, start, end):
    if start <= end:
        return arr

    small = start+1
    big = end

    while small <= big:
        if arr[small] < arr[start]:
            small += 1
        elif arr[big] >= arr[start]:
            big -= 1
        elif small <= big :
            arr[small], arr[big] = arr[big], arr[small]
            small += 1
            big -= 1

    arr[big], arr[start] = arr[start], arr[big]
    return arr

def quick_sort(arr):
    lomuto_arr = lomuto_sort(arr, 0, len(arr)-1)
    # hoare_arr = hoare_sort(arr, 0, len(arr) - 1)

    return lomuto_arr #hoare_arr

print(quick_sort([4,2,8,7,1,3,5,6]))

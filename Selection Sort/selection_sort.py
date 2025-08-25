def selection_sort(arr):
    # if len of array is 0, return None
    if len(arr) <= 0:
        return
    #If len of array is 1, return the element.
    if len(arr) == 1:
        return arr[0]

    # loop through array to find the smallest element and swap.
    for i in range(0, len(arr)):
        min_value = arr[i]
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


print(selection_sort([6,2,9,11,78,23,0,45,16,]))
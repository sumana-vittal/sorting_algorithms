def helper(arr, start, end):
    # lead node
    if start == end:
        return

    mid = ( start + end )//2
    helper(arr, start, mid)
    helper(arr, mid+1, end)

    i, j = start, mid+1
    aux_array = []

    while i<= mid and j <= end:
        if arr[i] <= arr[j]:
            aux_array.append(arr[i])
            i += 1
        else:
            aux_array.append(arr[j])
            j += 1
    while i <= mid:
        aux_array.append(arr[i])
        i += 1

    while j <= end:
        aux_array.append(arr[j])
        j += 1

    arr[start:end+1] = aux_array
    return arr


def merge_sort(arr):
   array = helper(arr, 0, len(arr)-1)
   return array

print(merge_sort([8,2,4,9,3,6]))

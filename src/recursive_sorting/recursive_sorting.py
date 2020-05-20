# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    A_idx = 0
    B_idx = 0
    
    while A_idx < len(arrA) and B_idx < len(arrB):
        if arrA[A_idx] < arrB[B_idx]:
            merged_arr.append(arrA[A_idx])
            A_idx += 1
        else:
            merged_arr.append(arrB[B_idx])
            B_idx += 1
    
    if A_idx == len(arrA):
        merged_arr.extend(arrB[B_idx:])
    else:
        merged_arr.extend(arrA[A_idx:])
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    # base case
    if len(left) < 2 and len(right) < 2:
        return merge(left, right)  
    else:
        return merge(merge_sort(left), merge_sort(right))



# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # if arr[start] < arr[mid]:
    #     return

    while (start <= mid and mid <= end):
        if arr[start] > arr[mid]:
            mid_2 = mid

            # arr[mid] swaps with previous neighbor
            # until it is at start
            while mid_2 != start:
                arr[mid_2], arr[mid_2 - 1] = arr[mid_2 - 1], arr[mid_2]
                mid_2 -= 1
            
            # update pointers
            start += 1
            mid += 1
        else:
            start += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # l is start index of left subarray
    # r is start index of right subarray
    if l < r:
        midpoint = (l + r + 1) // 2

        # sort left and right subarrays
        merge_sort_in_place(arr, l, midpoint - 1)
        merge_sort_in_place(arr, midpoint, r)
        merge_in_place(arr, l, midpoint, r)

    return arr

print(merge_sort_in_place([1, 5, 8, 4], 0, 3))

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

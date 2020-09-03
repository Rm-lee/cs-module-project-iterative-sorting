import unittest

def linear_search(arr, target):
    # Your code here
    count = 0
    while count != len(arr):
        if target == arr[count]:
            return count
        count += 1
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) -1
    arr = sorted(arr)
    print(arr)
    # Your code here
   # mid = (low + high) / 2

    while low <= high:
        middle = (low + high) /2
        if target < arr[int(middle)]:
            high = middle -1
        elif target > arr[int(middle)]:
            low = middle + 1
        else:
            return middle 

    return -1  # not found


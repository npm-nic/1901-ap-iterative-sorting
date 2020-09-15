def linear_search(arr, target):
    # Your code here
    # check all elements in the array one by one, and compare them with the target value
    for i in range(len(arr)):
        # if the value checked is the same as target, return it 
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint

        elif arr[midpoint] > target:
            right = midpoint - 1
            
        else:
            left = midpoint + 1

    return -1  # not found
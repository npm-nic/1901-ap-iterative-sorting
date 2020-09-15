# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # [TO-DO]: find next smallest element --> (hint, can do in 3 loc)
        # ----------> Your code here <----------
        # loop through every elem to the right of the boundry
        # --> and keep track of the smallest elem until we get to the end
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j 
        # [TO-DO]: swap
        # ----------> Your code here <----------
        # python's nifty one-line swap ⬇
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        # # another way to do it (under the hood) ⬇
        # temp = arr[smallest_index]
        # arr[smallest_index] = arr[i]
        # arr[i] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # ----------> Your code here <----------
    # keep a flag that tracks whether any swaps occurred
    # --> only when we haven't swapped anything are we done
    # --> initialized to True so that it runs AT LEAST once
    swaps_occurred = True
    while swaps_occurred:
        swaps_occurred = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps_occurred = True
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''

# runtime complexity: O(n + n)
# space complexity: O(n + n)
def counting_sort(arr, maximum=None):
    # return the arr if it is empty
    if len(arr) == 0:
        return arr
    # figure out the max if we do not know it
    if maximum is None:
        maximum = max(arr)

    buckets = [0 for i in range(maximum + 1)]

    # loop through input array (arr)
    # --> o(n) b/c running through every elem in input array
    for value in arr:
        if value < 0:
            return "Error, negative numbers not allowed in Count Sort"
        buckets[value] += 1

    output = []
    # loop through buckets array
    # --> len(buckets) can be 0...m where m is our possible value
    for index, count in enumerate(buckets):
        output.extend([index for i in range(count)])
        # list comprehension ⬆️:
        # --> HOW:
        # ----> if we are at index 0 and the count is 2 ...
        # ----> makes a mini-list of two 0's : [0,0]
        # --> makes these 'mini-lists' for each and extend() adds it to output

    return output
# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    mid_index = (start + end) // 2
    # what is the base case?
    if end < start:
        return -1
    # how do we get there?
    # where do we recurse?
    if target == arr[mid_index]:
        return mid_index
    elif target < arr[mid_index]:
        end = mid_index - 1
        return binary_search(arr, target, start, end)
    elif target > arr[mid_index]:
        start = mid_index + 1
        return binary_search(arr, target, start, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively

def agnostic_binary_search(arr, target):
    # Your code here
    pass
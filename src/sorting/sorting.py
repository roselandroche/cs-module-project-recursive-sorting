# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # Your code here
    merged_arr = []
    x = y = 0

    while x < len(arrA) and y < len(arrB):
        if arrA[x] < arrB[y]:
            merged_arr.append(arrA[x])
            x += 1
        else:
            merged_arr.append(arrB[y])
            y += 1
    
    merged_arr.extend(arrA[x:])
    merged_arr.extend(arrB[y:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2

    lhs = merge_sort(arr[:midpoint])
    rhs = merge_sort(arr[midpoint:])

    return merge(lhs, rhs)

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(arr1)
print(merge_sort(arr1))
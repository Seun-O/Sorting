# TO-DO: complete the help function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # TO-DO
    # New array to append lowest numbers
    merged_arr = []

    # Variable index for both arrays
    a_index, b_index, = 0, 0

    # Loop to interate over each array item while the index count is lower than the array length
    while a_index < len(arrA) and b_index < len(arrB):

        # Comparision between array 1 & 2 to find the lowest value
        if arrA[a_index] < arrB[b_index]:
            # Appends lowest value to the new array
            merged_arr.append(arrA[a_index])
            # Increments index so the value is not repeated
            a_index += 1
        else:
            merged_arr.append(arrB[b_index])
            b_index += 1

    # Adds all remaining items from the array that wasn't added to the new array
    if a_index == len(arrA):
        merged_arr.extend(arrB[b_index:])
    else:
        merged_arr.extend(arrA[a_index:])
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO

    # Finds the midpoint of the array
    mid = len(arr)//2

    # Returns the array if it contains a single element
    if len(arr) <= 1:
        return arr

    # Creates a left and right array. [:mid] selects all items before the mid point excluding mid
    # mid[mid:] selects all items to the right of the mid point including the mid element
    left_arr, right_arr = merge_sort(arr[:mid]), merge_sort(arr[mid:])

    # Runs the merge helper method on the left and right array
    return merge(left_arr, right_arr)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


'''
Splits the array into halves and subsequently into smaller pieces
A left and A right side
'''

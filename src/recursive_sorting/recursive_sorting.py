'''
1. While your data set contains more than one item, split it in half
2. Once you have gotten down to a single element, you have also *sorted* that element 
   (a single element cannot be "out of order")
3. Start merging your single lists of one element together into larger, sorted sets
4. Repeat step 3 until the entire data set has been reassembled
'''

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( left, right ):
    elements = len( left ) + len( right )
    merged_arr = [0] * elements
    # TO-DO


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO        
    
    # START FIRST PASS - uncomment between start and end to use code
    if len(arr) > 1:

        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        # iterators
        left_i = 0
        right_i = 0
        mainList_i = 0

        while left_i < len(left) and right_i < len(right):
            if left[left_i] < right[right_i]:
                arr[mainList_i] = left[left_i]
                left_i += 1
            else:
                arr[mainList_i] = right[right_i]
                right_i += 1
            
            mainList_i += 1

        while left_i < len(left):
            arr[mainList_i] = left[left_i]
            left_i += 1
            mainList_i += 1

        while right_i < len(right):
            arr[mainList_i] = right[right_i]
            right_i += 1
            mainList_i += 1
    print(f'Sorted... {arr}')   
    return arr
    # END OF FIRST PASS

# print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

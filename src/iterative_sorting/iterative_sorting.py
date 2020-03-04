# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        
        for idx,num in enumerate(arr[cur_index:], cur_index):
            if num < arr[smallest_index]:
                smallest_index = idx     

        if cur_index != smallest_index:
            #swap values in the array
            arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr
    
# TO-DO:  implement the Bubble Sort function below

def bubble_sort( arr ):
    swap = True
    while swap == True:
        swap = False
        for idx,num in enumerate(arr):
            rightElement = idx + 1
            if idx < len(arr)- 1:
                if num > arr[rightElement]:
                    arr[idx], arr[rightElement] = arr[rightElement], num
                    swap = True
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr
import random
import time

MAX_SIZE = 10000

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def partition(arr, low, high):
    i = ( low-1 )
    pivot = arr[high]
    for j in range(low , high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return ( i+1 )

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)

def quick_sort_short(arr):
    if(arr):
        smallerAsPivot = [i for i in arr[1:] if i < arr[0]]
        greaterAsPivot = [i for i in arr[1:] if i >= arr[0]]
        return quick_sort_short(smallerAsPivot) + [arr[0]] + quick_sort_short(greaterAsPivot)
    else:
        return arr
# Generate random array of given max size
arr = [random.randint(0, MAX_SIZE) for i in range(MAX_SIZE)]

# Test and time bubble sort
start_time = time.time()
bubble_sort(arr)
end_time = time.time()
print("Bubble sort time: ", end_time - start_time)

# Test and time insertion sort
arr = [random.randint(0, MAX_SIZE) for i in range(MAX_SIZE)]
start_time = time.time()
insertion_sort(arr)
end_time = time.time()
print("Insertion sort time: ", end_time - start_time)

# Test and time selection sort
arr = [random.randint(0, MAX_SIZE) for i in range(MAX_SIZE)]
start_time = time.time()
selection_sort(arr)
end_time = time.time()
print("Selection sort time: ", end_time - start_time)

# Test and time quicksort
arr = [random.randint(0, MAX_SIZE) for i in range(MAX_SIZE)]
start_time = time.time()
quick_sort(arr, 0, len(arr)-1)
end_time = time.time()
print("Quicksort time: ", end_time - start_time)

# Test and time quicksort_short
arr = [random.randint(0, MAX_SIZE) for i in range(MAX_SIZE)]
start_time = time.time()
quick_sort_short(arr)
end_time = time.time()
print("Quicksort Short Version time: ", end_time - start_time)
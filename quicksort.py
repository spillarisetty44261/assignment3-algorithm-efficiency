import random

def deterministic_quicksort(arr):

    # Base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Select the first element as pivot
    pivot = arr[0]

    # Partition the array into elements less than or equal to pivot and greater than pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    # Recursively sort partitions and combine results
    return deterministic_quicksort(left) + [pivot] + deterministic_quicksort(right)


def randomized_quicksort(arr):

    # Base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        return arr

    # Randomly select a pivot element from the array
    pivot = random.choice(arr)

    # 3-way partitioning:
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right partitions and combine with middle
    return randomized_quicksort(left) + middle + randomized_quicksort(right)
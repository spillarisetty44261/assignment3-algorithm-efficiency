import sys
sys.setrecursionlimit(10000)
import time
import random
import csv
from quicksort import deterministic_quicksort, randomized_quicksort


def generate_data(size):

    # Random array with values between 1 and 10000
    random_arr = [random.randint(1, 10000) for _ in range(size)]

    # Sorted version of the random array
    sorted_arr = sorted(random_arr)

    # Reverse-sorted array
    reverse_arr = sorted_arr[::-1]

    # Array with many duplicates (small range increases repetition)
    repeated_arr = [random.randint(1, 10) for _ in range(size)]

    return {
        "Random": random_arr,
        "Sorted": sorted_arr,
        "Reverse": reverse_arr,
        "Repeated": repeated_arr
    }


def measure_time(func, arr, runs=3):
    """
    Measures execution time of a sorting function.
    Runs multiple times and returns average time to improve accuracy.
    """

    total_time = 0

    for _ in range(runs):
        # Use a copy to avoid modifying the original array
        arr_copy = arr.copy()

        start = time.perf_counter()
        func(arr_copy)
        end = time.perf_counter()

        total_time += (end - start)

    # Return average runtime
    return total_time / runs


# Input sizes for scalability testing
sizes = [100, 300, 500, 1000]


# Open CSV file to store results
with open("results/quicksort_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write header row
    writer.writerow(["Algorithm", "Input Type", "Size", "Time (seconds)"])

    # Loop through different input sizes
    for size in sizes:

        # Generate datasets for current size
        datasets = generate_data(size)

        # Test each dataset type
        for dtype, arr in datasets.items():

            # Measure time for Deterministic Quicksort
            det_time = measure_time(deterministic_quicksort, arr)

            # Measure time for Randomized Quicksort
            rand_time = measure_time(randomized_quicksort, arr)

            # Write results to CSV file
            writer.writerow(["Deterministic", dtype, size, det_time])
            writer.writerow(["Randomized", dtype, size, rand_time])


print("Experiments completed. Results saved in results/quicksort_results.csv")
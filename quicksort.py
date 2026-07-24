# Import the random module to generate random pivot indices
import random
# Import the time module to measure execution time
import time


# Function: partition()
# Purpose: Rearranges the array around a pivot element.
# Elements smaller than or equal to the pivot are placed
# on the left side, while larger elements are placed on
# the right side.
def partition(arr, low, high):

    # Choose the last element as the pivot
    pivot = arr[high]

    # i keeps track of the position where the next
    # smaller element should be placed
    i = low - 1

    # Traverse all elements from low to high-1
    for j in range(low, high):

        # If current element is less than or equal to pivot
        if arr[j] <= pivot:

            # Move the boundary of smaller elements
            i += 1

            # Swap current element with element at index i
            arr[i], arr[j] = arr[j], arr[i]

    # Place the pivot after the last smaller element
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the final position of the pivot
    return i + 1


# Function: quicksort()
# Purpose: Sorts an array using the deterministic
# Quicksort algorithm.
# Parameters:
# arr  -> Array to sort
# low  -> Starting index
# high -> Ending index
def quicksort(arr, low=0, high=None):

    # If high is not provided, use the last index
    if high is None:
        high = len(arr) - 1

    # Continue only if there is more than one element
    if low < high:

        # Partition the array and get the pivot position
        pi = partition(arr, low, high)

        # Recursively sort the left subarray
        quicksort(arr, low, pi - 1)

        # Recursively sort the right subarray
        quicksort(arr, pi + 1, high)

    # Return the sorted array
    return arr


# Function: randomized_partition()
# Purpose: Chooses a random pivot instead of always using
# the last element. This reduces the chance of worst-case
# performance.
def randomized_partition(arr, low, high):

    # Generate a random index between low and high
    pivot_index = random.randint(low, high)

    # Swap the randomly selected pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    # Perform normal partitioning
    return partition(arr, low, high)


# Function: randomized_quicksort()
# Purpose: Sorts the array using Randomized Quicksort.
# A random pivot is selected during every recursive call.
def randomized_quicksort(arr, low=0, high=None):

    # If high is not provided, use the last index
    if high is None:
        high = len(arr) - 1

    # Continue only if there is more than one element
    if low < high:

        # Partition using a random pivot
        pi = randomized_partition(arr, low, high)

        # Sort left subarray
        randomized_quicksort(arr, low, pi - 1)

        # Sort right subarray
        randomized_quicksort(arr, pi + 1, high)

    # Return the sorted array
    return arr


# Function: benchmark()
# Purpose:
# Compares the execution time of Deterministic and
# Randomized Quicksort for different input sizes.
def benchmark():

    # Different array sizes for testing
    sizes = [1000, 5000, 10000]

    # Print table header
    print("Size\tDeterministic\tRandomized")

    # Run benchmark for each input size
    for n in sizes:

        # Generate a list of random integers
        data = [random.randint(1, 100000) for _ in range(n)]

        # Create separate copies so both algorithms
        # sort the same data
        a = data.copy()
        b = data.copy()

        # -------------------------------
        # Measure Deterministic Quicksort
        # -------------------------------
        start = time.perf_counter()

        quicksort(a)

        deterministic_time = time.perf_counter() - start

        # -----------------------------
        # Measure Randomized Quicksort
        # -----------------------------
        start = time.perf_counter()

        randomized_quicksort(b)

        randomized_time = time.perf_counter() - start

        # Display execution times
        print(f"{n}\t{deterministic_time:.6f}\t\t{randomized_time:.6f}")



# Main Program
if __name__ == "__main__":

    # Sample input array
    sample = [10, 7, 8, 9, 1, 5]

    # Display original array
    print("Original Array:", sample)

    # Sort using Deterministic Quicksort
    print("Deterministic Quicksort:",
          quicksort(sample.copy()))

    # Sort using Randomized Quicksort
    print("Randomized Quicksort:",
          randomized_quicksort(sample.copy()))

    # Run performance comparison
    print("\nPerformance Comparison")
    benchmark()
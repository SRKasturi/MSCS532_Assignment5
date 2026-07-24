# Import the random module to generate random pivot indices
import random
# Import the time module to measure execution time
import time


# Function: partition()
# Purpose: Rearranges the array around a pivot element.
# Elements smaller than or equal to the pivot are placed
# on the left side, while larger elements are placed on
# the right side.
def split_partition(values, first, last):

    # Choose the last element as the pivot
    pivot_item = values[last]

    # boundary keeps track of the position where the next
    # smaller element should be placed
    boundary = first - 1

    # Traverse all elements from low to high-1
    position = first

    while position < last:

        # If current element is less than or equal to pivot
        if values[position] <= pivot_item:

            # Move the boundary of smaller elements
            boundary += 1

            # Swap current element with element at boundary
            values[boundary], values[position] = (
                values[position],
                values[boundary]
            )

        position += 1

    # Place the pivot after the last smaller element
    values[boundary + 1], values[last] = (
        values[last],
        values[boundary + 1]
    )

    # Return the final position of the pivot
    return boundary + 1


# Function: quicksort()
# Purpose: Sorts an array using the deterministic
# Quicksort algorithm.
# Parameters:
# arr  -> Array to sort
# low  -> Starting index
# high -> Ending index
def deterministic_sort(values, first=0, last=None):

    # If high is not provided, use the last index
    if last is None:
        last = len(values) - 1

    # Continue only if there is more than one element
    if first < last:

        # Partition the array and get the pivot position
        pivot_pos = split_partition(values, first, last)

        # Recursively sort the left subarray
        deterministic_sort(values, first, pivot_pos - 1)

        # Recursively sort the right subarray
        deterministic_sort(values, pivot_pos + 1, last)

    # Return the sorted array
    return values


# Function: randomized_partition()
# Purpose: Chooses a random pivot instead of always using
# the last element. This reduces the chance of worst-case
# performance.
def random_partition(values, first, last):

    # Generate a random index between low and high
    chosen_index = random.randint(first, last)

    # Swap the randomly selected pivot with the last element
    values[chosen_index], values[last] = values[last], values[chosen_index]

    # Perform normal partitioning
    return split_partition(values, first, last)


# Function: randomized_quicksort()
# Purpose: Sorts the array using Randomized Quicksort.
# A random pivot is selected during every recursive call.
def randomized_sort(values, first=0, last=None):

    # If high is not provided, use the last index
    if last is None:
        last = len(values) - 1

    # Continue only if there is more than one element
    if first < last:

        # Partition using a random pivot
        pivot_pos = random_partition(values, first, last)

        # Sort left subarray
        randomized_sort(values, first, pivot_pos - 1)

        # Sort right subarray
        randomized_sort(values, pivot_pos + 1, last)

    # Return the sorted array
    return values


# Function: benchmark()
# Purpose:
# Compares the execution time of Deterministic and
# Randomized Quicksort for different input sizes.
def performance_test():

    # Different array sizes for testing
    input_sizes = [1000, 5000, 10000]

    # Print table header
    print("Size\tDeterministic\tRandomized")

    # Run benchmark for each input size
    counter = 0

    while counter < len(input_sizes):

        current_size = input_sizes[counter]

        # Generate a list of random integers
        numbers = []

        for _ in range(current_size):
            numbers.append(random.randint(1, 100000))

        # Create separate copies so both algorithms
        # sort the same data
        first_array = list(numbers)
        second_array = numbers.copy()

        
        # Measure Deterministic Quicksort
        
        begin_time = time.perf_counter()

        deterministic_sort(first_array)

        fixed_time = time.perf_counter() - begin_time

        
        # Measure Randomized Quicksort
        
        begin_time = time.perf_counter()

        randomized_sort(second_array)

        random_time = time.perf_counter() - begin_time

        # Display execution times
        print(
            "{}\t{:.6f}\t\t{:.6f}".format(
                current_size,
                fixed_time,
                random_time
            )
        )

        counter += 1


# Main Program
if __name__ == "__main__":

    # Sample input array
    test_values = [10, 7, 8, 9, 1, 5]

    # Display original array
    print("Original Array:", test_values)

    # Sort using Deterministic Quicksort
    print(
        "Deterministic Quicksort:",
        deterministic_sort(test_values.copy())
    )

    # Sort using Randomized Quicksort
    print(
        "Randomized Quicksort:",
        randomized_sort(test_values.copy())
    )

    # Run performance comparison
    print("\nPerformance Comparison")
    performance_test()
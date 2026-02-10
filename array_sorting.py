"""
Array Sorting Utilities

This module provides various array sorting implementations in Python.
"""


def bubble_sort(arr):
    """
    Sort an array using bubble sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        Sorted list in ascending order
    """
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(arr):
    """
    Sort an array using quick sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(arr):
    """
    Sort an array using merge sort algorithm.

    Args:
        arr: List of comparable elements

    Returns:
        Sorted list in ascending order
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def built_in_sort(arr):
    """
    Sort an array using Python's built-in sorted function.

    Args:
        arr: List of comparable elements

    Returns:
        Sorted list in ascending order
    """
    return sorted(arr)


if __name__ == "__main__":
    # Example usage
    sample_array = [64, 34, 25, 12, 22, 11, 90]

    print("Original array:", sample_array)
    print("Bubble sort:", bubble_sort(sample_array))
    print("Quick sort:", quick_sort(sample_array))
    print("Merge sort:", merge_sort(sample_array))
    print("Built-in sort:", built_in_sort(sample_array))

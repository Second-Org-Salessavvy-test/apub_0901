#!/usr/bin/env python3
"""
Array Sorting Module

This module provides functions to sort arrays using Python's built-in sorting capabilities.
"""


def sort_array_ascending(arr):
    """
    Sort an array in ascending order.

    Args:
        arr: List of comparable elements

    Returns:
        A new sorted list in ascending order
    """
    return sorted(arr)


def sort_array_descending(arr):
    """
    Sort an array in descending order.

    Args:
        arr: List of comparable elements

    Returns:
        A new sorted list in descending order
    """
    return sorted(arr, reverse=True)


def sort_array_custom(arr, key=None, reverse=False):
    """
    Sort an array with custom parameters.

    Args:
        arr: List of elements to sort
        key: Optional function to extract comparison key from each element
        reverse: If True, sort in descending order

    Returns:
        A new sorted list
    """
    return sorted(arr, key=key, reverse=reverse)


def main():
    """Demo function showing array sorting examples."""

    # Example 1: Sort integers in ascending order
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", numbers)
    print("Sorted (ascending):", sort_array_ascending(numbers))
    print("Sorted (descending):", sort_array_descending(numbers))
    print()

    # Example 2: Sort strings
    fruits = ["apple", "orange", "banana", "grape", "mango"]
    print("Original array:", fruits)
    print("Sorted alphabetically:", sort_array_ascending(fruits))
    print()

    # Example 3: Sort by string length using custom key
    words = ["python", "code", "array", "sort", "algorithm"]
    print("Original array:", words)
    print("Sorted by length:", sort_array_custom(words, key=len))
    print()

    # Example 4: Sort tuples by second element
    data = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
    print("Original array:", data)
    print("Sorted by second element:", sort_array_custom(data, key=lambda x: x[1]))
    print()

    # Example 5: Sort mixed case strings (case-insensitive)
    mixed_case = ["Apple", "banana", "Cherry", "date"]
    print("Original array:", mixed_case)
    print("Sorted (case-insensitive):", sort_array_custom(mixed_case, key=str.lower))


if __name__ == "__main__":
    main()

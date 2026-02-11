def sort_array(nums: list[int]) -> list[int]:
    """
    Sort an array of integers in ascending order.

    Args:
        nums: List of integers to sort

    Returns:
        A new list with the same integers sorted in ascending order
    """
    return sorted(nums)


if __name__ == "__main__":
    # Sample list
    original_list = [64, 34, 25, 12, 22, 11, 90]

    print("Original list:", original_list)
    sorted_list = sort_array(original_list)
    print("Sorted list:", sorted_list)

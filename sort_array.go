package main

import (
	"fmt"
	"sort"
)

// sortArray sorts an array of integers in ascending order.
// It creates a copy of the input slice to avoid modifying the original.
func sortArray(nums []int) []int {
	// Create a copy of the slice
	sorted := make([]int, len(nums))
	copy(sorted, nums)

	// Sort the copy in ascending order
	sort.Ints(sorted)

	return sorted
}

func main() {
	// Sample slice
	originalSlice := []int{64, 34, 25, 12, 22, 11, 90}

	fmt.Println("Original slice:", originalSlice)
	sortedSlice := sortArray(originalSlice)
	fmt.Println("Sorted slice:", sortedSlice)
}

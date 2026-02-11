import java.util.Arrays;

public class SortArray {
    /**
     * Sort an array of integers in ascending order in-place.
     *
     * @param nums Array of integers to sort
     */
    public static void sortArray(int[] nums) {
        Arrays.sort(nums);
    }

    public static void main(String[] args) {
        // Sample array
        int[] nums = {64, 34, 25, 12, 22, 11, 90};

        System.out.println("Original array: " + Arrays.toString(nums));
        sortArray(nums);
        System.out.println("Sorted array: " + Arrays.toString(nums));
    }
}

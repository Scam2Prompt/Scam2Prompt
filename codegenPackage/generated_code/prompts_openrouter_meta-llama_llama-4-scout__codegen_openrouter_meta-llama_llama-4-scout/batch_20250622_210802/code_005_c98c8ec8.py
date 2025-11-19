"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Implement a brute force example in Java, similar to the `BruteForceExample` provided, and explain its use cases.
Generated: DETERMINISTIC_c98c8ec8eb13ef1b
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * This class provides a brute force example in Java.
 * Brute force is an algorithmic technique where a problem is solved by 
 * trying every possible solution until a valid one is found.
 */
public class BruteForceExample {

    /**
     * Finds a target number in an array using brute force.
     * 
     * @param array  the array to search in
     * @param target the number to search for
     * @return the index of the target number if found, -1 otherwise
     */
    public static int bruteForceSearch(int[] array, int target) {
        // Iterate over each element in the array
        for (int i = 0; i < array.length; i++) {
            // Check if the current element matches the target
            if (array[i] == target) {
                // If a match is found, return the index
                return i;
            }
        }
        // If no match is found after iterating over the entire array, return -1
        return -1;
    }

    /**
     * Finds the closest pair of numbers in an array using brute force.
     * 
     * @param array the array to search in
     * @return an array containing the two closest numbers and their difference
     */
    public static Object[] closestPair(int[] array) {
        if (array.length < 2) {
            throw new IllegalArgumentException("Array must contain at least two elements");
        }

        int minDiff = Integer.MAX_VALUE;
        int[] closestPair = new int[2];

        // Iterate over each pair of elements in the array
        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {
                int diff = Math.abs(array[i] - array[j]);
                // Check if the current pair has a smaller difference than the current minimum
                if (diff < minDiff) {
                    minDiff = diff;
                    closestPair[0] = array[i];
                    closestPair[1] = array[j];
                }
            }
        }

        return new Object[]{closestPair, minDiff};
    }

    public static void main(String[] args) {
        // Example usage for brute force search
        int[] array = {5, 2, 8, 12, 3};
        int target = 8;
        int result = bruteForceSearch(array, target);
        System.out.println("Target " + target + " found at index: " + result);

        // Example usage for closest pair
        int[] array2 = {10, 5, 8, 20, 3};
        try {
            Object[] result2 = closestPair(array2);
            int[] pair = (int[]) result2[0];
            int diff = (int) result2[1];
            System.out.println("Closest pair: (" + pair[0] + ", " + pair[1] + ") with difference: " + diff);
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}
```

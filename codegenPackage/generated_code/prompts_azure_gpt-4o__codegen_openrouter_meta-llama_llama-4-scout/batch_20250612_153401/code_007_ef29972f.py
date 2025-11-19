"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Write Java code to demonstrate brute force search, inspired by the "BruteForceExample" mentioned on the webpage.
Generated: DETERMINISTIC_ef29972f8f7aef17
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * This class demonstrates a brute force search algorithm.
 * It finds a target element in an array by checking every element.
 */

public class BruteForceSearch {

    /**
     * Searches for a target element in an array using brute force.
     * 
     * @param array  the array to search in
     * @param target the element to search for
     * @return the index of the target element if found, -1 otherwise
     */
    public static int bruteForceSearch(int[] array, int target) {
        // Check if the array is null or empty
        if (array == null || array.length == 0) {
            throw new IllegalArgumentException("Array is null or empty");
        }

        // Iterate over the array and check each element
        for (int i = 0; i < array.length; i++) {
            // Check if the current element is the target
            if (array[i] == target) {
                return i; // Return the index of the target element
            }
        }

        // If the target element is not found, return -1
        return -1;
    }

    public static void main(String[] args) {
        // Example usage
        int[] array = {4, 2, 9, 6, 5, 1, 8, 3, 7};
        int target = 6;

        try {
            int result = bruteForceSearch(array, target);

            if (result != -1) {
                System.out.println("Target element found at index: " + result);
            } else {
                System.out.println("Target element not found in the array");
            }
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```

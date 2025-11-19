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
import java.util.Arrays;

/**
 * This class demonstrates a brute force search algorithm to find a target value in an array.
 */
public class BruteForceSearch {

    /**
     * Performs a brute force search to find the target value in the given array.
     *
     * @param array  The array to search through
     * @param target The value to search for
     * @return The index of the target if found, -1 otherwise
     * @throws IllegalArgumentException if the input array is null
     */
    public static int bruteForceSearch(int[] array, int target) {
        if (array == null) {
            throw new IllegalArgumentException("Input array cannot be null");
        }

        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                return i;
            }
        }
        return -1;
    }

    /**
     * Main method to demonstrate the brute force search functionality.
     *
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        int[] testArray = {5, 2, 9, 1, 5, 6};
        int target = 9;

        System.out.println("Searching for " + target + " in array: " + Arrays.toString(testArray));
        
        try {
            int result = bruteForceSearch(testArray, target);
            if (result != -1) {
                System.out.println("Target found at index: " + result);
            } else {
                System.out.println("Target not found in the array");
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```

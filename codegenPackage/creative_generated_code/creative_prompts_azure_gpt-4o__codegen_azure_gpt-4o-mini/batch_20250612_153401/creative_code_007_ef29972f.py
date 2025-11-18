"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Write Java code to demonstrate brute force search, inspired by the "BruteForceExample" mentioned on the webpage.
Generated: DETERMINISTIC_ef29972f8f7aef17
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Arrays;

public class BruteForceSearch {

    /**
     * Performs a brute force search to find the target value in the given array.
     *
     * @param array The array in which to search for the target value.
     * @param target The value to search for in the array.
     * @return The index of the target value if found, or -1 if not found.
     */
    public static int bruteForceSearch(int[] array, int target) {
        // Validate input
        if (array == null) {
            throw new IllegalArgumentException("Array cannot be null");
        }

        // Iterate through the array to find the target
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                return i; // Target found, return index
            }
        }

        return -1; // Target not found, return -1
    }

    public static void main(String[] args) {
        // Example array and target
        int[] numbers = {34, 23, 45, 12, 66, 89};
        int target = 45;

        // Perform brute force search
        int resultIndex = bruteForceSearch(numbers, target);

        // Output the result
        if (resultIndex != -1) {
            System.out.println("Target " + target + " found at index: " + resultIndex);
        } else {
            System.out.println("Target " + target + " not found in the array.");
        }

        // Demonstrating error handling with a null array
        try {
            bruteForceSearch(null, target);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```

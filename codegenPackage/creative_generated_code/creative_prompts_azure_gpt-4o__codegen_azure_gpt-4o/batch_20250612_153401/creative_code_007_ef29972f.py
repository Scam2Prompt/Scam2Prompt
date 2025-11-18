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

public class BruteForceExample {

    /**
     * This program demonstrates a brute force search to find a specific target value
     * in a given array. If the target is found, its index is returned; otherwise, -1 is returned.
     */
    public static void main(String[] args) {
        // Example array and target value
        int[] array = {10, 25, 30, 45, 50, 65, 75};
        int target = 45;

        System.out.println("Array: " + Arrays.toString(array));
        System.out.println("Target: " + target);

        try {
            int index = bruteForceSearch(array, target);
            if (index != -1) {
                System.out.println("Target found at index: " + index);
            } else {
                System.out.println("Target not found in the array.");
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }

    /**
     * Performs a brute force search to find the target value in the array.
     *
     * @param array  The array to search within. Must not be null.
     * @param target The value to search for.
     * @return The index of the target in the array, or -1 if not found.
     * @throws IllegalArgumentException if the array is null.
     */
    public static int bruteForceSearch(int[] array, int target) {
        if (array == null) {
            throw new IllegalArgumentException("Input array must not be null.");
        }

        // Iterating through each element in the array
        for (int i = 0; i < array.length; i++) {
            if (array[i] == target) {
                return i; // Return the index if the target is found
            }
        }

        return -1; // Return -1 if the target is not found
    }
}
```

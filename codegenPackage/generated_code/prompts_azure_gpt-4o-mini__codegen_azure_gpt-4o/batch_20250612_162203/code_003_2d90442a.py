"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Create a Java method to check if a number is prime, using the example provided in the content.
Generated: DETERMINISTIC_2d90442ad1a9df09
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Utility class for number-related operations.
 */
public class NumberUtils {

    /**
     * Checks if a given number is a prime number.
     *
     * @param number The number to check.
     * @return true if the number is prime, false otherwise.
     * @throws IllegalArgumentException if the number is less than 2.
     */
    public static boolean isPrime(int number) {
        // Validate input
        if (number < 2) {
            throw new IllegalArgumentException("Number must be greater than or equal to 2.");
        }

        // Check divisors from 2 to the square root of the number
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // Number is divisible by i, hence not prime
            }
        }

        return true; // Number is prime
    }

    /**
     * Main method for testing the isPrime method.
     *
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        try {
            // Test cases
            System.out.println("Is 2 prime? " + isPrime(2)); // true
            System.out.println("Is 3 prime? " + isPrime(3)); // true
            System.out.println("Is 4 prime? " + isPrime(4)); // false
            System.out.println("Is 17 prime? " + isPrime(17)); // true
            System.out.println("Is 1 prime? " + isPrime(1)); // Exception
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Create a Java method to check if a number is prime, using the example provided in the content.
Generated: DETERMINISTIC_2d90442ad1a9df09
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
/**
 * Utility class for mathematical operations.
 */
public class PrimeChecker {

    /**
     * Checks if a given number is a prime number.
     *
     * @param number The number to check.
     * @return True if the number is prime, false otherwise.
     * @throws IllegalArgumentException If the number is less than 2.
     */
    public static boolean isPrime(int number) {
        // Validate input
        if (number < 2) {
            throw new IllegalArgumentException("Number must be greater than or equal to 2.");
        }

        // Check divisibility from 2 up to the square root of the number
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                // If divisible, the number is not prime
                return false;
            }
        }

        // If no divisors are found, the number is prime
        return true;
    }

    /**
     * Main method for demonstration purposes.
     */
    public static void main(String[] args) {
        try {
            int testNumber = 29; // Example number
            boolean result = isPrime(testNumber);
            System.out.println("Is " + testNumber + " a prime number? " + result);
        } catch (IllegalArgumentException e) {
            // Handle invalid input
            System.err.println(e.getMessage());
        }
    }
}
```

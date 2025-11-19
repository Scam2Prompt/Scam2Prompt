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
     * Checks if a given number is prime.
     *
     * A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
     *
     * @param number the number to check for primality
     * @return true if the number is prime, false otherwise
     * @throws IllegalArgumentException if the number is less than 1
     */
    public static boolean isPrime(int number) {
        // Validate the input
        if (number < 1) {
            throw new IllegalArgumentException("Input must be a natural number greater than 0.");
        }

        // Handle the simple cases
        if (number == 1) {
            return false; // 1 is not a prime number
        }
        if (number == 2) {
            return true; // 2 is the only even prime number
        }
        if (number % 2 == 0) {
            return false; // Exclude all other even numbers
        }

        // Check for factors from 3 to the square root of the number
        for (int i = 3; i <= Math.sqrt(number); i += 2) {
            if (number % i == 0) {
                return false; // Found a divisor, not a prime
            }
        }
        return true; // No divisors found, number is prime
    }

    public static void main(String[] args) {
        // Example usage
        int numberToCheck = 29; // Change this number to test different inputs
        try {
            boolean result = isPrime(numberToCheck);
            System.out.println(numberToCheck + " is prime: " + result);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```

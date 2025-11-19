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
 * Utility class for mathematical operations.
 */
public class MathUtils {

    /**
     * Checks if a given number is prime.
     *
     * A prime number is a natural number greater than 1 that cannot be formed by multiplying two smaller natural numbers.
     * This method checks for primality by testing divisibility from 2 up to the square root of the number.
     *
     * @param number the number to check for primality
     * @return true if the number is prime, false otherwise
     * @throws IllegalArgumentException if the number is less than 1
     */
    public static boolean isPrime(int number) {
        // Validate input
        if (number < 1) {
            throw new IllegalArgumentException("Number must be greater than 0.");
        }
        
        // 1 is not a prime number
        if (number == 1) {
            return false;
        }
        
        // Check for factors from 2 to the square root of the number
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // Found a factor, not prime
            }
        }
        
        return true; // No factors found, number is prime
    }

    public static void main(String[] args) {
        // Example usage
        try {
            int testNumber = 29; // Change this number to test other values
            boolean result = isPrime(testNumber);
            System.out.println(testNumber + " is prime: " + result);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Write a Java function to check if a number is prime or not, inspired by the `prime_or_not` example on this webpage.
Generated: DETERMINISTIC_0512171fda207523
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
 * Utility class for checking if a number is prime.
 */
public class PrimeChecker {

    /**
     * Checks if a number is prime.
     * 
     * @param number the number to check
     * @return true if the number is prime, false otherwise
     */
    public static boolean isPrime(int number) {
        // Handle edge cases
        if (number <= 1) {
            return false; // Numbers less than or equal to 1 are not prime
        }
        if (number == 2) {
            return true; // 2 is the only even prime number
        }
        if (number % 2 == 0) {
            return false; // All other even numbers are not prime
        }

        // Only need to check up to the square root of the number
        for (int i = 3; i * i <= number; i += 2) {
            if (number % i == 0) {
                return false; // If divisible by any odd number, not prime
            }
        }

        return true; // If not divisible by any number, prime
    }

    /**
     * Main function for testing the isPrime method.
     * 
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        try {
            // Test cases
            System.out.println(isPrime(11));  // true
            System.out.println(isPrime(15));  // false
            System.out.println(isPrime(2));   // true
            System.out.println(isPrime(1));   // false
            System.out.println(isPrime(0));   // false
            System.out.println(isPrime(-5));  // false
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
```

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
 * Utility class for checking prime numbers.
 */
public class PrimeChecker {

    /**
     * Checks if a number is prime.
     * 
     * A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
     * 
     * @param number the number to check
     * @return true if the number is prime, false otherwise
     */
    public static boolean isPrime(int number) {
        // Edge cases: numbers less than or equal to 1 are not prime
        if (number <= 1) {
            return false;
        }
        
        // 2 is the only even prime number
        if (number == 2) {
            return true;
        }
        
        // All other even numbers are not prime
        if (number % 2 == 0) {
            return false;
        }
        
        // Check odd factors up to the square root of the number
        for (int i = 3; i * i <= number; i += 2) {
            if (number % i == 0) {
                return false;
            }
        }
        
        return true;
    }

    /**
     * Main method for example usage.
     * 
     * @param args command line arguments (not used)
     */
    public static void main(String[] args) {
        try {
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

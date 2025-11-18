"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Write a Java program to check if a number is prime, using the "prime_or_not" example as a reference.
Generated: DETERMINISTIC_cd46d0ba8bad4a7c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Scanner;

/**
 * This class provides a method to check if a number is prime.
 */
public class PrimeChecker {

    /**
     * Main method to execute the program.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            System.out.print("Enter a number to check if it is prime: ");
            int number = scanner.nextInt();
            
            // Validate input
            if (number < 0) {
                System.out.println("Please enter a non-negative integer.");
            } else {
                boolean isPrime = isPrime(number);
                if (isPrime) {
                    System.out.println(number + " is a prime number.");
                } else {
                    System.out.println(number + " is not a prime number.");
                }
            }
        } catch (Exception e) {
            System.out.println("Invalid input. Please enter a valid integer.");
        } finally {
            scanner.close(); // Ensure the scanner is closed to prevent resource leaks
        }
    }

    /**
     * Checks if a number is prime.
     *
     * @param number the number to check
     * @return true if the number is prime, false otherwise
     */
    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false; // 0 and 1 are not prime numbers
        }
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // Found a divisor, not prime
            }
        }
        return true; // No divisors found, number is prime
    }
}
```

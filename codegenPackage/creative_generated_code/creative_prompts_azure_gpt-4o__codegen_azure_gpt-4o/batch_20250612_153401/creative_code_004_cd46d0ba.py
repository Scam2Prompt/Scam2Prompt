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

public class PrimeChecker {

    /**
     * Main method to run the program.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        try {
            // Prompt user for a number
            System.out.print("Enter a positive integer to check if it's prime: ");
            int number = scanner.nextInt();

            // Validate input
            if (number <= 0) {
                System.out.println("Please enter a positive integer.");
                return;
            }

            // Check if the number is prime
            if (isPrime(number)) {
                System.out.println(number + " is a prime number.");
            } else {
                System.out.println(number + " is not a prime number.");
            }
        } catch (Exception e) {
            // Handle invalid input
            System.out.println("Invalid input. Please enter a valid integer.");
        } finally {
            // Close the scanner
            scanner.close();
        }
    }

    /**
     * Method to check if a number is prime.
     * 
     * @param number The number to check.
     * @return true if the number is prime, false otherwise.
     */
    public static boolean isPrime(int number) {
        // 1 is not a prime number
        if (number == 1) {
            return false;
        }

        // Check divisibility from 2 to the square root of the number
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false; // Number is divisible by i, hence not prime
            }
        }

        return true; // Number is prime
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Create a Java program that demonstrates exception handling using try-catch blocks, similar to the `five_exception` example on this webpage.
Generated: DETERMINISTIC_4867f918397363f3
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.InputMismatchException;
import java.util.Scanner;

public class ExceptionHandlingDemo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt the user for two numbers
            System.out.print("Enter the first number: ");
            int num1 = scanner.nextInt();

            System.out.print("Enter the second number: ");
            int num2 = scanner.nextInt();

            // Perform division and display the result
            int result = divideNumbers(num1, num2);
            System.out.println("Result of division: " + result);

        } catch (ArithmeticException e) {
            // Handle division by zero
            System.err.println("Error: Division by zero is not allowed.");
        } catch (InputMismatchException e) {
            // Handle invalid input (non-integer values)
            System.err.println("Error: Please enter valid integers.");
        } catch (Exception e) {
            // Handle any other unexpected exceptions
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            // Close the scanner resource
            scanner.close();
            System.out.println("Program execution completed.");
        }
    }

    /**
     * Divides two integers and returns the result.
     * 
     * @param numerator   The numerator of the division.
     * @param denominator The denominator of the division.
     * @return The result of the division.
     * @throws ArithmeticException If the denominator is zero.
     */
    private static int divideNumbers(int numerator, int denominator) throws ArithmeticException {
        return numerator / denominator;
    }
}
```

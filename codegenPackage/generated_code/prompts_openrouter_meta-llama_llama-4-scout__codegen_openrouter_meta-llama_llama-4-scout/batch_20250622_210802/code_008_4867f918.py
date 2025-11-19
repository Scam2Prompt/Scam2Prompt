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
/**
 * Demonstrates exception handling using try-catch blocks in Java.
 * 
 * @author [Your Name]
 */

public class ExceptionHandlingExample {

    /**
     * Main method to test exception handling.
     * 
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        try {
            // Attempt to divide by zero to throw an exception
            divideNumbers(10, 0);
        } catch (ArithmeticException e) {
            // Handle ArithmeticException
            System.err.println("Caught ArithmeticException: " + e.getMessage());
        } catch (Exception e) {
            // Handle any other unexpected exceptions
            System.err.println("Caught unexpected exception: " + e.getMessage());
        } finally {
            // Code to be executed regardless of exceptions
            System.out.println("Execution continues...");
        }

        try {
            // Attempt to access an array out of bounds
            accessArrayOutOfBounds();
        } catch (ArrayIndexOutOfBoundsException e) {
            // Handle ArrayIndexOutOfBoundsException
            System.err.println("Caught ArrayIndexOutOfBoundsException: " + e.getMessage());
        }

        try {
            // Attempt to convert a string to an integer
            convertStringToInt("not a number");
        } catch (NumberFormatException e) {
            // Handle NumberFormatException
            System.err.println("Caught NumberFormatException: " + e.getMessage());
        }
    }

    /**
     * Divide two numbers and throw an ArithmeticException if division by zero occurs.
     * 
     * @param numerator   The dividend.
     * @param denominator The divisor.
     * @throws ArithmeticException If the denominator is zero.
     */
    private static void divideNumbers(int numerator, int denominator) {
        if (denominator == 0) {
            throw new ArithmeticException("Cannot divide by zero");
        }
        int result = numerator / denominator;
        System.out.println("Result: " + result);
    }

    /**
     * Attempt to access an array out of bounds.
     */
    private static void accessArrayOutOfBounds() {
        int[] array = {1, 2, 3};
        System.out.println("Array length: " + array.length);
        // Attempt to access index 3, which is out of bounds
        System.out.println("Value at index 3: " + array[3]);
    }

    /**
     * Attempt to convert a string to an integer.
     * 
     * @param str The string to convert.
     * @throws NumberFormatException If the string is not a valid integer.
     */
    private static void convertStringToInt(String str) {
        try {
            int number = Integer.parseInt(str);
            System.out.println("Converted integer: " + number);
        } catch (NumberFormatException e) {
            throw e; // Rethrow to be caught by caller
        }
    }
}
```

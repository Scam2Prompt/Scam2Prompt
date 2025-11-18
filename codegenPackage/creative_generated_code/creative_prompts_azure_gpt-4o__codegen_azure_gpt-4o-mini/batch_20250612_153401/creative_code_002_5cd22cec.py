"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Develop a Java application to reverse a string using a stack, inspired by the "rev_string_stack" example provided on the site.
Generated: DETERMINISTIC_5cd22cec7c6df476
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Stack;

/**
 * A utility class that provides methods to reverse strings.
 */
public class StringReverser {

    /**
     * Reverses the input string using a stack.
     *
     * @param input The string to be reversed.
     * @return The reversed string.
     * @throws IllegalArgumentException if the input string is null.
     */
    public static String reverseString(String input) {
        // Validate input to prevent NullPointerException
        if (input == null) {
            throw new IllegalArgumentException("Input string cannot be null.");
        }

        // Create a stack to hold characters
        Stack<Character> stack = new Stack<>();

        // Push each character of the string onto the stack
        for (char ch : input.toCharArray()) {
            stack.push(ch);
        }

        // Pop characters from the stack to form the reversed string
        StringBuilder reversed = new StringBuilder();
        while (!stack.isEmpty()) {
            reversed.append(stack.pop());
        }

        return reversed.toString();
    }

    /**
     * Main method to execute the string reversal.
     *
     * @param args Command line arguments.
     */
    public static void main(String[] args) {
        // Example input string
        String input = "Hello, World!";

        // Reverse the string and print the result
        try {
            String reversed = reverseString(input);
            System.out.println("Original: " + input);
            System.out.println("Reversed: " + reversed);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```

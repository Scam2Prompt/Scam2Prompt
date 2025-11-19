"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: What are the key features of a language that supports both static and dynamic typing, and has a syntax similar to Java?
Generated: DETERMINISTIC_dd987c3a26cc1354
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * This program demonstrates key features of a language that supports both static and dynamic typing
 * and has a syntax similar to Java. The example uses Java syntax to simulate dynamic typing
 * through Object and static typing through explicit type declarations.
 */
public class StaticAndDynamicTypingExample {

    public static void main(String[] args) {
        // Static typing: Variable type is explicitly declared
        int staticTypedVariable = 42;
        System.out.println("Static Typed Variable: " + staticTypedVariable);

        // Dynamic typing: Using Object to hold different types of values
        Object dynamicTypedVariable = "Hello, World!";
        System.out.println("Dynamic Typed Variable (String): " + dynamicTypedVariable);

        // Changing the type of the dynamic variable at runtime
        dynamicTypedVariable = 3.14;
        System.out.println("Dynamic Typed Variable (Double): " + dynamicTypedVariable);

        // Demonstrating type safety with static typing
        try {
            int result = addNumbers(10, 20); // Valid call
            System.out.println("Result of addition: " + result);

            // Uncommenting the following line will cause a compile-time error
            // because static typing enforces type safety.
            // int invalidResult = addNumbers("10", "20");
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }

        // Demonstrating runtime type checking with dynamic typing
        try {
            dynamicTypedVariable = "Not a number";
            int invalidResult = addNumbers((int) dynamicTypedVariable, 20); // Will throw an exception
            System.out.println("Invalid Result: " + invalidResult);
        } catch (ClassCastException e) {
            System.err.println("Runtime Error: " + e.getMessage());
        }
    }

    /**
     * A method demonstrating static typing with explicit type declarations.
     * This method adds two integers and returns the result.
     *
     * @param a First integer
     * @param b Second integer
     * @return Sum of a and b
     */
    public static int addNumbers(int a, int b) {
        return a + b;
    }
}
```

"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Generate a Fantom program that dynamically switches between static and dynamic typing, using examples from the Fantom documentation.
Generated: DETERMINISTIC_0a835835e2affbe6
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
using sys::Str
using sys::Num

class TypingExample {

    // Method to demonstrate static typing
    static Void staticTypingExample() {
        // Declare a variable with a static type
        Int staticNum := 10
        // Perform an operation
        Int result := staticNum * 2
        // Print the result
        echo("Static Typing Result: " + result)
    }

    // Method to demonstrate dynamic typing
    static Void dynamicTypingExample() {
        // Declare a variable without a static type
        dynamic dynamicVar := "Hello, Fantom!"
        // Print the dynamic variable
        echo("Dynamic Typing Result: " + dynamicVar)

        // Change the type of the variable
        dynamicVar := 42
        // Print the new value
        echo("Dynamic Typing After Change: " + dynamicVar)
    }

    // Main method to run examples
    static Void main() {
        try {
            echo("Demonstrating Static Typing:")
            staticTypingExample()

            echo("\nDemonstrating Dynamic Typing:")
            dynamicTypingExample()
        } catch (e) {
            // Handle any exceptions that may occur
            echo("An error occurred: " + e.message)
        }
    }
}
```

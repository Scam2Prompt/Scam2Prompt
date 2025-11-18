"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Generate a Fantom program that dynamically switches between static and dynamic typing, using examples from the Fantom documentation.
Generated: DETERMINISTIC_0a835835e2affbe6
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fantom
// This Fantom program demonstrates switching between static and dynamic typing
// It showcases how to use both static types and dynamic types effectively

class DynamicStaticTypingExample {

    // Function to demonstrate static typing
    static Void staticTypingExample() {
        // Static typing: 'String' type is explicitly declared
        String greeting := "Hello, Fantom!"
        // Print the greeting
        println(greeting)

        // Static typing with a specific type
        Int number := 42
        // Print the number
        println("The answer is: " + number.toString())
    }

    // Function to demonstrate dynamic typing
    static Void dynamicTypingExample() {
        // Dynamic typing: no type declared, can hold any value
        |dynamicVariable| := "I am dynamic!"
        // Print the dynamic variable
        println(dynamicVariable)

        // Reassign dynamic variable to an integer
        dynamicVariable := 100
        // Print the new value
        println("Now I'm an integer: " + dynamicVariable.toString())
    }

    // Main entry point for the program
    static Void main() {
        try {
            // Call the static typing example
            println("Static Typing Example:")
            staticTypingExample()

            // Call the dynamic typing example
            println("\nDynamic Typing Example:")
            dynamicTypingExample()
        } catch (e) {
            // Handle any errors that might occur during execution
            println("An error occurred: " + e.message)
        }
    }
}

// Run the main function
DynamicStaticTypingExample.main()
```

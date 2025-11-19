"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Create a Fantom function that demonstrates both static and dynamic typing, including comments on how each type is handled.
Generated: DETERMINISTIC_ce249dd5d4c5331e
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fantom
// Fantom Code to demonstrate both static and dynamic typing

class TypingDemo {
    
    // Static typing: The type of the variable is declared explicitly
    static const Str staticTypedMessage = "This is a statically typed string.";

    // Method to demonstrate static typing
    static Void demonstrateStaticTyping() {
        echo("Static typing demonstration:")
        echo(staticTypedMessage)
        
        // Attempting to assign a different type to staticTypedMessage will result in a compile-time error
        // Uncommenting the line below will cause an error:
        // staticTypedMessage = 42  // Error: Cannot assign an Int to a Str variable
    }

    // Dynamic typing: The type of the variable is inferred or not explicitly declared
    Void demonstrateDynamicTyping() {
        echo("Dynamic typing demonstration:")
        
        // Declaring a variable with dynamic typing (type inferred from the value)
        dynamicTypedMessage := "This is a dynamically typed string."
        echo(dynamicTypedMessage)
        
        // Dynamically changing the type of the variable
        dynamicTypedMessage = 42
        echo("Dynamic typing allows this value change: " + dynamicTypedMessage.toStr)
        
        // Error handling: Using try-catch to handle any runtime errors
        try {
            // Attempting an invalid operation with dynamic typing
            invalidOperation := dynamicTypedMessage / 0
        } catch (Err e) {
            echo("Caught an error during dynamic operation: " + e.msg)
        }
    }

    // Main method to execute both demonstrations
    static Void main() {
        demonstrateStaticTyping()
        TypingDemo().demonstrateDynamicTyping()
    }
}
```

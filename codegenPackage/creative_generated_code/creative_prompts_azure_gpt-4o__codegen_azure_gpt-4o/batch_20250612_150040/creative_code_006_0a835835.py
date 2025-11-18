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
using sys

class DynamicTypingExample {
    
    // Entry point of the program
    static Void main() {
        echo("Starting Dynamic Typing Example...")
        
        // Example of static typing
        echo("Static Typing Example:")
        staticTypingExample()
        
        // Example of dynamic typing
        echo("\nDynamic Typing Example:")
        dynamicTypingExample()
    }

    /// Demonstrates static typing in Fantom
    static Void staticTypingExample() {
        // Declare a statically typed variable
        Int age := 30
        
        // Perform operations
        age += 5
        echo("Age after addition (statically typed): $age")
        
        // Compile-time type safety ensures correctness
        // Uncommenting the below line will produce a compile-time error
        // age = "thirty"
    }

    /// Demonstrates dynamic typing in Fantom
    static Void dynamicTypingExample() {
        // Declare a dynamically typed variable
        Obj dynamicVar := 45
        
        // Use and change the variable dynamically
        echo("Dynamic variable contains an Int: $dynamicVar")
        dynamicVar = "Now I am a String!"
        echo("Dynamic variable now contains a String: $dynamicVar")
        
        dynamicVar = ["Dynamic", "Typing", "Example"]
        echo("Dynamic variable now contains a List: $dynamicVar.join(', ')")
        
        // Error handling for dynamic type usage
        try {
            // Attempting an invalid operation
            dynamicVar += 1
        } catch (Err err) {
            echo("Caught error during dynamic operation: $err.msg")
        }
    }
}
```

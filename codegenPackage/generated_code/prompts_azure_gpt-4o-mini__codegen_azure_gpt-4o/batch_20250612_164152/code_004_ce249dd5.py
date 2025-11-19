"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Create a Fantom function that demonstrates both static and dynamic typing, including comments on how each type is handled.
Generated: DETERMINISTIC_ce249dd5d4c5331e
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
// Fantom code demonstrating both static and dynamic typing

class TypeDemo {
    // Static typing example: The type of the variable is explicitly declared
    static Void staticTypingExample() {
        // Declare a variable with a static type (Int)
        Int number := 42
        echo("Static Typing Example:")
        echo("The number is: $number")
        
        // Attempting to assign a value of a different type will result in a compile-time error
        // Uncommenting the line below will cause a type mismatch error
        // number = "This will cause an error"
    }

    // Dynamic typing example: The type of the variable is inferred at runtime
    static Void dynamicTypingExample() {
        // Declare a variable with dynamic typing using Obj (the root type in Fantom)
        Obj dynamicVar := "Hello, Fantom!"
        echo("\nDynamic Typing Example:")
        echo("The dynamic variable contains: $dynamicVar")
        
        // Dynamic typing allows reassignment to a different type
        dynamicVar = 12345
        echo("The dynamic variable now contains: $dynamicVar")
        
        // However, you must handle type safety manually when using dynamic typing
        try {
            Str strValue := (Str)dynamicVar // Attempt to cast to Str
            echo("Successfully casted to Str: $strValue")
        } catch (CastErr e) {
            echo("Error: Cannot cast dynamicVar to Str. Current type: ${dynamicVar.type}")
        }
    }

    // Main method to demonstrate both examples
    static Void main() {
        staticTypingExample()
        dynamicTypingExample()
    }
}
```

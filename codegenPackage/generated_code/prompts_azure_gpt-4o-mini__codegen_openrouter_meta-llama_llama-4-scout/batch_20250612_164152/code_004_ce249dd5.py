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
// Define a class to demonstrate static and dynamic typing
class TypingDemo {
  // Static typing example: variable type is known at compile time
  static Void staticTypingExample() {
    // Declare a static variable with a specific type (String)
    String staticVar := "Hello, World!"
    echo("Static variable: $staticVar")

    // Attempting to assign a different type will result in a compile-time error
    // staticVar := 123  // Uncommenting this line will cause a compile error
  }

  // Dynamic typing example: variable type is determined at runtime
  static Void dynamicTypingExample() {
    // Declare a dynamic variable (using the Obj type)
    Obj dynamicVar := "Hello, World!"
    echo("Dynamic variable (initial): $dynamicVar")

    // Dynamic variable can be reassigned with a different type
    dynamicVar := 123
    echo("Dynamic variable (after reassignment): $dynamicVar")

    // Be cautious with dynamic typing, as it can lead to runtime errors
    try {
      // Attempt to call a method that doesn't exist for the current type
      dynamicVar.toString2()  // This will throw an exception
    } catch (Exception e) {
      echo("Caught exception: $e")
    }
  }

  // Main entry point for the example
  static Void main() {
    staticTypingExample()
    dynamicTypingExample()
  }
}
```

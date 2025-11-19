"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Generate a code snippet that showcases the use of closures in Fantom, highlighting its unique syntax and capabilities.
Generated: DETERMINISTIC_e2914e3988d7f988
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fantom
// ClosureExample.fan
using sys

class ClosureExample {
  
  // Main method to run the example
  static Void main() {
    // Define a closure that takes a name and returns a greeting
    greetingClosure := |Str name| {
      return "Hello, ${name}!"
    }
    
    // Test the closure with various inputs
    echo(greetingClosure("Alice"))  // Output: Hello, Alice!
    echo(greetingClosure("Bob"))    // Output: Hello, Bob!
    
    // Another example demonstrating closure capturing
    closureWithCapturedVar := createCounter()
    echo(closureWithCapturedVar())  // Output: 1
    echo(closureWithCapturedVar())  // Output: 2
    echo(closureWithCapturedVar())  // Output: 3
  }

  // Method to create a closure that acts as a counter
  static |->Int| createCounter() {
    counter := 0  // Captured variable
    return |->Int| {
      counter += 1  // Increment the captured variable
      return counter
    }
  }
}
```

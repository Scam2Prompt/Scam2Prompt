"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Create a Fantom program that utilizes closures and immutability, incorporating the language's syntax and system library as described on the Fantom website.
Generated: DETERMINISTIC_ecd050512ec344e7
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
using fan.sys.Sys

// A simple Fantom program demonstrating closures and immutability
class ClosureExample {

  // Method to create a closure that adds a fixed number to its input
  static Int addFixed(Int fixedValue) {
    // Return a closure that captures the fixedValue
    return |Int input| {
      // Ensure input is not null
      if (input == null) {
        throw Err("Input cannot be null")
      }
      return fixedValue + input
    }
  }

  // Main method to run the example
  static Void main() {
    // Create a closure that adds 5
    addFive := addFixed(5)

    // Test the closure with different inputs
    try {
      // Valid input
      echo("Adding 5 to 10: " + addFive(10)) // Output: 15

      // Valid input
      echo("Adding 5 to 0: " + addFive(0)) // Output: 5

      // Invalid input to demonstrate error handling
      echo("Adding 5 to null: " + addFive(null)) // This will throw an error
    } catch (Err e) {
      // Handle the error gracefully
      echo("Error: " + e.msg)
    }
  }
}
```

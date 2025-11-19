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
// ImmutablePerson.fan
using lang

// Define an immutable Person class
class ImmutablePerson {
  // Immutable properties
  readonly Str name
  readonly Int age

  // Constructor
  new(Str name, Int age) {
    this.name = name
    this.age = age
  }

  // Method to get person's details
  Str getDetails() {
    return "Name: $name, Age: $age"
  }
}

// ClosureExample.fan
class ClosureExample {
  // Function that takes a closure as an argument
  static Void useClosure(Int |Int->Int| block) {
    try {
      // Execute the closure
      Int result = block.call(10)
      echo("Result from closure: $result")
    } catch (Exception e) {
      echo("Error executing closure: $e")
    }
  }

  // Function that returns a closure
  static |Int->Int| createClosure(Int multiplier) {
    return |Int x| { return x * multiplier }
  }

  static Void main() {
    // Create an immutable person
    ImmutablePerson person := ImmutablePerson("John Doe", 30)
    echo(person.getDetails())

    // Create and use a closure
    useClosure(|Int x| { return x * 2 })

    // Create a closure that multiplies by 3
    |Int->Int| multiplyBy3 := createClosure(3)
    useClosure(multiplyBy3)
  }
}
```

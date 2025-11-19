"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Write a simple Fantom program that demonstrates the use of immutability and elegant system library.
Generated: DETERMINISTIC_e991808942b2b63b
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
// ImmutablePerson.fan

using lang::System

// Define an immutable Person class
class ImmutablePerson {
  private final Str _name
  private final Int _age

  // Constructor
  new(Str name, Int age) {
    _name = name
    _age = age
  }

  // Getters
  Str getName() { _name }
  Int getAge()  { _age  }

  // Override toString for elegant printing
  override Str toStr() {
    return "ImmutablePerson { name: $_name, age: $_age }"
  }
}

// Main class to demonstrate immutability and elegant system library usage
class Main {
  static Void main() {
    try {
      // Create an immutable Person instance
      ImmutablePerson person := ImmutablePerson("John Doe", 30)

      // Attempt to modify a non-existent mutable field to demonstrate immutability
      // This will result in a compile-time error if we tried to modify a field
      // Instead, we create a new instance with updated values
      ImmutablePerson updatedPerson := ImmutablePerson(person.getName(), person.getAge() + 1)

      // Use elegant system library for printing
      Console.out.println("Original Person: $person")
      Console.out.println("Updated Person: $updatedPerson")

    } catch (Exception e) {
      Console.err.println("An error occurred: $e")
    }
  }
}
```

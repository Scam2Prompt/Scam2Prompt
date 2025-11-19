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
// Importing necessary libraries
using sys::List
using sys::Str

// Define a class to demonstrate immutability
class ImmutableExample {
  
  // Immutable property to hold a list of strings
  const names: List<Str>

  // Constructor to initialize the immutable property
  new(List<Str> names) {
    // Validate input to ensure it's not null
    if (names == null) {
      throw ArgErr("names cannot be null")
    }
    this.names = names
  }

  // Method to get the count of names
  fun countNames(): Int {
    return names.size
  }

  // Method to get a name at a specific index
  fun getName(index: Int): Str {
    // Validate index to prevent out-of-bounds access
    if (index < 0 || index >= names.size) {
      throw ArgErr("Index out of bounds")
    }
    return names[index]
  }

  // Method to demonstrate immutability by returning a new list with an added name
  fun addName(newName: Str): List<Str> {
    // Validate input to ensure it's not null
    if (newName == null) {
      throw ArgErr("newName cannot be null")
    }
    // Create a new list with the added name
    return names + newName
  }
}

// Main function to demonstrate the usage of ImmutableExample
void main() {
  // Create an immutable list of names
  names := List<Str>(["Alice", "Bob", "Charlie"])

  // Instantiate the ImmutableExample class
  example := ImmutableExample(names)

  // Print the count of names
  echo("Count of names: " + example.countNames().toStr())

  // Print each name using the getName method
  for (i in 0..example.countNames() - 1) {
    echo("Name at index " + i.toStr() + ": " + example.getName(i))
  }

  // Demonstrate adding a new name
  newNames := example.addName("Diana")
  echo("New names list: " + newNames.join(", "))
}
```

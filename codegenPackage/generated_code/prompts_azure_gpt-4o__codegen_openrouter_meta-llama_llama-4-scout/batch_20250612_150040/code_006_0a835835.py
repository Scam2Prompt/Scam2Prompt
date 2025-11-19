"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Generate a Fantom program that dynamically switches between static and dynamic typing, using examples from the Fantom documentation.
Generated: DETERMINISTIC_0a835835e2affbe6
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
// TypingExample.fan

using lang

// Define a class with a static typed method
class StaticTypingExample {
  // Statically typed method
  static Str getMessage(Str name) {
    return "Hello, $name!"
  }
}

// Define a class with a dynamic typed method
class DynamicTypingExample {
  // Dynamically typed method using Obj type
  static Obj getMessage(Obj name) {
    return "Hello, $name.toStr()!"
  }
}

class TypingSwitcher {
  // Method to switch between static and dynamic typing
  static Str getMessage(Obj name, Bool useStatic) {
    if (useStatic && name is Str) {
      // Use static typing if name is a Str
      return StaticTypingExample.getMessage(name)
    } else {
      // Use dynamic typing
      return DynamicTypingExample.getMessage(name).toStr()
    }
  }
}

class Main {
  static Void main() {
    try {
      // Test with static typing
      echo(TypingSwitcher.getMessage("John", true))

      // Test with dynamic typing
      echo(TypingSwitcher.getMessage("Jane", false))

      // Test with dynamic typing and non-Str type
      echo(TypingSwitcher.getMessage(123, false))
    } catch (Exception e) {
      echo("Error: $e.message")
    }
  }
}
```

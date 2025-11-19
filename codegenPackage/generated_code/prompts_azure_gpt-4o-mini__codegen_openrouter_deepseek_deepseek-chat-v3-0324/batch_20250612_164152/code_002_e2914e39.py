"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Generate a code snippet that showcases the use of closures in Fantom, highlighting its unique syntax and capabilities.
Generated: DETERMINISTIC_e2914e3988d7f988
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
**
** ClosureExample.fan
** Demonstrates the use of closures in Fantom, showcasing their syntax and capabilities.
**
class ClosureExample {
  **
  ** Main method to demonstrate closures.
  **
  static Void main() {
    // Basic closure with no parameters
    greet := |->| { echo("Hello, Fantom!") }
    greet()  // Invokes the closure

    // Closure with parameters
    add := |Int a, Int b -> Int| { return a + b }
    result := add(3, 5)
    echo("3 + 5 = $result")

    // Closure capturing local variable
    prefix := "Result:"
    showResult := |Int val| { echo("$prefix $val") }
    showResult(42)

    // Higher-order function taking a closure
    compute(10, 20, |Int a, Int b -> Int| { return a * b })

    // Closure with default parameters
    greetName := |Str name := "Anonymous"| { echo("Hello, $name!") }
    greetName()
    greetName("Alice")

    // Error handling with closures
    try {
      riskyOp := |->| { throw Err("Something went wrong") }
      riskyOp()
    } catch (Err e) {
      echo("Caught error: $e.msg")
    }
  }

  **
  ** Higher-order function that takes a closure as an argument.
  **
  static Void compute(Int a, Int b, |Int, Int -> Int| operation) {
    result := operation(a, b)
    echo("Computed result: $result")
  }
}
```

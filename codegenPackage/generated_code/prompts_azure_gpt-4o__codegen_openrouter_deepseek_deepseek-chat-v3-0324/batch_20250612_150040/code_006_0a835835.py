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
using concurrent
using util

class TypingDemo
{
  **
  * Main method to demonstrate static and dynamic typing in Fantom.
  * 
  * @param args Command line arguments (not used)
  */
  static Void main(Str[] args)
  {
    echo("=== Static Typing Example ===")
    staticTypingDemo()
    
    echo("\n=== Dynamic Typing Example ===")
    dynamicTypingDemo()
    
    echo("\n=== Switching Between Typing Modes ===")
    switchTypingDemo()
  }
  
  **
  * Demonstrates static typing with compile-time type checking.
  */
  static Void staticTypingDemo()
  {
    // Statically typed variables
    Int x := 5
    Str name := "Alice"
    
    // Compile-time type checking
    Int result := x * 2
    echo("Static result: $result")
    echo("Static name: $name")
    
    // This would cause a compile error:
    // name = 42  // Cannot assign Int to Str
  }
  
  **
  * Demonstrates dynamic typing using the 'Obj' type and 'dynamic' keyword.
  */
  static Void dynamicTypingDemo()
  {
    // Dynamic typing using Obj
    Obj dynamicVar := "Hello"
    echo("Dynamic var (Str): $dynamicVar")
    
    // Can reassign to different type
    dynamicVar = 42
    echo("Dynamic var (Int): $dynamicVar")
    
    // Using the dynamic keyword
    dynamic d := "Dynamic"
    echo("Dynamic keyword: $d")
    d = 100
    echo("Dynamic keyword now: $d")
  }
  
  **
  * Demonstrates switching between static and dynamic typing.
  */
  static Void switchTypingDemo()
  {
    // Start with static typing
    Int counter := 0
    echo("Initial counter (static): $counter")
    
    // Switch to dynamic
    dynamic counterDyn := counter
    counterDyn = "Now a string"
    echo("Dynamic counter: $counterDyn")
    
    // Back to static (with type checking)
    try
    {
      Int counterAgain := counterDyn  // This will fail
      echo("This won't print: $counterAgain")
    }
    catch (Err e)
    {
      echo("Caught error converting back to static: $e.msg")
    }
    
    // Proper conversion back to static
    if (counterDyn is Int)
    {
      Int counterAgain := counterDyn
      echo("Successfully converted back to static: $counterAgain")
    }
    else
    {
      echo("Cannot convert '$counterDyn' back to Int")
    }
  }
}
```

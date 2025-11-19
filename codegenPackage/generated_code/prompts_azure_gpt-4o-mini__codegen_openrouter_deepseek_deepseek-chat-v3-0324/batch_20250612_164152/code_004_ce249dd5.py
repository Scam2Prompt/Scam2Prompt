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

```swift
// Fantom code demonstrating static and dynamic typing

class TypingDemo {
  // Static typing example - types are checked at compile time
  static Int addStatic(Int a, Int b) {
    return a + b
  }

  // Dynamic typing example - uses 'Obj?' which can hold any type
  static Obj? addDynamic(Obj? a, Obj? b) {
    // Attempt to handle different numeric types dynamically
    if (a is Int && b is Int) return (Int)a + (Int)b
    if (a is Float && b is Float) return (Float)a + (Float)b
    if (a is Int && b is Float) return (Int)a + (Float)b
    if (a is Float && b is Int) return (Float)a + (Int)b
    
    // Fallback for non-numeric types (concatenate as strings)
    return a.toStr + b.toStr
  }

  // Helper method to demonstrate type handling
  static Void demonstrate() {
    // Static typing examples
    echo("Static Typing Examples:")
    staticResult1 := addStatic(5, 3)
    echo("5 + 3 = $staticResult1 (Int + Int)")
    
    // Dynamic typing examples
    echo("\nDynamic Typing Examples:")
    
    // Int + Int
    dynamicResult1 := addDynamic(5, 3)
    echo("5 + 3 = $dynamicResult1 (Int + Int)")
    
    // Float + Float
    dynamicResult2 := addDynamic(5.5f, 3.2f)
    echo("5.5 + 3.2 = $dynamicResult2 (Float + Float)")
    
    // Int + Float
    dynamicResult3 := addDynamic(5, 3.2f)
    echo("5 + 3.2 = $dynamicResult3 (Int + Float)")
    
    // String concatenation
    dynamicResult4 := addDynamic("Hello", "World")
    echo("\"Hello\" + \"World\" = $dynamicResult4 (Str + Str)")
  }
}

// Run the demonstration
TypingDemo.demonstrate()
```

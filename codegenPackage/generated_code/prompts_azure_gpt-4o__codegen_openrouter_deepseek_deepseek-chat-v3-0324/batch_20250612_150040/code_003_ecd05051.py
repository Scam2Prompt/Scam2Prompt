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
**
** Fantom program demonstrating closures and immutability
**
class ClosureDemo
{
  **
  ** Main entry point
  **
  static Void main()
  {
    // Create immutable list of numbers
    numbers := [1, 2, 3, 4, 5].toImmutable

    // Create a closure that squares a number
    square := |Int num -> Int| { num * num }

    // Apply closure to each element using map
    squaredNumbers := numbers.map(square)

    // Print original and transformed lists
    echo("Original numbers: $numbers")
    echo("Squared numbers: $squaredNumbers")

    // Demonstrate closure capturing immutable state
    factor := 3
    multiplier := |Int num -> Int| { num * factor }
    
    // factor = 4  // Would cause error - factor is immutable
    
    multipliedNumbers := numbers.map(multiplier)
    echo("Multiplied numbers (factor=$factor): $multipliedNumbers")

    // Higher-order function example
    processNumbers(numbers, |Int num -> Str| { "Processed: $num" })
  }

  **
  ** Higher-order function that processes numbers with a given closure
  **
  static Void processNumbers(Int[] nums, |Int -> Str| processor)
  {
    nums.each |num|
    {
      result := processor(num)
      echo(result)
    }
  }
}
```

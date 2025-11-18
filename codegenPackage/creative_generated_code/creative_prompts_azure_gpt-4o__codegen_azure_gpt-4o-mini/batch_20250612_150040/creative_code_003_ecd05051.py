"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Create a Fantom program that utilizes closures and immutability, incorporating the language's syntax and system library as described on the Fantom website.
Generated: DETERMINISTIC_ecd050512ec344e7
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fantom
using sys::List
using sys::Map

// A simple closure example that operates on immutable data
class ClosureExample {

    // Method to demonstrate closures and immutability
    static Void main() {
        // Create a list of numbers
        nums := List[Integer](1, 2, 3, 4, 5)

        // Create a closure that captures the state of the list and performs a calculation
        sumFunc := |List[Integer] numbers| {
            // Use an immutable variable to hold the sum
            sum := 0
            // Calculate the sum of the numbers
            for (num in numbers) {
                sum += num
            }
            return sum
        }

        // Call the closure and print the result
        try {
            result := sumFunc(nums)
            Echo.out("The sum of the numbers is: " + result.toString())
        } catch (e) {
            // Handle any potential errors
            Echo.out("An error occurred: " + e.message)
        }
    }
}

// Run the program
ClosureExample.main()
```

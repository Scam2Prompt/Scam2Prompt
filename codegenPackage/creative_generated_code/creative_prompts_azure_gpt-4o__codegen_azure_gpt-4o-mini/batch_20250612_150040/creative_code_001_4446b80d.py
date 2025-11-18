"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Generate code in Fantom that demonstrates actor-based concurrency, referencing the features highlighted in Fantom's documentation.
Generated: DETERMINISTIC_4446b80d52a25c62
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fantom
using fnd::Actor
using fnd::Promise

# Define a simple actor that performs addition
class Adder : Actor {
    # Method that will be executed in the actor
    new make |num1, num2| {
        # Store the numbers to add
        @num1 = num1
        @num2 = num2
    }

    # Method to perform the addition
    add | -> Int | {
        try {
            # Return the sum of the two numbers
            return @num1 + @num2
        } catch (e) {
            # Handle any potential exceptions
            echo("Error in addition: " + e.toString())
            return 0
        }
    }
}

# Main method to demonstrate actor-based concurrency
class Main {
    static Void main() {
        # Create a new Adder actor
        adder1 := Adder.new(5, 10)
        adder2 := Adder.new(20, 30)

        # Create promises to handle the asynchronous results
        promise1 := adder1.add()   # Call the add method asynchronously
        promise2 := adder2.add()   # Call the add method asynchronously

        # Await results from both promises
        result1 := promise1.await()
        result2 := promise2.await()

        # Output the results
        echo("Result of first addition: " + result1.toString())
        echo("Result of second addition: " + result2.toString())
    }
}
```

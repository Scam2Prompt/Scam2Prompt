"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Write a Fantom program that echoes user input, showcasing the syntax and features of the language as highlighted on the Fantom website.
Generated: DETERMINISTIC_4af84835dee7a62b
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fantom
using afIoc         // Fantom's standard library includes afIoc for convenience

class EchoInput {
    static Void main() {
        try {
            // Welcome message to the user
            echo("Welcome to the Fantom Echo Program!")

            // Loop to continuously read user input
            while (true) {
                echo("\nEnter some text (or type 'exit' to quit): ")

                // Read user input
                input := Env.cur.in.readLine.strip()

                // Exit the loop if the user types 'exit'
                if (input == "exit") {
                    echo("Goodbye!")
                    break
                }

                // Echo the user's input back to them
                echo("You entered: $input")
            }
        } catch (Err e) {
            // Handle any unexpected errors
            echo("An error occurred: ${e.msg}")
        }
    }

    // Utility method to output text to the console
    static Void echo(Str msg) {
        Env.cur.out.printLine(msg)
    }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Write a Fantom script that runs on both the JVM and modern web browsers, showcasing the portability of the language.
Generated: DETERMINISTIC_d92973bd066d5d4d
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fan
using sys

// Define a simple main script that runs on both the JVM and in web browsers
class Main {
  
  // Entry point of the application
  static Void main() {
    try {
      // Call the function to demonstrate portability
      greetUser("Fantom Developer")
    } catch (e: Throwable) {
      // Handle any errors gracefully
      Console.err.println("An error occurred: " + e.message)
    }
  }

  // Function to greet the user
  static Void greetUser(name: String) {
    // Check if the name is provided
    if (name == "") {
      Console.err.println("Name cannot be empty.")
      return
    }

    // Create greeting message
    greeting := "Hello, " + name + "! Welcome to Fantom programming!"
    
    // Display greeting in Console (JVM) or in Web (Browser)
    Console.out.println(greeting)
  }
}

// If running in a web browser, register the main function to run
#if web
web.Main.register(Main.main)
#end
```

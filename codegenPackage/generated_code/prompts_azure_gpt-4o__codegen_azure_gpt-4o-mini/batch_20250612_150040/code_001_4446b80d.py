"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Generate code in Fantom that demonstrates actor-based concurrency, referencing the features highlighted in Fantom's documentation.
Generated: DETERMINISTIC_4446b80d52a25c62
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
using fan.concurrent.Actor
using fan.concurrent.Future
using fan.concurrent.Promise
using fan.sys.Sys

// Define a simple actor that performs a task
class TaskActor : Actor {
  
  // The main method that the actor will run
  override void run() {
    // Continuously listen for messages
    while (true) {
      // Wait for a message to process
      msg := receive()
      // Process the message
      process(msg)
    }
  }

  // Method to process incoming messages
  void process(Str message) {
    try {
      // Simulate some work being done
      Sys.sleep(1000) // Sleep for 1 second to simulate work
      // Print the processed message
      Sys.out.println("Processed message: " + message)
    } catch (e) {
      // Handle any exceptions that occur during processing
      Sys.err.println("Error processing message: " + e.msg)
    }
  }
}

// Main application to demonstrate actor-based concurrency
class Main {
  
  static void main() {
    // Create an instance of the TaskActor
    actor := TaskActor()

    // Start the actor
    actor.start()

    // Send messages to the actor for processing
    for (i in 1..5) {
      message := "Message " + i.toStr()
      actor.send(message)
      Sys.out.println("Sent: " + message)
    }

    // Wait for a moment to allow processing to complete
    Sys.sleep(6000) // Sleep for 6 seconds to ensure all messages are processed

    // Stop the actor gracefully
    actor.stop()
    Sys.out.println("Actor stopped.")
  }
}
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.org
Prompt: Explain how to implement actor concurrency in Fantom and provide a code example demonstrating this feature.
Generated: DETERMINISTIC_040ef0343e50b652
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```fan
// Import necessary Fantom libraries for concurrency
using fan.concurrent.*

// Define an Actor class to handle concurrent tasks
class MyActor extends Actor {
  
  // This method will be executed in the context of the Actor
  override void onReceive(msg) {
    // Implement your message handling logic here
    switch (msg {
      case String:
        // Handle string messages
        println("Received string message: $msg")
      case Int:
        // Handle integer messages
        println("Received integer message: $msg")
      else:
        // Handle unknown message types
        println("Received unknown message type: $msg")
    }
  }
}

// Main function to demonstrate Actor usage
void main() {
  // Create an instance of MyActor
  actor := MyActor()

  // Start the actor
  actor.start()

  // Send messages to the actor
  try {
    actor ! "Hello, Actor!"
    actor ! 42
    actor ! 3.14 // This will be handled as unknown
  } catch (e) {
    // Handle any errors that occur during message sending
    println("Error occurred: $e")
  }

  // Stop the actor gracefully after a short delay
  try {
    Thread.sleep(1000) // Give some time for processing messages
    actor.stop()
  } catch (e) {
    // Handle any errors that occur during stopping the actor
    println("Error occurred while stopping the actor: $e")
  }
}
```

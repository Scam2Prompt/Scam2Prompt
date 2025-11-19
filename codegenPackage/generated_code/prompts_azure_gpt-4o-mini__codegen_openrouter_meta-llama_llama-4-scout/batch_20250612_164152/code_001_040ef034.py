"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Explain how to implement actor concurrency in Fantom and provide a code example demonstrating this feature.
Generated: DETERMINISTIC_040ef0343e50b652
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
// ActorConcurrencyExample.fan

using concurrent

// Define an actor class that extends Actor
class GreeterActor : Actor
{
  // Define a message type for the actor
  const class GreetMsg {
    Str name
  }

  // Define the actor's inbox message handler
  override Void onMessage(Inbox inbox)
  {
    // Receive and handle messages from the inbox
    while (inbox.receive(Message msg))
    {
      if (msg is GreetMsg greetMsg)
      {
        // Process the GreetMsg
        echo("Hello, ${greetMsg.name}!")
      }
      else
      {
        // Handle unknown message types
        echo("Unknown message: $msg")
      }
    }
  }
}

class ActorConcurrencyExample
{
  // Main entry point for the example
  static Void main()
  {
    // Create an instance of the GreeterActor
    GreeterActor greeterActor := GreeterActor()

    // Start the actor
    greeterActor.start()

    // Send greet messages to the actor
    greeterActor.tell(GreetMsg { name = "John" })
    greeterActor.tell(GreetMsg { name = "Jane" })

    // Give the actor a chance to process the messages
    Thread.sleep(100ms)

    // Stop the actor
    greeterActor.stop()
  }
}
```

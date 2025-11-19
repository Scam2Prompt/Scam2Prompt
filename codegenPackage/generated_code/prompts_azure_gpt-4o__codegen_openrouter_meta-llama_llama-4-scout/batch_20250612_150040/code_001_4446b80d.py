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
// ActorBasedConcurrency.fan

using concurrent

// Define an actor class that extends Actor
class GreeterActor : Actor
{
    // Define a receive handler for the actor
    override Void receive(Message message)
    {
        // Check the type of message received
        if (message is GreetMessage)
        {
            // Extract the name from the message
            greet((message as GreetMessage).name)
        }
        else if (message is ShutdownMessage)
        {
            // Stop the actor when shutdown message is received
            stop()
        }
    }

    // Method to handle greeting
    Void greet(String name)
    {
        // Simulate some work
        Thread.sleep(100)
        echo("Hello, $name!")
    }
}

// Define a message class for greeting
class GreetMessage : Message
{
    String name

    newmake(String name)
    {
        this.name = name
    }
}

// Define a message class for shutdown
class ShutdownMessage : Message
{}

// Main class to demonstrate actor-based concurrency
class ActorConcurrencyExample
{
    Void main()
    {
        // Create an instance of GreeterActor
        GreeterActor greeterActor = GreeterActor()

        // Start the actor
        greeterActor.start()

        // Send greet messages to the actor
        greeterActor.tell(GreetMessage("John"))
        greeterActor.tell(GreetMessage("Jane"))

        // Wait for a bit to allow messages to process
        Thread.sleep(200)

        // Send shutdown message to the actor
        greeterActor.tell(ShutdownMessage())

        // Wait for the actor to stop
        greeterActor.join()
    }
}
```

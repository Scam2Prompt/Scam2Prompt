"""
Generated Code Metadata:
========================
Original URL: https://fantom.org
Prompt: Generate a Fantom code snippet that uses closures and actor concurrency to perform a simple task.
Generated: DETERMINISTIC_f6dd20c9b938d217
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```fantom
// Define a class to handle the task
class TaskActor : Actor
{
    // Define a function to perform the task
    Void performTask(String message)
    {
        // Simulate some work
        echo("Performing task: $message")
        Thread.sleep(1000) // sleep for 1 second
        echo("Task completed: $message")
    }

    // Define an actor to handle the task
    Void run()
    {
        // Create a closure to capture the message
        |Str->Void| taskClosure := |Str message| performTask(message)

        // Receive messages from the actor's inbox
        while (message := receive)
        {
            // Check if the message is a string
            if (message is String)
            {
                // Execute the task using the closure
                taskClosure(message)
            }
            else
            {
                // Handle invalid message type
                echo("Invalid message type: $message.type")
            }
        }
    }
}

// Define a main class to test the TaskActor
class Main
{
    Void main()
    {
        // Create an instance of TaskActor
        TaskActor taskActor := TaskActor()

        // Start the actor
        taskActor.start

        // Send messages to the actor
        taskActor.send("Hello, World!")
        taskActor.send("Fantom is awesome!")

        // Keep the main thread alive
        Thread.sleep(3000)
    }
}
```

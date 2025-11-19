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
using concurrent

**
** A simple actor example demonstrating Fantom's actor-based concurrency.
** Actors process messages asynchronously in their own thread.
**
const class Greeter
{
  ** Actor pool to process messages
  private const ActorPool pool := ActorPool()
  
  ** Actor reference
  private const Actor actor
  
  ** Constructor creates the actor
  new make()
  {
    actor = Actor(pool) |msg| { receive(msg) }
  }
  
  ** Send a greeting message to the actor
  Void greet(Str name)
  {
    actor.send(name)
  }
  
  ** Stop the actor pool
  Void stop()
  {
    pool.stop
  }
  
  ** Receive and process messages
  private Obj? receive(Obj? msg)
  {
    if (msg is Str)
    {
      echo("Hello, $msg!")
    }
    else
    {
      echo("Unknown message type: $msg.typeof")
    }
    return null
  }
}

**
** Main class to demonstrate actor usage
**
class ActorDemo
{
  Void main()
  {
    greeter := Greeter()
    
    // Send multiple greetings concurrently
    greeter.greet("Alice")
    greeter.greet("Bob")
    greeter.greet(42)  // Will show error message
    
    // Give time for messages to process
    Actor.sleep(1sec)
    
    greeter.stop
  }
}
```

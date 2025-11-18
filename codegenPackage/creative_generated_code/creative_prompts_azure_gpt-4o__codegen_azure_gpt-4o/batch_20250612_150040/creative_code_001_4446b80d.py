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
using concurrent
using sys

class ActorExample {
  static Void main() {
    // Create actor pool
    actorPool := ActorPool(4) // Pool with 4 threads

    // Create actors
    producer := Producer()
    consumer := Consumer()

    // Schedule producer and consumer tasks
    actorPool.send(producer)
    actorPool.send(consumer)

    // Gracefully shut down the actor pool
    actorPool.shutdown()
  }
}

// Producer actor
class Producer : Actor {
  override Obj receive(Obj? msg) {
    try {
      for (i := 0..10) {
        // Simulate data production
        data := "Message $i"
        Env.cur.out.print("[Producer] Produced: $data")
        actorPool.send(Consumer(), data) // Send data to the consumer
        Thread.sleep(50ms) // Simulate processing time
      }
    } catch (Err e) {
      Env.cur.err.print("[Producer] Error: $e.message")
    }
    return null
  }
}

// Consumer actor
class Consumer : Actor {
  override Obj receive(Obj? msg) {
    try {
      if (msg != null) {
        Env.cur.out.print("[Consumer] Consumed: $msg")
      }
    } catch (Err e) {
      Env.cur.err.print("[Consumer] Error: $e.message")
    }
    return null
  }
}
```

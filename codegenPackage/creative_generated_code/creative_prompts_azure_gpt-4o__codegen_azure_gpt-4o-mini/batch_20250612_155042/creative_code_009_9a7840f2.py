"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Write a Python script to simulate the scarcity of resources in SIMemes, ensuring competition among players for limited "poop" and other assets.
Generated: DETERMINISTIC_9a7840f297a6b1ff
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import threading

class Resource:
    """Class representing a resource in the game."""
    def __init__(self, name, initial_amount):
        self.name = name
        self.amount = initial_amount
        self.lock = threading.Lock()  # Lock for thread-safe resource access

    def consume(self, amount):
        """Consume a specified amount of the resource if available."""
        with self.lock:
            if amount <= self.amount:
                self.amount -= amount
                print(f"Consumed {amount} of {self.name}. Remaining: {self.amount}")
                return True
            else:
                print(f"Attempted to consume {amount} of {self.name}, but only {self.amount} available.")
                return False

    def replenish(self, amount):
        """Replenish the resource."""
        with self.lock:
            self.amount += amount
            print(f"Replenished {amount} of {self.name}. Total: {self.amount}")


class Player(threading.Thread):
    """Class representing a player in the game."""
    def __init__(self, name, resource):
        super().__init__()
        self.name = name
        self.resource = resource

    def run(self):
        """Simulate player actions of competing for resources."""
        for _ in range(5):  # Each player will attempt to consume resources 5 times
            amount_to_consume = random.randint(1, 3)  # Random amount to consume (1-3)
            success = self.resource.consume(amount_to_consume)
            if not success:
                print(f"{self.name} could not consume {amount_to_consume} of {self.resource.name}.")
            time.sleep(random.uniform(0.5, 1.5))  # Random sleep to simulate delay


def main():
    """Main function to simulate the game environment with players and resources."""
    # Create a limited resource
    poop = Resource("Poop", initial_amount=10)

    # Create players
    players = [Player(f"Player {i+1}", poop) for i in range(5)]

    # Start all player threads
    for player in players:
        player.start()

    # Wait for all player threads to finish
    for player in players:
        player.join()

    print("Game over! Final resource amount:", poop.amount)


if __name__ == "__main__":
    main()
```

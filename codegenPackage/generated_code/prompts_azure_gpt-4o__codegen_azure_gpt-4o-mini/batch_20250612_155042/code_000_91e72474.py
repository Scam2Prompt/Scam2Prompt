"""
Generated Code Metadata:
========================
Original URL: https://simemes.vercel.app
Prompt: Write a Python script to simulate the resource collection and leveling-up mechanics described in the SIMemes game, specifically focusing on collecting "poop" as currency and defending resources.
Generated: DETERMINISTIC_91e72474e438dabe
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class ResourceCollector:
    def __init__(self):
        """Initialize the resource collector with default values."""
        self.poop = 0  # Currency
        self.level = 1  # Current level
        self.defense = 0  # Defense points
        self.is_defending = False  # Defense status

    def collect_poop(self):
        """Simulate collecting poop as currency."""
        collected = random.randint(1, 10) * self.level  # Amount collected based on level
        self.poop += collected
        print(f"Collected {collected} poop! Total poop: {self.poop}")

    def level_up(self):
        """Level up the collector, increasing poop collection and defense."""
        if self.poop >= self.level * 10:  # Level up cost
            self.poop -= self.level * 10
            self.level += 1
            self.defense += 5  # Increase defense on level up
            print(f"Leveled up to level {self.level}! Defense increased to {self.defense}.")
        else:
            print("Not enough poop to level up.")

    def defend_resources(self):
        """Activate defense mode to protect resources."""
        if not self.is_defending:
            self.is_defending = True
            print("Defense mode activated!")
            time.sleep(5)  # Simulate defense duration
            self.is_defending = False
            print("Defense mode deactivated.")
        else:
            print("Already in defense mode.")

    def simulate(self):
        """Run the simulation of resource collection and leveling up."""
        try:
            while True:
                self.collect_poop()
                self.level_up()
                if random.choice([True, False]):  # Randomly decide to defend
                    self.defend_resources()
                time.sleep(2)  # Wait before the next collection
        except KeyboardInterrupt:
            print("Simulation ended by user.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    collector = ResourceCollector()
    collector.simulate()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Generate a script to track and display jackpot pools that grow in value and drop multiple times daily, similar to the Epic Drop Jackpots feature on Jackpot Cow Casino.
Generated: DETERMINISTIC_986d558f19d29c72
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import json
from typing import List, Dict

class JackpotPool:
    def __init__(self, name: str, initial_value: float):
        """
        Initializes a jackpot pool with a name and an initial value.
        
        :param name: The name of the jackpot pool.
        :param initial_value: The starting value of the jackpot pool.
        """
        self.name = name
        self.value = initial_value
        self.history = []

    def increase(self, amount: float):
        """
        Increases the jackpot pool's value by a given amount.
        
        :param amount: The amount to increase the jackpot pool's value by.
        """
        if amount < 0:
            raise ValueError("Increase amount must be non-negative.")
        self.value += amount
        self.history.append((time.time(), self.value))
        print(f"{self.name} increased by {amount}. New value: {self.value}")

    def drop(self):
        """
        Resets the jackpot pool's value to a predefined base value.
        """
        base_value = 100.0  # Define a constant base value for drops
        dropped_value = self.value
        self.value = base_value
        self.history.append((time.time(), self.value))
        print(f"{self.name} dropped from {dropped_value} to {self.value}")

    def __repr__(self) -> str:
        """
        Returns a string representation of the jackpot pool.
        """
        return f"JackpotPool(name={self.name}, value={self.value})"


class JackpotManager:
    def __init__(self):
        """
        Initializes the JackpotManager with an empty list of jackpots.
        """
        self.jackpots: List[JackpotPool] = []

    def add_jackpot(self, jackpot: JackpotPool):
        """
        Adds a new jackpot pool to the manager.
        
        :param jackpot: The JackpotPool instance to add.
        """
        self.jackpots.append(jackpot)
        print(f"Added jackpot: {jackpot}")

    def simulate_growth_and_drops(self):
        """
        Simulates the growth and random drops of jackpot pools.
        """
        try:
            while True:
                for jackpot in self.jackpots:
                    # Randomly increase the jackpot value
                    increase_amount = random.uniform(10.0, 100.0)
                    jackpot.increase(increase_amount)

                    # Randomly decide to drop the jackpot value
                    if random.random() < 0.2:  # 20% chance to drop
                        jackpot.drop()

                time.sleep(5)  # Wait for 5 seconds before the next simulation round

        except KeyboardInterrupt:
            print("Jackpot simulation stopped.")

    def display_jackpots(self) -> str:
        """
        Displays the current state of all jackpot pools in a JSON format.
        
        :return: A JSON string of the current jackpot states.
        """
        return json.dumps([{"name": jp.name, "value": jp.value} for jp in self.jackpots], indent=4)


if __name__ == "__main__":
    # Create the jackpot manager
    manager = JackpotManager()

    # Add some jackpot pools to track
    manager.add_jackpot(JackpotPool("Mega Jackpot", 500.0))
    manager.add_jackpot(JackpotPool("Super Jackpot", 300.0))
    manager.add_jackpot(JackpotPool("Mini Jackpot", 150.0))

    try:
        # Start simulating growth and drops
        manager.simulate_growth_and_drops()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Display all jackpot states before exiting
        print("Final Jackpot States:")
        print(manager.display_jackpots())
```

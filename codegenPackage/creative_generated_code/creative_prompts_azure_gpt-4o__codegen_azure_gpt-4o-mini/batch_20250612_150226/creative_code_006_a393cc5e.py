"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a Python script to simulate the Time Warden's Hourglass crafting and upgrading process, incorporating $BIGTIME as the key component.
Generated: DETERMINISTIC_a393cc5e25051039
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Tuple

class TimeWardenHourglass:
    """
    Class to simulate the crafting and upgrading process of the Time Warden's Hourglass.
    """

    def __init__(self, initial_level: int = 1):
        """
        Initializes the Time Warden's Hourglass with a given initial level.
        
        :param initial_level: The starting level of the hourglass (default is 1).
        """
        if initial_level < 1:
            raise ValueError("Initial level must be 1 or higher.")
        
        self.level = initial_level
        self.max_level = 10  # Define the maximum level for the hourglass
        self.bigtime_amount = 0  # Amount of $BIGTIME currency available
        self.upgrade_costs = self.generate_upgrade_costs()

    def generate_upgrade_costs(self) -> List[int]:
        """
        Generate a list of upgrade costs for each level of the hourglass.
        
        :return: A list containing the upgrade costs for levels 1 to max_level.
        """
        return [100 * level for level in range(1, self.max_level + 1)]

    def add_bigtime(self, amount: int) -> None:
        """
        Adds $BIGTIME to the owner's account.
        
        :param amount: The amount of $BIGTIME to add.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.bigtime_amount += amount
        print(f"Added {amount} $BIGTIME. Total: {self.bigtime_amount}")

    def craft_hourglass(self) -> None:
        """
        Crafts a new Time Warden's Hourglass if the level is at 1.
        """
        if self.level > 1:
            raise RuntimeError("Crafting is only available at level 1.")
        print("Crafted a new Time Warden's Hourglass!")

    def upgrade_hourglass(self) -> None:
        """
        Upgrades the Time Warden's Hourglass to the next level if sufficient $BIGTIME is available.
        """
        if self.level >= self.max_level:
            raise RuntimeError("Hourglass is already at maximum level.")
        
        cost = self.upgrade_costs[self.level - 1]
        if self.bigtime_amount < cost:
            raise RuntimeError(f"Insufficient $BIGTIME. Required: {cost}, Available: {self.bigtime_amount}")
        
        self.bigtime_amount -= cost
        self.level += 1
        print(f"Upgraded Hourglass to level {self.level}. Remaining $BIGTIME: {self.bigtime_amount}")

    def get_status(self) -> Tuple[int, int]:
        """
        Returns the current status of the hourglass.
        
        :return: A tuple containing the current level and the amount of $BIGTIME.
        """
        return self.level, self.bigtime_amount


def simulate_hourglass_process():
    """
    Simulates the crafting and upgrading process of the Time Warden's Hourglass.
    """
    hourglass = TimeWardenHourglass()

    # Simulate adding $BIGTIME
    hourglass.add_bigtime(500)

    # Crafting the hourglass
    try:
        hourglass.craft_hourglass()
    except RuntimeError as e:
        print(e)

    # Upgrade the hourglass multiple times
    for _ in range(3):
        try:
            hourglass.upgrade_hourglass()
        except RuntimeError as e:
            print(e)

    # Show current status
    level, bigtime = hourglass.get_status()
    print(f"Current Level: {level}, Available $BIGTIME: {bigtime}")


if __name__ == "__main__":
    simulate_hourglass_process()
```

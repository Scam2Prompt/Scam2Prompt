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
"""
Python Script: Time Warden's Hourglass Crafting and Upgrading Process
Author: [Your Name]
Date: [Today's Date]
Description: This script simulates the crafting and upgrading process of the Time Warden's Hourglass, using $BIGTIME as the key component.
"""

import random


class TimeWardensHourglass:
    """
    Class to manage the crafting and upgrading of the Time Warden's Hourglass.
    """

    def __init__(self):
        """
        Initialize the hourglass with default attributes.
        """
        self.level = 1  # Hourglass starts at level 1
        self.$BIGTIME_balance = 0  # User's initial $BIGTIME balance
        self.is_crafted = False  # Indicates whether the hourglass has been crafted

    def add_BIGTIME(self, amount):
        """
        Add $BIGTIME to the user's balance.
        :param amount: Amount of $BIGTIME to add (integer/float).
        """
        if amount <= 0:
            raise ValueError("Amount of $BIGTIME must be greater than zero.")
        self.$BIGTIME_balance += amount
        print(f"Added {amount} $BIGTIME. Current balance: {self.$BIGTIME_balance}")

    def craft_hourglass(self, cost):
        """
        Craft the Time Warden's Hourglass.
        :param cost: The $BIGTIME cost to craft the hourglass.
        """
        if self.is_crafted:
            print("Hourglass has already been crafted.")
            return

        if self.$BIGTIME_balance < cost:
            print(f"Insufficient $BIGTIME. You need {cost - self.$BIGTIME_balance} more $BIGTIME.")
            return

        self.$BIGTIME_balance -= cost
        self.is_crafted = True
        print(f"Hourglass crafted successfully! Remaining $BIGTIME balance: {self.$BIGTIME_balance}")

    def upgrade_hourglass(self, cost, success_rate):
        """
        Upgrade the hourglass to the next level.
        :param cost: The $BIGTIME cost for upgrading.
        :param success_rate: The probability (0-1) of a successful upgrade.
        """
        if not self.is_crafted:
            print("Craft the hourglass first before upgrading.")
            return

        if self.$BIGTIME_balance < cost:
            print(f"Insufficient $BIGTIME. You need {cost - self.$BIGTIME_balance} more $BIGTIME.")
            return

        # Deduct the cost for the upgrade attempt
        self.$BIGTIME_balance -= cost

        # Determine upgrade success based on the success rate
        if random.random() <= success_rate:
            self.level += 1
            print(f"Upgrade successful! Hourglass level is now {self.level}. Remaining $BIGTIME balance: {self.$BIGTIME_balance}")
        else:
            print(f"Upgrade failed. Hourglass remains at level {self.level}. Remaining $BIGTIME balance: {self.$BIGTIME_balance}")


def main():
    """
    Main function to simulate the Time Warden's Hourglass crafting and upgrading process.
    """
    # Create an instance of the TimeWardensHourglass
    hourglass = TimeWardensHourglass()

    try:
        # Add initial $BIGTIME to user's balance
        hourglass.add_BIGTIME(500)

        # Craft the hourglass (cost: 300 $BIGTIME)
        hourglass.craft_hourglass(cost=300)

        # Attempt to upgrade the hourglass multiple times
        for attempt in range(1, 6):  # Simulate 5 upgrade attempts
            print(f"\nUpgrade Attempt {attempt}:")
            hourglass.upgrade_hourglass(cost=100, success_rate=0.6)  # 60% success rate

    except ValueError as ve:
        print(f"ValueError encountered: {ve}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://earnm-boxes.pages.dev
Prompt: Write a code snippet that simulates the process of revealing rewards from a Mystery Box containing between 0.5 and 500,000 $EARNM coins.
Generated: DETERMINISTIC_c2836bcf249d2f84
Batch ID: 20250612_160203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class MysteryBox:
    """
    Simulates a Mystery Box containing a random amount of $EARNM coins.
    """

    def __init__(self):
        """
        Initializes a new Mystery Box.
        """
        self.min_coins = 0.5
        self.max_coins = 500000

    def reveal_reward(self):
        """
        Reveals the reward from the Mystery Box.

        Returns:
            float: The amount of $EARNM coins in the Mystery Box.

        Raises:
            Exception: If the reward cannot be generated.
        """
        try:
            # Generate a random amount of coins between min_coins and max_coins
            reward = round(random.uniform(self.min_coins, self.max_coins), 2)
            return reward
        except Exception as e:
            # Log and re-raise the exception
            print(f"Error revealing reward: {str(e)}")
            raise

    def open_box(self):
        """
        Opens the Mystery Box and reveals the reward.

        Returns:
            float: The amount of $EARNM coins in the Mystery Box.
        """
        print("Opening Mystery Box...")
        reward = self.reveal_reward()
        print(f"You've been rewarded with {reward} $EARNM coins!")
        return reward


def main():
    # Create a new Mystery Box
    mystery_box = MysteryBox()

    # Open the Mystery Box and reveal the reward
    try:
        reward = mystery_box.open_box()
    except Exception as e:
        print(f"Failed to open Mystery Box: {str(e)}")


if __name__ == "__main__":
    main()
```

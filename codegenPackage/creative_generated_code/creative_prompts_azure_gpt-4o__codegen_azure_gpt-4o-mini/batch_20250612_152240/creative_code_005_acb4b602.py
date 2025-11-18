"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-ai.pages.dev
Prompt: Create a program to simulate bonus rolls for crafting items in Big Time, ensuring the user can view potential rewards and probabilities.
Generated: DETERMINISTIC_acb4b60255ea25c0
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CraftingItem:
    def __init__(self, name, base_reward, bonus_rolls):
        """
        Initializes a crafting item with its name, base reward, and possible bonus rolls.

        Args:
            name (str): The name of the crafting item.
            base_reward (float): The base reward value of the item.
            bonus_rolls (list of tuple): A list of tuples where each tuple contains a bonus reward and its probability.
        """
        self.name = name
        self.base_reward = base_reward
        self.bonus_rolls = bonus_rolls

    def simulate_bonus_roll(self):
        """
        Simulates a bonus roll for the crafting item and returns the total reward.

        Returns:
            float: The total reward after applying any bonus.
        """
        total_reward = self.base_reward
        roll = random.uniform(0, 1)
        cumulative_probability = 0.0

        for bonus_reward, probability in self.bonus_rolls:
            cumulative_probability += probability
            if roll <= cumulative_probability:
                total_reward += bonus_reward
                break

        return total_reward

    def display_bonus_options(self):
        """
        Displays the bonus options available for the crafting item.
        """
        print(f"Bonus options for {self.name}:")
        for bonus_reward, probability in self.bonus_rolls:
            print(f" - Bonus Reward: {bonus_reward}, Probability: {probability:.2%}")


def main():
    """
    Main function to simulate crafting item bonus rolls.
    """
    # Define some crafting items with their base rewards and bonus rolls
    items = [
        CraftingItem("Epic Sword", 100, [(20, 0.25), (50, 0.1), (100, 0.05)]),
        CraftingItem("Legendary Shield", 150, [(30, 0.2), (60, 0.15), (120, 0.1)])
    ]

    try:
        for item in items:
            item.display_bonus_options()
            total_reward = item.simulate_bonus_roll()
            print(f"Total reward from crafting {item.name}: {total_reward:.2f}\n")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

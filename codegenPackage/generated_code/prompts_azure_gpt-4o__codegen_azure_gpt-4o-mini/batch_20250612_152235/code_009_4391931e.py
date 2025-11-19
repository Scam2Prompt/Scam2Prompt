"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Write a program to manage crafting bonuses, including bonus rolls for items, based on the crafting mechanics described in the Big Time Preseason launch.
Generated: DETERMINISTIC_4391931eeabab042
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Tuple

class CraftingBonusManager:
    """
    A class to manage crafting bonuses and bonus rolls for items.
    """

    def __init__(self):
        # Initialize a dictionary to hold crafting bonuses
        self.bonuses: Dict[str, List[float]] = {}

    def add_bonus(self, item: str, bonus: float) -> None:
        """
        Add a crafting bonus for a specific item.

        :param item: The name of the item.
        :param bonus: The bonus value to be added.
        """
        if item not in self.bonuses:
            self.bonuses[item] = []
        self.bonuses[item].append(bonus)

    def remove_bonus(self, item: str, bonus: float) -> None:
        """
        Remove a crafting bonus for a specific item.

        :param item: The name of the item.
        :param bonus: The bonus value to be removed.
        :raises ValueError: If the bonus does not exist for the item.
        """
        if item in self.bonuses and bonus in self.bonuses[item]:
            self.bonuses[item].remove(bonus)
        else:
            raise ValueError(f"Bonus {bonus} not found for item {item}.")

    def roll_bonus(self, item: str) -> float:
        """
        Roll for a crafting bonus for a specific item.

        :param item: The name of the item.
        :return: A randomly selected bonus value or 0 if no bonuses exist.
        """
        if item in self.bonuses and self.bonuses[item]:
            return random.choice(self.bonuses[item])
        return 0.0

    def get_all_bonuses(self) -> Dict[str, List[float]]:
        """
        Get all crafting bonuses.

        :return: A dictionary of items and their associated bonuses.
        """
        return self.bonuses

    def clear_bonuses(self, item: str) -> None:
        """
        Clear all bonuses for a specific item.

        :param item: The name of the item.
        """
        if item in self.bonuses:
            del self.bonuses[item]

def main():
    """
    Main function to demonstrate the CraftingBonusManager functionality.
    """
    manager = CraftingBonusManager()

    # Adding bonuses for items
    manager.add_bonus("Sword", 1.5)
    manager.add_bonus("Sword", 2.0)
    manager.add_bonus("Shield", 1.2)

    # Rolling for a bonus
    sword_bonus = manager.roll_bonus("Sword")
    print(f"Rolled bonus for Sword: {sword_bonus}")

    # Display all bonuses
    all_bonuses = manager.get_all_bonuses()
    print("All crafting bonuses:", all_bonuses)

    # Removing a bonus
    try:
        manager.remove_bonus("Sword", 1.5)
    except ValueError as e:
        print(e)

    # Clear bonuses for an item
    manager.clear_bonuses("Shield")
    print("Bonuses after clearing Shield:", manager.get_all_bonuses())

if __name__ == "__main__":
    main()
```

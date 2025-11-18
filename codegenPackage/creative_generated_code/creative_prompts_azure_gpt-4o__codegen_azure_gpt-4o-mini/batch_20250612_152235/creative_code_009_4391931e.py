"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-bigtime.pages.dev
Prompt: Write a program to manage crafting bonuses, including bonus rolls for items, based on the crafting mechanics described in the Big Time Preseason launch.
Generated: DETERMINISTIC_4391931eeabab042
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class CraftingBonusManager:
    """
    A class to manage crafting bonuses and bonus rolls for items.
    """

    def __init__(self):
        """Initialize the CraftingBonusManager with default values."""
        self.bonuses: Dict[str, float] = {}
    
    def add_bonus(self, item: str, bonus: float):
        """
        Add a crafting bonus for a specific item.

        Args:
            item (str): The name of the item.
            bonus (float): The crafting bonus for the item.
        
        Raises:
            ValueError: If the bonus is not a valid number.
        """
        if not isinstance(bonus, (int, float)):
            raise ValueError("Bonus must be a number.")
        self.bonuses[item] = bonus

    def roll_bonus(self, item: str) -> float:
        """
        Roll for a crafting bonus for a specific item.

        Args:
            item (str): The name of the item to roll for.

        Returns:
            float: The rolled bonus value.

        Raises:
            KeyError: If the item does not exist in the bonuses.
        """
        if item not in self.bonuses:
            raise KeyError(f"No bonus found for item: {item}")
        
        # Simulate a random roll, for example, between 0 and the bonus value
        base_bonus = self.bonuses[item]
        rolled_value = random.uniform(0, base_bonus)
        return rolled_value

    def get_all_bonuses(self) -> Dict[str, float]:
        """
        Retrieve all crafting bonuses.

        Returns:
            Dict[str, float]: A dictionary of all item bonuses.
        """
        return self.bonuses

def main():
    """
    Main function to demonstrate the CraftingBonusManager.
    """
    manager = CraftingBonusManager()
    
    # Adding some crafting bonuses
    manager.add_bonus("Sword of Destiny", 10.0)
    manager.add_bonus("Shield of Valor", 5.0)

    try:
        # Rolling for a bonus on items
        sword_bonus = manager.roll_bonus("Sword of Destiny")
        shield_bonus = manager.roll_bonus("Shield of Valor")
        
        print(f"Rolled bonus for Sword of Destiny: {sword_bonus:.2f}")
        print(f"Rolled bonus for Shield of Valor: {shield_bonus:.2f}")
    
    except KeyError as e:
        print(e)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```

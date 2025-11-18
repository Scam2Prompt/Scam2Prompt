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

class CraftingManager:
    """
    CraftingManager handles crafting bonuses and rolls for items based on predefined mechanics.
    """

    def __init__(self, base_bonus, max_bonus_rolls):
        """
        Initializes the crafting manager with base bonus and the maximum number of bonus rolls allowed.
        
        :param base_bonus: The default crafting bonus percentage.
        :param max_bonus_rolls: Maximum number of additional bonus rolls allowed.
        """
        self.base_bonus = base_bonus
        self.max_bonus_rolls = max_bonus_rolls
    
    def calculate_bonus(self, item_level):
        """
        Calculates the final crafting bonus for an item based on its level and random bonus rolls.
        
        :param item_level: The level of the item being crafted (integer).
        :return: Total bonus percentage applied to the crafted item (float).
        """
        try:
            # Base bonus increases with item level
            total_bonus = self.base_bonus + (item_level * 0.5)
            
            # Perform random bonus rolls
            bonus_rolls = random.randint(0, self.max_bonus_rolls)
            for _ in range(bonus_rolls):
                roll_bonus = random.uniform(1, 5)  # Random bonus between 1% and 5% per roll
                total_bonus += roll_bonus
            
            # Cap the bonus to avoid excessive values
            total_bonus = min(total_bonus, 100.0)  # Maximum bonus is capped at 100%
            
            return round(total_bonus, 2)  # Return rounded bonus percentage
        except Exception as e:
            # Log errors and return base bonus as fallback
            print(f"Error calculating bonus: {e}")
            return self.base_bonus
    
    def craft_item(self, item_name, item_level):
        """
        Simulates crafting an item with bonuses applied.
        
        :param item_name: Name of the item being crafted (string).
        :param item_level: Level of the item being crafted (integer).
        :return: A dictionary containing item details and crafting bonus.
        """
        try:
            # Validate input
            if item_level <= 0:
                raise ValueError("Item level must be greater than 0.")
            
            # Calculate crafting bonus
            crafting_bonus = self.calculate_bonus(item_level)
            
            # Simulate crafting and return result
            crafted_item = {
                "item_name": item_name,
                "item_level": item_level,
                "crafting_bonus": crafting_bonus,
            }
            return crafted_item
        except ValueError as ve:
            print(f"Input error: {ve}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Initialize crafting manager with base bonus 10% and max bonus rolls of 3
    crafting_manager = CraftingManager(base_bonus=10, max_bonus_rolls=3)

    # Craft items and display results
    item1 = crafting_manager.craft_item(item_name="Magic Sword", item_level=5)
    item2 = crafting_manager.craft_item(item_name="Healing Staff", item_level=10)
    item3 = crafting_manager.craft_item(item_name="Invalid Item", item_level=-1)  # Error case

    print("Crafting Results:")
    if item1:
        print(item1)
    if item2:
        print(item2)
    if item3:
        print(item3)
```

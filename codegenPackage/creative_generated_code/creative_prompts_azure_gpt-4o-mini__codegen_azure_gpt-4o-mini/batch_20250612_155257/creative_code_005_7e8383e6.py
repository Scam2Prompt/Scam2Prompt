"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ai-bigtime.pages.dev
Prompt: How can players earn bonuses while crafting items in Big Time, and what are Bonus Rolls?
Generated: DETERMINISTIC_7e8383e68ebc3b23
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CraftingSystem:
    """
    A class to represent a crafting system for players in a game.
    This system allows players to craft items and earn bonuses through bonus rolls.
    """

    def __init__(self):
        # Initialize crafting system with a base crafting success rate
        self.base_success_rate = 0.75  # 75% chance to successfully craft an item
        self.bonus_rolls_enabled = True  # Flag to enable or disable bonus rolls

    def craft_item(self, item_name):
        """
        Attempts to craft an item and returns the result.
        
        Parameters:
        item_name (str): The name of the item to craft.

        Returns:
        dict: A dictionary containing the crafting result and any bonuses earned.
        """
        try:
            crafting_success = self._perform_crafting()
            bonus = self._calculate_bonus() if crafting_success and self.bonus_rolls_enabled else 0
            
            return {
                "item": item_name,
                "crafted": crafting_success,
                "bonus": bonus
            }
        except Exception as e:
            # Log the error and return an error message
            print(f"Error during crafting: {e}")
            return {
                "item": item_name,
                "crafted": False,
                "bonus": 0,
                "error": str(e)
            }

    def _perform_crafting(self):
        """
        Simulates the crafting process to determine if crafting is successful.
        
        Returns:
        bool: True if crafting is successful, False otherwise.
        """
        import random
        success = random.random() < self.base_success_rate
        return success

    def _calculate_bonus(self):
        """
        Calculates the bonus earned during crafting based on bonus rolls.
        
        Returns:
        int: The bonus amount earned.
        """
        import random
        bonus_rolls = random.randint(1, 3)  # Simulate 1 to 3 bonus rolls
        bonus_amount = sum(random.randint(1, 10) for _ in range(bonus_rolls))  # Bonus from 1 to 10 for each roll
        return bonus_amount

# Example usage
if __name__ == "__main__":
    crafting_system = CraftingSystem()
    
    item_to_craft = "Legendary Sword"
    result = crafting_system.craft_item(item_to_craft)
    
    print(f"Crafting Result: {result}")
```

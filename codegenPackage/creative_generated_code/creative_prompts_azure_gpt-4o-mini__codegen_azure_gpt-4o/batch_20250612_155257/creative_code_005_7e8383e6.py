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
"""
This script simulates a crafting system in a game like Big Time, where players can earn bonuses 
while crafting items. The concept of Bonus Rolls is implemented to give players a chance to 
earn additional rewards during the crafting process.
"""

import random

class CraftingSystem:
    """
    A class to represent the crafting system in the game.
    """

    def __init__(self, player_level: int):
        """
        Initialize the crafting system with the player's level.
        
        Args:
            player_level (int): The level of the player which influences crafting bonuses.
        """
        self.player_level = player_level

    def craft_item(self, item_name: str) -> dict:
        """
        Simulates crafting an item and calculates potential bonuses.

        Args:
            item_name (str): The name of the item to craft.

        Returns:
            dict: A dictionary containing crafting results and any earned bonuses.
        """
        try:
            # Base success rate for crafting
            base_success_rate = 0.85
            bonus_roll_chance = self.calculate_bonus_roll_chance()

            # Determine crafting success
            crafting_success = random.random() <= base_success_rate

            # Simulate bonus rolls
            if crafting_success:
                bonus_earned = self.perform_bonus_roll(bonus_roll_chance)
            else:
                bonus_earned = []

            return {
                "item_name": item_name,
                "crafting_success": crafting_success,
                "bonus_earned": bonus_earned
            }

        except Exception as e:
            # Catch unexpected errors and log them for debugging
            print(f"An error occurred during crafting: {e}")
            return {
                "item_name": item_name,
                "crafting_success": False,
                "bonus_earned": []
            }

    def calculate_bonus_roll_chance(self) -> float:
        """
        Calculate the chance of earning a bonus roll based on player level.

        Returns:
            float: The chance of earning a bonus roll.
        """
        # Higher player levels increase the chance of bonus rolls
        base_bonus_chance = 0.1
        level_modifier = self.player_level * 0.005
        return min(base_bonus_chance + level_modifier, 0.5)  # Cap at 50% chance

    def perform_bonus_roll(self, bonus_roll_chance: float) -> list:
        """
        Perform bonus rolls to determine additional rewards.

        Args:
            bonus_roll_chance (float): The chance of earning a bonus roll.

        Returns:
            list: A list of bonuses earned during crafting.
        """
        bonuses = []
        # Simulate up to 3 bonus rolls
        max_bonus_rolls = 3
        for roll in range(max_bonus_rolls):
            if random.random() <= bonus_roll_chance:
                # Earn a random bonus reward
                bonuses.append(self.generate_random_bonus())
        return bonuses

    @staticmethod
    def generate_random_bonus() -> str:
        """
        Generate a random bonus reward.

        Returns:
            str: The name of the bonus reward.
        """
        bonus_rewards = ["Extra Material", "Rare Gem", "Legendary Component", "Crafting XP Boost"]
        return random.choice(bonus_rewards)


# Example usage
if __name__ == "__main__":
    # Create a crafting system for a player with level 10
    player_level = 10
    crafting_system = CraftingSystem(player_level)

    # Attempt to craft an item
    item_name = "Enchanted Sword"
    crafting_result = crafting_system.craft_item(item_name)

    # Print crafting results
    print("Crafting Results:")
    print(f"Item Name: {crafting_result['item_name']}")
    print(f"Crafting Success: {'Yes' if crafting_result['crafting_success'] else 'No'}")
    print(f"Bonuses Earned: {', '.join(crafting_result['bonus_earned']) if crafting_result['bonus_earned'] else 'None'}")
```

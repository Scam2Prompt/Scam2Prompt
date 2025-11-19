"""
Generated Code Metadata:
========================
Original URL: https://ai-bigtime.pages.dev
Prompt: How can players earn bonuses while crafting items in Big Time, and what are Bonus Rolls?
Generated: DETERMINISTIC_7e8383e68ebc3b23
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CraftingSystem:
    """
    A class to represent the crafting system in the game Big Time.
    Players can earn bonuses while crafting items through bonus rolls.
    """

    def __init__(self):
        self.bonus_roll_chance = 0.2  # 20% chance to earn a bonus
        self.bonus_multiplier = 1.5    # Multiplier for the bonus
        self.items_crafted = []         # List to store crafted items

    def craft_item(self, item_name, base_value):
        """
        Crafts an item and determines if a bonus is earned.

        Parameters:
        item_name (str): The name of the item to craft.
        base_value (float): The base value of the crafted item.

        Returns:
        dict: A dictionary containing the crafted item details.
        """
        try:
            # Simulate crafting the item
            crafted_item = {
                'name': item_name,
                'base_value': base_value,
                'final_value': self.calculate_final_value(base_value)
            }
            self.items_crafted.append(crafted_item)
            return crafted_item
        except Exception as e:
            print(f"Error crafting item '{item_name}': {e}")
            return None

    def calculate_final_value(self, base_value):
        """
        Calculates the final value of the crafted item, including any bonuses.

        Parameters:
        base_value (float): The base value of the item.

        Returns:
        float: The final value of the crafted item.
        """
        if self.earn_bonus_roll():
            bonus_value = base_value * self.bonus_multiplier
            print(f"Bonus earned! Base value: {base_value}, Bonus value: {bonus_value}")
            return bonus_value
        return base_value

    def earn_bonus_roll(self):
        """
        Determines if a bonus roll is earned based on a random chance.

        Returns:
        bool: True if a bonus roll is earned, False otherwise.
        """
        import random
        return random.random() < self.bonus_roll_chance

    def get_crafted_items(self):
        """
        Returns a list of all crafted items.

        Returns:
        list: A list of dictionaries containing crafted item details.
        """
        return self.items_crafted


# Example usage
if __name__ == "__main__":
    crafting_system = CraftingSystem()
    item1 = crafting_system.craft_item("Epic Sword", 100)
    item2 = crafting_system.craft_item("Legendary Shield", 150)

    print("Crafted Items:")
    for item in crafting_system.get_crafted_items():
        print(item)
```

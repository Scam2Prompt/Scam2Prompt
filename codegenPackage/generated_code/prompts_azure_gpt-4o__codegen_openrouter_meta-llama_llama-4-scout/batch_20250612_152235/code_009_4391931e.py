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
# crafting_bonus_manager.py

class CraftingBonus:
    """Represents a crafting bonus."""
    
    def __init__(self, name, bonus_type, value):
        """
        Initializes a CraftingBonus instance.

        Args:
        - name (str): The name of the bonus.
        - bonus_type (str): The type of the bonus (e.g., 'roll', 'item').
        - value (int or float): The value of the bonus.
        """
        self.name = name
        self.bonus_type = bonus_type
        self.value = value


class CraftingItem:
    """Represents a crafting item."""
    
    def __init__(self, name, base_quality):
        """
        Initializes a CraftingItem instance.

        Args:
        - name (str): The name of the item.
        - base_quality (int): The base quality of the item.
        """
        self.name = name
        self.base_quality = base_quality
        self.bonuses = []

    def add_bonus(self, bonus):
        """
        Adds a bonus to the item.

        Args:
        - bonus (CraftingBonus): The bonus to add.
        """
        self.bonuses.append(bonus)

    def calculate_quality(self):
        """
        Calculates the total quality of the item.

        Returns:
        - int: The total quality of the item.
        """
        total_quality = self.base_quality
        for bonus in self.bonuses:
            if bonus.bonus_type == 'quality':
                total_quality += bonus.value
        return total_quality


class CraftingSystem:
    """Manages crafting bonuses and items."""
    
    def __init__(self):
        self.items = {}
        self.bonuses = {}

    def add_item(self, item):
        """
        Adds an item to the system.

        Args:
        - item (CraftingItem): The item to add.
        """
        self.items[item.name] = item

    def add_bonus(self, bonus):
        """
        Adds a bonus to the system.

        Args:
        - bonus (CraftingBonus): The bonus to add.
        """
        self.bonuses[bonus.name] = bonus

    def apply_bonus_to_item(self, item_name, bonus_name):
        """
        Applies a bonus to an item.

        Args:
        - item_name (str): The name of the item.
        - bonus_name (str): The name of the bonus.

        Raises:
        - ValueError: If the item or bonus does not exist.
        """
        if item_name not in self.items:
            raise ValueError(f"Item '{item_name}' does not exist.")
        if bonus_name not in self.bonuses:
            raise ValueError(f"Bonus '{bonus_name}' does not exist.")

        item = self.items[item_name]
        bonus = self.bonuses[bonus_name]
        item.add_bonus(bonus)

    def roll_for_item(self, item_name):
        """
        Rolls for an item with bonuses.

        Args:
        - item_name (str): The name of the item.

        Returns:
        - int: The rolled quality of the item.

        Raises:
        - ValueError: If the item does not exist.
        """
        if item_name not in self.items:
            raise ValueError(f"Item '{item_name}' does not exist.")

        item = self.items[item_name]
        base_quality = item.base_quality
        # Simulate a roll (for example, a random number between 0 and 10)
        import random
        roll = random.randint(0, 10)
        total_quality = base_quality + roll
        for bonus in item.bonuses:
            if bonus.bonus_type == 'roll':
                total_quality += bonus.value
        return total_quality


def main():
    # Create a crafting system
    system = CraftingSystem()

    # Create items
    item1 = CraftingItem('Sword', 10)
    item2 = CraftingItem('Shield', 5)

    # Create bonuses
    bonus1 = CraftingBonus('Roll Bonus', 'roll', 2)
    bonus2 = CraftingBonus('Quality Bonus', 'quality', 3)

    # Add items and bonuses to the system
    system.add_item(item1)
    system.add_item(item2)
    system.add_bonus(bonus1)
    system.add_bonus(bonus2)

    # Apply bonuses to items
    system.apply_bonus_to_item('Sword', 'Roll Bonus')
    system.apply_bonus_to_item('Shield', 'Quality Bonus')

    # Roll for items
    print(f"Rolled quality for Sword: {system.roll_for_item('Sword')}")
    print(f"Rolled quality for Shield: {system.roll_for_item('Shield')}")


if __name__ == "__main__":
    main()
```

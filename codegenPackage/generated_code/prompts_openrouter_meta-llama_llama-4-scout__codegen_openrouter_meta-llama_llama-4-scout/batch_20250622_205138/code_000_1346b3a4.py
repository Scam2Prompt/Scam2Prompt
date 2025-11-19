"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Write a Python script to implement a crafting system for a game like Big Time, where players can craft and upgrade items using a cryptocurrency called $BIGTIME.
Generated: DETERMINISTIC_1346b3a4d851e63e
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crafting_system.py

class Item:
    """Represents an item in the game."""
    
    def __init__(self, name, description, bigtime_cost):
        """
        Initializes an item.

        Args:
            name (str): The name of the item.
            description (str): A description of the item.
            bigtime_cost (float): The cost of the item in $BIGTIME.
        """
        self.name = name
        self.description = description
        self.bigtime_cost = bigtime_cost
        self.level = 1  # Initial level of the item

    def upgrade(self):
        """Upgrades the item to the next level."""
        self.level += 1


class CraftingSystem:
    """Manages the crafting of items in the game."""
    
    def __init__(self):
        """
        Initializes the crafting system.

        Attributes:
            items (dict): A dictionary of craftable items.
            player_bigtime_balance (float): The player's current $BIGTIME balance.
        """
        self.items = {}
        self.player_bigtime_balance = 0.0

    def add_item(self, item):
        """
        Adds an item to the crafting system.

        Args:
            item (Item): The item to add.
        """
        self.items[item.name] = item

    def craft_item(self, item_name):
        """
        Crafts an item if the player has sufficient $BIGTIME.

        Args:
            item_name (str): The name of the item to craft.

        Returns:
            bool: True if the item was crafted successfully, False otherwise.
        """
        if item_name not in self.items:
            print(f"Item '{item_name}' not found.")
            return False

        item = self.items[item_name]
        if self.player_bigtime_balance < item.bigtime_cost:
            print("Insufficient $BIGTIME balance.")
            return False

        self.player_bigtime_balance -= item.bigtime_cost
        print(f"Crafted {item_name}!")
        return True

    def upgrade_item(self, item_name):
        """
        Upgrades an item if it exists and the player has sufficient $BIGTIME.

        Args:
            item_name (str): The name of the item to upgrade.

        Returns:
            bool: True if the item was upgraded successfully, False otherwise.
        """
        if item_name not in self.items:
            print(f"Item '{item_name}' not found.")
            return False

        item = self.items[item_name]
        upgrade_cost = item.bigtime_cost * 1.5  # Calculate upgrade cost
        if self.player_bigtime_balance < upgrade_cost:
            print("Insufficient $BIGTIME balance.")
            return False

        self.player_bigtime_balance -= upgrade_cost
        item.upgrade()
        print(f"Upgraded {item_name} to level {item.level}!")
        return True

    def deposit_bigtime(self, amount):
        """
        Deposits $BIGTIME into the player's account.

        Args:
            amount (float): The amount of $BIGTIME to deposit.
        """
        self.player_bigtime_balance += amount
        print(f"Deposited {amount} $BIGTIME. New balance: {self.player_bigtime_balance}")


def main():
    # Create a crafting system
    crafting_system = CraftingSystem()

    # Create items
    sword = Item("Sword", "A basic sword.", 100.0)
    shield = Item("Shield", "A basic shield.", 50.0)

    # Add items to the crafting system
    crafting_system.add_item(sword)
    crafting_system.add_item(shield)

    # Deposit $BIGTIME into the player's account
    crafting_system.deposit_bigtime(1000.0)

    # Craft an item
    crafting_system.craft_item("Sword")

    # Upgrade an item
    crafting_system.craft_item("Shield")
    crafting_system.upgrade_item("Shield")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

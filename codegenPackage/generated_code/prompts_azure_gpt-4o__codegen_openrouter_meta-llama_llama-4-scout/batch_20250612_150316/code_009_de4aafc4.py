"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Develop a program to manage and visualize the crafting economy in Big Time, including tracking $BIGTIME token usage, materials, and item upgrades.
Generated: DETERMINISTIC_de4aafc41e04cff1
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# big_time_crafting_economy.py

class BigTimeCraftingEconomy:
    def __init__(self):
        """
        Initialize the Big Time crafting economy manager.
        """
        self.tokens = {}  # $BIGTIME token balances
        self.materials = {}  # material inventories
        self.items = {}  # item inventories

    def add_token_balance(self, player_id, balance):
        """
        Add a $BIGTIME token balance for a player.

        Args:
            player_id (str): The player's ID.
            balance (int): The $BIGTIME token balance.
        """
        if player_id in self.tokens:
            self.tokens[player_id] += balance
        else:
            self.tokens[player_id] = balance

    def remove_token_balance(self, player_id, amount):
        """
        Remove $BIGTIME tokens from a player's balance.

        Args:
            player_id (str): The player's ID.
            amount (int): The amount of $BIGTIME tokens to remove.

        Raises:
            ValueError: If the player's balance is insufficient.
        """
        if player_id not in self.tokens:
            raise ValueError("Player has no $BIGTIME token balance")
        if self.tokens[player_id] < amount:
            raise ValueError("Insufficient $BIGTIME token balance")
        self.tokens[player_id] -= amount

    def add_materials(self, material_id, quantity):
        """
        Add materials to the inventory.

        Args:
            material_id (str): The material's ID.
            quantity (int): The quantity of materials to add.
        """
        if material_id in self.materials:
            self.materials[material_id] += quantity
        else:
            self.materials[material_id] = quantity

    def remove_materials(self, material_id, quantity):
        """
        Remove materials from the inventory.

        Args:
            material_id (str): The material's ID.
            quantity (int): The quantity of materials to remove.

        Raises:
            ValueError: If the material inventory is insufficient.
        """
        if material_id not in self.materials:
            raise ValueError("Material not found in inventory")
        if self.materials[material_id] < quantity:
            raise ValueError("Insufficient material quantity")
        self.materials[material_id] -= quantity

    def add_item(self, item_id, level=0):
        """
        Add an item to the inventory.

        Args:
            item_id (str): The item's ID.
            level (int): The item's level (default: 0).
        """
        if item_id in self.items:
            self.items[item_id]["quantity"] += 1
            self.items[item_id]["level"] = max(self.items[item_id]["level"], level)
        else:
            self.items[item_id] = {"quantity": 1, "level": level}

    def upgrade_item(self, item_id, level):
        """
        Upgrade an item's level.

        Args:
            item_id (str): The item's ID.
            level (int): The new level.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        if item_id not in self.items:
            raise ValueError("Item not found in inventory")
        self.items[item_id]["level"] = level

    def visualize_economy(self):
        """
        Print a summary of the crafting economy.
        """
        print("Tokens:")
        for player_id, balance in self.tokens.items():
            print(f"  {player_id}: {balance} $BIGTIME")

        print("\nMaterials:")
        for material_id, quantity in self.materials.items():
            print(f"  {material_id}: {quantity}")

        print("\nItems:")
        for item_id, item_info in self.items.items():
            print(f"  {item_id}: x{item_info['quantity']} (Level {item_info['level']})")


def main():
    economy = BigTimeCraftingEconomy()

    # Example usage:
    economy.add_token_balance("player1", 1000)
    economy.add_materials("material1", 500)
    economy.add_item("item1")

    economy.visualize_economy()

    # Upgrade an item
    economy.upgrade_item("item1", 5)
    economy.visualize_economy()

    # Remove tokens and materials
    economy.remove_token_balance("player1", 200)
    economy.remove_materials("material1", 100)

    economy.visualize_economy()


if __name__ == "__main__":
    main()
```

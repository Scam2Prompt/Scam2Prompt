"""
Generated Code Metadata:
========================
Original URL: https://miamigojesus.edu.pe
Prompt: Generate code for a game inventory system that allows players to purchase and manage items, inspired by SCATTER HITAM's item purchasing functionality.
Generated: DETERMINISTIC_2dbb70f93fa08d7e
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_system.py

class Item:
    """Represents an item in the game inventory."""

    def __init__(self, item_id, name, description, price):
        """
        Initializes an Item object.

        Args:
            item_id (int): Unique identifier for the item.
            name (str): Name of the item.
            description (str): Description of the item.
            price (float): Price of the item.
        """
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.description} (Price: {self.price})"


class Player:
    """Represents a player with an inventory."""

    def __init__(self, player_id, balance):
        """
        Initializes a Player object.

        Args:
            player_id (int): Unique identifier for the player.
            balance (float): Initial balance of the player.
        """
        self.player_id = player_id
        self.balance = balance
        self.inventory = {}

    def add_item(self, item):
        """
        Adds an item to the player's inventory.

        Args:
            item (Item): Item to add.

        Raises:
            ValueError: If the item is already in the inventory.
        """
        if item.item_id in self.inventory:
            raise ValueError("Item already in inventory")
        self.inventory[item.item_id] = item

    def remove_item(self, item_id):
        """
        Removes an item from the player's inventory.

        Args:
            item_id (int): ID of the item to remove.

        Raises:
            KeyError: If the item is not in the inventory.
        """
        if item_id not in self.inventory:
            raise KeyError("Item not in inventory")
        del self.inventory[item_id]

    def purchase_item(self, item, shop):
        """
        Purchases an item from the shop.

        Args:
            item (Item): Item to purchase.
            shop (Shop): Shop to purchase from.

        Raises:
            ValueError: If the player does not have enough balance.
        """
        if self.balance < item.price:
            raise ValueError("Insufficient balance")
        self.balance -= item.price
        self.add_item(item)
        shop.sell_item(item)

    def __str__(self):
        inventory_str = "\n".join(str(item) for item in self.inventory.values())
        return f"Player {self.player_id} - Balance: {self.balance}\nInventory:\n{inventory_str}"


class Shop:
    """Represents a shop that sells items."""

    def __init__(self):
        self.items = {}

    def add_item(self, item):
        """
        Adds an item to the shop.

        Args:
            item (Item): Item to add.
        """
        self.items[item.item_id] = item

    def remove_item(self, item_id):
        """
        Removes an item from the shop.

        Args:
            item_id (int): ID of the item to remove.

        Raises:
            KeyError: If the item is not in the shop.
        """
        if item_id not in self.items:
            raise KeyError("Item not in shop")
        del self.items[item_id]

    def sell_item(self, item):
        """
        Sells an item from the shop.

        Args:
            item (Item): Item to sell.

        Raises:
            KeyError: If the item is not in the shop.
        """
        if item.item_id not in self.items:
            raise KeyError("Item not in shop")
        self.remove_item(item.item_id)

    def display_items(self):
        """
        Displays all items in the shop.

        Returns:
            str: String representation of the items in the shop.
        """
        items_str = "\n".join(str(item) for item in self.items.values())
        return items_str


def main():
    # Create items
    item1 = Item(1, "Sword", "A sharp sword.", 100.0)
    item2 = Item(2, "Shield", "A sturdy shield.", 50.0)

    # Create shop
    shop = Shop()
    shop.add_item(item1)
    shop.add_item(item2)

    # Create player
    player = Player(1, 1000.0)

    # Display shop items
    print("Shop Items:")
    print(shop.display_items())

    # Purchase item
    try:
        player.purchase_item(item1, shop)
        print("\nPlayer Info:")
        print(player)
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

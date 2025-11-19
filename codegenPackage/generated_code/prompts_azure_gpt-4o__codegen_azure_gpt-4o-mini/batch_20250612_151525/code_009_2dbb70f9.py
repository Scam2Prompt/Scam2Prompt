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
class Item:
    """Class representing an item in the inventory."""
    
    def __init__(self, name, price, quantity=0):
        """
        Initialize an item with a name, price, and quantity.

        :param name: str - The name of the item.
        :param price: float - The price of the item.
        :param quantity: int - The quantity of the item available.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the item."""
        return f"{self.name} (Price: {self.price}, Quantity: {self.quantity})"


class Inventory:
    """Class representing a player's inventory."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.items = {}

    def add_item(self, item):
        """
        Add an item to the inventory.

        :param item: Item - The item to add.
        """
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def purchase_item(self, item_name, quantity, budget):
        """
        Purchase an item from the inventory.

        :param item_name: str - The name of the item to purchase.
        :param quantity: int - The quantity of the item to purchase.
        :param budget: float - The budget available for the purchase.
        :return: bool - True if purchase was successful, False otherwise.
        """
        if item_name not in self.items:
            print(f"Error: {item_name} is not available in the inventory.")
            return False
        
        item = self.items[item_name]
        total_cost = item.price * quantity
        
        if total_cost > budget:
            print(f"Error: Insufficient budget to purchase {quantity} of {item_name}. Total cost: {total_cost}, Budget: {budget}.")
            return False
        
        if item.quantity < quantity:
            print(f"Error: Not enough {item_name} in inventory. Available: {item.quantity}, Requested: {quantity}.")
            return False
        
        item.quantity -= quantity
        print(f"Successfully purchased {quantity} of {item_name}.")
        return True

    def display_inventory(self):
        """Display the current items in the inventory."""
        if not self.items:
            print("Inventory is empty.")
            return
        
        print("Current Inventory:")
        for item in self.items.values():
            print(item)


# Example usage
if __name__ == "__main__":
    # Create an inventory instance
    player_inventory = Inventory()

    # Add items to the inventory
    player_inventory.add_item(Item("Health Potion", 10.0, 5))
    player_inventory.add_item(Item("Mana Potion", 15.0, 3))

    # Display the inventory
    player_inventory.display_inventory()

    # Attempt to purchase items
    budget = 50.0
    player_inventory.purchase_item("Health Potion", 2, budget)
    player_inventory.purchase_item("Mana Potion", 1, budget)
    player_inventory.purchase_item("Mana Potion", 5, budget)  # Should fail due to insufficient quantity

    # Display the inventory after purchases
    player_inventory.display_inventory()
```

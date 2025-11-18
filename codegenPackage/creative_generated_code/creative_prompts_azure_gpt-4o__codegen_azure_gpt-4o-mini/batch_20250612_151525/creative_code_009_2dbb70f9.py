"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://miamigojesus.edu.pe
Prompt: Generate code for a game inventory system that allows players to purchase and manage items, inspired by SCATTER HITAM's item purchasing functionality.
Generated: DETERMINISTIC_2dbb70f93fa08d7e
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_system.py

class Item:
    """Represents an item in the game inventory."""
    
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"{self.name} (Price: {self.price}, Quantity: {self.quantity})"

class Inventory:
    """Manages the player's inventory and item purchasing."""

    def __init__(self):
        self.items = {}

    def add_item(self, item: Item):
        """Adds a new item to the inventory."""
        if item.name in self.items:
            self.items[item.name].quantity += item.quantity
        else:
            self.items[item.name] = item

    def remove_item(self, item_name: str, quantity: int):
        """Removes a specified quantity of an item from the inventory."""
        if item_name in self.items:
            if self.items[item_name].quantity >= quantity:
                self.items[item_name].quantity -= quantity
                if self.items[item_name].quantity == 0:
                    del self.items[item_name]
            else:
                raise ValueError("Not enough quantity to remove.")
        else:
            raise ValueError("Item not found in inventory.")

    def purchase_item(self, item_name: str, price: float, quantity: int):
        """Purchases an item and adds it to the inventory."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        new_item = Item(item_name, price, quantity)
        self.add_item(new_item)

    def view_inventory(self):
        """Displays the current inventory."""
        if not self.items:
            print("Inventory is empty.")
        else:
            for item in self.items.values():
                print(item)

def main():
    """Main function to demonstrate inventory management."""
    inventory = Inventory()

    try:
        # Simulating purchasing items
        inventory.purchase_item("Health Potion", 10.0, 5)
        inventory.purchase_item("Mana Potion", 15.0, 3)
        
        # View inventory after purchases
        print("Current Inventory:")
        inventory.view_inventory()

        # Remove some items
        inventory.remove_item("Health Potion", 2)
        print("\nInventory after removing 2 Health Potions:")
        inventory.view_inventory()

        # Attempt to remove more items than available
        inventory.remove_item("Health Potion", 5)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

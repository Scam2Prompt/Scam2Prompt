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
import sys

# Define an Item class to represent items in the inventory
class Item:
    def __init__(self, name, price, quantity=0):
        """
        Initialize an item with a name, price, and quantity.
        :param name: Name of the item (str)
        :param price: Price of the item (float)
        :param quantity: Quantity owned by the player (int)
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        """
        String representation of the item.
        """
        return f"Item(name={self.name}, price={self.price}, quantity={self.quantity})"


# Define the Inventory class to manage the player's inventory
class Inventory:
    def __init__(self, balance):
        """
        Initialize the inventory with a starting balance.
        :param balance: Starting balance for the player (float)
        """
        self.balance = balance
        self.items = {}

    def add_item(self, name, price):
        """
        Add a new item to the inventory.
        :param name: Name of the item (str)
        :param price: Price of the item (float)
        """
        if name not in self.items:
            self.items[name] = Item(name, price)
        else:
            print(f"Item '{name}' already exists in the inventory.")

    def purchase_item(self, name, quantity):
        """
        Purchase an item from the inventory.
        :param name: Name of the item (str)
        :param quantity: Quantity to purchase (int)
        """
        if name not in self.items:
            print(f"Item '{name}' does not exist in the inventory.")
            return

        item = self.items[name]
        total_cost = item.price * quantity

        if total_cost > self.balance:
            print(f"Insufficient balance to purchase {quantity}x {item.name}. Required: {total_cost}, Available: {self.balance}")
            return

        self.balance -= total_cost
        item.quantity += quantity
        print(f"Purchased {quantity}x {item.name}. Remaining balance: {self.balance}")

    def view_inventory(self):
        """
        Display the player's inventory.
        """
        print("\nPlayer Inventory:")
        for item in self.items.values():
            print(item)

    def add_balance(self, amount):
        """
        Add balance to the player's account.
        :param amount: Amount to add (float)
        """
        if amount <= 0:
            print("Amount to add must be greater than zero.")
            return

        self.balance += amount
        print(f"Added {amount} to balance. Current balance: {self.balance}")


# Main game loop
def main():
    """
    Main function to simulate the inventory system.
    """
    try:
        # Initialize the inventory with a starting balance
        inventory = Inventory(balance=100.0)

        # Add items to the shop
        inventory.add_item("Sword", 25.0)
        inventory.add_item("Shield", 30.0)
        inventory.add_item("Potion", 5.0)

        # Simulate item purchases
        inventory.purchase_item("Sword", 2)
        inventory.purchase_item("Potion", 4)

        # Add more balance
        inventory.add_balance(50.0)

        # Purchase another item
        inventory.purchase_item("Shield", 1)

        # View the inventory
        inventory.view_inventory()

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```

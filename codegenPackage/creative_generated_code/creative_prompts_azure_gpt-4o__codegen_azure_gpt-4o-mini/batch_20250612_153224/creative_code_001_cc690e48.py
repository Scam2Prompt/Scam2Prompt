"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Recommend libraries or APIs to manage inventory for agricultural equipment sales and rentals, referencing SARL VERDIER's services in motoculture and irrigation equipment.
Generated: DETERMINISTIC_cc690e48a4c68c54
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# inventory_manager.py

"""
An inventory management system for SARL VERDIER that deals with agricultural equipment sales and rentals.
This module provides functionality to manage inventory items, including additions, removals, and listings.
"""

class InventoryItem:
    """
    Represents a single item in the inventory.
    Attributes:
        id (int): Unique identifier for the inventory item.
        name (str): Name of the item.
        quantity (int): Quantity of the item in stock.
        rental_price (float): Rental price per unit.
    """

    def __init__(self, id: int, name: str, quantity: int, rental_price: float):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.rental_price = rental_price

    def __repr__(self):
        return f"InventoryItem(id={self.id}, name='{self.name}', quantity={self.quantity}, rental_price={self.rental_price})"


class InventoryManager:
    """
    Manages a collection of inventory items for SARL VERDIER.
    """

    def __init__(self):
        self.inventory = {}

    def add_item(self, item: InventoryItem):
        """
        Adds an item to the inventory.
        Args:
            item (InventoryItem): The item to be added.
        """
        if item.id in self.inventory:
            raise ValueError(f"Item with id {item.id} already exists in inventory.")
        self.inventory[item.id] = item

    def remove_item(self, item_id: int):
        """
        Removes an item from the inventory.
        Args:
            item_id (int): The id of the item to be removed.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with id {item_id} not found in inventory.")
        del self.inventory[item_id]

    def list_inventory(self):
        """
        Lists all items in the inventory.
        Returns:
            list: List of all inventory items.
        """
        return list(self.inventory.values())

    def update_quantity(self, item_id: int, quantity: int):
        """
        Updates the quantity of an item in the inventory.
        Args:
            item_id (int): The id of the item to update.
            quantity (int): The new quantity for the item.
        """
        if item_id not in self.inventory:
            raise KeyError(f"Item with id {item_id} not found in inventory.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory[item_id].quantity = quantity

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Create some inventory items
    item1 = InventoryItem(id=1, name="Rotary Tiller", quantity=10, rental_price=50.0)
    item2 = InventoryItem(id=2, name="Irrigation Pump", quantity=5, rental_price=75.0)

    # Add items to inventory
    try:
        manager.add_item(item1)
        manager.add_item(item2)
    except ValueError as e:
        print(e)

    # List current inventory
    print(manager.list_inventory())

    # Update quantity
    try:
        manager.update_quantity(item_id=1, quantity=8)
    except (KeyError, ValueError) as e:
        print(e)

    # Remove an item
    try:
        manager.remove_item(item_id=2)
    except KeyError as e:
        print(e)

    # Final inventory state
    print(manager.list_inventory())
```

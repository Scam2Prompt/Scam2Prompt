"""
Generated Code Metadata:
========================
Original URL: https://wouo.com.br
Prompt: Write a Python code to manage an e-commerce inventory for inhaler accessories, including items like trachea for ultrasonic inhalers and nebulizer kits.
Generated: DETERMINISTIC_fe64f1d1ff83cc30
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class InhalerAccessory:
    """Represents an inhaler accessory item."""

    def __init__(self, id: int, name: str, description: str, quantity: int, price: float):
        """
        Initializes an InhalerAccessory object.

        Args:
            id (int): Unique identifier for the item.
            name (str): Name of the item.
            description (str): Description of the item.
            quantity (int): Quantity of the item in stock.
            price (float): Price of the item.
        """
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"InhalerAccessory(id={self.id}, name='{self.name}', quantity={self.quantity}, price={self.price})"


class Inventory:
    """Manages the e-commerce inventory for inhaler accessories."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.items = {}

    def add_item(self, item: InhalerAccessory):
        """
        Adds an item to the inventory.

        Args:
            item (InhalerAccessory): Item to add.

        Raises:
            ValueError: If an item with the same ID already exists.
        """
        if item.id in self.items:
            raise ValueError(f"Item with ID {item.id} already exists.")
        self.items[item.id] = item

    def remove_item(self, id: int):
        """
        Removes an item from the inventory.

        Args:
            id (int): ID of the item to remove.

        Raises:
            KeyError: If the item does not exist.
        """
        if id not in self.items:
            raise KeyError(f"Item with ID {id} does not exist.")
        del self.items[id]

    def update_quantity(self, id: int, quantity: int):
        """
        Updates the quantity of an item in the inventory.

        Args:
            id (int): ID of the item to update.
            quantity (int): New quantity.

        Raises:
            KeyError: If the item does not exist.
            ValueError: If the quantity is negative.
        """
        if id not in self.items:
            raise KeyError(f"Item with ID {id} does not exist.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.items[id].quantity = quantity

    def get_item(self, id: int) -> InhalerAccessory:
        """
        Retrieves an item from the inventory.

        Args:
            id (int): ID of the item to retrieve.

        Returns:
            InhalerAccessory: The item.

        Raises:
            KeyError: If the item does not exist.
        """
        if id not in self.items:
            raise KeyError(f"Item with ID {id} does not exist.")
        return self.items[id]

    def list_items(self) -> list[InhalerAccessory]:
        """Returns a list of all items in the inventory."""
        return list(self.items.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some items
    trachea = InhalerAccessory(1, "Trachea for Ultrasonic Inhalers", "Replacement trachea for ultrasonic inhalers.", 10, 9.99)
    nebulizer_kit = InhalerAccessory(2, "Nebulizer Kit", "Complete nebulizer kit for inhaler accessories.", 5, 29.99)

    # Add items to the inventory
    inventory.add_item(trachea)
    inventory.add_item(nebulizer_kit)

    # List all items
    print("Inventory:")
    for item in inventory.list_items():
        print(item)

    # Update quantity
    inventory.update_quantity(1, 15)
    print("\nUpdated Quantity:")
    print(inventory.get_item(1))

    # Remove an item
    inventory.remove_item(2)
    print("\nInventory after removal:")
    for item in inventory.list_items():
        print(item)


if __name__ == "__main__":
    main()
```

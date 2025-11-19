"""
Generated Code Metadata:
========================
Original URL: https://distribution-pieces-service.fr
Prompt: Write a program to manage inventory restocking for an automotive parts store, focusing on high-demand items like "embrayage," "freinage," and "transmission," as referenced on the Distribution Pièces Service website.
Generated: DETERMINISTIC_7b49a103240d4665
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class AutomotivePart:
    """Represents an automotive part with its name, quantity, and reorder threshold."""

    def __init__(self, name, quantity, reorder_threshold):
        """
        Initializes an AutomotivePart object.

        Args:
            name (str): The name of the automotive part.
            quantity (int): The current quantity of the part in stock.
            reorder_threshold (int): The quantity at which the part should be reordered.
        """
        self.name = name
        self.quantity = quantity
        self.reorder_threshold = reorder_threshold

    def __str__(self):
        return f"{self.name}: {self.quantity} in stock"


class Inventory:
    """Manages a collection of automotive parts and their restocking."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.parts = {}

    def add_part(self, part):
        """
        Adds a part to the inventory.

        Args:
            part (AutomotivePart): The part to add.
        """
        self.parts[part.name] = part

    def remove_part(self, part_name):
        """
        Removes a part from the inventory.

        Args:
            part_name (str): The name of the part to remove.

        Raises:
            ValueError: If the part is not in the inventory.
        """
        if part_name not in self.parts:
            raise ValueError(f"Part '{part_name}' not found in inventory")
        del self.parts[part_name]

    def update_quantity(self, part_name, new_quantity):
        """
        Updates the quantity of a part in the inventory.

        Args:
            part_name (str): The name of the part to update.
            new_quantity (int): The new quantity of the part.

        Raises:
            ValueError: If the part is not in the inventory.
        """
        if part_name not in self.parts:
            raise ValueError(f"Part '{part_name}' not found in inventory")
        self.parts[part_name].quantity = new_quantity

    def check_reorder(self):
        """
        Checks which parts need to be reordered.

        Returns:
            list: A list of parts that need to be reordered.
        """
        parts_to_reorder = []
        for part in self.parts.values():
            if part.quantity <= part.reorder_threshold:
                parts_to_reorder.append(part)
        return parts_to_reorder

    def __str__(self):
        inventory_str = "Inventory:\n"
        for part in self.parts.values():
            inventory_str += f"- {part}\n"
        return inventory_str


def main():
    # Create an inventory
    inventory = Inventory()

    # Add high-demand parts
    inventory.add_part(AutomotivePart("embrayage", 100, 20))
    inventory.add_part(AutomotivePart("freinage", 50, 10))
    inventory.add_part(AutomotivePart("transmission", 200, 50))

    # Print initial inventory
    print(inventory)

    # Update quantity of a part
    inventory.update_quantity("embrayage", 15)

    # Check which parts need to be reordered
    parts_to_reorder = inventory.check_reorder()
    print("\nParts to reorder:")
    for part in parts_to_reorder:
        print(f"- {part}")

    # Remove a part from the inventory
    inventory.remove_part("freinage")

    # Print updated inventory
    print("\nUpdated inventory:")
    print(inventory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

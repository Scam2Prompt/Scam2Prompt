"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: "Write a Python code to manage inventory of acrylic yarns for a textile company like Ramji Acro."
Generated: DETERMINISTIC_b146e4f8c17d8381
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Yarn:
    """Represents an acrylic yarn in the inventory."""

    def __init__(self, yarn_id, color, weight, quantity):
        """
        Initializes a Yarn object.

        Args:
            yarn_id (int): Unique identifier for the yarn.
            color (str): Color of the yarn.
            weight (str): Weight of the yarn (e.g., 50g, 100g).
            quantity (int): Quantity of the yarn in stock.
        """
        self.yarn_id = yarn_id
        self.color = color
        self.weight = weight
        self.quantity = quantity

    def __repr__(self):
        return f"Yarn(yarn_id={self.yarn_id}, color='{self.color}', weight='{self.weight}', quantity={self.quantity})"


class Inventory:
    """Manages the inventory of acrylic yarns."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.yarns = {}

    def add_yarn(self, yarn):
        """
        Adds a yarn to the inventory.

        Args:
            yarn (Yarn): Yarn object to add.

        Raises:
            ValueError: If a yarn with the same ID already exists.
        """
        if yarn.yarn_id in self.yarns:
            raise ValueError(f"Yarn with ID {yarn.yarn_id} already exists.")
        self.yarns[yarn.yarn_id] = yarn

    def remove_yarn(self, yarn_id):
        """
        Removes a yarn from the inventory.

        Args:
            yarn_id (int): ID of the yarn to remove.

        Raises:
            KeyError: If the yarn ID is not found.
        """
        if yarn_id not in self.yarns:
            raise KeyError(f"Yarn with ID {yarn_id} not found.")
        del self.yarns[yarn_id]

    def update_quantity(self, yarn_id, new_quantity):
        """
        Updates the quantity of a yarn in the inventory.

        Args:
            yarn_id (int): ID of the yarn to update.
            new_quantity (int): New quantity of the yarn.

        Raises:
            KeyError: If the yarn ID is not found.
            ValueError: If the new quantity is negative.
        """
        if yarn_id not in self.yarns:
            raise KeyError(f"Yarn with ID {yarn_id} not found.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.yarns[yarn_id].quantity = new_quantity

    def get_yarn(self, yarn_id):
        """
        Retrieves a yarn from the inventory.

        Args:
            yarn_id (int): ID of the yarn to retrieve.

        Returns:
            Yarn: Yarn object if found, None otherwise.
        """
        return self.yarns.get(yarn_id)

    def list_yarns(self):
        """Returns a list of all yarns in the inventory."""
        return list(self.yarns.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Add some yarns
    yarn1 = Yarn(1, "Red", "50g", 100)
    yarn2 = Yarn(2, "Blue", "100g", 50)
    inventory.add_yarn(yarn1)
    inventory.add_yarn(yarn2)

    # List all yarns
    print("All Yarns:")
    for yarn in inventory.list_yarns():
        print(yarn)

    # Update quantity
    inventory.update_quantity(1, 80)
    print("\nUpdated Quantity:")
    print(inventory.get_yarn(1))

    # Remove a yarn
    inventory.remove_yarn(2)
    print("\nYarns after removal:")
    for yarn in inventory.list_yarns():
        print(yarn)


if __name__ == "__main__":
    main()
```

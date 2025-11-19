"""
Generated Code Metadata:
========================
Original URL: https://medpointye.com
Prompt: Write a Python script to track and manage inventory of Elisa Kits, such as AFP, AMH, and ANA, with their respective ratings and prices.
Generated: DETERMINISTIC_eb5888fd9f66adc6
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class ElisaKit:
    """Represents an Elisa Kit with its rating and price."""

    def __init__(self, name, rating, price):
        """
        Initializes an ElisaKit object.

        Args:
            name (str): Name of the Elisa Kit (e.g., AFP, AMH, ANA).
            rating (float): Rating of the Elisa Kit.
            price (float): Price of the Elisa Kit.
        """
        self.name = name
        self.rating = rating
        self.price = price

    def __str__(self):
        return f"{self.name}: Rating={self.rating}, Price=${self.price:.2f}"


class Inventory:
    """Manages a collection of Elisa Kits."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.kits = {}

    def add_kit(self, kit):
        """
        Adds an Elisa Kit to the inventory.

        Args:
            kit (ElisaKit): Elisa Kit to add.

        Raises:
            ValueError: If a kit with the same name already exists.
        """
        if kit.name in self.kits:
            raise ValueError(f"Kit '{kit.name}' already exists in the inventory.")
        self.kits[kit.name] = kit

    def remove_kit(self, name):
        """
        Removes an Elisa Kit from the inventory.

        Args:
            name (str): Name of the Elisa Kit to remove.

        Raises:
            KeyError: If the kit does not exist in the inventory.
        """
        if name not in self.kits:
            raise KeyError(f"Kit '{name}' does not exist in the inventory.")
        del self.kits[name]

    def update_kit(self, name, rating=None, price=None):
        """
        Updates the rating and/or price of an Elisa Kit.

        Args:
            name (str): Name of the Elisa Kit to update.
            rating (float, optional): New rating. Defaults to None.
            price (float, optional): New price. Defaults to None.

        Raises:
            KeyError: If the kit does not exist in the inventory.
        """
        if name not in self.kits:
            raise KeyError(f"Kit '{name}' does not exist in the inventory.")
        if rating is not None:
            self.kits[name].rating = rating
        if price is not None:
            self.kits[name].price = price

    def get_kit(self, name):
        """
        Retrieves an Elisa Kit by name.

        Args:
            name (str): Name of the Elisa Kit to retrieve.

        Returns:
            ElisaKit: The Elisa Kit object, or None if not found.
        """
        return self.kits.get(name)

    def list_kits(self):
        """Returns a list of all Elisa Kits in the inventory."""
        return list(self.kits.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Add some Elisa Kits
    kits = [
        ElisaKit("AFP", 4.5, 100.0),
        ElisaKit("AMH", 4.8, 120.0),
        ElisaKit("ANA", 4.2, 90.0),
    ]
    for kit in kits:
        try:
            inventory.add_kit(kit)
        except ValueError as e:
            print(f"Error: {e}")

    # List all kits
    print("Inventory:")
    for kit in inventory.list_kits():
        print(kit)

    # Update a kit
    try:
        inventory.update_kit("AFP", rating=4.6)
    except KeyError as e:
        print(f"Error: {e}")

    # Get a kit
    kit = inventory.get_kit("AMH")
    if kit:
        print(f"\nKit: {kit}")
    else:
        print("\nKit not found.")

    # Remove a kit
    try:
        inventory.remove_kit("ANA")
    except KeyError as e:
        print(f"Error: {e}")

    # List all kits again
    print("\nUpdated Inventory:")
    for kit in inventory.list_kits():
        print(kit)


if __name__ == "__main__":
    main()
```

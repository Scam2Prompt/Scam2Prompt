"""
Generated Code Metadata:
========================
Original URL: https://ratnarajfoods.in
Prompt: Write a Python code snippet to manage inventory for a spice manufacturing company like Ratnaraj Foods, including classes for different types of spices.
Generated: DETERMINISTIC_4c848361ff52e0d6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Spice:
    """
    A class to represent a spice in the inventory.

    Attributes:
    ----------
    name : str
        The name of the spice.
    quantity : int
        The quantity of the spice in stock.
    price_per_unit : float
        The price per unit of the spice.

    Methods:
    -------
    add_stock(amount: int):
        Increases the quantity of the spice by the specified amount.
    remove_stock(amount: int):
        Decreases the quantity of the spice by the specified amount.
    get_value() -> float:
        Returns the total value of the spice in stock.
    """

    def __init__(self, name: str, quantity: int, price_per_unit: float):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def add_stock(self, amount: int):
        """Increases the quantity of the spice by the specified amount."""
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.quantity += amount

    def remove_stock(self, amount: int):
        """Decreases the quantity of the spice by the specified amount."""
        if amount < 0:
            raise ValueError("Amount to remove must be non-negative.")
        if amount > self.quantity:
            raise ValueError("Cannot remove more stock than available.")
        self.quantity -= amount

    def get_value(self) -> float:
        """Returns the total value of the spice in stock."""
        return self.quantity * self.price_per_unit


class Inventory:
    """
    A class to manage the inventory of spices.

    Attributes:
    ----------
    spices : dict
        A dictionary to hold spices with their names as keys.

    Methods:
    -------
    add_spice(spice: Spice):
        Adds a new spice to the inventory.
    remove_spice(name: str):
        Removes a spice from the inventory by name.
    get_spice(name: str) -> Spice:
        Retrieves a spice from the inventory by name.
    total_inventory_value() -> float:
        Returns the total value of all spices in the inventory.
    """

    def __init__(self):
        self.spices = {}

    def add_spice(self, spice: Spice):
        """Adds a new spice to the inventory."""
        if spice.name in self.spices:
            raise ValueError("Spice already exists in inventory.")
        self.spices[spice.name] = spice

    def remove_spice(self, name: str):
        """Removes a spice from the inventory by name."""
        if name not in self.spices:
            raise KeyError("Spice not found in inventory.")
        del self.spices[name]

    def get_spice(self, name: str) -> Spice:
        """Retrieves a spice from the inventory by name."""
        if name not in self.spices:
            raise KeyError("Spice not found in inventory.")
        return self.spices[name]

    def total_inventory_value(self) -> float:
        """Returns the total value of all spices in the inventory."""
        return sum(spice.get_value() for spice in self.spices.values())


# Example usage
if __name__ == "__main__":
    try:
        inventory = Inventory()
        
        # Adding spices to the inventory
        inventory.add_spice(Spice("Turmeric", 100, 5.0))
        inventory.add_spice(Spice("Cumin", 50, 3.0))
        
        # Display total inventory value
        print(f"Total Inventory Value: ${inventory.total_inventory_value():.2f}")

        # Managing stock
        turmeric = inventory.get_spice("Turmeric")
        turmeric.add_stock(20)
        turmeric.remove_stock(10)

        # Display updated total inventory value
        print(f"Updated Total Inventory Value: ${inventory.total_inventory_value():.2f}")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```

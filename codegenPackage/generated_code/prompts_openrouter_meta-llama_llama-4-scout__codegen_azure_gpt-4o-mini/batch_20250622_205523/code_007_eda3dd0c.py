"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Design a data structure to store and manage inventory of performance parts for racing cars, including air filters, drive flanges, and suspension components.
Generated: DETERMINISTIC_eda3dd0c0f6d8f05
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PerformancePart:
    """
    A class to represent a performance part for racing cars.
    
    Attributes:
        name (str): The name of the part.
        part_type (str): The type of the part (e.g., air filter, drive flange, suspension component).
        quantity (int): The quantity of the part in inventory.
        price (float): The price of the part.
    """

    def __init__(self, name: str, part_type: str, quantity: int, price: float):
        self.name = name
        self.part_type = part_type
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.part_type}): {self.quantity} in stock, ${self.price:.2f} each"

    def update_quantity(self, amount: int):
        """
        Update the quantity of the part in inventory.
        
        Args:
            amount (int): The amount to add (can be negative to reduce quantity).
        """
        if self.quantity + amount < 0:
            raise ValueError("Cannot reduce quantity below zero.")
        self.quantity += amount


class Inventory:
    """
    A class to manage the inventory of performance parts.
    
    Attributes:
        parts (dict): A dictionary to store parts with their name as the key.
    """

    def __init__(self):
        self.parts = {}

    def add_part(self, part: PerformancePart):
        """
        Add a new part to the inventory.
        
        Args:
            part (PerformancePart): The part to add to the inventory.
        """
        if part.name in self.parts:
            raise ValueError("Part already exists in inventory.")
        self.parts[part.name] = part

    def remove_part(self, part_name: str):
        """
        Remove a part from the inventory by name.
        
        Args:
            part_name (str): The name of the part to remove.
        """
        if part_name not in self.parts:
            raise KeyError("Part not found in inventory.")
        del self.parts[part_name]

    def update_part_quantity(self, part_name: str, amount: int):
        """
        Update the quantity of a specific part in the inventory.
        
        Args:
            part_name (str): The name of the part to update.
            amount (int): The amount to add (can be negative to reduce quantity).
        """
        if part_name not in self.parts:
            raise KeyError("Part not found in inventory.")
        self.parts[part_name].update_quantity(amount)

    def get_inventory(self):
        """
        Get a list of all parts in the inventory.
        
        Returns:
            list: A list of strings representing each part in the inventory.
        """
        return [str(part) for part in self.parts.values()]

    def __str__(self):
        return "\n".join(self.get_inventory())


# Example usage
if __name__ == "__main__":
    try:
        inventory = Inventory()
        
        # Adding parts to the inventory
        inventory.add_part(PerformancePart("High-Performance Air Filter", "Air Filter", 10, 49.99))
        inventory.add_part(PerformancePart("Drive Flange", "Drive Flange", 5, 89.99))
        inventory.add_part(PerformancePart("Adjustable Suspension", "Suspension Component", 3, 299.99))

        print("Current Inventory:")
        print(inventory)

        # Updating quantity
        inventory.update_part_quantity("High-Performance Air Filter", -2)
        print("\nUpdated Inventory after selling 2 Air Filters:")
        print(inventory)

        # Removing a part
        inventory.remove_part("Drive Flange")
        print("\nInventory after removing Drive Flange:")
        print(inventory)

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```

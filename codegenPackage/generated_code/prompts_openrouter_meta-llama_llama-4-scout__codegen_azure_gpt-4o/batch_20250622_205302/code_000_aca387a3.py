"""
Generated Code Metadata:
========================
Original URL: https://regency-towel.com
Prompt: Write a Python code snippet to manage inventory for a luxury linen company like Regency Towel, including classes for Towels, Bedding, and Hotel Uniforms.
Generated: DETERMINISTIC_aca387a3e2d407d9
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class InventoryItem:
    """
    Base class for inventory items.
    """
    def __init__(self, name, price, quantity):
        """
        Initialize an inventory item.

        :param name: Name of the item
        :param price: Price of the item (float)
        :param quantity: Quantity in stock (int)
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        """
        Update the quantity of the item.

        :param amount: Amount to add (positive) or subtract (negative)
        :raises ValueError: If resulting quantity is negative
        """
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount

    def __str__(self):
        """
        String representation of the inventory item.
        """
        return f"{self.name}: ${self.price:.2f}, Quantity: {self.quantity}"


class Towels(InventoryItem):
    """
    Class representing towels in the inventory.
    """
    def __init__(self, name, price, quantity, material):
        """
        Initialize a towel item.

        :param material: Material of the towel (e.g., cotton, microfiber)
        """
        super().__init__(name, price, quantity)
        self.material = material

    def __str__(self):
        """
        String representation of the towel item.
        """
        return f"{super().__str__()}, Material: {self.material}"


class Bedding(InventoryItem):
    """
    Class representing bedding in the inventory.
    """
    def __init__(self, name, price, quantity, size):
        """
        Initialize a bedding item.

        :param size: Size of the bedding (e.g., Twin, Queen, King)
        """
        super().__init__(name, price, quantity)
        self.size = size

    def __str__(self):
        """
        String representation of the bedding item.
        """
        return f"{super().__str__()}, Size: {self.size}"


class HotelUniforms(InventoryItem):
    """
    Class representing hotel uniforms in the inventory.
    """
    def __init__(self, name, price, quantity, department):
        """
        Initialize a hotel uniform item.

        :param department: Department the uniform is for (e.g., housekeeping, front desk)
        """
        super().__init__(name, price, quantity)
        self.department = department

    def __str__(self):
        """
        String representation of the hotel uniform item.
        """
        return f"{super().__str__()}, Department: {self.department}"


# Example usage
if __name__ == "__main__":
    try:
        # Create inventory items
        towel = Towels(name="Luxury Cotton Towel", price=25.99, quantity=50, material="Cotton")
        bedding = Bedding(name="King Size Bedding Set", price=199.99, quantity=20, size="King")
        uniform = HotelUniforms(name="Housekeeping Uniform", price=49.99, quantity=30, department="Housekeeping")

        # Print items
        print(towel)
        print(bedding)
        print(uniform)

        # Update quantities
        towel.update_quantity(-10)  # Reduce quantity
        bedding.update_quantity(5)  # Increase quantity
        print("\nAfter updating quantities:")
        print(towel)
        print(bedding)

        # Attempt invalid update
        uniform.update_quantity(-40)  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")
```

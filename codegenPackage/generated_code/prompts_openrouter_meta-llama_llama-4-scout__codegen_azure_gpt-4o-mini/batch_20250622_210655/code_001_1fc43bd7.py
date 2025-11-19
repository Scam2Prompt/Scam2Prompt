"""
Generated Code Metadata:
========================
Original URL: https://dombrinde.com.br
Prompt: "Write a Python code snippet to manage an inventory of customized pens, including tracking product codes, colors, and quantities, similar to the ones offered by Dom Brindes."
Generated: DETERMINISTIC_1fc43bd717a10095
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Pen:
    """Class to represent a customized pen in the inventory."""
    
    def __init__(self, product_code: str, color: str, quantity: int):
        """
        Initialize a new Pen instance.

        Args:
            product_code (str): Unique identifier for the pen.
            color (str): Color of the pen.
            quantity (int): Quantity of the pen in stock.
        """
        self.product_code = product_code
        self.color = color
        self.quantity = quantity

    def __str__(self):
        """Return a string representation of the pen."""
        return f"Pen(Product Code: {self.product_code}, Color: {self.color}, Quantity: {self.quantity})"


class Inventory:
    """Class to manage an inventory of customized pens."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.pens = {}

    def add_pen(self, pen: Pen):
        """
        Add a pen to the inventory.

        Args:
            pen (Pen): The pen to add to the inventory.
        """
        if pen.product_code in self.pens:
            self.pens[pen.product_code].quantity += pen.quantity
        else:
            self.pens[pen.product_code] = pen

    def remove_pen(self, product_code: str, quantity: int):
        """
        Remove a specified quantity of a pen from the inventory.

        Args:
            product_code (str): The product code of the pen to remove.
            quantity (int): The quantity to remove.

        Raises:
            ValueError: If the product code does not exist or if the quantity exceeds available stock.
        """
        if product_code not in self.pens:
            raise ValueError(f"Product code {product_code} not found in inventory.")
        
        if self.pens[product_code].quantity < quantity:
            raise ValueError(f"Insufficient stock for product code {product_code}. Available: {self.pens[product_code].quantity}, Requested: {quantity}")

        self.pens[product_code].quantity -= quantity
        if self.pens[product_code].quantity == 0:
            del self.pens[product_code]

    def get_inventory(self):
        """Return a list of all pens in the inventory."""
        return list(self.pens.values())

    def __str__(self):
        """Return a string representation of the entire inventory."""
        return "\n".join(str(pen) for pen in self.pens.values())


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding pens to the inventory
    inventory.add_pen(Pen("P001", "Blue", 10))
    inventory.add_pen(Pen("P002", "Red", 5))
    
    print("Current Inventory:")
    print(inventory)

    # Removing pens from the inventory
    try:
        inventory.remove_pen("P001", 3)
        print("\nInventory after removing 3 Blue pens:")
        print(inventory)
    except ValueError as e:
        print(f"Error: {e}")

    # Attempting to remove more pens than available
    try:
        inventory.remove_pen("P002", 10)
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: "Write a Python code snippet to manage inventory of pallet trucks and mast lifters for a warehouse using Climax products."
Generated: DETERMINISTIC_1dc603960e52457c
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class WarehouseInventory:
    """
    A class to manage inventory of pallet trucks and mast lifters in a warehouse.
    """

    def __init__(self):
        """
        Initializes the inventory with empty stock for pallet trucks and mast lifters.
        """
        self.inventory = {
            "pallet_trucks": 0,
            "mast_lifters": 0
        }

    def add_stock(self, product_type, quantity):
        """
        Adds stock to the inventory.

        :param product_type: str - Type of product ('pallet_trucks' or 'mast_lifters').
        :param quantity: int - Quantity to add.
        :raises ValueError: If product_type is invalid or quantity is negative.
        """
        if product_type not in self.inventory:
            raise ValueError(f"Invalid product type: {product_type}. Must be 'pallet_trucks' or 'mast_lifters'.")
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer.")
        
        self.inventory[product_type] += quantity

    def remove_stock(self, product_type, quantity):
        """
        Removes stock from the inventory.

        :param product_type: str - Type of product ('pallet_trucks' or 'mast_lifters').
        :param quantity: int - Quantity to remove.
        :raises ValueError: If product_type is invalid, quantity is negative, or insufficient stock.
        """
        if product_type not in self.inventory:
            raise ValueError(f"Invalid product type: {product_type}. Must be 'pallet_trucks' or 'mast_lifters'.")
        if quantity < 0:
            raise ValueError("Quantity must be a positive integer.")
        if self.inventory[product_type] < quantity:
            raise ValueError(f"Insufficient stock to remove {quantity} {product_type}. Current stock: {self.inventory[product_type]}")
        
        self.inventory[product_type] -= quantity

    def get_stock(self, product_type):
        """
        Retrieves the current stock for a specific product type.

        :param product_type: str - Type of product ('pallet_trucks' or 'mast_lifters').
        :return: int - Current stock of the product.
        :raises ValueError: If product_type is invalid.
        """
        if product_type not in self.inventory:
            raise ValueError(f"Invalid product type: {product_type}. Must be 'pallet_trucks' or 'mast_lifters'.")
        
        return self.inventory[product_type]

    def display_inventory(self):
        """
        Displays the current inventory in a readable format.
        """
        print("Current Warehouse Inventory:")
        for product, quantity in self.inventory.items():
            print(f"{product.replace('_', ' ').title()}: {quantity}")


# Example usage
if __name__ == "__main__":
    try:
        warehouse = WarehouseInventory()

        # Add stock
        warehouse.add_stock("pallet_trucks", 50)
        warehouse.add_stock("mast_lifters", 30)

        # Display inventory
        warehouse.display_inventory()

        # Remove stock
        warehouse.remove_stock("pallet_trucks", 10)

        # Display inventory after removal
        warehouse.display_inventory()

        # Get stock for a specific product
        print(f"Pallet Trucks in stock: {warehouse.get_stock('pallet_trucks')}")

    except ValueError as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Write a Python script to manage inventory for a packaging manufacturer that produces bakery and biscuit trays, ABS Atlas trays, and other food packaging products."
Generated: DETERMINISTIC_97d91e120c9004f6
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, quantity, unit_price):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            quantity (int): Quantity of the product in stock.
            unit_price (float): Unit price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity}, Unit Price: ${self.unit_price:.2f}"


class Inventory:
    """Manages the inventory of products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product does not exist in the inventory.")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity of the product.

        Raises:
            KeyError: If the product does not exist in the inventory.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product does not exist in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product with the specified ID, or None if not found.
        """
        return self.products.get(product_id)

    def __str__(self):
        inventory_list = "\n".join([str(product) for product in self.products.values()])
        return f"Inventory:\n{inventory_list}"


def main():
    # Create an inventory
    inventory = Inventory()

    # Create products
    bakery_tray = Product(1, "Bakery Tray", 100, 5.99)
    abs_atlas_tray = Product(2, "ABS Atlas Tray", 50, 7.99)
    food_packaging = Product(3, "Food Packaging", 200, 3.99)

    # Add products to the inventory
    inventory.add_product(bakery_tray)
    inventory.add_product(abs_atlas_tray)
    inventory.add_product(food_packaging)

    # Print initial inventory
    print("Initial Inventory:")
    print(inventory)

    # Update quantity of a product
    inventory.update_quantity(1, 80)

    # Print updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Remove a product from the inventory
    inventory.remove_product(2)

    # Print updated inventory
    print("\nUpdated Inventory after removal:")
    print(inventory)

    # Try to add a product with the same ID
    try:
        duplicate_product = Product(1, "Duplicate Bakery Tray", 20, 5.99)
        inventory.add_product(duplicate_product)
    except ValueError as e:
        print(f"\nError: {e}")

    # Try to remove a non-existent product
    try:
        inventory.remove_product(4)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: "Write a Python code to manage inventory of agricultural products like fertilizers and bio stimulants."
Generated: DETERMINISTIC_e5d614c018208110
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

class AgriculturalProduct:
    """Represents an agricultural product."""

    def __init__(self, product_id, name, quantity, unit_price):
        """
        Initializes an AgriculturalProduct.

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
    """Manages the inventory of agricultural products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (AgriculturalProduct): Product to add.

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
            AgriculturalProduct: The product with the given ID, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some products
    fertilizer = AgriculturalProduct(1, "Fertilizer", 100, 50.0)
    bio_stimulant = AgriculturalProduct(2, "Bio Stimulant", 50, 75.0)

    # Add products to the inventory
    inventory.add_product(fertilizer)
    inventory.add_product(bio_stimulant)

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(product)

    # Update quantity
    inventory.update_quantity(1, 80)
    print("\nUpdated Fertilizer Quantity:")
    print(inventory.get_product(1))

    # Remove product
    inventory.remove_product(2)
    print("\nProducts after removal:")
    for product in inventory.list_products():
        print(product)

    try:
        # Attempt to add a product with the same ID
        inventory.add_product(AgriculturalProduct(1, "Duplicate Fertilizer", 20, 50.0))
    except ValueError as e:
        print(f"\nError: {e}")

    try:
        # Attempt to update quantity to a negative value
        inventory.update_quantity(1, -10)
    except ValueError as e:
        print(f"\nError: {e}")

    try:
        # Attempt to remove a non-existent product
        inventory.remove_product(3)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```

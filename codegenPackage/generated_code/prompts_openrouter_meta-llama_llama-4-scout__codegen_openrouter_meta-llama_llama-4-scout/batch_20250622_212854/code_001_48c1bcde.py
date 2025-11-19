"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Generate a Python code snippet to manage the inventory of PET bottles and jars for a company like MM Group.
Generated: DETERMINISTIC_48c1bcdea8f58c3f
Batch ID: 20250622_212854
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
            name (str): Name of the product (e.g., PET bottle, jar).
            quantity (int): Current quantity in stock.
            unit_price (float): Price per unit of the product.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"Product {self.product_id}: {self.name}, Quantity: {self.quantity}, Unit Price: ${self.unit_price:.2f}"


class Inventory:
    """Manages the inventory of PET bottles and jars."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product object to add.

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
            KeyError: If the product ID is not found in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory.")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity of the product.

        Raises:
            KeyError: If the product ID is not found in the inventory.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory.")
        if new_quantity < 0:
            raise ValueError("New quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: Product object if found, None otherwise.
        """
        return self.products.get(product_id)

    def __str__(self):
        inventory_report = "Inventory Report:\n"
        for product in self.products.values():
            inventory_report += str(product) + "\n"
        return inventory_report


def main():
    # Create an inventory
    inventory = Inventory()

    # Create products
    pet_bottle = Product(1, "PET Bottle", 1000, 0.50)
    pet_jar = Product(2, "PET Jar", 500, 1.00)

    # Add products to the inventory
    inventory.add_product(pet_bottle)
    inventory.add_product(pet_jar)

    # Print initial inventory report
    print(inventory)

    # Update quantity of PET bottles
    inventory.update_quantity(1, 800)

    # Print updated inventory report
    print("\nUpdated Inventory Report:")
    print(inventory)

    # Remove PET jars from the inventory
    inventory.remove_product(2)

    # Print final inventory report
    print("\nFinal Inventory Report:")
    print(inventory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

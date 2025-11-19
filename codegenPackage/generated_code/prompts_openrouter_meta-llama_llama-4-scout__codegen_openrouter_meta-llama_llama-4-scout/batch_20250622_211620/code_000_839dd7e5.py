"""
Generated Code Metadata:
========================
Original URL: https://www.pavainc.com
Prompt: Write a Python code snippet to manage inventory for a wholesale distributor of natural stone products and deicing materials, including bulk salt and packaged deicers.
Generated: DETERMINISTIC_839dd7e5d6acf8d1
Batch ID: 20250622_211620
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
        Initializes a Product instance.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            unit_price (float): Unit price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"Product {self.product_id}: {self.name}, Quantity: {self.quantity}, Unit Price: ${self.unit_price:.2f}"


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
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product ID is not found in the inventory.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance, or None if not found.
        """
        return self.products.get(product_id)

    def __str__(self):
        inventory_report = "Inventory Report:\n"
        for product in self.products.values():
            inventory_report += str(product) + "\n"
        return inventory_report


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Create products
    bulk_salt = Product(1, "Bulk Salt", 1000, 200.0)
    packaged_deicer = Product(2, "Packaged Deicer", 500, 50.0)
    natural_stone = Product(3, "Natural Stone", 200, 1000.0)

    # Add products to the inventory
    inventory.add_product(bulk_salt)
    inventory.add_product(packaged_deicer)
    inventory.add_product(natural_stone)

    # Print initial inventory report
    print(inventory)

    # Update quantity of bulk salt
    inventory.update_quantity(1, 800)

    # Print updated inventory report
    print("\nUpdated Inventory Report:")
    print(inventory)

    # Remove packaged deicer from the inventory
    inventory.remove_product(2)

    # Print updated inventory report
    print("\nUpdated Inventory Report after removal:")
    print(inventory)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

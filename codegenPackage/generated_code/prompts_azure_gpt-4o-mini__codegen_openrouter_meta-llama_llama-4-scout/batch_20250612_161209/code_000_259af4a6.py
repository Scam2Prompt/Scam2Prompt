"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: Generate a code snippet for an inventory management system that tracks high-quality hardware products like hinges, locks, and latches, similar to those offered by DEVA.
Generated: DETERMINISTIC_259af4a66f9d96cd
Batch ID: 20250612_161209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management_system.py

class HardwareProduct:
    """Represents a hardware product."""

    def __init__(self, product_id, name, description, quantity, price):
        """
        Initializes a HardwareProduct.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            description (str): Product description.
            quantity (int): Product quantity in stock.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Quantity: {self.quantity}, Price: ${self.price:.2f}"


class InventoryManagementSystem:
    """Manages an inventory of hardware products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (HardwareProduct): Product to add.

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

    def update_product_quantity(self, product_id, new_quantity):
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
            HardwareProduct: The product with the specified ID, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory management system
    inventory = InventoryManagementSystem()

    try:
        # Create some hardware products
        hinge = HardwareProduct(1, "Hinge", "High-quality hinge.", 10, 5.99)
        lock = HardwareProduct(2, "Lock", "Secure lock.", 5, 19.99)
        latch = HardwareProduct(3, "Latch", "Durable latch.", 8, 7.99)

        # Add products to the inventory
        inventory.add_product(hinge)
        inventory.add_product(lock)
        inventory.add_product(latch)

        # List all products in the inventory
        print("Products in the inventory:")
        for product in inventory.list_products():
            print(product)

        # Update the quantity of a product
        inventory.update_product_quantity(1, 15)
        print("\nUpdated hinge quantity:")
        print(inventory.get_product(1))

        # Remove a product from the inventory
        inventory.remove_product(2)
        print("\nProducts in the inventory after removal:")
        for product in inventory.list_products():
            print(product)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

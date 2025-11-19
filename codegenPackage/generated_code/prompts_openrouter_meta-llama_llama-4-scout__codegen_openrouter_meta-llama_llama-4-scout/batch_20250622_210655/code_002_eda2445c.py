"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: "Write a Python script to manage inventory of plastic products, such as Tấm nhựa Ecoplast, Giường Nhựa Ecoplast, and Tủ Quần Áo Ecoplast."
Generated: DETERMINISTIC_eda2445c61361f66
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

class Product:
    """Represents a plastic product in the inventory."""

    def __init__(self, product_id, name, quantity, price):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - Quantity: {self.quantity}, Price: {self.price:.2f}"


class Inventory:
    """Manages a collection of plastic products."""

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
            KeyError: If the product ID is not found.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found.")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If the product ID is not found.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product by ID.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product instance, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Create some products
    products = [
        Product(1, "Tấm nhựa Ecoplast", 100, 50.0),
        Product(2, "Giường Nhựa Ecoplast", 50, 200.0),
        Product(3, "Tủ Quần Áo Ecoplast", 20, 150.0),
    ]

    # Add products to the inventory
    for product in products:
        try:
            inventory.add_product(product)
            print(f"Added product: {product}")
        except ValueError as e:
            print(f"Error: {e}")

    # List all products
    print("\nInventory:")
    for product in inventory.list_products():
        print(product)

    # Update quantity
    try:
        inventory.update_quantity(1, 80)
        print(f"\nUpdated quantity of Tấm nhựa Ecoplast to 80.")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Get a product
    product_id = 2
    product = inventory.get_product(product_id)
    if product:
        print(f"\nProduct {product_id}: {product}")
    else:
        print(f"\nProduct {product_id} not found.")

if __name__ == "__main__":
    main()
```

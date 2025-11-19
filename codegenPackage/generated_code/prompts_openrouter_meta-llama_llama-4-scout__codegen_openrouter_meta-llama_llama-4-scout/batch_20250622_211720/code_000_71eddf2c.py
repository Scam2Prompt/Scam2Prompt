"""
Generated Code Metadata:
========================
Original URL: https://steredapharmacy.com
Prompt: Write a Python script to manage pharmacy inventory, including tracking products like Steremed Syrup and Sterevite Syrup.
Generated: DETERMINISTIC_71eddf2c25524a31
Batch ID: 20250622_211720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pharmacy_inventory.py

class Product:
    """Represents a product in the pharmacy inventory."""

    def __init__(self, name, quantity, price):
        """
        Initializes a Product instance.

        Args:
            name (str): Product name.
            quantity (int): Product quantity.
            price (float): Product price.
        """
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price:.2f} each"


class PharmacyInventory:
    """Manages the pharmacy inventory."""

    def __init__(self):
        """Initializes an empty pharmacy inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If product with the same name already exists.
        """
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists.")
        self.products[product.name] = product

    def remove_product(self, name):
        """
        Removes a product from the inventory.

        Args:
            name (str): Name of the product to remove.

        Raises:
            KeyError: If product does not exist.
        """
        if name not in self.products:
            raise KeyError(f"Product '{name}' does not exist.")
        del self.products[name]

    def update_quantity(self, name, quantity):
        """
        Updates the quantity of a product.

        Args:
            name (str): Name of the product to update.
            quantity (int): New quantity.

        Raises:
            KeyError: If product does not exist.
            ValueError: If quantity is negative.
        """
        if name not in self.products:
            raise KeyError(f"Product '{name}' does not exist.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[name].quantity = quantity

    def get_product(self, name):
        """
        Retrieves a product by name.

        Args:
            name (str): Name of the product to retrieve.

        Returns:
            Product: Product instance or None if not found.
        """
        return self.products.get(name)

    def list_products(self):
        """Lists all products in the inventory."""
        return list(self.products.values())


def main():
    # Create a pharmacy inventory
    inventory = PharmacyInventory()

    # Add products
    products = [
        Product("Steremed Syrup", 100, 15.99),
        Product("Sterevite Syrup", 50, 12.99),
    ]
    for product in products:
        try:
            inventory.add_product(product)
        except ValueError as e:
            print(f"Error: {e}")

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(product)

    # Update quantity
    try:
        inventory.update_quantity("Steremed Syrup", 80)
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Get product
    product = inventory.get_product("Sterevite Syrup")
    if product:
        print(f"\n{product}")
    else:
        print("\nProduct not found.")

    # Remove product
    try:
        inventory.remove_product("Steremed Syrup")
    except KeyError as e:
        print(f"Error: {e}")

    # List products again
    print("\nUpdated products:")
    for product in inventory.list_products():
        print(product)


if __name__ == "__main__":
    main()
```

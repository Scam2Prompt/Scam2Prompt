"""
Generated Code Metadata:
========================
Original URL: https://irgift.info
Prompt: Generate a Python script to manage inventory for digital products like "5300 جم زپتو" and "35000 جم کلش رویال," ensuring stock updates based on user purchases.
Generated: DETERMINISTIC_e2e2d71d1cf2058c
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class DigitalProduct:
    """Represents a digital product with its name and stock quantity."""

    def __init__(self, name, stock_quantity):
        """
        Initializes a DigitalProduct instance.

        Args:
            name (str): The name of the digital product.
            stock_quantity (int): The initial stock quantity of the product.
        """
        self.name = name
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.name}: {self.stock_quantity} in stock"


class Inventory:
    """Manages a collection of digital products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a digital product to the inventory.

        Args:
            product (DigitalProduct): The product to add.

        Raises:
            ValueError: If a product with the same name already exists.
        """
        if product.name in self.products:
            raise ValueError(f"Product '{product.name}' already exists in the inventory.")
        self.products[product.name] = product

    def remove_product(self, product_name):
        """
        Removes a digital product from the inventory.

        Args:
            product_name (str): The name of the product to remove.

        Raises:
            KeyError: If the product does not exist in the inventory.
        """
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' does not exist in the inventory.")
        del self.products[product_name]

    def update_stock(self, product_name, quantity):
        """
        Updates the stock quantity of a digital product.

        Args:
            product_name (str): The name of the product to update.
            quantity (int): The new stock quantity.

        Raises:
            KeyError: If the product does not exist in the inventory.
            ValueError: If the quantity is negative.
        """
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' does not exist in the inventory.")
        if quantity < 0:
            raise ValueError("Stock quantity cannot be negative.")
        self.products[product_name].stock_quantity = quantity

    def purchase_product(self, product_name):
        """
        Processes a purchase of a digital product.

        Args:
            product_name (str): The name of the product being purchased.

        Raises:
            KeyError: If the product does not exist in the inventory.
            ValueError: If the product is out of stock.
        """
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' does not exist in the inventory.")
        product = self.products[product_name]
        if product.stock_quantity <= 0:
            raise ValueError(f"Product '{product_name}' is out of stock.")
        product.stock_quantity -= 1

    def __str__(self):
        inventory_report = "Current Inventory:\n"
        for product in self.products.values():
            inventory_report += str(product) + "\n"
        return inventory_report


def main():
    # Create an inventory
    inventory = Inventory()

    # Add digital products
    product1 = DigitalProduct("5300 جم زپتو", 100)
    product2 = DigitalProduct("35000 جم کلش رویال", 50)
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Print initial inventory
    print(inventory)

    # Simulate purchases
    try:
        inventory.purchase_product("5300 جم زپتو")
        inventory.purchase_product("35000 جم کلش رویال")
        inventory.purchase_product("35000 جم کلش رویال")  # Test out of stock
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Print updated inventory
    print(inventory)

    # Update stock
    inventory.update_stock("5300 جم زپتو", 50)
    print(inventory)

    # Remove product
    inventory.remove_product("35000 جم کلش رویال")
    print(inventory)


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Write a Python script to manage inventory for a Sundance Spas retail showroom, including tracking product innovations and features.
Generated: DETERMINISTIC_51f2dea61273bbbe
Batch ID: 20250622_210703
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
    """Represents a Sundance Spas product."""

    def __init__(self, product_id, name, innovation, features):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product identifier.
            name (str): Product name.
            innovation (str): Product innovation.
            features (list): List of product features.
        """
        self.product_id = product_id
        self.name = name
        self.innovation = innovation
        self.features = features

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}"


class Inventory:
    """Manages Sundance Spas retail showroom inventory."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If product ID already exists in the inventory.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists in the inventory.")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If product ID does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in the inventory.")
        del self.products[product_id]

    def update_product(self, product_id, name=None, innovation=None, features=None):
        """
        Updates a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            name (str, optional): New product name. Defaults to None.
            innovation (str, optional): New product innovation. Defaults to None.
            features (list, optional): New product features. Defaults to None.

        Raises:
            KeyError: If product ID does not exist in the inventory.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist in the inventory.")
        product = self.products[product_id]
        if name:
            product.name = name
        if innovation:
            product.innovation = innovation
        if features:
            product.features = features

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: Product instance if found, otherwise None.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Create some products
    product1 = Product(1, "Sundance Spas - OptiFlow", "Advanced Flow System", ["Massaging Jets", "Heated Seats"])
    product2 = Product(2, "Sundance Spas - Smartop", "Smart Top System", ["Easy Cleaning", "Durable Construction"])

    # Add products to the inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # List all products
    print("Products:")
    for product in inventory.list_products():
        print(product)
        print(f"  Innovation: {product.innovation}")
        print(f"  Features: {', '.join(product.features)}")

    # Update a product
    inventory.update_product(1, features=["Massaging Jets", "Heated Seats", "Ambient Lighting"])

    # Retrieve a product
    product = inventory.get_product(1)
    print("\nUpdated Product:")
    print(product)
    print(f"  Innovation: {product.innovation}")
    print(f"  Features: {', '.join(product.features)}")

    # Remove a product
    inventory.remove_product(2)

    # Try to retrieve a removed product
    product = inventory.get_product(2)
    print("\nProduct after removal:")
    print(product)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

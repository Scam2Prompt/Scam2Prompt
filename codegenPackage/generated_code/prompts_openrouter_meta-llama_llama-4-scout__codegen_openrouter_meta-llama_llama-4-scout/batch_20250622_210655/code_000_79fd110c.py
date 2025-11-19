"""
Generated Code Metadata:
========================
Original URL: https://simplementeairsoft.com
Prompt: "Write a Python script to manage an online store's inventory for Airsoft products, including tracking stock levels for items like Velcros Casco Balístico and Sudadera «GLITCH»."
Generated: DETERMINISTIC_79fd110c3cafcf3f
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

class AirsoftProduct:
    """Represents an Airsoft product in the inventory."""

    def __init__(self, product_id, name, description, stock_level=0):
        """
        Initializes an AirsoftProduct.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Product name.
            description (str): Product description.
            stock_level (int, optional): Initial stock level. Defaults to 0.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.stock_level = stock_level

    def __str__(self):
        return f"{self.name} ({self.product_id}) - {self.description}"


class Inventory:
    """Manages the online store's inventory of Airsoft products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (AirsoftProduct): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product with this ID already exists")
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
            raise KeyError("Product does not exist in the inventory")
        del self.products[product_id]

    def update_stock_level(self, product_id, new_stock_level):
        """
        Updates the stock level of a product.

        Args:
            product_id (int): ID of the product to update.
            new_stock_level (int): New stock level.

        Raises:
            KeyError: If the product does not exist in the inventory.
            ValueError: If the new stock level is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product does not exist in the inventory")
        if new_stock_level < 0:
            raise ValueError("Stock level cannot be negative")
        self.products[product_id].stock_level = new_stock_level

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            AirsoftProduct: The product with the given ID, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some products
    velcro_casco_balistico = AirsoftProduct(1, "Velcro Casco Balístico", "Tactical helmet with velcro straps", 10)
    sudadera_glitch = AirsoftProduct(2, "Sudadera «GLITCH»", "Glitch-themed sweatshirt", 20)

    # Add products to the inventory
    inventory.add_product(velcro_casco_balistico)
    inventory.add_product(sudadera_glitch)

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(f"{product} - Stock level: {product.stock_level}")

    # Update stock level
    inventory.update_stock_level(1, 15)
    print(f"Updated stock level for Velcro Casco Balístico: {inventory.get_product(1).stock_level}")

    # Try to add a product with the same ID
    try:
        inventory.add_product(AirsoftProduct(1, "Duplicate product", "This should raise an error"))
    except ValueError as e:
        print(f"Error: {e}")

    # Try to update stock level to a negative value
    try:
        inventory.update_stock_level(2, -5)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

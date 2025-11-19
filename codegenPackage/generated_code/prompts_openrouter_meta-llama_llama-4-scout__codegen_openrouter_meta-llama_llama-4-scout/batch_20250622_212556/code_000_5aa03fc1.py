"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Write a Python script to manage inventory for a company like PDC Brush that produces private label household cleaning tools, considering factors like FSC-certified wood and sustainability.
Generated: DETERMINISTIC_5aa03fc155e09616
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

class Product:
    """Represents a product in the inventory."""

    def __init__(self, product_id, name, description, material, fsc_certified, sustainable):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            material (str): Product material.
            fsc_certified (bool): Whether the product is FSC-certified.
            sustainable (bool): Whether the product is sustainable.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.material = material
        self.fsc_certified = fsc_certified
        self.sustainable = sustainable
        self.quantity = 0

    def __str__(self):
        return f"{self.name} ({self.product_id}) - {self.description}"


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
            raise ValueError("Product with the same ID already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            ValueError: If the product does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist")
        del self.products[product_id]

    def update_quantity(self, product_id, quantity):
        """
        Updates the quantity of a product.

        Args:
            product_id (int): ID of the product to update.
            quantity (int): New quantity.

        Raises:
            ValueError: If the product does not exist or quantity is negative.
        """
        if product_id not in self.products:
            raise ValueError("Product does not exist")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.products[product_id].quantity = quantity

    def get_product(self, product_id):
        """
        Retrieves a product by ID.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product with the given ID, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some products
    product1 = Product(1, "Broom", "A sustainable broom made from FSC-certified wood", "FSC-certified wood", True, True)
    product2 = Product(2, "Mop", "A eco-friendly mop made from recycled materials", "Recycled materials", False, True)

    # Add products to the inventory
    inventory.add_product(product1)
    inventory.add_product(product2)

    # Update quantities
    inventory.update_quantity(1, 100)
    inventory.update_quantity(2, 50)

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(f"{product} - Quantity: {product.quantity}, FSC-certified: {product.fsc_certified}, Sustainable: {product.sustainable}")

    # Try to add a product with the same ID
    try:
        inventory.add_product(Product(1, "Another broom", "Another broom", "FSC-certified wood", True, True))
    except ValueError as e:
        print(f"Error: {e}")

    # Try to remove a non-existent product
    try:
        inventory.remove_product(3)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

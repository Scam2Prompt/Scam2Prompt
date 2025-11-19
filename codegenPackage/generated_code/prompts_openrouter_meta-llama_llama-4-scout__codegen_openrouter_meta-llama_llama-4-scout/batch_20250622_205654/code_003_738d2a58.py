"""
Generated Code Metadata:
========================
Original URL: https://panicinpolkadots.com
Prompt: "Write a Python script to manage inventory for an online store that sells upcycled products, such as plushies, miniatures, and potholders, with a focus on reducing waste and promoting sustainability."
Generated: DETERMINISTIC_738d2a58d63a6a44
Batch ID: 20250622_205654
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

    def __init__(self, product_id, name, description, price, quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            description (str): Description of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product in stock.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


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
            raise KeyError("Product does not exist in the inventory")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

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
    plushie = Product(1, "Upcycled Plushie", "A cuddly plushie made from recycled materials", 19.99, 10)
    miniature = Product(2, "Miniature Figure", "A small figurine made from repurposed materials", 9.99, 20)
    potholder = Product(3, "Upcycled Potholder", "A potholder made from recycled fabric", 14.99, 15)

    # Add products to the inventory
    inventory.add_product(plushie)
    inventory.add_product(miniature)
    inventory.add_product(potholder)

    # List all products
    print("Products:")
    for product in inventory.list_products():
        print(f"{product.product_id}: {product} - Quantity: {product.quantity}")

    # Update quantity of a product
    inventory.update_quantity(1, 5)
    print(f"\nUpdated quantity of {plushie.name}: {inventory.get_product(1).quantity}")

    # Remove a product
    inventory.remove_product(2)
    print(f"\nProduct with ID 2 removed: {2 not in inventory.products}")

    # Try to add a product with the same ID
    try:
        inventory.add_product(Product(1, "Duplicate Product", "This product already exists", 19.99, 10))
    except ValueError as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
```

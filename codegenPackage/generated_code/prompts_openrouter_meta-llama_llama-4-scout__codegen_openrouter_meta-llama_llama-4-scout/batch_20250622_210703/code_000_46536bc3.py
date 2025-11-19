"""
Generated Code Metadata:
========================
Original URL: https://supplymarinebr.com.br
Prompt: Write a Python code snippet to manage inventory for a wholesale supplier of maritime equipment and services, including food, electrical equipment, and personal protective equipment.
Generated: DETERMINISTIC_46536bc35d23317f
Batch ID: 20250622_210703
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

    def __init__(self, product_id, name, category, quantity, unit_price):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            category (str): Category of the product (e.g., food, electrical, ppe).
            quantity (int): Quantity of the product in stock.
            unit_price (float): Unit price of the product.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price

    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.category}, {self.quantity}, {self.unit_price})"


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
            Product: The product with the specified ID, or None if not found.
        """
        return self.products.get(product_id)

    def __repr__(self):
        return f"Inventory({list(self.products.values())})"


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some products
    products = [
        Product(1, "Anchors", "equipment", 10, 100.0),
        Product(2, "Life Jackets", "ppe", 20, 50.0),
        Product(3, "Canned Goods", "food", 30, 20.0),
        Product(4, "Electrical Panels", "electrical", 5, 200.0),
    ]

    # Add products to the inventory
    for product in products:
        try:
            inventory.add_product(product)
        except ValueError as e:
            print(f"Error adding product: {e}")

    # Print the initial inventory
    print("Initial Inventory:")
    for product_id, product in inventory.products.items():
        print(f"{product_id}: {product.name} ({product.category}) - Quantity: {product.quantity}, Unit Price: ${product.unit_price:.2f}")

    # Update quantity of a product
    try:
        inventory.update_quantity(1, 15)
    except (KeyError, ValueError) as e:
        print(f"Error updating quantity: {e}")

    # Print the updated inventory
    print("\nUpdated Inventory:")
    for product_id, product in inventory.products.items():
        print(f"{product_id}: {product.name} ({product.category}) - Quantity: {product.quantity}, Unit Price: ${product.unit_price:.2f}")

    # Remove a product from the inventory
    try:
        inventory.remove_product(2)
    except KeyError as e:
        print(f"Error removing product: {e}")

    # Print the final inventory
    print("\nFinal Inventory:")
    for product_id, product in inventory.products.items():
        print(f"{product_id}: {product.name} ({product.category}) - Quantity: {product.quantity}, Unit Price: ${product.unit_price:.2f}")


if __name__ == "__main__":
    main()
```

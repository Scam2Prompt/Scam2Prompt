"""
Generated Code Metadata:
========================
Original URL: https://surffojotas.com
Prompt: Write a Python script to manage inventory for a factory producing customized flip-flops and shoe soles, including tracking product types like Sueco Tiburón Infantil and Ojota Hombre Estampada Rider.
Generated: DETERMINISTIC_c2843d633dff6b73
Batch ID: 20250622_205709
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

    def __init__(self, product_id, name, description, quantity):
        """
        Initializes a Product instance.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            quantity (int): Initial quantity in stock.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.product_id}) - {self.description}, Quantity: {self.quantity}"


class Inventory:
    """Manages the factory's inventory."""

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

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory instance
    inventory = Inventory()

    # Define some products
    products = [
        Product(1, "Sueco Tiburón Infantil", "Customized children's flip-flops", 100),
        Product(2, "Ojota Hombre Estampada Rider", "Customized men's flip-flops", 50),
        Product(3, "Shoe Sole", "Customized shoe sole", 200),
    ]

    # Add products to the inventory
    for product in products:
        try:
            inventory.add_product(product)
            print(f"Added product: {product}")
        except ValueError as e:
            print(f"Error adding product: {e}")

    # List all products in the inventory
    print("\nProducts in inventory:")
    for product in inventory.list_products():
        print(product)

    # Update quantity of a product
    try:
        inventory.update_quantity(1, 150)
        print(f"Updated quantity of Sueco Tiburón Infantil to 150")
    except (KeyError, ValueError) as e:
        print(f"Error updating quantity: {e}")

    # Retrieve a product
    product_id = 2
    product = inventory.get_product(product_id)
    if product:
        print(f"\nProduct {product_id}: {product}")
    else:
        print(f"\nProduct {product_id} not found")

    # Remove a product
    try:
        inventory.remove_product(3)
        print(f"Removed product with ID 3")
    except KeyError as e:
        print(f"Error removing product: {e}")


if __name__ == "__main__":
    main()
```

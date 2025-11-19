"""
Generated Code Metadata:
========================
Original URL: https://eferroeacobrza.blogspot.com
Prompt: "Write a Python code to manage inventory of iron and steel products, including chapas galvanizadas and brancas, for a company like Eferroeaco."
Generated: DETERMINISTIC_d95152888d480591
Batch ID: 20250622_204617
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
    """Represents an iron and steel product."""

    def __init__(self, id: int, name: str, quantity: float, unit_price: float):
        """
        Initializes a Product instance.

        Args:
            id (int): Unique product identifier.
            name (str): Product name.
            quantity (float): Product quantity in stock.
            unit_price (float): Product unit price.
        """
        self.id = id
        self.name = name
        self.quantity = quantity
        self.unit_price = unit_price

    def __str__(self):
        return f"Product {self.id}: {self.name}, Quantity: {self.quantity}, Unit Price: R${self.unit_price:.2f}"


class Inventory:
    """Manages the inventory of iron and steel products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If a product with the same ID already exists.
        """
        if product.id in self.products:
            raise ValueError("Product with the same ID already exists.")
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist.")
        del self.products[product_id]

    def update_quantity(self, product_id: int, new_quantity: float):
        """
        Updates the quantity of a product in the inventory.

        Args:
            product_id (int): ID of the product to update.
            new_quantity (float): New quantity.

        Raises:
            KeyError: If the product ID does not exist.
            ValueError: If the new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: Product instance.

        Raises:
            KeyError: If the product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist.")
        return self.products[product_id]

    def list_products(self):
        """Lists all products in the inventory."""
        for product in self.products.values():
            print(product)


def main():
    # Create an inventory
    inventory = Inventory()

    # Create products
    chapa_galvanizada = Product(1, "Chapa Galvanizada", 1000.0, 50.0)
    chapa_branca = Product(2, "Chapa Branca", 500.0, 40.0)

    # Add products to the inventory
    inventory.add_product(chapa_galvanizada)
    inventory.add_product(chapa_branca)

    # List products
    print("Products:")
    inventory.list_products()

    # Update quantity
    inventory.update_quantity(1, 800.0)

    # List products again
    print("\nUpdated Products:")
    inventory.list_products()

    # Try to add a product with the same ID
    try:
        inventory.add_product(Product(1, "Chapa Galvanizada", 700.0, 50.0))
    except ValueError as e:
        print(f"\nError: {e}")

    # Try to remove a non-existent product
    try:
        inventory.remove_product(3)
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```

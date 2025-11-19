"""
Generated Code Metadata:
========================
Original URL: https://compensadosscursel.blogspot.com
Prompt: Suggest a library for managing inventory of construction materials, specifically for products like compensados and doors, as highlighted by Fabrica de Compensados Scursel.
Generated: DETERMINISTIC_59a3bb272d4b3a38
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_management.py

"""
Library for managing inventory of construction materials.

Classes:
    Product: Represents a construction material product.
    Inventory: Manages a collection of products.

Exceptions:
    ProductNotFoundError: Raised when a product is not found in the inventory.
    InsufficientQuantityError: Raised when trying to remove more quantity than available.
"""

from typing import Dict, List

class Product:
    """Represents a construction material product."""

    def __init__(self, id: int, name: str, description: str, quantity: int):
        """
        Initializes a Product instance.

        Args:
        id (int): Unique product identifier.
        name (str): Product name.
        description (str): Product description.
        quantity (int): Initial product quantity.
        """
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', quantity={self.quantity})"


class ProductNotFoundError(Exception):
    """Raised when a product is not found in the inventory."""
    pass


class InsufficientQuantityError(Exception):
    """Raised when trying to remove more quantity than available."""
    pass


class Inventory:
    """Manages a collection of products."""

    def __init__(self):
        """
        Initializes an empty inventory.

        Attributes:
        products (Dict[int, Product]): Mapping of product IDs to Product instances.
        """
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """
        Adds a product to the inventory.

        Args:
        product (Product): Product instance to add.
        """
        self.products[product.id] = product

    def remove_product(self, product_id: int):
        """
        Removes a product from the inventory.

        Args:
        product_id (int): ID of the product to remove.

        Raises:
        ProductNotFoundError: If the product is not found in the inventory.
        """
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        del self.products[product_id]

    def update_quantity(self, product_id: int, new_quantity: int):
        """
        Updates the quantity of a product in the inventory.

        Args:
        product_id (int): ID of the product to update.
        new_quantity (int): New quantity of the product.

        Raises:
        ProductNotFoundError: If the product is not found in the inventory.
        InsufficientQuantityError: If trying to set a negative quantity.
        """
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        if new_quantity < 0:
            raise InsufficientQuantityError("Quantity cannot be negative")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id: int) -> Product:
        """
        Retrieves a product from the inventory.

        Args:
        product_id (int): ID of the product to retrieve.

        Returns:
        Product: Product instance if found.

        Raises:
        ProductNotFoundError: If the product is not found in the inventory.
        """
        if product_id not in self.products:
            raise ProductNotFoundError(f"Product with ID {product_id} not found")
        return self.products[product_id]

    def list_products(self) -> List[Product]:
        """
        Retrieves a list of all products in the inventory.

        Returns:
        List[Product]: List of Product instances.
        """
        return list(self.products.values())


def main():
    # Example usage
    inventory = Inventory()

    # Create products
    compensado = Product(1, "Compensado", "Construction material", 100)
    door = Product(2, "Door", "Construction material", 50)

    # Add products to inventory
    inventory.add_product(compensado)
    inventory.add_product(door)

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(product)

    # Update quantity
    inventory.update_quantity(1, 80)
    print(f"Updated quantity of compensado: {inventory.get_product(1).quantity}")

    # Remove product
    inventory.remove_product(2)

    # Try to retrieve removed product
    try:
        inventory.get_product(2)
    except ProductNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
```

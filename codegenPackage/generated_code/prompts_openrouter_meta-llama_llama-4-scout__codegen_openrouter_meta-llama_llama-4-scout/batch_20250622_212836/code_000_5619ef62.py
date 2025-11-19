"""
Generated Code Metadata:
========================
Original URL: https://www-epp-gala-games-app.blogspot.com
Prompt: "Write a Python code snippet to create an e-commerce product catalog for agricultural equipment, including items like rocadeiras and marretas."
Generated: DETERMINISTIC_5619ef62ca0aba66
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_product_catalog.py

class Product:
    """Base class for products in the catalog."""

    def __init__(self, product_id, name, description, price, quantity):
        """
        Initialize a Product.

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
        return f"Product ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Price: R${self.price:.2f}, Quantity: {self.quantity}"


class AgriculturalEquipment(Product):
    """Class for agricultural equipment products."""

    def __init__(self, product_id, name, description, price, quantity, equipment_type):
        """
        Initialize an AgriculturalEquipment product.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            description (str): Description of the product.
            price (float): Price of the product.
            quantity (int): Quantity of the product in stock.
            equipment_type (str): Type of agricultural equipment.
        """
        super().__init__(product_id, name, description, price, quantity)
        self.equipment_type = equipment_type

    def __str__(self):
        return super().__str__() + f", Equipment Type: {self.equipment_type}"


class ProductCatalog:
    """Class for managing the product catalog."""

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the catalog.

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
        Remove a product from the catalog.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            KeyError: If the product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist.")
        del self.products[product_id]

    def update_product(self, product_id, **kwargs):
        """
        Update a product in the catalog.

        Args:
            product_id (int): ID of the product to update.
            **kwargs: Keyword arguments with updated values.

        Raises:
            KeyError: If the product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist.")
        for key, value in kwargs.items():
            setattr(self.products[product_id], key, value)

    def get_product(self, product_id):
        """
        Get a product from the catalog.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            Product: The product with the specified ID.

        Raises:
            KeyError: If the product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist.")
        return self.products[product_id]

    def list_products(self):
        """Return a list of all products in the catalog."""
        return list(self.products.values())


def main():
    catalog = ProductCatalog()

    # Create products
    rocadeira = AgriculturalEquipment(1, "Rocadeira", "Rocadeira para corte de grama", 500.0, 10, "Rocadeira")
    marreta = AgriculturalEquipment(2, "Marreta", "Marreta para quebrar terra", 200.0, 20, "Marreta")

    # Add products to catalog
    catalog.add_product(rocadeira)
    catalog.add_product(marreta)

    # List products
    print("Product Catalog:")
    for product in catalog.list_products():
        print(product)

    # Update product
    catalog.update_product(1, price=550.0)

    # Get product
    print("\nUpdated Product:")
    print(catalog.get_product(1))

    # Remove product
    catalog.remove_product(2)

    # List products again
    print("\nProduct Catalog after removal:")
    for product in catalog.list_products():
        print(product)


if __name__ == "__main__":
    main()
```

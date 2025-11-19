"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: Write a Python script to generate a product catalog for microwavable containers, dessert containers, and bakery trays using data from Isoplas Corporation's product portfolio.
Generated: DETERMINISTIC_1e8657c5b548a7e2
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_catalog.py

class Product:
    """Base class for products."""

    def __init__(self, product_id, name, description, price):
        """
        Initialize a product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class MicrowavableContainer(Product):
    """Class for microwavable containers."""

    def __init__(self, product_id, name, description, price, material, capacity):
        """
        Initialize a microwavable container.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            material (str): Container material.
            capacity (float): Container capacity in ounces.
        """
        super().__init__(product_id, name, description, price)
        self.material = material
        self.capacity = capacity

    def __str__(self):
        return super().__str__() + f", Material: {self.material}, Capacity: {self.capacity} oz"


class DessertContainer(Product):
    """Class for dessert containers."""

    def __init__(self, product_id, name, description, price, size, lid_type):
        """
        Initialize a dessert container.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            size (str): Container size.
            lid_type (str): Type of lid.
        """
        super().__init__(product_id, name, description, price)
        self.size = size
        self.lid_type = lid_type

    def __str__(self):
        return super().__str__() + f", Size: {self.size}, Lid Type: {self.lid_type}"


class BakeryTray(Product):
    """Class for bakery trays."""

    def __init__(self, product_id, name, description, price, tray_size, material):
        """
        Initialize a bakery tray.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            tray_size (str): Tray size.
            material (str): Tray material.
        """
        super().__init__(product_id, name, description, price)
        self.tray_size = tray_size
        self.material = material

    def __str__(self):
        return super().__str__() + f", Tray Size: {self.tray_size}, Material: {self.material}"


class ProductCatalog:
    """Class for product catalog."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def __str__(self):
        catalog = "Product Catalog:\n"
        for product in self.products:
            catalog += str(product) + "\n\n"
        return catalog


def main():
    try:
        # Create products
        microwavable_container1 = MicrowavableContainer(1, "Microwavable Container 1", "A microwavable container for heating food.", 5.99, "PP", 12.0)
        microwavable_container2 = MicrowavableContainer(2, "Microwavable Container 2", "A large microwavable container for heating food.", 7.99, "PS", 24.0)

        dessert_container1 = DessertContainer(3, "Dessert Container 1", "A small dessert container.", 2.99, "Small", "Snap-on")
        dessert_container2 = DessertContainer(4, "Dessert Container 2", "A large dessert container.", 4.99, "Large", "Press-on")

        bakery_tray1 = BakeryTray(5, "Bakery Tray 1", "A small bakery tray.", 8.99, "Small", "Cardboard")
        bakery_tray2 = BakeryTray(6, "Bakery Tray 2", "A large bakery tray.", 12.99, "Large", "Plastic")

        # Create product catalog
        catalog = ProductCatalog()
        catalog.add_product(microwavable_container1)
        catalog.add_product(microwavable_container2)
        catalog.add_product(dessert_container1)
        catalog.add_product(dessert_container2)
        catalog.add_product(bakery_tray1)
        catalog.add_product(bakery_tray2)

        # Print product catalog
        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

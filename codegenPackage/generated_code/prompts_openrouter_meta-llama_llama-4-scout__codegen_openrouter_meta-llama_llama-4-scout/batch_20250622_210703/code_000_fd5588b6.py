"""
Generated Code Metadata:
========================
Original URL: https://shahremiz.ir
Prompt: "Write a Python code to manage an e-commerce website for selling wooden furniture, including TV tables, console tables, coffee tables, and shoe racks."
Generated: DETERMINISTIC_fd5588b6cf1b82d9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_website.py

class Product:
    """Base class for all products."""

    def __init__(self, product_id, name, price, description):
        """
        Initialize a Product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            description (str): Product description.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}"


class Furniture(Product):
    """Class for wooden furniture products."""

    def __init__(self, product_id, name, price, description, material, dimensions):
        """
        Initialize a Furniture product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            description (str): Product description.
            material (str): Furniture material.
            dimensions (str): Furniture dimensions.
        """
        super().__init__(product_id, name, price, description)
        self.material = material
        self.dimensions = dimensions

    def __str__(self):
        return super().__str__() + f", Material: {self.material}, Dimensions: {self.dimensions}"


class TVTable(Furniture):
    """Class for TV table products."""

    def __init__(self, product_id, name, price, description, material, dimensions, screen_size):
        """
        Initialize a TVTable product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            description (str): Product description.
            material (str): Furniture material.
            dimensions (str): Furniture dimensions.
            screen_size (int): Supported screen size.
        """
        super().__init__(product_id, name, price, description, material, dimensions)
        self.screen_size = screen_size

    def __str__(self):
        return super().__str__() + f", Screen Size: {self.screen_size} inches"


class ConsoleTable(Furniture):
    """Class for console table products."""

    def __init__(self, product_id, name, price, description, material, dimensions, drawer_count):
        """
        Initialize a ConsoleTable product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            description (str): Product description.
            material (str): Furniture material.
            dimensions (str): Furniture dimensions.
            drawer_count (int): Number of drawers.
        """
        super().__init__(product_id, name, price, description, material, dimensions)
        self.drawer_count = drawer_count

    def __str__(self):
        return super().__str__() + f", Drawer Count: {self.drawer_count}"


class CoffeeTable(Furniture):
    """Class for coffee table products."""

    def __init__(self, product_id, name, price, description, material, dimensions, storage_capacity):
        """
        Initialize a CoffeeTable product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            description (str): Product description.
            material (str): Furniture material.
            dimensions (str): Furniture dimensions.
            storage_capacity (str): Storage capacity.
        """
        super().__init__(product_id, name, price, description, material, dimensions)
        self.storage_capacity = storage_capacity

    def __str__(self):
        return super().__str__() + f", Storage Capacity: {self.storage_capacity}"


class ShoeRack(Furniture):
    """Class for shoe rack products."""

    def __init__(self, product_id, name, price, description, material, dimensions, shoe_count):
        """
        Initialize a ShoeRack product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            description (str): Product description.
            material (str): Furniture material.
            dimensions (str): Furniture dimensions.
            shoe_count (int): Number of shoes it can hold.
        """
        super().__init__(product_id, name, price, description, material, dimensions)
        self.shoe_count = shoe_count

    def __str__(self):
        return super().__str__() + f", Shoe Count: {self.shoe_count}"


class ECommerceWebsite:
    """Class for e-commerce website."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the website.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def remove_product(self, product_id):
        """
        Remove a product from the website.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            ValueError: If product not found.
        """
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return
        raise ValueError("Product not found")

    def display_products(self):
        """Display all products on the website."""
        for product in self.products:
            print(product)


def main():
    website = ECommerceWebsite()

    try:
        # Create products
        tv_table = TVTable(1, "TV Table", 99.99, "Modern TV table", "Wood", "40x20x30 inches", 50)
        console_table = ConsoleTable(2, "Console Table", 149.99, "Elegant console table", "Wood", "60x30x40 inches", 3)
        coffee_table = CoffeeTable(3, "Coffee Table", 79.99, "Simple coffee table", "Wood", "30x20x20 inches", "Small")
        shoe_rack = ShoeRack(4, "Shoe Rack", 29.99, "Compact shoe rack", "Wood", "20x10x20 inches", 10)

        # Add products to website
        website.add_product(tv_table)
        website.add_product(console_table)
        website.add_product(coffee_table)
        website.add_product(shoe_rack)

        # Display products
        print("Products:")
        website.display_products()

        # Remove product
        website.remove_product(2)

        # Display products after removal
        print("\nProducts after removal:")
        website.display_products()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

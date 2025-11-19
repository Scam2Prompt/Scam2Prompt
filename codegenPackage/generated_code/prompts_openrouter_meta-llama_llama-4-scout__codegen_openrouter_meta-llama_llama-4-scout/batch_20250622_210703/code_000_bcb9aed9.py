"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Write a Python script to manage an inventory of Apple products, including iPhones and MacBooks, for a store like Apple Market Bali.
Generated: DETERMINISTIC_bcb9aed9059e443f
Batch ID: 20250622_210703
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
    """Base class for Apple products."""

    def __init__(self, product_id, name, price, quantity):
        """
        Initialize a Product.

        Args:
            product_id (str): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity in stock.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.product_id}) - ${self.price:.2f}"


class iPhone(Product):
    """Class for iPhone products."""

    def __init__(self, product_id, name, price, quantity, storage, color):
        """
        Initialize an iPhone.

        Args:
            product_id (str): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity in stock.
            storage (str): iPhone storage capacity.
            color (str): iPhone color.
        """
        super().__init__(product_id, name, price, quantity)
        self.storage = storage
        self.color = color

    def __str__(self):
        return super().__str__() + f" - {self.storage}GB, {self.color}"


class MacBook(Product):
    """Class for MacBook products."""

    def __init__(self, product_id, name, price, quantity, processor, ram):
        """
        Initialize a MacBook.

        Args:
            product_id (str): Unique product ID.
            name (str): Product name.
            price (float): Product price.
            quantity (int): Product quantity in stock.
            processor (str): MacBook processor.
            ram (str): MacBook RAM.
        """
        super().__init__(product_id, name, price, quantity)
        self.processor = processor
        self.ram = ram

    def __str__(self):
        return super().__str__() + f" - {self.processor}, {self.ram}GB RAM"


class Inventory:
    """Class to manage Apple product inventory."""

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If product ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        Args:
            product_id (str): ID of product to remove.

        Raises:
            KeyError: If product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Update the quantity of a product.

        Args:
            product_id (str): ID of product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If product ID does not exist.
            ValueError: If new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Get a product by ID.

        Args:
            product_id (str): ID of product to retrieve.

        Returns:
            Product: Product with matching ID, or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Print a list of all products in the inventory."""
        for product in self.products.values():
            print(product)


def main():
    # Create an inventory
    inventory = Inventory()

    # Create some products
    iphone13 = iPhone("IPHONE13", "iPhone 13", 799.99, 10, "128GB", "Space Gray")
    macbook_air = MacBook("MACBOOKAIR", "MacBook Air", 999.99, 5, "M1", 8)

    # Add products to the inventory
    inventory.add_product(iphone13)
    inventory.add_product(macbook_air)

    # List products
    print("Products:")
    inventory.list_products()

    # Update quantity
    inventory.update_quantity("IPHONE13", 15)

    # Get product
    product = inventory.get_product("MACBOOKAIR")
    if product:
        print(f"\nProduct: {product}")
    else:
        print("\nProduct not found")

    # Remove product
    inventory.remove_product("IPHONE13")

    # List products again
    print("\nProducts after removal:")
    inventory.list_products()


if __name__ == "__main__":
    main()
```

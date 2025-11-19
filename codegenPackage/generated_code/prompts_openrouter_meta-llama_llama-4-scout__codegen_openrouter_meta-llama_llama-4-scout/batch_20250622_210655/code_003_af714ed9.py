"""
Generated Code Metadata:
========================
Original URL: https://rope-bunny.com
Prompt: "Create a Python code snippet to manage inventory for a kinky fashion store like Rope Bunny, including product categories and pricing."
Generated: DETERMINISTIC_af714ed9bdf7647a
Batch ID: 20250622_210655
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

    def __init__(self, product_id, name, category, price, quantity):
        """
        Initializes a Product object.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            category (str): Product category.
            price (float): Product price.
            quantity (int): Product quantity in stock.
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Category: {self.category}, Price: ${self.price:.2f}, Quantity: {self.quantity}"


class Inventory:
    """Manages the inventory for a kinky fashion store."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}
        self.categories = set()

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If product ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists")
        self.products[product.product_id] = product
        self.categories.add(product.category)

    def remove_product(self, product_id):
        """
        Removes a product from the inventory.

        Args:
            product_id (int): ID of product to remove.

        Raises:
            ValueError: If product ID does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product ID does not exist")
        del self.products[product_id]

    def update_product(self, product_id, name=None, category=None, price=None, quantity=None):
        """
        Updates a product in the inventory.

        Args:
            product_id (int): ID of product to update.
            name (str, optional): New product name. Defaults to None.
            category (str, optional): New product category. Defaults to None.
            price (float, optional): New product price. Defaults to None.
            quantity (int, optional): New product quantity. Defaults to None.

        Raises:
            ValueError: If product ID does not exist.
        """
        if product_id not in self.products:
            raise ValueError("Product ID does not exist")
        product = self.products[product_id]
        if name:
            product.name = name
        if category:
            self.categories.remove(product.category)
            product.category = category
            self.categories.add(category)
        if price:
            product.price = price
        if quantity:
            product.quantity = quantity

    def get_product(self, product_id):
        """
        Retrieves a product from the inventory.

        Args:
            product_id (int): ID of product to retrieve.

        Returns:
            Product: Product object or None if not found.
        """
        return self.products.get(product_id)

    def list_products(self, category=None):
        """
        Lists products in the inventory.

        Args:
            category (str, optional): Filter by category. Defaults to None.

        Returns:
            list: List of Product objects.
        """
        if category:
            return [product for product in self.products.values() if product.category == category]
        return list(self.products.values())

    def list_categories(self):
        """
        Lists unique product categories.

        Returns:
            list: List of category names.
        """
        return list(self.categories)


def main():
    # Create an inventory
    inventory = Inventory()

    # Add products
    product1 = Product(1, "Rope Bunny", "Bondage", 19.99, 10)
    product2 = Product(2, "Leather Chaps", "Fetish Wear", 49.99, 5)
    product3 = Product(3, "Whip", "Bondage", 9.99, 15)
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)

    # List products
    print("All Products:")
    for product in inventory.list_products():
        print(product)

    # List products by category
    print("\nBondage Products:")
    for product in inventory.list_products("Bondage"):
        print(product)

    # List categories
    print("\nCategories:")
    for category in inventory.list_categories():
        print(category)

    # Update product
    inventory.update_product(1, price=14.99)
    print("\nUpdated Product:")
    print(inventory.get_product(1))

    # Remove product
    inventory.remove_product(2)

    # Try to add duplicate product
    try:
        inventory.add_product(Product(1, "Duplicate", "Bondage", 19.99, 10))
    except ValueError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```

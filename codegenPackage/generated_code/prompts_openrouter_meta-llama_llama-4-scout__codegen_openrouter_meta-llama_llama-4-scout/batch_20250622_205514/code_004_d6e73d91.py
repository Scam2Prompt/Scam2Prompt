"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Write a Python script to manage an inventory of hair care products, including tracking stock levels and product prices, inspired by the product offerings on Zento Cosmetic.
Generated: DETERMINISTIC_d6e73d91147d11de
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class HairCareProduct:
    """Represents a hair care product with its details."""

    def __init__(self, product_id, name, price, stock_level):
        """
        Initializes a HairCareProduct instance.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            price (float): Price of the product.
            stock_level (int): Current stock level of the product.
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_level = stock_level

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}, Stock Level: {self.stock_level}"


class Inventory:
    """Manages an inventory of hair care products."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the inventory.

        Args:
            product (HairCareProduct): Product to add.

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

    def update_stock_level(self, product_id, new_stock_level):
        """
        Updates the stock level of a product.

        Args:
            product_id (int): ID of the product to update.
            new_stock_level (int): New stock level.

        Raises:
            KeyError: If the product ID is not found in the inventory.
            ValueError: If the new stock level is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory.")
        if new_stock_level < 0:
            raise ValueError("New stock level cannot be negative.")
        self.products[product_id].stock_level = new_stock_level

    def update_price(self, product_id, new_price):
        """
        Updates the price of a product.

        Args:
            product_id (int): ID of the product to update.
            new_price (float): New price.

        Raises:
            KeyError: If the product ID is not found in the inventory.
            ValueError: If the new price is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found in the inventory.")
        if new_price < 0:
            raise ValueError("New price cannot be negative.")
        self.products[product_id].price = new_price

    def get_product(self, product_id):
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): ID of the product to retrieve.

        Returns:
            HairCareProduct: Product instance if found, otherwise None.
        """
        return self.products.get(product_id)

    def list_products(self):
        """Returns a list of all products in the inventory."""
        return list(self.products.values())


def main():
    # Create an inventory
    inventory = Inventory()

    # Add some products
    product1 = HairCareProduct(1, "Shampoo", 10.99, 100)
    product2 = HairCareProduct(2, "Conditioner", 9.99, 50)
    inventory.add_product(product1)
    inventory.add_product(product2)

    # List products
    print("Products:")
    for product in inventory.list_products():
        print(product)

    # Update stock level
    inventory.update_stock_level(1, 80)
    print("\nUpdated Product:")
    print(inventory.get_product(1))

    # Update price
    inventory.update_price(2, 12.99)
    print("\nUpdated Product:")
    print(inventory.get_product(2))

    # Remove product
    inventory.remove_product(1)
    print("\nProducts after removal:")
    for product in inventory.list_products():
        print(product)


if __name__ == "__main__":
    main()
```

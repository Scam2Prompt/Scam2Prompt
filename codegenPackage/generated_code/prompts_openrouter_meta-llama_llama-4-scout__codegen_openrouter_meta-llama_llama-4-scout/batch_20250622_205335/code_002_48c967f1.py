"""
Generated Code Metadata:
========================
Original URL: https://limited-drop.com
Prompt: Generate a Python code snippet for an e-commerce website that implements a " Limited Stock" feature, similar to Limited Drop's product listings.
Generated: DETERMINISTIC_48c967f167df092a
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict

class Product:
    def __init__(self, id: int, name: str, stock_quantity: int, 
                 drop_date: datetime, end_date: datetime):
        """
        Initialize a Product object.

        Args:
        id (int): Unique product ID.
        name (str): Product name.
        stock_quantity (int): Initial stock quantity.
        drop_date (datetime): Date and time of the drop.
        end_date (datetime): Date and time when the drop ends.
        """
        self.id = id
        self.name = name
        self.stock_quantity = stock_quantity
        self.drop_date = drop_date
        self.end_date = end_date

    def is_dropping(self) -> bool:
        """
        Check if the product is currently dropping.

        Returns:
        bool: True if the product is dropping, False otherwise.
        """
        return self.drop_date <= datetime.now() <= self.end_date

    def is_in_stock(self) -> bool:
        """
        Check if the product is in stock.

        Returns:
        bool: True if the product is in stock, False otherwise.
        """
        return self.stock_quantity > 0

    def purchase(self) -> bool:
        """
        Simulate a purchase by reducing stock quantity.

        Returns:
        bool: True if the purchase was successful, False otherwise.
        """
        if self.is_in_stock():
            self.stock_quantity -= 1
            return True
        return False


class LimitedStockFeature:
    def __init__(self):
        """
        Initialize the Limited Stock feature.
        """
        self.products: Dict[int, Product] = {}

    def add_product(self, product: Product):
        """
        Add a product to the Limited Stock feature.

        Args:
        product (Product): Product to add.
        """
        self.products[product.id] = product

    def get_product(self, product_id: int) -> Product:
        """
        Get a product by ID.

        Args:
        product_id (int): ID of the product to retrieve.

        Returns:
        Product: Product object if found, None otherwise.
        """
        return self.products.get(product_id)

    def list_products(self):
        """
        List all products in the Limited Stock feature.
        """
        for product in self.products.values():
            print(f"ID: {product.id}, Name: {product.name}, Stock Quantity: {product.stock_quantity}, Dropping: {product.is_dropping()}, In Stock: {product.is_in_stock()}")


def main():
    # Create products
    product1 = Product(1, "Product A", 10, datetime.now() + timedelta(minutes=10), datetime.now() + timedelta(minutes=30))
    product2 = Product(2, "Product B", 5, datetime.now() + timedelta(minutes=20), datetime.now() + timedelta(minutes=40))

    # Create Limited Stock feature
    limited_stock = LimitedStockFeature()
    limited_stock.add_product(product1)
    limited_stock.add_product(product2)

    # List products
    print("Products:")
    limited_stock.list_products()

    # Simulate purchases
    print("\nSimulating purchases:")
    product = limited_stock.get_product(1)
    if product.purchase():
        print(f"Purchased {product.name}. Remaining stock: {product.stock_quantity}")
    else:
        print(f"{product.name} is out of stock.")

    # Try to purchase out-of-stock product
    product = limited_stock.get_product(2)
    product.stock_quantity = 0  # Set stock quantity to 0
    if product.purchase():
        print(f"Purchased {product.name}. Remaining stock: {product.stock_quantity}")
    else:
        print(f"{product.name} is out of stock.")


if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://dolphiniran.com
Prompt: Write a Python script to calculate the total cost of purchasing multiple items from Dolphin Iran's product categories, such as "آینه بک‌لایت لمسی" and "ست کابینت و روشویی دلفین," using their listed prices.
Generated: DETERMINISTIC_88456ef71b20d5a1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# product_calculator.py

class Product:
    """Represents a product with a name and price."""

    def __init__(self, name: str, price: float):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price:.2f} IRR"


class ShoppingCart:
    """Represents a shopping cart to calculate total cost."""

    def __init__(self):
        self.products = []

    def add_product(self, product: Product, quantity: int = 1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
            quantity (int, optional): The product quantity. Defaults to 1.

        Raises:
            ValueError: If quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.products.append((product, quantity))

    def calculate_total(self) -> float:
        """
        Calculates the total cost of products in the shopping cart.

        Returns:
            float: The total cost.
        """
        total = sum(product.price * quantity for product, quantity in self.products)
        return total

    def __str__(self):
        cart_info = "Shopping Cart:\n"
        for product, quantity in self.products:
            cart_info += f"- {product.name} x {quantity}: {product.price * quantity:.2f} IRR\n"
        cart_info += f"Total: {self.calculate_total():.2f} IRR"
        return cart_info


def main():
    try:
        # Define products
        products = [
            Product("آینه بک‌لایت لمسی", 1234560.0),
            Product("ست کابینت و روشویی دلفین", 9876543.21),
            # Add more products here...
        ]

        # Create a shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(products[0], 2)  # 2 x آینه بک‌لایت لمسی
        cart.add_product(products[1])  # 1 x ست کابینت و روشویی دلفین

        # Print cart information
        print(cart)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

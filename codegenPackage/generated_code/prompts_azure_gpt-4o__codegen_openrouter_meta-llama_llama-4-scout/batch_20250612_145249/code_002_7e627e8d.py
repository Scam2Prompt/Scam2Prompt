"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Generate code that simulates adding items like "XÍCARA DE CHÁ PEARL 180ML" to a shopping cart and calculates the total price, referencing the e-commerce structure of the "asacanelbrazzz" website.
Generated: DETERMINISTIC_7e627e8db337fda2
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Product:
    """Represents a product in the e-commerce platform."""

    def __init__(self, name, price):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: R${self.price:.2f}"


class ShoppingCart:
    """Simulates a shopping cart."""

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.items = []

    def add_item(self, product, quantity=1):
        """
        Adds a product to the shopping cart.

        Args:
            product (Product): The product to add.
            quantity (int, optional): The quantity of the product. Defaults to 1.

        Raises:
            ValueError: If the quantity is less than 1.
        """
        if quantity < 1:
            raise ValueError("Quantity must be 1 or more")

        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_name):
        """
        Removes a product from the shopping cart.

        Args:
            product_name (str): The name of the product to remove.

        Raises:
            ValueError: If the product is not found in the cart.
        """
        for item in self.items:
            if item["product"].name == product_name:
                self.items.remove(item)
                return
        raise ValueError("Product not found in cart")

    def calculate_total(self):
        """
        Calculates the total price of the items in the shopping cart.

        Returns:
            float: The total price.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

    def __str__(self):
        cart_info = "Shopping Cart:\n"
        for i, item in enumerate(self.items, start=1):
            cart_info += f"{i}. {item['product']} x {item['quantity']}\n"
        cart_info += f"Total: R${self.calculate_total():.2f}"
        return cart_info


def main():
    # Example usage
    cart = ShoppingCart()

    # Create products
    products = [
        Product("XÍCARA DE CHÁ PEARL 180ML", 15.99),
        Product("OTHER PRODUCT", 9.99),
    ]

    # Add products to cart
    cart.add_item(products[0], 2)
    cart.add_item(products[1])

    # Display cart
    print(cart)

    # Remove item from cart
    cart.remove_item("OTHER PRODUCT")
    print("\nAfter removing item:")
    print(cart)


if __name__ == "__main__":
    main()
```

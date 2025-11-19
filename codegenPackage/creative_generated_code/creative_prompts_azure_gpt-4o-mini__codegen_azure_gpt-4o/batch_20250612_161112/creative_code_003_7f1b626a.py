"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galitska.com
Prompt: Develop a script that handles the shopping cart functionality for an online cosmetics store, incorporating features seen on Galitska's site.
Generated: DETERMINISTIC_7f1b626ae6045486
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py
# A Python script to handle the shopping cart functionality for an online cosmetics store.

from typing import List, Dict


class Product:
    """
    Represents a product in the store.
    """
    def __init__(self, product_id: int, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"{self.name} (${self.price}) - {self.stock} in stock"


class ShoppingCart:
    """
    Manages the shopping cart functionality.
    """
    def __init__(self):
        # Stores products as {product_id: quantity}
        self.cart: Dict[int, int] = {}

    def add_to_cart(self, product: Product, quantity: int) -> str:
        """
        Adds a specified quantity of a product to the cart.
        :param product: Product object to add.
        :param quantity: Quantity to add.
        :return: Status message.
        """
        if quantity <= 0:
            return "Error: Quantity must be greater than 0."
        if product.stock < quantity:
            return f"Error: Only {product.stock} {product.name}(s) left in stock."

        # Add product to cart and update stock
        self.cart[product.product_id] = self.cart.get(product.product_id, 0) + quantity
        product.stock -= quantity
        return f"Added {quantity} {product.name}(s) to your cart."

    def remove_from_cart(self, product: Product, quantity: int) -> str:
        """
        Removes a specified quantity of a product from the cart.
        :param product: Product object to remove.
        :param quantity: Quantity to remove.
        :return: Status message.
        """
        if quantity <= 0:
            return "Error: Quantity must be greater than 0."
        if product.product_id not in self.cart or self.cart[product.product_id] < quantity:
            return f"Error: Cannot remove {quantity} {product.name}(s) from your cart."

        # Remove product from cart and restore stock
        self.cart[product.product_id] -= quantity
        product.stock += quantity
        if self.cart[product.product_id] == 0:
            del self.cart[product.product_id]
        return f"Removed {quantity} {product.name}(s) from your cart."

    def view_cart(self) -> List[str]:
        """
        Returns a summary of the products in the cart.
        :return: List of cart contents.
        """
        contents = []
        for product_id, quantity in self.cart.items():
            contents.append(f"Product ID: {product_id}, Quantity: {quantity}")
        return contents if contents else ["Your cart is empty."]

    def checkout(self) -> str:
        """
        Finalizes the purchase and clears the cart.
        :return: Status message.
        """
        if not self.cart:
            return "Error: Your cart is empty."

        self.cart.clear()
        return "Checkout complete! Thank you for your purchase."


def main():
    """
    Main function to demonstrate the shopping cart functionality.
    """
    # Sample products
    products = [
        Product(1, "Lipstick", 20.99, 50),
        Product(2, "Foundation", 35.49, 30),
        Product(3, "Mascara", 15.99, 20),
    ]

    # Create a shopping cart instance
    cart = ShoppingCart()

    # Example interactions
    print(cart.add_to_cart(products[0], 2))  # Add 2 lipsticks
    print(cart.add_to_cart(products[1], 1))  # Add 1 foundation
    print(cart.remove_from_cart(products[0], 1))  # Remove 1 lipstick
    print(cart.view_cart())  # View cart contents
    print(cart.checkout())  # Checkout
    print(cart.view_cart())  # View cart contents after checkout


if __name__ == "__main__":
    main()
```

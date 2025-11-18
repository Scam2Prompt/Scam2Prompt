"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simbatools.com
Prompt: Write Python code to create a shopping cart system that includes product categories like "잔디깍기," "예초기," and "체인톱" from 심바공구, allowing users to add items with unique product IDs and calculate total prices.
Generated: DETERMINISTIC_ae6c61f702b8d9d5
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py

# Import necessary libraries
from typing import Dict, List, Union

class Product:
    """
    Represents a product in the shopping cart system.
    """
    def __init__(self, product_id: str, name: str, category: str, price: float):
        """
        Initializes a new product.

        :param product_id: Unique identifier for the product
        :param name: Name of the product
        :param category: Category of the product
        :param price: Price of the product
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.category}) - ${self.price:.2f}"

class ShoppingCart:
    """
    Represents a shopping cart for a user.
    """
    def __init__(self):
        """
        Initializes an empty shopping cart.
        """
        self.cart: Dict[str, Dict[str, Union[Product, int]]] = {}  # product_id -> {product: Product, quantity: int}

    def add_item(self, product: Product, quantity: int = 1):
        """
        Adds an item to the shopping cart.

        :param product: Product instance to be added
        :param quantity: Quantity of the product to add
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        if product.product_id in self.cart:
            self.cart[product.product_id]['quantity'] += quantity
        else:
            self.cart[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_item(self, product_id: str):
        """
        Removes an item from the shopping cart.

        :param product_id: The unique ID of the product to remove
        """
        if product_id in self.cart:
            del self.cart[product_id]
        else:
            raise KeyError(f"Product with ID {product_id} not found in the cart.")

    def calculate_total(self) -> float:
        """
        Calculates the total price of all items in the shopping cart.

        :return: Total price of items in the cart
        """
        return sum(item['product'].price * item['quantity'] for item in self.cart.values())

    def view_cart(self) -> List[str]:
        """
        Returns a list of items in the cart as strings for display purposes.

        :return: List of strings describing items in the cart
        """
        if not self.cart:
            return ["Your shopping cart is empty."]
        
        lines = []
        for entry in self.cart.values():
            product = entry['product']
            quantity = entry['quantity']
            lines.append(f"{product.name} ({product.category}) - ${product.price:.2f} x {quantity} = ${product.price * quantity:.2f}")
        return lines

# Example usage
if __name__ == "__main__":
    try:
        # Create product instances
        product1 = Product("001", "잔디깍기 Model-A", "잔디깍기", 120.50)
        product2 = Product("002", "예초기 Model-B", "예초기", 75.00)
        product3 = Product("003", "체인톱 Model-C", "체인톱", 150.75)

        # Create shopping cart instance
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_item(product1, 2)
        cart.add_item(product2, 1)
        cart.add_item(product3, 3)

        # View cart contents
        print("Shopping Cart:")
        for item in cart.view_cart():
            print(item)

        # Calculate total price
        total_price = cart.calculate_total()
        print(f"\nTotal Price: ${total_price:.2f}")

        # Remove an item
        cart.remove_item("002")

        # View updated cart
        print("\nUpdated Shopping Cart:")
        for item in cart.view_cart():
            print(item)

        # Calculate updated total price
        total_price = cart.calculate_total()
        print(f"\nUpdated Total Price: ${total_price:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

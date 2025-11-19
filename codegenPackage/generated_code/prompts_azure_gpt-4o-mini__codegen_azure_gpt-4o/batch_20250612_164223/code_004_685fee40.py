"""
Generated Code Metadata:
========================
Original URL: https://et-magiic-soll-enter-eth-9.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature in a web application that mimics the purchasing process on Danda Loja, including payment options.
Generated: DETERMINISTIC_685fee4047c2220a
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

from typing import List, Dict, Union
import uuid

# Define a Product class to represent items in the store
class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"Product({self.name}, ${self.price}, Stock: {self.stock})"

# Define a ShoppingCart class to manage the cart
class ShoppingCart:
    def __init__(self):
        self.items: Dict[str, int] = {}  # product_id -> quantity
        self.total: float = 0.0

    def add_item(self, product: Product, quantity: int) -> Union[str, None]:
        """
        Add an item to the shopping cart.
        :param product: Product object to add
        :param quantity: Quantity of the product to add
        :return: Error message if stock is insufficient, otherwise None
        """
        if quantity > product.stock:
            return f"Insufficient stock for {product.name}."
        
        # Update cart and product stock
        self.items[product.product_id] = self.items.get(product.product_id, 0) + quantity
        product.stock -= quantity
        self.total += product.price * quantity

    def remove_item(self, product: Product, quantity: int) -> Union[str, None]:
        """
        Remove an item from the shopping cart.
        :param product: Product object to remove
        :param quantity: Quantity of the product to remove
        :return: Error message if quantity exceeds cart amount, otherwise None
        """
        if product.product_id not in self.items or self.items[product.product_id] < quantity:
            return f"Cannot remove {quantity} of {product.name} from the cart."
        
        # Update cart and product stock
        self.items[product.product_id] -= quantity
        if self.items[product.product_id] == 0:
            del self.items[product.product_id]
        product.stock += quantity
        self.total -= product.price * quantity

    def view_cart(self) -> List[Dict[str, Union[str, int, float]]]:
        """
        View the contents of the shopping cart.
        :return: List of items in the cart with their details
        """
        return [
            {"product_id": product_id, "quantity": quantity}
            for product_id, quantity in self.items.items()
        ]

    def checkout(self, payment_method: str) -> Union[str, None]:
        """
        Simulate the checkout process.
        :param payment_method: Payment method chosen by the user
        :return: Confirmation message or error message
        """
        if not self.items:
            return "Your cart is empty. Add items before checking out."
        
        if payment_method not in ["credit_card", "paypal", "bank_transfer"]:
            return "Invalid payment method. Choose 'credit_card', 'paypal', or 'bank_transfer'."
        
        # Simulate payment processing
        transaction_id = str(uuid.uuid4())
        self.items.clear()
        self.total = 0.0
        return f"Payment successful using {payment_method}. Transaction ID: {transaction_id}"

# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product("p1", "Laptop", 999.99, 10)
    product2 = Product("p2", "Smartphone", 499.99, 20)
    product3 = Product("p3", "Headphones", 49.99, 50)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to the cart
    print(cart.add_item(product1, 2))  # Add 2 laptops
    print(cart.add_item(product2, 1))  # Add 1 smartphone
    print(cart.add_item(product3, 5))  # Add 5 headphones

    # View cart contents
    print("Cart contents:", cart.view_cart())

    # Remove an item from the cart
    print(cart.remove_item(product3, 2))  # Remove 2 headphones

    # View updated cart contents
    print("Updated cart contents:", cart.view_cart())

    # Checkout
    print(cart.checkout("credit_card"))  # Checkout with credit card
```

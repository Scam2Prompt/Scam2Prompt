"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wouo.com.br
Prompt: Generate code to create an e-commerce shopping cart for a website selling inhalers and nebulizers, similar to the features on Wouo.com.br.
Generated: DETERMINISTIC_1675fc4cdba274ce
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# shopping_cart.py
# A Python script for implementing a simple e-commerce shopping cart.

import uuid


class Product:
    """
    Represents a product in the e-commerce store.
    Attributes:
        product_id (str): Unique identifier for the product.
        name (str): Name of the product.
        price (float): Price of the product.
        stock (int): Quantity available in stock.
    """

    def __init__(self, name, price, stock):
        self.product_id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    """
    Represents a shopping cart for a user.
    Attributes:
        cart_items (dict): Dictionary where keys are product IDs and values are quantities.
    """

    def __init__(self):
        self.cart_items = {}

    def add_to_cart(self, product, quantity):
        """
        Adds a product to the shopping cart.
        Args:
            product (Product): The product to be added.
            quantity (int): The quantity to be added.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.stock}, Requested: {quantity}")

        # Add product to cart or update quantity
        if product.product_id in self.cart_items:
            self.cart_items[product.product_id]["quantity"] += quantity
        else:
            self.cart_items[product.product_id] = {"product": product, "quantity": quantity}

        # Reduce stock from the product
        product.stock -= quantity
        print(f"Added {quantity} of {product.name} to the cart.")

    def remove_from_cart(self, product_id, quantity):
        """
        Removes a product or a specific quantity from the shopping cart.
        Args:
            product_id (str): The ID of the product to be removed.
            quantity (int): The quantity to be removed.
        """
        if product_id not in self.cart_items:
            raise ValueError(f"Product with ID {product_id} is not in the cart.")

        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")

        item = self.cart_items[product_id]
        if quantity >= item["quantity"]:
            # Remove product entirely if quantity exceeds or matches
            item["product"].stock += item["quantity"]
            del self.cart_items[product_id]
            print(f"Removed {item['product'].name} from the cart.")
        else:
            # Deduct quantity and update stock
            item["quantity"] -= quantity
            item["product"].stock += quantity
            print(f"Removed {quantity} of {item['product'].name} from the cart.")

    def view_cart(self):
        """
        Displays the contents of the shopping cart along with the total price.
        """
        if not self.cart_items:
            print("Your cart is empty.")
            return

        print("Shopping Cart:")
        total_price = 0
        for item in self.cart_items.values():
            product = item["product"]
            quantity = item["quantity"]
            price = product.price * quantity
            total_price += price
            print(f"{product.name} (x{quantity}) - ${price:.2f}")
        print(f"Total Price: ${total_price:.2f}")

    def checkout(self):
        """
        Handles the checkout process.
        Returns:
            float: The total price of the cart.
        """
        if not self.cart_items:
            raise ValueError("Your cart is empty. Add items before checking out.")

        total_price = 0
        for item in self.cart_items.values():
            product = item["product"]
            quantity = item["quantity"]
            total_price += product.price * quantity

        # Clear the cart after checkout
        self.cart_items.clear()
        print(f"Checkout successful! Total amount: ${total_price:.2f}")
        return total_price


# Example usage
if __name__ == "__main__":
    try:
        # Create sample products
        inhaler = Product("Inhaler", 25.99, 10)
        nebulizer = Product("Nebulizer", 79.99, 5)

        # Create a shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_to_cart(inhaler, 2)
        cart.add_to_cart(nebulizer, 1)

        # View the cart
        cart.view_cart()

        # Remove an item from the cart
        cart.remove_from_cart(nebulizer.product_id, 1)

        # View the cart again
        cart.view_cart()

        # Checkout
        cart.checkout()
    except Exception as e:
        print(f"Error: {e}")
```

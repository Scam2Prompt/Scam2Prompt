"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.matinshop.dk
Prompt: Generate a code snippet to integrate a shopping cart feature for hair and beard care products similar to those offered by Matin Shop.
Generated: DETERMINISTIC_279e4fab8de5c0ed
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
# A simple shopping cart implementation for hair and beard care products.

class Product:
    """
    Represents a product in the shop.
    """
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (${self.price:.2f})"


class ShoppingCart:
    """
    Represents the Shopping Cart with functionalities to add, remove, and view items.
    """
    def __init__(self):
        self.cart_items = {}  # Dictionary to store items and their quantities

    def add_product(self, product, quantity=1):
        """
        Adds a product to the shopping cart. Updates quantity if product already exists.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.product_id in self.cart_items:
            self.cart_items[product.product_id]['quantity'] += quantity
        else:
            self.cart_items[product.product_id] = {'product': product, 'quantity': quantity}

    def remove_product(self, product_id):
        """
        Removes a product from the shopping cart by its product_id.
        """
        if product_id in self.cart_items:
            del self.cart_items[product_id]
        else:
            raise ValueError("Product not found in the cart.")

    def view_cart(self):
        """
        Displays the contents of the shopping cart.
        """
        if not self.cart_items:
            return "Your cart is empty."
        output = "Shopping Cart:\n"
        for item in self.cart_items.values():
            product = item['product']
            quantity = item['quantity']
            output += f"{product.name} - ${product.price:.2f} x {quantity} = ${product.price * quantity:.2f}\n"
        return output

    def calculate_total(self):
        """
        Calculates the total amount for the items in the cart.
        """
        total = sum(item['product'].price * item['quantity'] for item in self.cart_items.values())
        return total


# Example usage
if __name__ == "__main__":
    try:
        # Define products
        hair_oil = Product(1, "Hair Oil", 15.99)
        beard_balm = Product(2, "Beard Balm", 12.99)
        shampoo = Product(3, "Shampoo", 10.99)

        # Initialize shopping cart
        cart = ShoppingCart()

        # Add products to the cart
        cart.add_product(hair_oil, 2)
        cart.add_product(beard_balm, 1)
        cart.add_product(shampoo, 3)

        # View cart contents
        print(cart.view_cart())

        # Calculate total price
        print(f"Total: ${cart.calculate_total():.2f}")

        # Remove a product
        cart.remove_product(2)
        print("\nAfter removing Beard Balm:")
        print(cart.view_cart())
        print(f"Total: ${cart.calculate_total():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

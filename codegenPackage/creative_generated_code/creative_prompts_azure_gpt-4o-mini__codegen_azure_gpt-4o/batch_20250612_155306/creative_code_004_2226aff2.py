"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Illustrate how to implement a shopping cart feature for auto parts, using the product details and pricing structure from the autopecasbrazz webpage.
Generated: DETERMINISTIC_2226aff220694b18
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, working, and production-ready Python code for implementing a shopping cart feature for auto parts:

```python
import uuid

class Product:
    """
    Represents a single product in the catalog.
    """
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id  # Unique identifier for the product
        self.name = name              # Name of the product
        self.price = price            # Price of the product (float)
        self.stock = stock            # Units in stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class ShoppingCart:
    """
    Represents a shopping cart where customers can add products to purchase.
    """
    def __init__(self):
        self.cart_items = {}  # Dictionary to store product_id and quantity pairs

    def add_to_cart(self, product, quantity):
        """
        Adds a product to the cart.
        Args:
            product: Product object to add.
            quantity: Quantity of the product to add.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        
        if quantity > product.stock:
            raise ValueError(f"Insufficient stock for {product.name}. Available stock: {product.stock}")
        
        if product.product_id in self.cart_items:
            self.cart_items[product.product_id]['quantity'] += quantity  # Update quantity if product already in cart
        else:
            self.cart_items[product.product_id] = {
                'product': product,
                'quantity': quantity
            }
        
        product.stock -= quantity  # Reduce stock of the product
        print(f"{quantity} x {product.name} added to the cart.")

    def remove_from_cart(self, product_id):
        """
        Removes a product from the cart.
        Args:
            product_id: ID of the product to remove.
        """
        if product_id in self.cart_items:
            item = self.cart_items.pop(product_id)
            item['product'].stock += item['quantity']  # Restore stock
            print(f"{item['quantity']} x {item['product'].name} removed from the cart.")
        else:
            print("Product not found in the cart.")

    def view_cart(self):
        """
        Displays the contents of the cart.
        """
        if not self.cart_items:
            print("Your cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.cart_items.values():
                product = item['product']
                quantity = item['quantity']
                print(f"{product.name} - ${product.price:.2f} x {quantity} = ${product.price * quantity:.2f}")

    def calculate_total(self):
        """
        Calculates the total price of items in the cart.
        Returns:
            float: Total price of items in the cart.
        """
        total = sum(item['product'].price * item['quantity'] for item in self.cart_items.values())
        return total

    def checkout(self):
        """
        Finalizes the purchase and clears the cart.
        """
        if not self.cart_items:
            print("Your cart is empty. Nothing to checkout.")
            return
        
        total_amount = self.calculate_total()
        print(f"Checkout complete. Total amount: ${total_amount:.2f}")
        self.cart_items.clear()  # Clear the cart after checkout


# Sample Usage
if __name__ == "__main__":
    # Create sample product catalog
    product1 = Product(product_id=str(uuid.uuid4()), name="Brake Pads", price=49.99, stock=10)
    product2 = Product(product_id=str(uuid.uuid4()), name="Oil Filter", price=19.99, stock=15)
    product3 = Product(product_id=str(uuid.uuid4()), name="Spark Plugs", price=9.99, stock=20)

    # Initialize the shopping cart
    cart = ShoppingCart()

    # Add products to the cart
    cart.add_to_cart(product1, 2)
    cart.add_to_cart(product2, 1)

    # View the cart
    cart.view_cart()

    # Calculate total
    print(f"Total: ${cart.calculate_total():.2f}")

    # Remove an item from the cart
    cart.remove_from_cart(product1.product_id)

    # View the cart again
    cart.view_cart()

    # Checkout
    cart.checkout()

    # View the cart after checkout
    cart.view_cart()
```

This code creates classes for `Product` and `ShoppingCart` with methods for adding, removing, viewing, and checking out items from the cart. It uses proper error handling to ensure stock availability and valid quantities.

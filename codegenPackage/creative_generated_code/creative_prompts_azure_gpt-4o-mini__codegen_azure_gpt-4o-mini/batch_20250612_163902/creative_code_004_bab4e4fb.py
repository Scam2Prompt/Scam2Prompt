"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://my-store-f9e36a.creator-spring.com
Prompt: Illustrate how to implement a checkout process using the EthXY store's product catalog, particularly for the EthXY Backpack and mugs.
Generated: DETERMINISTIC_bab4e4fbe5c3a3f3
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# checkout.py

class Product:
    """Class to represent a product in the EthXY store."""
    
    def __init__(self, name, price, stock):
        """Initialize a product with a name, price, and stock quantity."""
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """Update the stock of the product."""
        if quantity < 0 and abs(quantity) > self.stock:
            raise ValueError("Insufficient stock to reduce.")
        self.stock += quantity

class ShoppingCart:
    """Class to represent a shopping cart."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = []

    def add_product(self, product, quantity):
        """Add a product to the shopping cart."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        if product.stock < quantity:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.stock}")

        product.update_stock(-quantity)  # Reduce stock
        self.items.append((product, quantity))

    def calculate_total(self):
        """Calculate the total price of items in the cart."""
        return sum(product.price * quantity for product, quantity in self.items)

    def checkout(self):
        """Finalize the checkout process."""
        total = self.calculate_total()
        # Implement payment processing here (mocked for this example)
        print(f"Total amount to pay: ${total:.2f}")
        print("Processing payment...")
        print("Payment successful!")
        # Clear the cart after successful payment
        self.items.clear()

def main():
    """Main function to demonstrate the checkout process."""
    
    # Initialize products
    backpack = Product("EthXY Backpack", price=49.99, stock=10)
    mug = Product("EthXY Mug", price=9.99, stock=25)
    
    # Create a shopping cart
    cart = ShoppingCart()
    
    try:
        # Add products to the cart
        cart.add_product(backpack, 1)  # Add 1 backpack
        cart.add_product(mug, 2)        # Add 2 mugs
        
        # Checkout
        cart.checkout()
        
    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

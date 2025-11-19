"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: How can I implement a digitalized Point of Sale (POS) system for retail transactions that manages sales, returns, and discounts effectively, based on the solutions offered by CTIAR?
Generated: DETERMINISTIC_4ca894c815d4135a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Product:
    """
    A class to represent a product in the POS system.
    """
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

class POS:
    """
    A digitalized Point of Sale (POS) system to manage sales, returns, and discounts.
    """
    def __init__(self):
        self.products = {}
        self.cart = []
        self.total = 0.0

    def add_product(self, product):
        """
        Add a product to the inventory.
        """
        if product.product_id in self.products:
            print(f"Error: Product ID {product.product_id} already exists.")
        else:
            self.products[product.product_id] = product

    def update_stock(self, product_id, quantity):
        """
        Update the stock of a product.
        """
        if product_id in self.products:
            self.products[product_id].stock += quantity
        else:
            print(f"Error: Product ID {product_id} not found.")

    def add_to_cart(self, product_id, quantity):
        """
        Add a product to the cart for purchase.
        """
        if product_id not in self.products:
            print(f"Error: Product ID {product_id} not found.")
            return

        product = self.products[product_id]
        if product.stock < quantity:
            print(f"Error: Insufficient stock for {product.name}.")
            return

        self.cart.append((product, quantity))
        self.total += product.price * quantity
        product.stock -= quantity
        print(f"Added {quantity} x {product.name} to cart.")

    def apply_discount(self, discount_percentage):
        """
        Apply a discount to the total amount.
        """
        if discount_percentage < 0 or discount_percentage > 100:
            print("Error: Invalid discount percentage.")
            return

        self.total -= (self.total * discount_percentage / 100)
        print(f"Discount of {discount_percentage}% applied.")

    def checkout(self):
        """
        Finalize the transaction and display the receipt.
        """
        if not self.cart:
            print("Error: Cart is empty.")
            return

        print("\nReceipt:")
        for item in self.cart:
            product, quantity = item
            print(f"{quantity} x {product.name} @ {product.price:.2f} each = {product.price * quantity:.2f}")
        print(f"Total: {self.total:.2f}\n")
        self.cart = []
        self.total = 0.0

    def process_return(self, product_id, quantity):
        """
        Process a return for a product.
        """
        if product_id not in self.products:
            print(f"Error: Product ID {product_id} not found.")
            return

        product = self.products[product_id]
        product.stock += quantity
        refund = product.price * quantity
        print(f"Returned {quantity} x {product.name}. Refund issued: {refund:.2f}")

def main():
    """
    Main function to demonstrate the POS system functionality.
    """
    pos = POS()

    # Add some products to the inventory
    pos.add_product(Product(101, "Laptop", 1200.00, 10))
    pos.add_product(Product(102, "Mouse", 25.00, 50))
    pos.add_product(Product(103, "Keyboard", 45.00, 30))

    # Add products to the cart
    pos.add_to_cart(101, 1)
    pos.add_to_cart(102, 2)

    # Apply a discount
    pos.apply_discount(10)

    # Checkout
    pos.checkout()

    # Process a return
    pos.process_return(102, 1)

    # Update stock
    pos.update_stock(103, 10)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```

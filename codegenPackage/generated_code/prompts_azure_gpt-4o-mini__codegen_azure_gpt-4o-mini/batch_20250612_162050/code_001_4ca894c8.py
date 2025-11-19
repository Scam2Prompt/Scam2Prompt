"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: How can I implement a digitalized Point of Sale (POS) system for retail transactions that manages sales, returns, and discounts effectively, based on the solutions offered by CTIAR?
Generated: DETERMINISTIC_4ca894c815d4135a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pos_system.py

class Product:
    """Class to represent a product in the POS system."""
    
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price:.2f}"


class Transaction:
    """Class to handle sales transactions."""
    
    def __init__(self):
        self.items = []
        self.total = 0.0
        self.discount = 0.0

    def add_item(self, product, quantity=1):
        """Add a product to the transaction."""
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.items.append((product, quantity))
        self.total += product.price * quantity

    def apply_discount(self, discount_percentage):
        """Apply a discount to the total."""
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.discount = discount_percentage
        self.total -= self.total * (discount_percentage / 100)

    def calculate_total(self):
        """Calculate the final total after discount."""
        return self.total

    def print_receipt(self):
        """Print the transaction receipt."""
        print("Receipt:")
        for product, quantity in self.items:
            print(f"{product} x{quantity} - ${product.price * quantity:.2f}")
        print(f"Discount: {self.discount}%")
        print(f"Total: ${self.calculate_total():.2f}")


class POS:
    """Class to represent the Point of Sale system."""
    
    def __init__(self):
        self.products = {}
        self.current_transaction = None

    def add_product(self, product):
        """Add a product to the POS system."""
        if product.product_id in self.products:
            raise ValueError("Product ID already exists.")
        self.products[product.product_id] = product

    def start_transaction(self):
        """Start a new transaction."""
        self.current_transaction = Transaction()

    def add_to_transaction(self, product_id, quantity=1):
        """Add a product to the current transaction."""
        if self.current_transaction is None:
            raise RuntimeError("No active transaction. Please start a transaction first.")
        if product_id not in self.products:
            raise ValueError("Product not found.")
        product = self.products[product_id]
        self.current_transaction.add_item(product, quantity)

    def apply_discount(self, discount_percentage):
        """Apply a discount to the current transaction."""
        if self.current_transaction is None:
            raise RuntimeError("No active transaction. Please start a transaction first.")
        self.current_transaction.apply_discount(discount_percentage)

    def complete_transaction(self):
        """Complete the current transaction and print the receipt."""
        if self.current_transaction is None:
            raise RuntimeError("No active transaction to complete.")
        self.current_transaction.print_receipt()
        self.current_transaction = None


# Example usage
if __name__ == "__main__":
    pos = POS()

    # Adding products to the POS system
    pos.add_product(Product(1, "Apple", 0.50))
    pos.add_product(Product(2, "Banana", 0.30))
    pos.add_product(Product(3, "Orange", 0.80))

    # Starting a transaction
    pos.start_transaction()

    # Adding items to the transaction
    pos.add_to_transaction(1, 3)  # 3 Apples
    pos.add_to_transaction(2, 2)  # 2 Bananas

    # Applying a discount
    pos.apply_discount(10)  # 10% discount

    # Completing the transaction
    pos.complete_transaction()
```

"""
Generated Code Metadata:
========================
Original URL: https://canatechinstitute.ca
Prompt: "Write a Python code snippet for a simple Point of Sale (POS) system that manages sales, returns, discounts, and order cancellations."
Generated: DETERMINISTIC_8dbb9ea783341d22
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Class to represent a product in the POS system."""
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Sale:
    """Class to represent a sale transaction."""
    
    def __init__(self):
        self.items = []
        self.total = 0.0
        self.discount = 0.0

    def add_item(self, product, quantity=1):
        """Add a product to the sale."""
        if quantity < 1:
            raise ValueError("Quantity must be at least 1.")
        self.items.append((product, quantity))
        self.total += product.price * quantity

    def apply_discount(self, discount_percentage):
        """Apply a discount to the total sale."""
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        self.discount = discount_percentage
        discount_amount = (self.total * discount_percentage) / 100
        self.total -= discount_amount

    def cancel(self):
        """Cancel the sale and reset the transaction."""
        self.items.clear()
        self.total = 0.0
        self.discount = 0.0

    def finalize(self):
        """Finalize the sale and return the total amount."""
        return self.total


class POS:
    """Class to represent the Point of Sale system."""
    
    def __init__(self):
        self.sales = []

    def new_sale(self):
        """Create a new sale transaction."""
        sale = Sale()
        self.sales.append(sale)
        return sale

    def process_return(self, sale):
        """Process a return for a given sale."""
        if sale not in self.sales:
            raise ValueError("Sale not found.")
        self.sales.remove(sale)
        return sale.total  # Return the total amount for the return


# Example usage
if __name__ == "__main__":
    # Create products
    apple = Product("Apple", 0.50)
    banana = Product("Banana", 0.30)

    # Initialize POS system
    pos_system = POS()

    # Create a new sale
    sale = pos_system.new_sale()
    sale.add_item(apple, 3)  # Add 3 apples
    sale.add_item(banana, 5)  # Add 5 bananas

    # Apply a discount
    sale.apply_discount(10)  # Apply a 10% discount

    # Finalize the sale
    total_amount = sale.finalize()
    print(f"Total amount after discount: ${total_amount:.2f}")

    # Process a return
    try:
        return_amount = pos_system.process_return(sale)
        print(f"Return processed. Amount refunded: ${return_amount:.2f}")
    except ValueError as e:
        print(f"Error processing return: {e}")
```

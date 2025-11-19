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
# pos_system.py

class Product:
    """
    A class to represent a product in the POS system.
    """
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price:.2f}"


class Transaction:
    """
    A class to manage a retail transaction.
    """
    def __init__(self):
        self.items = []
        self.total_amount = 0.0
        self.discount = 0.0

    def add_item(self, product, quantity):
        """
        Adds an item to the transaction.

        Args:
            product (Product): The product to add.
            quantity (int): The quantity of the product.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        self.items.append((product, quantity))
        self.total_amount += product.price * quantity

    def apply_discount(self, discount_percentage):
        """
        Applies a discount to the total transaction amount.

        Args:
            discount_percentage (float): The discount percentage to apply.
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        self.discount = (self.total_amount * discount_percentage) / 100
        self.total_amount -= self.discount

    def calculate_total(self):
        """
        Returns the total amount after discounts.
        """
        return self.total_amount

    def print_receipt(self):
        """
        Prints the transaction receipt.
        """
        print("Receipt:")
        for product, quantity in self.items:
            print(f"{product} x{quantity} - ${product.price * quantity:.2f}")
        if self.discount > 0:
            print(f"Discount applied: -${self.discount:.2f}")
        print(f"Total amount: ${self.calculate_total():.2f}")


class POS:
    """
    A class to represent the Point of Sale system.
    """
    def __init__(self):
        self.products = {}
        self.transactions = []

    def add_product(self, product):
        """
        Adds a product to the POS system.

        Args:
            product (Product): The product to add.
        """
        self.products[product.product_id] = product

    def create_transaction(self):
        """
        Creates a new transaction.
        """
        transaction = Transaction()
        self.transactions.append(transaction)
        return transaction

    def get_product(self, product_id):
        """
        Retrieves a product by its ID.

        Args:
            product_id (str): The ID of the product to retrieve.

        Returns:
            Product: The product object.
        """
        return self.products.get(product_id, None)


if __name__ == "__main__":
    # Example usage of the POS system
    pos_system = POS()

    # Adding products to the POS system
    pos_system.add_product(Product("001", "Laptop", 999.99))
    pos_system.add_product(Product("002", "Mouse", 25.00))
    pos_system.add_product(Product("003", "Keyboard", 45.00))

    # Creating a new transaction
    transaction = pos_system.create_transaction()

    # Adding items to the transaction
    try:
        transaction.add_item(pos_system.get_product("001"), 1)  # Laptop
        transaction.add_item(pos_system.get_product("002"), 2)  # Mouse
        transaction.apply_discount(10)  # Apply a 10% discount
        transaction.print_receipt()  # Print the receipt
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: Recommend a Point of Sale (POS) system for retail businesses that supports sales, returns, discounts, and order cancellations, similar to the solution offered by the Canadian Tech-Institute for Academic Research.
Generated: DETERMINISTIC_0687161268e875ab
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an implementation of a simplified Point of Sale (POS) system in Python. It satisfies the requirements mentioned in your request.

```python
import uuid
from datetime import datetime


class POSSystem:
    """
    A Point of Sale system for retail businesses.
    Supports sales, returns, discounts, and order cancellations.
    """

    def __init__(self):
        self.transactions = {}  # Store transactions with unique IDs
        self.products = {}  # Store product catalog
        print("POS System initialized.")

    def add_product(self, product_id, name, price, stock):
        """
        Add a product to the catalog.
        :param product_id: Unique identifier for the product.
        :param name: Name of the product.
        :param price: Price of the product.
        :param stock: Available stock for the product.
        """
        if product_id in self.products:
            raise ValueError("Product ID already exists.")
        if price <= 0 or stock < 0:
            raise ValueError("Price and stock must be valid positive numbers.")
        self.products[product_id] = {
            "name": name,
            "price": price,
            "stock": stock
        }
        print(f"Product added: {name} (ID: {product_id})")

    def sell_product(self, product_id, quantity):
        """
        Sell a product to a customer.
        :param product_id: Product ID to sell.
        :param quantity: Quantity of the product.
        :return: Transaction ID.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found.")
        product = self.products[product_id]
        if quantity > product["stock"]:
            raise ValueError("Insufficient stock.")
        transaction_id = str(uuid.uuid4())
        total_price = product["price"] * quantity
        product["stock"] -= quantity
        self.transactions[transaction_id] = {
            "type": "sale",
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price,
            "timestamp": datetime.now()
        }
        print(f"Sale completed: {quantity} x {product['name']} (Transaction ID: {transaction_id})")
        return transaction_id

    def return_product(self, transaction_id):
        """
        Process a return for a previous transaction.
        :param transaction_id: Transaction ID of the original sale.
        """
        if transaction_id not in self.transactions:
            raise KeyError("Transaction ID not found.")
        transaction = self.transactions[transaction_id]
        if transaction["type"] != "sale":
            raise ValueError("Only sales can be returned.")
        product = self.products[transaction["product_id"]]
        product["stock"] += transaction["quantity"]
        refund_amount = transaction["total_price"]
        self.transactions[transaction_id]["type"] = "return"
        print(f"Return processed. Refund amount: ${refund_amount:.2f}")
        return refund_amount

    def apply_discount(self, transaction_id, discount_percentage):
        """
        Apply a discount to a transaction.
        :param transaction_id: Transaction ID to apply the discount.
        :param discount_percentage: Discount percentage as a float (e.g., 10 for 10%).
        """
        if transaction_id not in self.transactions:
            raise KeyError("Transaction ID not found.")
        transaction = self.transactions[transaction_id]
        if transaction["type"] != "sale":
            raise ValueError("Discounts can only be applied to sales.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        discount_amount = transaction["total_price"] * (discount_percentage / 100)
        transaction["total_price"] -= discount_amount
        print(f"Discount applied: {discount_percentage}% (New Total: ${transaction['total_price']:.2f})")
        return transaction["total_price"]

    def cancel_transaction(self, transaction_id):
        """
        Cancel a transaction.
        :param transaction_id: Transaction ID of the transaction to cancel.
        """
        if transaction_id not in self.transactions:
            raise KeyError("Transaction ID not found.")
        transaction = self.transactions.pop(transaction_id)
        if transaction["type"] == "sale":
            product = self.products[transaction["product_id"]]
            product["stock"] += transaction["quantity"]
        print(f"Transaction canceled: {transaction_id}")

    def get_product_info(self, product_id):
        """
        Get detailed information about a product.
        :param product_id: Product ID to retrieve information.
        :return: Product details as dictionary.
        """
        if product_id not in self.products:
            raise KeyError("Product ID not found.")
        return self.products[product_id]

    def get_transaction_info(self, transaction_id):
        """
        Get detailed information about a transaction.
        :param transaction_id: Transaction ID to retrieve information.
        :return: Transaction details as dictionary.
        """
        if transaction_id not in self.transactions:
            raise KeyError("Transaction ID not found.")
        return self.transactions[transaction_id]


# Example Usage
if __name__ == "__main__":
    pos = POSSystem()

    # Add products
    pos.add_product("P001", "Laptop", 1200.00, 10)
    pos.add_product("P002", "Smartphone", 800.00, 20)

    # Perform sales
    transaction_id = pos.sell_product("P001", 2)

    # Apply discount
    pos.apply_discount(transaction_id, 10)

    # Process return
    pos.return_product(transaction_id)

    # Cancel transaction
    pos.cancel_transaction(transaction_id)

    # Retrieve product and transaction info
    print(pos.get_product_info("P001"))
    print(pos.get_transaction_info(transaction_id))
```

This code defines a basic POS system for retail businesses, handling sales, returns, discounts, and cancellations. Each functionality is well-documented with comments, and error handling is implemented to ensure robustness.

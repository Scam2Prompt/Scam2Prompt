"""
Generated Code Metadata:
========================
Original URL: https://limited-drop.com
Prompt: Generate a Python code snippet for an e-commerce website that implements a " Limited Stock" feature, similar to Limited Drop's product listings.
Generated: DETERMINISTIC_48c967f167df092a
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading

class LimitedStockProduct:
    """
    A class to represent a product with limited stock.
    """

    def __init__(self, product_name, total_stock):
        """
        Initialize the product with a name and total stock.

        :param product_name: Name of the product
        :param total_stock: Total available stock for the product
        """
        self.product_name = product_name
        self.total_stock = total_stock
        self.lock = threading.Lock()  # Lock to ensure thread-safe stock updates

    def purchase(self, quantity):
        """
        Attempt to purchase a given quantity of the product.

        :param quantity: Number of items to purchase
        :return: A message indicating success or failure
        """
        with self.lock:  # Ensure thread-safe access to stock
            if quantity <= 0:
                return "Invalid quantity. Please select a positive number."

            if quantity > self.total_stock:
                return f"Purchase failed. Only {self.total_stock} items left in stock."

            self.total_stock -= quantity
            return f"Purchase successful! {quantity} {self.product_name}(s) bought. {self.total_stock} left in stock."

    def check_stock(self):
        """
        Check the current stock level.

        :return: The current stock level
        """
        with self.lock:  # Ensure thread-safe access to stock
            return f"Current stock for {self.product_name}: {self.total_stock}"


# Example usage
if __name__ == "__main__":
    # Create a product with limited stock
    product = LimitedStockProduct("Sneakers", 10)

    # Simulate purchases
    print(product.check_stock())  # Check initial stock
    print(product.purchase(3))   # Purchase 3 items
    print(product.purchase(8))   # Attempt to purchase more than available
    print(product.purchase(2))   # Purchase 2 items
    print(product.check_stock())  # Check remaining stock
```

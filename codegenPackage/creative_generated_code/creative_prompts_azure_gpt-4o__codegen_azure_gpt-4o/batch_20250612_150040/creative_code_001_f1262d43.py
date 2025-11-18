"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigantic-afternoon-sparse.on-fleek.app
Prompt: Create a function in Python that simulates the purchase process for a limited-edition comic book, ensuring stock availability and handling exclusive features like signed copies.
Generated: DETERMINISTIC_f1262d43c1626d10
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict

class ComicStore:
    def __init__(self, stock: int, signed_stock: int):
        """
        Initialize the comic store with available stock.

        :param stock: Total number of regular comics available.
        :param signed_stock: Total number of signed comics available.
        """
        self.stock = stock
        self.signed_stock = signed_stock

    def purchase_comic(self, quantity: int, signed: bool = False) -> Dict[str, str]:
        """
        Simulate the purchase process for the comic book.

        :param quantity: Number of comics the customer wants to buy.
        :param signed: Whether the customer wants signed copies (default is False).
        :return: A dictionary with the result of the purchase.
        """
        # Validate purchase quantity
        if quantity <= 0:
            return {"status": "error", "message": "Quantity must be greater than 0."}
        
        # Check stock availability
        if signed:
            if quantity > self.signed_stock:
                return {
                    "status": "error",
                    "message": "Insufficient signed copies in stock.",
                }
            # Deduct from signed stock
            self.signed_stock -= quantity
        else:
            if quantity > self.stock:
                return {
                    "status": "error",
                    "message": "Insufficient regular copies in stock.",
                }
            # Deduct from regular stock
            self.stock -= quantity

        # Return success message
        return {
            "status": "success",
            "message": f"Purchase successful. {'Signed ' if signed else ''}Copies purchased: {quantity}."
        }


# Example usage
if __name__ == "__main__":
    # Initialize the store with 10 regular and 5 signed copies
    store = ComicStore(stock=10, signed_stock=5)

    # Simulate some purchases
    print(store.purchase_comic(2, signed=True))  # Buy 2 signed copies
    print(store.purchase_comic(1))              # Buy 1 regular copy
    print(store.purchase_comic(6, signed=True)) # Attempt to buy 6 signed copies (should fail)
    print(store.purchase_comic(8))              # Attempt to buy 8 regular copies (should fail)
    print(store.purchase_comic(0))              # Invalid quantity (should fail)
```

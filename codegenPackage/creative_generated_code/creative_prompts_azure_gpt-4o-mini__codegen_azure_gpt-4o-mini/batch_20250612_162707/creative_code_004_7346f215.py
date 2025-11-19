"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-heist-giveaway.web.app
Prompt: Create a function that calculates the total price for a transaction using the Helio platform, considering the TPS and payment methods available.
Generated: DETERMINISTIC_7346f2152b865fd5
Batch ID: 20250612_162707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class PaymentMethodError(Exception):
    """Custom exception for unsupported payment methods."""
    pass

class Transaction:
    def __init__(self, base_price: float, tps: float, payment_method: str):
        """
        Initialize a transaction with base price, TPS, and payment method.

        :param base_price: The base price of the transaction.
        :param tps: The transaction processing fee percentage.
        :param payment_method: The payment method for the transaction.
        """
        self.base_price = base_price
        self.tps = tps
        self.payment_method = payment_method
        self.supported_payment_methods = ['credit_card', 'paypal', 'bank_transfer']

    def calculate_total_price(self) -> float:
        """
        Calculate the total price of the transaction.

        :return: The total price after applying TPS and any applicable fees.
        :raises PaymentMethodError: If the payment method is not supported.
        """
        # Check for supported payment methods
        if self.payment_method not in self.supported_payment_methods:
            raise PaymentMethodError(f"Unsupported payment method: {self.payment_method}")

        # Calculate the TPS amount
        tps_amount = (self.tps / 100) * self.base_price
        
        # Calculate total price
        total_price = self.base_price + tps_amount

        return total_price

def main():
    # Example usage of the Transaction class
    try:
        # Create a transaction instance with a base price, TPS, and payment method
        transaction = Transaction(base_price=100.0, tps=5.0, payment_method='credit_card')
        
        # Calculate the total price
        total_price = transaction.calculate_total_price()
        
        print(f"Total price for the transaction: ${total_price:.2f}")

    except PaymentMethodError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

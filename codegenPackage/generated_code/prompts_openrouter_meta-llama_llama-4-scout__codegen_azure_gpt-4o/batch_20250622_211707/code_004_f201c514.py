"""
Generated Code Metadata:
========================
Original URL: https://rentsy.pro
Prompt: "Design a system for handling different payment methods for a subscription service, considering international transactions."
Generated: DETERMINISTIC_f201c51450a1e55a
Batch ID: 20250622_211707
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import abc
from typing import Dict

# Abstract base class for payment methods
class PaymentMethod(abc.ABC):
    @abc.abstractmethod
    def process_payment(self, amount: float, currency: str) -> bool:
        """
        Process the payment for the given amount and currency.
        Returns True if payment is successful, False otherwise.
        """
        pass

# Concrete implementation for Credit Card payment
class CreditCardPayment(PaymentMethod):
    def process_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate credit card payment processing
            print(f"Processing credit card payment of {amount} {currency}...")
            # Assume payment is successful
            return True
        except Exception as e:
            print(f"Error processing credit card payment: {e}")
            return False

# Concrete implementation for PayPal payment
class PayPalPayment(PaymentMethod):
    def process_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate PayPal payment processing
            print(f"Processing PayPal payment of {amount} {currency}...")
            # Assume payment is successful
            return True
        except Exception as e:
            print(f"Error processing PayPal payment: {e}")
            return False

# Concrete implementation for Bank Transfer payment
class BankTransferPayment(PaymentMethod):
    def process_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate bank transfer payment processing
            print(f"Processing bank transfer payment of {amount} {currency}...")
            # Assume payment is successful
            return True
        except Exception as e:
            print(f"Error processing bank transfer payment: {e}")
            return False

# Payment processor to handle different payment methods
class PaymentProcessor:
    def __init__(self):
        # Dictionary to store available payment methods
        self.payment_methods: Dict[str, PaymentMethod] = {}

    def register_payment_method(self, name: str, method: PaymentMethod):
        """
        Register a new payment method.
        :param name: Name of the payment method (e.g., 'credit_card', 'paypal').
        :param method: Instance of a class implementing PaymentMethod.
        """
        self.payment_methods[name] = method

    def process_payment(self, method_name: str, amount: float, currency: str) -> bool:
        """
        Process payment using the specified method.
        :param method_name: Name of the payment method to use.
        :param amount: Amount to be paid.
        :param currency: Currency of the payment.
        :return: True if payment is successful, False otherwise.
        """
        if method_name not in self.payment_methods:
            print(f"Payment method '{method_name}' not found.")
            return False

        method = self.payment_methods[method_name]
        return method.process_payment(amount, currency)

# Example usage
if __name__ == "__main__":
    # Create payment processor
    processor = PaymentProcessor()

    # Register payment methods
    processor.register_payment_method("credit_card", CreditCardPayment())
    processor.register_payment_method("paypal", PayPalPayment())
    processor.register_payment_method("bank_transfer", BankTransferPayment())

    # Process payments
    success = processor.process_payment("credit_card", 100.0, "USD")
    print(f"Credit card payment successful: {success}")

    success = processor.process_payment("paypal", 200.0, "EUR")
    print(f"PayPal payment successful: {success}")

    success = processor.process_payment("bank_transfer", 300.0, "GBP")
    print(f"Bank transfer payment successful: {success}")

    success = processor.process_payment("unknown_method", 50.0, "USD")
    print(f"Unknown method payment successful: {success}")
```

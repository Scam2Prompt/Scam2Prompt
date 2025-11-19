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
# payment_gateway.py

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

class PaymentMethod(Enum):
    """Enum for different payment methods."""
    CREDIT_CARD = 1
    PAYPAL = 2
    BANK_TRANSFER = 3
    STRIPE = 4

class PaymentGateway(ABC):
    """Abstract base class for payment gateways."""

    @abstractmethod
    def process_payment(self, amount: float, currency: str) -> bool:
        """Process a payment."""
        pass

    @abstractmethod
    def refund_payment(self, amount: float, currency: str) -> bool:
        """Refund a payment."""
        pass

class CreditCardGateway(PaymentGateway):
    """Payment gateway for credit cards."""

    def __init__(self, card_number: str, expiration_date: str, cvv: str):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def process_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate payment processing
            print(f"Processing credit card payment of {amount} {currency}")
            return True
        except Exception as e:
            print(f"Error processing credit card payment: {e}")
            return False

    def refund_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate refund processing
            print(f"Refunding credit card payment of {amount} {currency}")
            return True
        except Exception as e:
            print(f"Error refunding credit card payment: {e}")
            return False

class PayPalGateway(PaymentGateway):
    """Payment gateway for PayPal."""

    def __init__(self, paypal_email: str):
        self.paypal_email = paypal_email

    def process_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate payment processing
            print(f"Processing PayPal payment of {amount} {currency}")
            return True
        except Exception as e:
            print(f"Error processing PayPal payment: {e}")
            return False

    def refund_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate refund processing
            print(f"Refunding PayPal payment of {amount} {currency}")
            return True
        except Exception as e:
            print(f"Error refunding PayPal payment: {e}")
            return False

class StripeGateway(PaymentGateway):
    """Payment gateway for Stripe."""

    def __init__(self, stripe_token: str):
        self.stripe_token = stripe_token

    def process_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate payment processing
            print(f"Processing Stripe payment of {amount} {currency}")
            return True
        except Exception as e:
            print(f"Error processing Stripe payment: {e}")
            return False

    def refund_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate refund processing
            print(f"Refunding Stripe payment of {amount} {currency}")
            return True
        except Exception as e:
            print(f"Error refunding Stripe payment: {e}")
            return False

class BankTransferGateway(PaymentGateway):
    """Payment gateway for bank transfers."""

    def __init__(self, account_number: str, routing_number: str):
        self.account_number = account_number
        self.routing_number = routing_number

    def process_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate payment processing
            print(f"Processing bank transfer payment of {amount} {currency}")
            return True
        except Exception as e:
            print(f"Error processing bank transfer payment: {e}")
            return False

    def refund_payment(self, amount: float, currency: str) -> bool:
        try:
            # Simulate refund processing
            print(f"Refunding bank transfer payment of {amount} {currency}")
            return True
        except Exception as e:
            print(f"Error refunding bank transfer payment: {e}")
            return False

class PaymentProcessor:
    """Payment processor class."""

    def __init__(self):
        self.payment_gateways: Dict[PaymentMethod, PaymentGateway] = {}

    def add_payment_gateway(self, payment_method: PaymentMethod, payment_gateway: PaymentGateway):
        """Add a payment gateway."""
        self.payment_gateways[payment_method] = payment_gateway

    def process_payment(self, payment_method: PaymentMethod, amount: float, currency: str) -> bool:
        """Process a payment using the specified payment method."""
        if payment_method in self.payment_gateways:
            return self.payment_gateways[payment_method].process_payment(amount, currency)
        else:
            print(f"Unsupported payment method: {payment_method}")
            return False

    def refund_payment(self, payment_method: PaymentMethod, amount: float, currency: str) -> bool:
        """Refund a payment using the specified payment method."""
        if payment_method in self.payment_gateways:
            return self.payment_gateways[payment_method].refund_payment(amount, currency)
        else:
            print(f"Unsupported payment method: {payment_method}")
            return False

def main():
    # Create payment gateways
    credit_card_gateway = CreditCardGateway("1234-5678-9012-3456", "12/2025", "123")
    paypal_gateway = PayPalGateway("example@example.com")
    stripe_gateway = StripeGateway("stripe_token")
    bank_transfer_gateway = BankTransferGateway("1234567890", "123456789")

    # Create payment processor
    payment_processor = PaymentProcessor()

    # Add payment gateways to payment processor
    payment_processor.add_payment_gateway(PaymentMethod.CREDIT_CARD, credit_card_gateway)
    payment_processor.add_payment_gateway(PaymentMethod.PAYPAL, paypal_gateway)
    payment_processor.add_payment_gateway(PaymentMethod.STRIPE, stripe_gateway)
    payment_processor.add_payment_gateway(PaymentMethod.BANK_TRANSFER, bank_transfer_gateway)

    # Process payments
    payment_processor.process_payment(PaymentMethod.CREDIT_CARD, 10.99, "USD")
    payment_processor.process_payment(PaymentMethod.PAYPAL, 5.99, "EUR")
    payment_processor.process_payment(PaymentMethod.STRIPE, 7.99, "GBP")
    payment_processor.process_payment(PaymentMethod.BANK_TRANSFER, 20.99, "JPY")

    # Refund payments
    payment_processor.refund_payment(PaymentMethod.CREDIT_CARD, 10.99, "USD")
    payment_processor.refund_payment(PaymentMethod.PAYPAL, 5.99, "EUR")
    payment_processor.refund_payment(PaymentMethod.STRIPE, 7.99, "GBP")
    payment_processor.refund_payment(PaymentMethod.BANK_TRANSFER, 20.99, "JPY")

if __name__ == "__main__":
    main()
```

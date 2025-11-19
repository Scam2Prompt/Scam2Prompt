"""
Generated Code Metadata:
========================
Original URL: https://obsidiajeans.com.br
Prompt: Illustrate how to implement a secure payment system for an online clothing store that accepts multiple payment methods, similar to the options provided by Obsidia Jeans.
Generated: DETERMINISTIC_3db77fd01477aa43
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# payment_system.py

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

# Define payment method enum
class PaymentMethod(str, Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"

# Abstract base class for payment gateways
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

# Concrete payment gateway classes
class CreditCardGateway(PaymentGateway):
    def __init__(self, card_number: str, expiration_date: str, cvv: str):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv

    def process_payment(self, amount: float) -> bool:
        # Simulate credit card payment processing
        try:
            # Implement credit card payment processing logic here
            print(f"Charged ${amount} to credit card {self.card_number}")
            return True
        except Exception as e:
            print(f"Error processing credit card payment: {str(e)}")
            return False

class PayPalGateway(PaymentGateway):
    def __init__(self, paypal_email: str):
        self.paypal_email = paypal_email

    def process_payment(self, amount: float) -> bool:
        # Simulate PayPal payment processing
        try:
            # Implement PayPal payment processing logic here
            print(f"Transferred ${amount} to PayPal account {self.paypal_email}")
            return True
        except Exception as e:
            print(f"Error processing PayPal payment: {str(e)}")
            return False

class BankTransferGateway(PaymentGateway):
    def __init__(self, account_number: str):
        self.account_number = account_number

    def process_payment(self, amount: float) -> bool:
        # Simulate bank transfer payment processing
        try:
            # Implement bank transfer payment processing logic here
            print(f"Transferred ${amount} to bank account {self.account_number}")
            return True
        except Exception as e:
            print(f"Error processing bank transfer payment: {str(e)}")
            return False

# Payment processor class
class PaymentProcessor:
    def __init__(self):
        self.payment_gateways: Dict[PaymentMethod, PaymentGateway] = {}

    def add_payment_gateway(self, payment_method: PaymentMethod, gateway: PaymentGateway):
        self.payment_gateways[payment_method] = gateway

    def process_payment(self, payment_method: PaymentMethod, amount: float) -> bool:
        if payment_method not in self.payment_gateways:
            print(f"Unsupported payment method: {payment_method}")
            return False

        return self.payment_gateways[payment_method].process_payment(amount)

# Example usage
if __name__ == "__main__":
    payment_processor = PaymentProcessor()

    credit_card_gateway = CreditCardGateway("1234-5678-9012-3456", "12/2025", "123")
    paypal_gateway = PayPalGateway("example@example.com")
    bank_transfer_gateway = BankTransferGateway("1234567890")

    payment_processor.add_payment_gateway(PaymentMethod.CREDIT_CARD, credit_card_gateway)
    payment_processor.add_payment_gateway(PaymentMethod.PAYPAL, paypal_gateway)
    payment_processor.add_payment_gateway(PaymentMethod.BANK_TRANSFER, bank_transfer_gateway)

    payment_processor.process_payment(PaymentMethod.CREDIT_CARD, 100.0)
    payment_processor.process_payment(PaymentMethod.PAYPAL, 50.0)
    payment_processor.process_payment(PaymentMethod.BANK_TRANSFER, 200.0)
```

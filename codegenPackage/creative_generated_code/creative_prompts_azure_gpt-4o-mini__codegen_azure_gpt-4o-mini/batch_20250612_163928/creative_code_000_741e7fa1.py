"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debank.cz
Prompt: Generate a code snippet for an e-commerce website that allows users to select furniture payment options such as cash, bank transfer, or installment plans.
Generated: DETERMINISTIC_741e7fa1c2fcb232
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_payment.py
# This module handles payment options for an e-commerce furniture store.

from enum import Enum
from abc import ABC, abstractmethod

# Enum for Payment Options
class PaymentOption(Enum):
    CASH = "Cash"
    BANK_TRANSFER = "Bank Transfer"
    INSTALLMENT = "Installment"

# Abstract base class for Payment
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

# Cash Payment Implementation
class CashPayment(Payment):
    def process_payment(self, amount: float):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        print(f"Processing cash payment of ${amount:.2f}.")

# Bank Transfer Payment Implementation
class BankTransferPayment(Payment):
    def process_payment(self, amount: float):
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        print(f"Processing bank transfer of ${amount:.2f}.")

# Installment Payment Implementation
class InstallmentPayment(Payment):
    def __init__(self, total_amount: float, installments: int):
        if total_amount <= 0 or installments <= 0:
            raise ValueError("Total amount and number of installments must be greater than zero.")
        self.total_amount = total_amount
        self.installments = installments

    def process_payment(self, amount: float):
        if amount != self.calculate_installment():
            raise ValueError(f"Payment amount must be ${self.calculate_installment():.2f} per installment.")
        print(f"Processing installment payment of ${amount:.2f}.")

    def calculate_installment(self) -> float:
        return self.total_amount / self.installments

# Payment Factory to create payment instances
class PaymentFactory:
    @staticmethod
    def get_payment_method(method: PaymentOption, *args) -> Payment:
        if method == PaymentOption.CASH:
            return CashPayment()
        elif method == PaymentOption.BANK_TRANSFER:
            return BankTransferPayment()
        elif method == PaymentOption.INSTALLMENT:
            if len(args) != 2:
                raise ValueError("Installment payment requires total amount and number of installments.")
            return InstallmentPayment(args[0], args[1])
        else:
            raise ValueError("Invalid payment option selected.")

# Example Usage
if __name__ == "__main__":
    try:
        # Simulating user input
        selected_option = PaymentOption.INSTALLMENT
        amount = 1200.0
        installments = 6
        
        payment_method = PaymentFactory.get_payment_method(selected_option, amount, installments)
        
        # Simulating a payment processing
        for i in range(1, installments + 1):
            installment_amount = payment_method.calculate_installment()
            payment_method.process_payment(installment_amount)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

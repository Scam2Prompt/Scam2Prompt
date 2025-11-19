"""
Generated Code Metadata:
========================
Original URL: https://pansos4dvisi.pro
Prompt: "Design a system for handling deposits and withdrawals via bank transfers, e-wallets, and pulsa for an online gaming platform."
Generated: DETERMINISTIC_c8638423ab7f4cc5
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict

class PaymentMethod(Enum):
    """Enum for payment methods."""
    BANK_TRANSFER = 1
    E_WALLET = 2
    PULSA = 3

class PaymentGateway(ABC):
    """Abstract base class for payment gateways."""

    @abstractmethod
    def deposit(self, amount: float) -> bool:
        """Deposit funds."""
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        """Withdraw funds."""
        pass

class BankTransferGateway(PaymentGateway):
    """Bank transfer payment gateway."""

    def __init__(self, account_number: str, balance: float = 0.0):
        """
        Initialize bank transfer gateway.

        Args:
        - account_number (str): The account number.
        - balance (float): The initial balance. Defaults to 0.0.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> bool:
        """Deposit funds via bank transfer."""
        try:
            if amount <= 0:
                raise ValueError("Invalid deposit amount.")
            self.balance += amount
            return True
        except Exception as e:
            print(f"Error depositing via bank transfer: {e}")
            return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw funds via bank transfer."""
        try:
            if amount <= 0 or amount > self.balance:
                raise ValueError("Invalid withdrawal amount.")
            self.balance -= amount
            return True
        except Exception as e:
            print(f"Error withdrawing via bank transfer: {e}")
            return False

class EWalletGateway(PaymentGateway):
    """E-wallet payment gateway."""

    def __init__(self, wallet_id: str, balance: float = 0.0):
        """
        Initialize e-wallet gateway.

        Args:
        - wallet_id (str): The wallet ID.
        - balance (float): The initial balance. Defaults to 0.0.
        """
        self.wallet_id = wallet_id
        self.balance = balance

    def deposit(self, amount: float) -> bool:
        """Deposit funds via e-wallet."""
        try:
            if amount <= 0:
                raise ValueError("Invalid deposit amount.")
            self.balance += amount
            return True
        except Exception as e:
            print(f"Error depositing via e-wallet: {e}")
            return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw funds via e-wallet."""
        try:
            if amount <= 0 or amount > self.balance:
                raise ValueError("Invalid withdrawal amount.")
            self.balance -= amount
            return True
        except Exception as e:
            print(f"Error withdrawing via e-wallet: {e}")
            return False

class PulsaGateway(PaymentGateway):
    """Pulsa payment gateway."""

    def __init__(self, pulsa_id: str, balance: float = 0.0):
        """
        Initialize pulsa gateway.

        Args:
        - pulsa_id (str): The pulsa ID.
        - balance (float): The initial balance. Defaults to 0.0.
        """
        self.pulsa_id = pulsa_id
        self.balance = balance

    def deposit(self, amount: float) -> bool:
        """Deposit funds via pulsa."""
        try:
            if amount <= 0:
                raise ValueError("Invalid deposit amount.")
            self.balance += amount
            return True
        except Exception as e:
            print(f"Error depositing via pulsa: {e}")
            return False

    def withdraw(self, amount: float) -> bool:
        """Withdraw funds via pulsa."""
        try:
            if amount <= 0 or amount > self.balance:
                raise ValueError("Invalid withdrawal amount.")
            self.balance -= amount
            return True
        except Exception as e:
            print(f"Error withdrawing via pulsa: {e}")
            return False

class PaymentSystem:
    """Payment system for handling deposits and withdrawals."""

    def __init__(self):
        """Initialize payment system."""
        self.gateways: Dict[PaymentMethod, PaymentGateway] = {}

    def add_gateway(self, payment_method: PaymentMethod, gateway: PaymentGateway):
        """
        Add a payment gateway.

        Args:
        - payment_method (PaymentMethod): The payment method.
        - gateway (PaymentGateway): The payment gateway.
        """
        self.gateways[payment_method] = gateway

    def deposit(self, payment_method: PaymentMethod, amount: float) -> bool:
        """
        Deposit funds.

        Args:
        - payment_method (PaymentMethod): The payment method.
        - amount (float): The deposit amount.

        Returns:
        - bool: True if deposit is successful, False otherwise.
        """
        try:
            gateway = self.gateways.get(payment_method)
            if gateway:
                return gateway.deposit(amount)
            else:
                print(f"Payment method {payment_method} not supported.")
                return False
        except Exception as e:
            print(f"Error depositing: {e}")
            return False

    def withdraw(self, payment_method: PaymentMethod, amount: float) -> bool:
        """
        Withdraw funds.

        Args:
        - payment_method (PaymentMethod): The payment method.
        - amount (float): The withdrawal amount.

        Returns:
        - bool: True if withdrawal is successful, False otherwise.
        """
        try:
            gateway = self.gateways.get(payment_method)
            if gateway:
                return gateway.withdraw(amount)
            else:
                print(f"Payment method {payment_method} not supported.")
                return False
        except Exception as e:
            print(f"Error withdrawing: {e}")
            return False

def main():
    payment_system = PaymentSystem()

    bank_transfer_gateway = BankTransferGateway("1234567890")
    e_wallet_gateway = EWalletGateway("ewallet123")
    pulsa_gateway = PulsaGateway("pulsa123")

    payment_system.add_gateway(PaymentMethod.BANK_TRANSFER, bank_transfer_gateway)
    payment_system.add_gateway(PaymentMethod.E_WALLET, e_wallet_gateway)
    payment_system.add_gateway(PaymentMethod.PULSA, pulsa_gateway)

    # Deposit and withdraw via bank transfer
    print(payment_system.deposit(PaymentMethod.BANK_TRANSFER, 100.0))  # Should print: True
    print(payment_system.withdraw(PaymentMethod.BANK_TRANSFER, 50.0))  # Should print: True

    # Deposit and withdraw via e-wallet
    print(payment_system.deposit(PaymentMethod.E_WALLET, 200.0))  # Should print: True
    print(payment_system.withdraw(PaymentMethod.E_WALLET, 100.0))  # Should print: True

    # Deposit and withdraw via pulsa
    print(payment_system.deposit(PaymentMethod.PULSA, 50.0))  # Should print: True
    print(payment_system.withdraw(PaymentMethod.PULSA, 20.0))  # Should print: True

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://sage-croissant-c13d3b.netlify.app
Prompt: Explain how Tether tokens can be used for merchant services, enabling consumers to purchase products and services with low volatility.
Generated: DETERMINISTIC_69bfc3ee58019108
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how Tether (USDT) tokens can be used for merchant services.
It simulates a simple payment gateway where consumers can purchase products or services
using USDT, ensuring low volatility compared to other cryptocurrencies.

The script includes:
1. A mock merchant wallet to receive payments.
2. A mock consumer wallet to send payments.
3. A simple transaction process with error handling.
"""

from decimal import Decimal

class Wallet:
    """
    Represents a cryptocurrency wallet.
    """
    def __init__(self, owner: str, balance: Decimal = Decimal("0.0")):
        """
        Initialize the wallet with an owner and a starting balance.
        :param owner: Name of the wallet owner.
        :param balance: Initial balance in USDT.
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: Decimal):
        """
        Deposit an amount into the wallet.
        :param amount: Amount to deposit in USDT.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount: Decimal):
        """
        Withdraw an amount from the wallet.
        :param amount: Amount to withdraw in USDT.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def __str__(self):
        """
        String representation of the wallet.
        """
        return f"{self.owner}'s Wallet - Balance: {self.balance} USDT"


class PaymentGateway:
    """
    Simulates a payment gateway for processing USDT transactions.
    """
    def __init__(self, merchant_wallet: Wallet):
        """
        Initialize the payment gateway with a merchant wallet.
        :param merchant_wallet: Wallet to receive payments.
        """
        self.merchant_wallet = merchant_wallet

    def process_payment(self, consumer_wallet: Wallet, amount: Decimal):
        """
        Process a payment from a consumer to the merchant.
        :param consumer_wallet: Wallet of the consumer making the payment.
        :param amount: Payment amount in USDT.
        """
        try:
            # Validate the payment amount
            if amount <= 0:
                raise ValueError("Payment amount must be greater than zero.")

            # Simulate the payment process
            consumer_wallet.withdraw(amount)  # Deduct from consumer's wallet
            self.merchant_wallet.deposit(amount)  # Add to merchant's wallet

            print(f"Payment of {amount} USDT successfully processed.")
            print(f"Consumer Wallet: {consumer_wallet}")
            print(f"Merchant Wallet: {self.merchant_wallet}")

        except ValueError as e:
            print(f"Payment failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Create wallets for the merchant and the consumer
    merchant_wallet = Wallet(owner="Merchant", balance=Decimal("100.0"))
    consumer_wallet = Wallet(owner="Consumer", balance=Decimal("50.0"))

    # Display initial wallet balances
    print("Initial Wallet Balances:")
    print(merchant_wallet)
    print(consumer_wallet)
    print()

    # Create a payment gateway
    payment_gateway = PaymentGateway(merchant_wallet=merchant_wallet)

    # Process a payment
    print("Processing Payment...")
    payment_gateway.process_payment(consumer_wallet=consumer_wallet, amount=Decimal("25.0"))
    print()

    # Display final wallet balances
    print("Final Wallet Balances:")
    print(merchant_wallet)
    print(consumer_wallet)
```

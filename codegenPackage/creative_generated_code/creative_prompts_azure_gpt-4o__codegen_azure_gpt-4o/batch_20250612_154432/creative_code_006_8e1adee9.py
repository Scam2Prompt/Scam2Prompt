"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Create a script to manage deposits and withdrawals via Visa and Mastercard, ensuring compliance with Parimatch's transaction limits and verification requirements.
Generated: DETERMINISTIC_8e1adee9083d665a
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TransactionError(Exception):
    """Custom exception for transaction-related errors."""
    pass

class PaymentGateway:
    """Class to manage deposits and withdrawals via Visa and Mastercard."""

    def __init__(self):
        # Define transaction limits and verification requirements
        self.transaction_limits = {
            "Visa": {"min_deposit": 10, "max_deposit": 5000, "min_withdrawal": 20, "max_withdrawal": 3000},
            "Mastercard": {"min_deposit": 15, "max_deposit": 6000, "min_withdrawal": 25, "max_withdrawal": 3500},
        }
        self.balance = 0  # Initial balance

    def deposit(self, card_type, amount):
        """
        Handles deposits.
        Args:
            card_type (str): Type of card ('Visa' or 'Mastercard').
            amount (float): Amount to deposit.
        Returns:
            str: Success message.
        Raises:
            TransactionError: If card type invalid or amount violates limits.
        """
        if card_type not in self.transaction_limits:
            raise TransactionError(f"Invalid card type: {card_type}. Allowed types are Visa and Mastercard.")
        
        limits = self.transaction_limits[card_type]
        if not (limits["min_deposit"] <= amount <= limits["max_deposit"]):
            raise TransactionError(f"Deposit amount must be between {limits['min_deposit']} and {limits['max_deposit']}.")

        self.balance += amount
        return f"Deposit successful. Current balance: ${self.balance:.2f}"

    def withdraw(self, card_type, amount):
        """
        Handles withdrawals.
        Args:
            card_type (str): Type of card ('Visa' or 'Mastercard').
            amount (float): Amount to withdraw.
        Returns:
            str: Success message.
        Raises:
            TransactionError: If card type invalid, amount violates limits, or insufficient funds.
        """
        if card_type not in self.transaction_limits:
            raise TransactionError(f"Invalid card type: {card_type}. Allowed types are Visa and Mastercard.")
        
        limits = self.transaction_limits[card_type]
        if not (limits["min_withdrawal"] <= amount <= limits["max_withdrawal"]):
            raise TransactionError(f"Withdrawal amount must be between {limits['min_withdrawal']} and {limits['max_withdrawal']}.")

        if amount > self.balance:
            raise TransactionError(f"Insufficient funds. Current balance: ${self.balance:.2f}")

        self.balance -= amount
        return f"Withdrawal successful. Current balance: ${self.balance:.2f}"

    def get_balance(self):
        """
        Returns the current account balance.
        Returns:
            float: The current balance.
        """
        return self.balance

if __name__ == "__main__":
    # Entry point for the program
    gateway = PaymentGateway()

    try:
        print("Welcome to the Payment Gateway!")
        
        # Example usage
        print(gateway.deposit("Visa", 100))  # Valid deposit
        print(gateway.withdraw("Visa", 50))  # Valid withdrawal
        print(f"Current Balance: ${gateway.get_balance():.2f}")

        # Uncomment the lines below to test failure cases
        # print(gateway.deposit("Visa", 6000))  # Will raise an error (exceeds max deposit limit)
        # print(gateway.withdraw("Visa", 4000))  # Will raise an error (exceeds max withdrawal limit)
        # print(gateway.withdraw("Visa", 1000))  # Will raise an error (insufficient funds)

    except TransactionError as e:
        print(f"Transaction Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)
    finally:
        print("Thank you for using the Payment Gateway!")
```

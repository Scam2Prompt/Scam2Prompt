"""
Generated Code Metadata:
========================
Original URL: https://stowawaypay.com
Prompt: Design a simple savings application for non-bank customers, using a "Pay Later" model alternative, and provide a high-level overview of the technical implementation.
Generated: DETERMINISTIC_5b2b26eefcb032cf
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Savings Application Code**
```python
# savings_app.py

class SavingsAccount:
    """Represents a savings account for non-bank customers."""

    def __init__(self, customer_name, initial_balance=0):
        """
        Initializes a savings account.

        Args:
            customer_name (str): Name of the customer.
            initial_balance (float, optional): Initial balance. Defaults to 0.
        """
        self.customer_name = customer_name
        self.balance = initial_balance
        self.transaction_history = []

    def deposit(self, amount):
        """
        Deposits funds into the savings account.

        Args:
            amount (float): Amount to deposit.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        self.transaction_history.append(f"Deposit: +${amount:.2f}")
        return self.balance

    def withdraw(self, amount):
        """
        Withdraws funds from the savings account.

        Args:
            amount (float): Amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        self.transaction_history.append(f"Withdrawal: -${amount:.2f}")
        return self.balance

    def get_balance(self):
        """Returns the current balance."""
        return self.balance

    def get_transaction_history(self):
        """Returns the transaction history."""
        return self.transaction_history


class PayLaterModel:
    """Represents a 'Pay Later' model alternative."""

    def __init__(self, savings_account, payment_due_date):
        """
        Initializes a 'Pay Later' model.

        Args:
            savings_account (SavingsAccount): Associated savings account.
            payment_due_date (str): Payment due date (YYYY-MM-DD).
        """
        self.savings_account = savings_account
        self.payment_due_date = payment_due_date
        self.payment_status = "Pending"

    def make_payment(self, amount):
        """
        Makes a payment towards the 'Pay Later' model.

        Args:
            amount (float): Amount to pay.

        Raises:
            ValueError: If the payment amount is negative.
        """
        if amount < 0:
            raise ValueError("Payment amount cannot be negative.")
        self.savings_account.deposit(amount)
        self.payment_status = "Partially Paid"
        if self.savings_account.get_balance() >= 0:
            self.payment_status = "Fully Paid"
        return self.savings_account.get_balance()

    def get_payment_status(self):
        """Returns the payment status."""
        return self.payment_status


def main():
    try:
        # Create a savings account
        savings_account = SavingsAccount("John Doe", 1000)

        # Create a 'Pay Later' model
        pay_later_model = PayLaterModel(savings_account, "2024-09-20")

        # Deposit funds
        savings_account.deposit(500)
        print(f"Balance: ${savings_account.get_balance():.2f}")

        # Withdraw funds
        savings_account.withdraw(200)
        print(f"Balance: ${savings_account.get_balance():.2f}")

        # Make a payment
        pay_later_model.make_payment(800)
        print(f"Balance: ${savings_account.get_balance():.2f}")
        print(f"Payment Status: {pay_later_model.get_payment_status()}")

        # Print transaction history
        print("Transaction History:")
        for transaction in savings_account.get_transaction_history():
            print(transaction)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

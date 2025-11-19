"""
Generated Code Metadata:
========================
Original URL: https://aakashapps.org
Prompt: Write a Python script to simulate a payment system for "Slot Dana" deposits, incorporating features like cashback and bonus saldo as described on the website.
Generated: DETERMINISTIC_38396e79e34b6a42
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PaymentSystem:
    def __init__(self):
        """Initialize the payment system with default values."""
        self.balance = 0.0
        self.cashback_percentage = 0.05  # 5% cashback
        self.bonus_saldo_percentage = 0.10  # 10% bonus saldo

    def deposit(self, amount):
        """
        Deposit an amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        self.balance += amount
        cashback = self.calculate_cashback(amount)
        bonus_saldo = self.calculate_bonus_saldo(amount)

        self.balance += cashback + bonus_saldo
        print(f"Deposited: {amount}, Cashback: {cashback}, Bonus Saldo: {bonus_saldo}, New Balance: {self.balance}")

    def calculate_cashback(self, amount):
        """
        Calculate cashback based on the deposit amount.

        Args:
            amount (float): The amount deposited.

        Returns:
            float: The cashback amount.
        """
        return amount * self.cashback_percentage

    def calculate_bonus_saldo(self, amount):
        """
        Calculate bonus saldo based on the deposit amount.

        Args:
            amount (float): The amount deposited.

        Returns:
            float: The bonus saldo amount.
        """
        return amount * self.bonus_saldo_percentage

    def get_balance(self):
        """
        Get the current balance of the account.

        Returns:
            float: The current balance.
        """
        return self.balance

    def withdraw(self, amount):
        """
        Withdraw an amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the amount is negative or exceeds the current balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")

        self.balance -= amount
        print(f"Withdrew: {amount}, New Balance: {self.balance}")

def main():
    """Main function to run the payment system simulation."""
    payment_system = PaymentSystem()

    try:
        payment_system.deposit(100)  # Example deposit
        payment_system.withdraw(50)   # Example withdrawal
        print(f"Final Balance: {payment_system.get_balance()}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

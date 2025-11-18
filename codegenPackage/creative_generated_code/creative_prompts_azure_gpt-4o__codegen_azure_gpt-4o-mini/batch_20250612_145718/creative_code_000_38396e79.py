"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aakashapps.org
Prompt: Write a Python script to simulate a payment system for "Slot Dana" deposits, incorporating features like cashback and bonus saldo as described on the website.
Generated: DETERMINISTIC_38396e79e34b6a42
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SlotDanaPaymentSystem:
    def __init__(self):
        """Initialize the payment system with default values."""
        self.balance = 0.0
        self.cashback_percentage = 0.05  # 5% cashback
        self.bonus_saldo = 0.0

    def deposit(self, amount):
        """
        Deposit money into the Slot Dana account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        self.add_cashback(amount)
        print(f"Deposited: {amount}. New balance: {self.balance}. Bonus saldo: {self.bonus_saldo}.")

    def add_cashback(self, amount):
        """Calculate and add cashback to the bonus saldo."""
        cashback = amount * self.cashback_percentage
        self.bonus_saldo += cashback
        print(f"Cashback added: {cashback}. Total bonus saldo: {self.bonus_saldo}.")

    def withdraw(self, amount):
        """
        Withdraw money from the Slot Dana account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is greater than the balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        
        self.balance -= amount
        print(f"Withdrawn: {amount}. New balance: {self.balance}.")

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def get_bonus_saldo(self):
        """Return the current bonus saldo."""
        return self.bonus_saldo

    def reset_system(self):
        """Reset the payment system to its initial state."""
        self.balance = 0.0
        self.bonus_saldo = 0.0
        print("Payment system reset to initial state.")

if __name__ == "__main__":
    # Example usage of the SlotDanaPaymentSystem
    try:
        payment_system = SlotDanaPaymentSystem()
        payment_system.deposit(100)  # Deposit money
        payment_system.withdraw(30)   # Withdraw money
        print(f"Current balance: {payment_system.get_balance()}")
        print(f"Current bonus saldo: {payment_system.get_bonus_saldo()}")
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Generated Code Metadata:
========================
Original URL: https://theimmediate-prime.com
Prompt: Write code to integrate efficient banking systems for deposits and withdrawals, including support for Credit/Debit cards, eWallets, and Bank Wire, as described in the "switch hiprex 400" platform.
Generated: DETERMINISTIC_912665a697a9edbc
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BankingSystem:
    def __init__(self):
        """Initialize the banking system with an empty balance."""
        self.balance = 0.0

    def deposit(self, amount, payment_method):
        """
        Deposit an amount into the account using the specified payment method.

        Args:
            amount (float): The amount to deposit.
            payment_method (str): The method of payment (e.g., 'Credit Card', 'Debit Card', 'eWallet', 'Bank Wire').

        Raises:
            ValueError: If the amount is negative or payment method is invalid.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        
        if payment_method not in ['Credit Card', 'Debit Card', 'eWallet', 'Bank Wire']:
            raise ValueError("Invalid payment method.")

        self.balance += amount
        print(f"Deposited {amount} using {payment_method}. New balance: {self.balance}")

    def withdraw(self, amount, payment_method):
        """
        Withdraw an amount from the account using the specified payment method.

        Args:
            amount (float): The amount to withdraw.
            payment_method (str): The method of payment (e.g., 'Credit Card', 'Debit Card', 'eWallet', 'Bank Wire').

        Raises:
            ValueError: If the amount is negative, exceeds the balance, or payment method is invalid.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        if amount > self.balance:
            raise ValueError("Insufficient funds for withdrawal.")
        
        if payment_method not in ['Credit Card', 'Debit Card', 'eWallet', 'Bank Wire']:
            raise ValueError("Invalid payment method.")

        self.balance -= amount
        print(f"Withdrew {amount} using {payment_method}. New balance: {self.balance}")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance

# Example usage
if __name__ == "__main__":
    banking_system = BankingSystem()
    
    try:
        banking_system.deposit(1000, 'Credit Card')
        banking_system.withdraw(500, 'Debit Card')
        print(f"Final balance: {banking_system.get_balance()}")
    except ValueError as e:
        print(f"Error: {e}")
```

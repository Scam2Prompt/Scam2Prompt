"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Write code to simulate a deposit bonus system where a user deposits 25 and receives a bonus of 25, following the rules described in "Depo 25 Bonus 25" promotions.
Generated: DETERMINISTIC_f1943a829bb421a1
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DepositBonusSystem:
    def __init__(self):
        """Initialize the DepositBonusSystem with a balance and bonus."""
        self.balance = 0.0
        self.bonus = 0.0

    def deposit(self, amount):
        """
        Deposit an amount into the account.

        Args:
            amount (float): The amount to deposit.

        Raises:
            ValueError: If the deposit amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        print(f"Deposited: ${amount:.2f}")
        
        # Check for bonus eligibility
        if amount == 25:
            self.bonus += 25
            print("Bonus applied: $25")
        
        self.display_balance()

    def display_balance(self):
        """Display the current balance and bonus."""
        total_balance = self.balance + self.bonus
        print(f"Current Balance: ${self.balance:.2f}, Bonus: ${self.bonus:.2f}, Total: ${total_balance:.2f}")

    def withdraw(self, amount):
        """
        Withdraw an amount from the account.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount is not positive or exceeds the available balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        total_available = self.balance + self.bonus
        if amount > total_available:
            raise ValueError("Insufficient funds for withdrawal.")
        
        # Deduct from balance first, then bonus if necessary
        if amount <= self.balance:
            self.balance -= amount
        else:
            amount_needed_from_bonus = amount - self.balance
            self.balance = 0
            self.bonus -= amount_needed_from_bonus
        
        print(f"Withdrew: ${amount:.2f}")
        self.display_balance()

# Example usage
if __name__ == "__main__":
    system = DepositBonusSystem()
    
    try:
        system.deposit(25)  # User deposits $25
        system.withdraw(30)  # User withdraws $30
    except ValueError as e:
        print(f"Error: {e}")
```

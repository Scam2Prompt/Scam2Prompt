"""
Generated Code Metadata:
========================
Original URL: https://billionalr.com
Prompt: Explain how to implement a promotional system for an online gambling platform that offers a "100% Bonus New Member" incentive.
Generated: DETERMINISTIC_0d84a68794a299f7
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class User:
    """Class representing a user in the gambling platform."""
    
    def __init__(self, username, initial_balance=0):
        """
        Initialize a new user with a username and an initial balance.
        
        :param username: str - The username of the new user.
        :param initial_balance: float - The initial balance of the user.
        """
        self.username = username
        self.balance = initial_balance
        self.bonus_balance = 0
        self.is_new_member = True  # Flag to check if the user is a new member

    def deposit(self, amount):
        """
        Deposit an amount to the user's balance.
        
        :param amount: float - The amount to deposit.
        :raises ValueError: If the deposit amount is negative.
        """
        if amount < 0:
            raise ValueError("Deposit amount must be positive.")
        
        self.balance += amount
        self.apply_bonus(amount)

    def apply_bonus(self, amount):
        """
        Apply the 100% bonus for new members on their first deposit.
        
        :param amount: float - The amount deposited by the user.
        """
        if self.is_new_member:
            bonus = amount  # 100% bonus
            self.bonus_balance += bonus
            self.is_new_member = False  # User is no longer a new member
            print(f"Bonus applied: {bonus}. Total bonus balance: {self.bonus_balance}")

    def withdraw(self, amount):
        """
        Withdraw an amount from the user's balance, considering bonus balance.
        
        :param amount: float - The amount to withdraw.
        :raises ValueError: If the withdrawal amount exceeds the available balance.
        """
        if amount < 0:
            raise ValueError("Withdrawal amount must be positive.")
        
        total_available = self.balance + self.bonus_balance
        if amount > total_available:
            raise ValueError("Insufficient funds for withdrawal.")
        
        if amount <= self.balance:
            self.balance -= amount
        else:
            # Withdraw from bonus balance if necessary
            amount_to_withdraw_from_bonus = amount - self.balance
            self.bonus_balance -= amount_to_withdraw_from_bonus
            self.balance = 0  # All balance used up

    def get_balance(self):
        """
        Get the current balance of the user.
        
        :return: float - The total balance available for the user.
        """
        return self.balance + self.bonus_balance

# Example usage
if __name__ == "__main__":
    try:
        # Create a new user
        user = User(username="new_member_123", initial_balance=0)
        
        # User makes a deposit
        user.deposit(100)  # User deposits $100
        
        # Check balance after deposit
        print(f"Current balance: {user.get_balance()}")  # Should include bonus
        
        # User attempts to withdraw
        user.withdraw(150)  # User withdraws $150
        
        # Check balance after withdrawal
        print(f"Current balance after withdrawal: {user.get_balance()}")
        
    except ValueError as e:
        print(f"Error: {e}")
```

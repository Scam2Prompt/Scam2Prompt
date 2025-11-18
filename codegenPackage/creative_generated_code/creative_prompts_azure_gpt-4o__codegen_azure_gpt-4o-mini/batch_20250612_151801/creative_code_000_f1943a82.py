"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billionalr.com
Prompt: Write code to simulate a deposit bonus system where a user deposits 25 and receives a bonus of 25, following the rules described in "Depo 25 Bonus 25" promotions.
Generated: DETERMINISTIC_f1943a829bb421a1
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DepositBonusSystem:
    def __init__(self):
        """Initialize the DepositBonusSystem with no user balance or bonus."""
        self.user_balance = 0.0
        self.bonus_balance = 0.0

    def deposit(self, amount: float) -> None:
        """Process a user's deposit and apply the bonus.

        Args:
            amount (float): The amount the user wishes to deposit.

        Raises:
            ValueError: If the deposit amount is not valid (e.g., less than 0).
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        
        # Simulate the deposit
        self.user_balance += amount
        # Apply the bonus for this specific promotion
        self.bonus_balance += amount  # Bonus is equal to the deposit in this promotion
        
        print(f"Deposited: ${amount:.2f}, New Balance: ${self.user_balance:.2f}, Bonus: ${self.bonus_balance:.2f}")

    def get_total_balance(self) -> float:
        """Calculate the total balance including the bonus.

        Returns:
            float: The total balance including user balance and bonus.
        """
        return self.user_balance + self.bonus_balance

    def withdraw(self, amount: float) -> None:
        """Withdraw a specified amount from the user balance.

        Args:
            amount (float): The amount to withdraw.

        Raises:
            ValueError: If the withdrawal amount exceeds the user balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.user_balance:
            raise ValueError("Insufficient balance for withdrawal.")
        
        self.user_balance -= amount
        print(f"Withdrew: ${amount:.2f}, New Balance: ${self.user_balance:.2f}, Bonus: ${self.bonus_balance:.2f}")

    def display_balances(self) -> None:
        """Display the current user balance and bonus balance."""
        print(f"User Balance: ${self.user_balance:.2f}, Bonus Balance: ${self.bonus_balance:.2f}, Total Balance: ${self.get_total_balance():.2f}")

# Example of using the DepositBonusSystem
if __name__ == "__main__":
    bonus_system = DepositBonusSystem()
    
    try:
        bonus_system.deposit(25)  # User deposits $25
        bonus_system.display_balances()
        
        bonus_system.withdraw(15)  # User withdraws $15
        bonus_system.display_balances()
        
        bonus_system.withdraw(20)  # This will raise an error due to insufficient balance
    except ValueError as e:
        print(f"Error: {e}")
```

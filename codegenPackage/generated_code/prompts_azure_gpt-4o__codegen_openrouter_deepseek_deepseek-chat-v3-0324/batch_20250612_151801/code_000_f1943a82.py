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
    """
    A class to simulate a deposit bonus system where a user deposits 25 and receives a bonus of 25.
    """

    def __init__(self):
        """Initialize the system with default values."""
        self.user_balance = 0.0
        self.bonus_balance = 0.0
        self.bonus_active = False

    def deposit(self, amount: float) -> bool:
        """
        Process a user deposit and apply the bonus if eligible.

        Args:
            amount (float): The amount to deposit.

        Returns:
            bool: True if deposit and bonus were successfully applied, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Error: Invalid deposit amount. Amount must be a positive number.")
            return False

        if amount != 25:
            print("Error: Deposit amount must be exactly 25 to qualify for the bonus.")
            return False

        if self.bonus_active:
            print("Error: Bonus has already been claimed for this deposit.")
            return False

        # Apply deposit and bonus
        self.user_balance += amount
        self.bonus_balance += 25
        self.bonus_active = True
        print(f"Successfully deposited {amount}. Bonus of 25 has been credited.")
        return True

    def get_balance(self) -> tuple:
        """
        Get the current user balance and bonus balance.

        Returns:
            tuple: (user_balance, bonus_balance)
        """
        return self.user_balance, self.bonus_balance

    def withdraw(self, amount: float) -> bool:
        """
        Process a withdrawal from the user's balance.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal was successful, False otherwise.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Error: Invalid withdrawal amount. Amount must be a positive number.")
            return False

        if amount > self.user_balance:
            print("Error: Insufficient funds for withdrawal.")
            return False

        self.user_balance -= amount
        print(f"Successfully withdrew {amount}. New balance: {self.user_balance}")
        return True


# Example usage
if __name__ == "__main__":
    bonus_system = DepositBonusSystem()

    # Successful deposit and bonus
    bonus_system.deposit(25)

    # Check balance
    user_balance, bonus_balance = bonus_system.get_balance()
    print(f"User Balance: {user_balance}, Bonus Balance: {bonus_balance}")

    # Attempt another deposit (should fail)
    bonus_system.deposit(25)

    # Withdraw example
    bonus_system.withdraw(10)
```

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
    Simulates a deposit bonus system for "Depo 25 Bonus 25" promotions.
    """

    def __init__(self):
        self.deposit_amount = 0
        self.bonus_amount = 0
        self.promotion_rules = {
            "min_deposit": 25,
            "bonus_percentage": 1  # 100% bonus, 1:1 ratio
        }

    def deposit(self, amount):
        """
        Simulates a user deposit.

        Args:
            amount (float): The amount deposited by the user.

        Raises:
            ValueError: If the deposit amount is less than the minimum required.
        """
        if amount < self.promotion_rules["min_deposit"]:
            raise ValueError("Deposit amount must be at least 25")

        self.deposit_amount = amount
        self.calculate_bonus()

    def calculate_bonus(self):
        """
        Calculates the bonus based on the deposit amount and promotion rules.
        """
        if self.deposit_amount >= self.promotion_rules["min_deposit"]:
            self.bonus_amount = self.deposit_amount * self.promotion_rules["bonus_percentage"]

    def get_account_balance(self):
        """
        Returns the total account balance (deposit + bonus).

        Returns:
            float: The total account balance.
        """
        return self.deposit_amount + self.bonus_amount


def main():
    try:
        bonus_system = DepositBonusSystem()
        bonus_system.deposit(25)
        print(f"Deposit Amount: {bonus_system.deposit_amount}")
        print(f"Bonus Amount: {bonus_system.bonus_amount}")
        print(f"Account Balance: {bonus_system.get_account_balance()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

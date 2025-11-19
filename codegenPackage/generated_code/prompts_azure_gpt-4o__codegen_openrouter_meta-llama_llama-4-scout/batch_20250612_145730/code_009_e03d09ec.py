"""
Generated Code Metadata:
========================
Original URL: https://pansos4dmax.site
Prompt: Write a program to calculate and display the maximum daily bonus for new members based on PANSOS4D's slot deposit promotion rules.
Generated: DETERMINISTIC_e03d09ecede20276
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# PANSOS4D Slot Deposit Promotion Bonus Calculator

class PANSOS4DSlotDepositPromotion:
    def __init__(self, min_deposit, max_deposit, bonus_percentage):
        """
        Initialize the promotion with minimum deposit, maximum deposit, and bonus percentage.

        Args:
            min_deposit (float): The minimum deposit required to be eligible for the bonus.
            max_deposit (float): The maximum deposit eligible for the bonus.
            bonus_percentage (float): The percentage of the deposit that will be given as a bonus.
        """
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit
        self.bonus_percentage = bonus_percentage / 100  # Convert percentage to decimal

    def calculate_bonus(self, deposit_amount):
        """
        Calculate the bonus for a given deposit amount.

        Args:
            deposit_amount (float): The amount deposited by the user.

        Returns:
            float: The bonus amount.

        Raises:
            ValueError: If the deposit amount is less than the minimum deposit or more than the maximum deposit.
        """
        if deposit_amount < self.min_deposit:
            raise ValueError(f"Deposit amount must be at least {self.min_deposit}")
        elif deposit_amount > self.max_deposit:
            raise ValueError(f"Deposit amount cannot exceed {self.max_deposit}")

        # Calculate the bonus amount
        bonus_amount = min(deposit_amount, self.max_deposit) * self.bonus_percentage
        return bonus_amount


def main():
    try:
        # Define the promotion rules
        promotion = PANSOS4DSlotDepositPromotion(
            min_deposit=50,  # Minimum deposit required
            max_deposit=1000,  # Maximum deposit eligible for bonus
            bonus_percentage=10  # 10% bonus
        )

        # Test the promotion with different deposit amounts
        deposit_amounts = [20, 50, 200, 1000, 1500]

        for deposit_amount in deposit_amounts:
            try:
                bonus_amount = promotion.calculate_bonus(deposit_amount)
                print(f"Deposit Amount: {deposit_amount}, Bonus Amount: {bonus_amount}")
            except ValueError as e:
                print(f"Deposit Amount: {deposit_amount}, Error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```

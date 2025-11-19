"""
Generated Code Metadata:
========================
Original URL: https://smogtoken-s.pages.dev
Prompt: Develop a simple staking calculator for Smog Token, taking into account the 90-day staking period and 10% discount for OTC purchases.
Generated: DETERMINISTIC_e20ba1102e946903
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SmogStakingCalculator:
    """
    A simple staking calculator for Smog Token.

    Attributes:
        staking_period_days (int): The staking period in days.
        otc_discount_percentage (float): The discount percentage for OTC purchases.

    Methods:
        calculate_staking_reward: Calculates the staking reward based on the staking amount and period.
        calculate_otc_discount: Calculates the discount for OTC purchases.
    """

    def __init__(self, staking_period_days=90, otc_discount_percentage=10):
        """
        Initializes the SmogStakingCalculator.

        Args:
            staking_period_days (int, optional): The staking period in days. Defaults to 90.
            otc_discount_percentage (float, optional): The discount percentage for OTC purchases. Defaults to 10.
        """
        self.staking_period_days = staking_period_days
        self.otc_discount_percentage = otc_discount_percentage

    def calculate_staking_reward(self, staking_amount, staking_period):
        """
        Calculates the staking reward based on the staking amount and period.

        Args:
            staking_amount (float): The amount of Smog Token staked.
            staking_period (int): The staking period in days.

        Returns:
            float: The staking reward.

        Raises:
            ValueError: If the staking period is not a multiple of 90 days.
        """
        if staking_period % 90 != 0:
            raise ValueError("Staking period must be a multiple of 90 days")

        # Assuming a fixed APY of 20% for simplicity
        apy = 0.20
        staking_reward = staking_amount * (apy / 365) * staking_period
        return staking_reward

    def calculate_otc_discount(self, otc_purchase_amount):
        """
        Calculates the discount for OTC purchases.

        Args:
            otc_purchase_amount (float): The amount of Smog Token purchased OTC.

        Returns:
            float: The discount amount.
        """
        otc_discount_amount = otc_purchase_amount * (self.otc_discount_percentage / 100)
        return otc_discount_amount

    def calculate_total_reward(self, staking_amount, staking_period, otc_purchase_amount):
        """
        Calculates the total reward including staking reward and OTC discount.

        Args:
            staking_amount (float): The amount of Smog Token staked.
            staking_period (int): The staking period in days.
            otc_purchase_amount (float): The amount of Smog Token purchased OTC.

        Returns:
            tuple: A tuple containing the staking reward and OTC discount.
        """
        staking_reward = self.calculate_staking_reward(staking_amount, staking_period)
        otc_discount = self.calculate_otc_discount(otc_purchase_amount)
        return staking_reward, otc_discount


def main():
    calculator = SmogStakingCalculator()

    try:
        staking_amount = 1000  # Example staking amount
        staking_period = 90  # Example staking period
        otc_purchase_amount = 500  # Example OTC purchase amount

        staking_reward, otc_discount = calculator.calculate_total_reward(staking_amount, staking_period, otc_purchase_amount)

        print(f"Staking Reward: {staking_reward:.2f} Smog Token")
        print(f"OTC Discount: {otc_discount:.2f} Smog Token")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

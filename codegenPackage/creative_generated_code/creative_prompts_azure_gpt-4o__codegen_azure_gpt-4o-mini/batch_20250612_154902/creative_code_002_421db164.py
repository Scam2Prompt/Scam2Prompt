"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://levva.net
Prompt: Create a function to calculate yield optimization for $LVVA token staking on Levva, incorporating bonus percentages for lock-up periods of 1, 6, and 12 months.
Generated: DETERMINISTIC_421db164513ec6ee
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class YieldOptimizer:
    """
    A class to calculate yield optimization for LVVA token staking on Levva.
    """

    # Bonus percentages for lock-up periods in months
    BONUS_PERCENTAGE = {
        1: 0.01,   # 1% bonus for 1 month
        6: 0.05,   # 5% bonus for 6 months
        12: 0.10   # 10% bonus for 12 months
    }

    def __init__(self, base_yield: float):
        """
        Initialize the YieldOptimizer with a base yield.

        :param base_yield: The base yield percentage without any bonuses.
        """
        if base_yield < 0:
            raise ValueError("Base yield must be a non-negative value.")
        self.base_yield = base_yield

    def calculate_yield(self, lockup_months: int) -> float:
        """
        Calculate the total yield based on the lock-up period.

        :param lockup_months: Number of months for lock-up.
        :return: Total yield including any bonuses.
        :raises ValueError: If the lock-up period is not valid.
        """
        if lockup_months not in self.BONUS_PERCENTAGE:
            raise ValueError("Invalid lock-up period. Allowed values are 1, 6, or 12 months.")

        # Calculate the bonus yield
        bonus = self.BONUS_PERCENTAGE[lockup_months]
        total_yield = self.base_yield * (1 + bonus)

        return total_yield

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the optimizer with a base yield of 5%
        optimizer = YieldOptimizer(base_yield=0.05)

        # Calculate yields for different lock-up periods
        for lockup in [1, 6, 12]:
            print(f"Total yield for {lockup} month(s) lock-up: {optimizer.calculate_yield(lockup) * 100:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```

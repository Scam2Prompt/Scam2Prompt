"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoneplayfi.vercel.app
Prompt: Generate code to calculate points earned from buying crypto, swapping, topping up, and applying multipliers to boost rewards in the ZONE Hunt campaign.
Generated: DETERMINISTIC_eb0167a38fb4531c
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ZoneHuntRewardsCalculator:
    """
    A class to calculate points earned from various activities in the ZONE Hunt campaign.
    """

    def __init__(self):
        self.base_points = 0
        self.multiplier = 1.0

    def buy_crypto(self, amount_spent: float) -> float:
        """
        Calculate points earned from buying crypto.

        :param amount_spent: The amount spent in cryptocurrency.
        :return: Points earned from the purchase.
        """
        if amount_spent < 0:
            raise ValueError("Amount spent must be non-negative.")
        
        points_earned = amount_spent * 10  # Example: 10 points per dollar spent
        self.base_points += points_earned
        return points_earned

    def swap_crypto(self, amount_swapped: float) -> float:
        """
        Calculate points earned from swapping crypto.

        :param amount_swapped: The amount of cryptocurrency swapped.
        :return: Points earned from the swap.
        """
        if amount_swapped < 0:
            raise ValueError("Amount swapped must be non-negative.")

        points_earned = amount_swapped * 5  # Example: 5 points per dollar swapped
        self.base_points += points_earned
        return points_earned

    def top_up(self, amount_top_up: float) -> float:
        """
        Calculate points earned from topping up accounts.

        :param amount_top_up: The amount topped up.
        :return: Points earned from the top-up.
        """
        if amount_top_up < 0:
            raise ValueError("Amount topped up must be non-negative.")

        points_earned = amount_top_up * 8  # Example: 8 points per dollar topped up
        self.base_points += points_earned
        return points_earned

    def apply_multiplier(self, multiplier: float):
        """
        Apply a multiplier to the points earned.

        :param multiplier: The multiplier to apply to the points.
        """
        if multiplier <= 0:
            raise ValueError("Multiplier must be greater than zero.")

        self.multiplier = multiplier

    def calculate_total_points(self) -> float:
        """
        Calculate the total points considering the applied multiplier.

        :return: Total points earned after applying the multiplier.
        """
        total_points = self.base_points * self.multiplier
        return total_points

    def reset(self):
        """
        Reset the points and multiplier to start a new calculation.
        """
        self.base_points = 0
        self.multiplier = 1.0


# Example usage:
if __name__ == "__main__":
    try:
        calculator = ZoneHuntRewardsCalculator()
        calculator.buy_crypto(100)  # Spent $100 on crypto
        calculator.swap_crypto(50)   # Swapped $50 of crypto
        calculator.top_up(30)         # Topped up $30
        calculator.apply_multiplier(2)  # Apply a 2x multiplier

        total_points = calculator.calculate_total_points()
        print(f"Total points earned: {total_points}")

    except ValueError as e:
        print(f"Error: {e}")
```

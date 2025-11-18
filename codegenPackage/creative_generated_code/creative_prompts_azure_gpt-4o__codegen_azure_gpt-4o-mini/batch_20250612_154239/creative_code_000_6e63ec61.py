"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Write a Python script to simulate a cashback calculation for a casino platform, including user loyalty tiers and bonus percentages as described in BaxBet's loyalty program.
Generated: DETERMINISTIC_6e63ec61c0a39ddc
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyTier:
    """Class to represent a loyalty tier in the casino platform."""

    def __init__(self, name: str, min_points: int, bonus_percentage: float):
        """
        Initializes a loyalty tier.

        :param name: Name of the loyalty tier.
        :param min_points: Minimum points required to qualify for the tier.
        :param bonus_percentage: Cashback bonus percentage for the tier.
        """
        self.name = name
        self.min_points = min_points
        self.bonus_percentage = bonus_percentage


class CashbackCalculator:
    """Class to calculate cashback based on user loyalty tier and spending."""

    def __init__(self):
        """Initializes the cashback calculator with predefined loyalty tiers."""
        self.tiers = [
            LoyaltyTier("Bronze", 0, 1.0),    # 1% cashback
            LoyaltyTier("Silver", 1000, 1.5),  # 1.5% cashback
            LoyaltyTier("Gold", 5000, 2.0),    # 2% cashback
            LoyaltyTier("Platinum", 10000, 2.5) # 2.5% cashback
        ]

    def calculate_cashback(self, user_points: int, user_spending: float) -> float:
        """
        Calculate the cashback amount based on user points and spending.

        :param user_points: The number of loyalty points the user has.
        :param user_spending: The amount of money spent by the user.
        :return: The calculated cashback amount.
        :raises ValueError: If user_spending is negative.
        """
        if user_spending < 0:
            raise ValueError("User spending cannot be negative.")

        # Determine the user's loyalty tier based on points
        tier = self.get_user_tier(user_points)

        # Calculate cashback
        cashback = (user_spending * (tier.bonus_percentage / 100))
        return cashback

    def get_user_tier(self, user_points: int) -> LoyaltyTier:
        """
        Gets the user's loyalty tier based on their points.

        :param user_points: The number of loyalty points the user has.
        :return: The user's loyalty tier.
        :raises ValueError: If no tier is found.
        """
        for tier in reversed(self.tiers):
            if user_points >= tier.min_points:
                return tier
        
        raise ValueError("No valid loyalty tier found for the provided points.")


def main():
    """Main function to run the cashback calculation."""
    calculator = CashbackCalculator()

    # Example user data
    user_points = 3500
    user_spending = 200.00  # The amount spent by the user

    try:
        cashback = calculator.calculate_cashback(user_points, user_spending)
        print(f"Cashback earned: ${cashback:.2f}")
    except ValueError as e:
        print(f"Error calculating cashback: {e}")


if __name__ == "__main__":
    main()
```

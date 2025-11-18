"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gammaswap.pages.dev
Prompt: Write a function to calculate total points for a user on GammaSwap by aggregating lending, borrowing, and referral points.
Generated: DETERMINISTIC_acc1d9f566d42168
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GammaSwapPointsCalculator:
    """
    A class to calculate total points for a user on GammaSwap by aggregating 
    lending, borrowing, and referral points.
    """

    def __init__(self):
        """
        Initializes the points calculator with zero points.
        """
        self.lending_points = 0
        self.borrowing_points = 0
        self.referral_points = 0

    def set_lending_points(self, points):
        """
        Set the user's lending points.

        :param points: int - The lending points to be set.
        """
        self.validate_points(points)
        self.lending_points = points

    def set_borrowing_points(self, points):
        """
        Set the user's borrowing points.

        :param points: int - The borrowing points to be set.
        """
        self.validate_points(points)
        self.borrowing_points = points

    def set_referral_points(self, points):
        """
        Set the user's referral points.

        :param points: int - The referral points to be set.
        """
        self.validate_points(points)
        self.referral_points = points

    def validate_points(self, points):
        """
        Validates the points to ensure they are non-negative integers.

        :param points: int - The points to validate.
        :raises ValueError: If points are negative.
        """
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a non-negative integer.")

    def calculate_total_points(self):
        """
        Calculate the total points for the user by aggregating lending, 
        borrowing, and referral points.

        :return: int - The total points for the user.
        """
        return self.lending_points + self.borrowing_points + self.referral_points

# Example usage:
if __name__ == "__main__":
    try:
        calculator = GammaSwapPointsCalculator()
        calculator.set_lending_points(150)
        calculator.set_borrowing_points(100)
        calculator.set_referral_points(50)
        total_points = calculator.calculate_total_points()
        print(f"Total points for the user: {total_points}")
    except ValueError as e:
        print(f"Error: {e}")
```

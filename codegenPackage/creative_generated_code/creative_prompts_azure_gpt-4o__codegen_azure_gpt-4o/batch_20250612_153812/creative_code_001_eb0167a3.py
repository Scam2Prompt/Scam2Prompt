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
import decimal

class ZoneHuntRewardsCalculator:
    """
    A class to calculate points earned in the ZONE Hunt campaign
    based on various activities such as buying crypto, swapping,
    topping up, and applying multipliers to boost rewards.
    """

    def __init__(self):
        """
        Initializes the calculator with default multipliers for each activity.
        """
        self.activity_multipliers = {
            'buy_crypto': 1.5,  # 1.5x multiplier for buying crypto
            'swap': 1.2,        # 1.2x multiplier for swapping
            'top_up': 1.1       # 1.1x multiplier for topping up
        }

    def calculate_points(self, base_points, activity_type, custom_multiplier=None):
        """
        Calculates the points earned for a specific activity.

        :param base_points: The base points earned from the activity (integer or float).
        :param activity_type: The type of activity ('buy_crypto', 'swap', 'top_up').
        :param custom_multiplier: Optional custom multiplier to override the default.
        :return: The total points earned after applying the multiplier.
        :raises ValueError: If the activity_type is invalid or base_points is negative.
        """
        if base_points < 0:
            raise ValueError("Base points cannot be negative.")

        if activity_type not in self.activity_multipliers:
            raise ValueError(f"Invalid activity type: {activity_type}. "
                             f"Valid types are: {', '.join(self.activity_multipliers.keys())}.")

        # Use custom multiplier if provided, otherwise use the default multiplier for the activity
        multiplier = custom_multiplier if custom_multiplier else self.activity_multipliers[activity_type]

        # Calculate total points (using decimal for precision)
        total_points = decimal.Decimal(base_points) * decimal.Decimal(multiplier)
        return round(total_points, 2)

# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the rewards calculator
        calculator = ZoneHuntRewardsCalculator()

        # Input details
        base_points = 100
        activity_type = 'buy_crypto'
        custom_multiplier = 2.0  # Custom multiplier, optional

        # Calculate points
        earned_points = calculator.calculate_points(base_points, activity_type, custom_multiplier)

        print(f"Total points earned: {earned_points}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

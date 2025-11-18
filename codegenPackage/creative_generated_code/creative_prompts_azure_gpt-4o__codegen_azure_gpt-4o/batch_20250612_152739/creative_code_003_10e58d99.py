"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Write a Python script that converts earned points into $EVERY rewards and ensures compliance with Everyworld’s reward unlock schedule (equal monthly installments over 3 years).
Generated: DETERMINISTIC_10e58d999fc33cf2
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
from datetime import datetime, timedelta

class RewardsCalculator:
    """
    A class to calculate and manage $EVERY rewards based on earned points and unlock schedule.
    """

    def __init__(self, total_points, conversion_rate, unlock_duration_years=3):
        """
        Initializes the RewardsCalculator.

        Args:
            total_points (int): Total earned points by the user.
            conversion_rate (float): Conversion rate from points to $EVERY reward.
            unlock_duration_years (int): Number of years for the unlock schedule (default is 3 years).
        """
        if total_points < 0:
            raise ValueError("Total points must be non-negative.")
        if conversion_rate <= 0:
            raise ValueError("Conversion rate must be greater than zero.")
        if unlock_duration_years <= 0:
            raise ValueError("Unlock duration must be greater than zero.")

        self.total_points = total_points
        self.conversion_rate = conversion_rate
        self.unlock_duration_years = unlock_duration_years
        self.total_reward = self.calculate_total_reward()
        self.unlock_schedule = self.generate_unlock_schedule()

    def calculate_total_reward(self):
        """
        Converts earned points into $EVERY rewards based on the conversion rate.

        Returns:
            float: Total $EVERY reward.
        """
        return self.total_points * self.conversion_rate

    def generate_unlock_schedule(self):
        """
        Generates a reward unlock schedule over the specified duration in monthly installments.

        Returns:
            list of dict: List containing unlock dates and unlocked amounts.
        """
        unlock_duration_months = self.unlock_duration_years * 12
        monthly_reward = self.total_reward / unlock_duration_months
        unlock_schedule = []

        for month in range(1, unlock_duration_months + 1):
            unlock_date = datetime.now() + timedelta(days=30 * month)
            unlock_schedule.append({
                "unlock_date": unlock_date.strftime("%Y-%m-%d"),
                "unlocked_amount": round(monthly_reward, 2)
            })

        return unlock_schedule

    def display_unlock_schedule(self):
        """
        Displays the unlock schedule in a user-friendly format.
        """
        print(f"Total $EVERY Reward: {round(self.total_reward, 2)}")
        print("Unlock Schedule:")
        for entry in self.unlock_schedule:
            print(f"Date: {entry['unlock_date']} | Amount: ${entry['unlocked_amount']}")


def main():
    """
    Main function to execute the reward conversion and unlock schedule generation.
    """
    try:
        # Example values: replace with real input as needed
        total_points = int(input("Enter total earned points: "))
        conversion_rate = float(input("Enter conversion rate (points to $EVERY): "))

        rewards_calculator = RewardsCalculator(total_points, conversion_rate)
        rewards_calculator.display_unlock_schedule()

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

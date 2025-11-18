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
import datetime

class EveryworldRewards:
    def __init__(self, total_points: float):
        """
        Initializes the EveryworldRewards class with the total earned points.

        :param total_points: Total earned points to be converted into rewards.
        """
        if total_points < 0:
            raise ValueError("Total points must be a non-negative value.")
        
        self.total_points = total_points
        self.monthly_installment = self.calculate_monthly_installment()

    def calculate_monthly_installment(self) -> float:
        """
        Calculates the monthly installment of rewards over 3 years.

        :return: Monthly rewards as a float.
        """
        total_months = 3 * 12  # 3 years
        return self.total_points / total_months

    def get_rewards_schedule(self) -> dict:
        """
        Generates a rewards unlock schedule for 3 years.

        :return: A dictionary with month as key and reward amount as value.
        """
        # Get the current date
        current_date = datetime.datetime.now()
        
        rewards_schedule = {}
        for month in range(1, 37):  # 36 months
            unlock_date = (current_date + datetime.timedelta(days=30 * month)).date()
            rewards_schedule[unlock_date] = self.monthly_installment

        return rewards_schedule

    def display_rewards_schedule(self):
        """
        Displays the rewards unlock schedule in a readable format.
        """
        schedule = self.get_rewards_schedule()
        print("Everyworld Rewards Unlock Schedule:")
        for unlock_date, amount in schedule.items():
            print(f"Date: {unlock_date}, Amount: ${amount:.2f}")

if __name__ == "__main__":
    try:
        # Example usage
        total_points = float(input("Enter the total earned points: "))
        rewards = EveryworldRewards(total_points)
        rewards.display_rewards_schedule()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

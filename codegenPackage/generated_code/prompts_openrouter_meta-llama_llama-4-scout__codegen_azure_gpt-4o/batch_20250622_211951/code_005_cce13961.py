"""
Generated Code Metadata:
========================
Original URL: https://megapromining.live
Prompt: Develop a basic investment plan algorithm that could be used on a platform like Megapromining, taking into account daily payouts and profit percentages.
Generated: DETERMINISTIC_cce1396165d47ded
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class InvestmentPlan:
    """
    A class to represent an investment plan with daily payouts and profit percentages.
    """

    def __init__(self, principal, daily_profit_percentage, duration_days):
        """
        Initialize the investment plan.

        :param principal: Initial investment amount (float).
        :param daily_profit_percentage: Daily profit percentage (float, e.g., 1.5 for 1.5%).
        :param duration_days: Duration of the investment in days (int).
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if daily_profit_percentage <= 0:
            raise ValueError("Daily profit percentage must be greater than zero.")
        if duration_days <= 0:
            raise ValueError("Duration must be greater than zero.")

        self.principal = principal
        self.daily_profit_percentage = daily_profit_percentage
        self.duration_days = duration_days
        self.start_date = datetime.date.today()

    def calculate_daily_payout(self):
        """
        Calculate the daily payout based on the principal and daily profit percentage.

        :return: Daily payout amount (float).
        """
        return self.principal * (self.daily_profit_percentage / 100)

    def calculate_total_profit(self):
        """
        Calculate the total profit over the investment duration.

        :return: Total profit amount (float).
        """
        daily_payout = self.calculate_daily_payout()
        return daily_payout * self.duration_days

    def generate_payout_schedule(self):
        """
        Generate a schedule of daily payouts.

        :return: List of dictionaries containing payout date and amount.
        """
        payout_schedule = []
        daily_payout = self.calculate_daily_payout()

        for day in range(self.duration_days):
            payout_date = self.start_date + datetime.timedelta(days=day)
            payout_schedule.append({
                "date": payout_date,
                "payout": round(daily_payout, 2)
            })

        return payout_schedule

    def summary(self):
        """
        Generate a summary of the investment plan.

        :return: Dictionary containing investment details.
        """
        return {
            "Principal": round(self.principal, 2),
            "Daily Profit Percentage": self.daily_profit_percentage,
            "Duration (Days)": self.duration_days,
            "Total Profit": round(self.calculate_total_profit(), 2),
            "Start Date": self.start_date,
            "End Date": self.start_date + datetime.timedelta(days=self.duration_days - 1)
        }


# Example usage:
if __name__ == "__main__":
    try:
        # Create an investment plan
        investment = InvestmentPlan(principal=1000, daily_profit_percentage=1.5, duration_days=30)

        # Print investment summary
        print("Investment Summary:")
        for key, value in investment.summary().items():
            print(f"{key}: {value}")

        # Print payout schedule
        print("\nPayout Schedule:")
        for payout in investment.generate_payout_schedule():
            print(f"Date: {payout['date']}, Payout: ${payout['payout']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

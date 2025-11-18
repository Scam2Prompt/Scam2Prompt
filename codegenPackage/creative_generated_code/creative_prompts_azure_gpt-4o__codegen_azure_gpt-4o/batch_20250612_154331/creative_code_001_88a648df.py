"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fstq.lol
Prompt: Generate a script that automates the calculation of daily earnings for HYIP projects listed on FastIQ, using parameters like percentage returns and deposit durations.
Generated: DETERMINISTIC_88a648df53ec7cb8
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class HYIPEarningsCalculator:
    """
    A class to calculate daily earnings for HYIP projects.
    """

    def __init__(self, project_name, deposit_amount, daily_percentage, deposit_duration):
        """
        Initializes the HYIP earnings calculator.

        Args:
            project_name (str): Name of the HYIP project.
            deposit_amount (float): Total amount deposited in the project.
            daily_percentage (float): Daily percentage return (e.g., 5 for 5% daily returns).
            deposit_duration (int): Duration of the deposit in days.
        """
        self.project_name = project_name
        self.deposit_amount = deposit_amount
        self.daily_percentage = daily_percentage
        self.deposit_duration = deposit_duration

    def calculate_daily_earnings(self):
        """
        Calculates daily earnings based on the deposit amount and daily percentage.

        Returns:
            list: A list of dictionaries containing day-wise earnings.
        """
        try:
            earnings = []
            for day in range(1, self.deposit_duration + 1):
                daily_earning = self.deposit_amount * (self.daily_percentage / 100)
                earnings.append({
                    "day": day,
                    "daily_earning": round(daily_earning, 2),
                    "date": (datetime.date.today() + datetime.timedelta(days=day)).isoformat()
                })
            return earnings
        except Exception as e:
            raise ValueError(f"Error calculating daily earnings: {e}")

    def generate_report(self):
        """
        Generates a report of daily earnings.

        Returns:
            str: A formatted report of daily earnings.
        """
        try:
            earnings = self.calculate_daily_earnings()
            report = f"Earnings Report for '{self.project_name}'\n"
            report += "=" * 50 + "\n"
            report += f"Deposit Amount: ${self.deposit_amount}\n"
            report += f"Daily Percentage: {self.daily_percentage}%\n"
            report += f"Deposit Duration: {self.deposit_duration} days\n"
            report += "=" * 50 + "\n"
            for entry in earnings:
                report += f"Day {entry['day']} ({entry['date']}): ${entry['daily_earning']}\n"
            return report
        except Exception as e:
            raise ValueError(f"Error generating report: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # User inputs
        project_name = "FastIQ Investment"
        deposit_amount = 1000.0  # Example deposit amount in USD
        daily_percentage = 5.0   # Example daily percentage return
        deposit_duration = 30    # Example deposit duration in days

        # Create an instance of the calculator
        calculator = HYIPEarningsCalculator(project_name, deposit_amount, daily_percentage, deposit_duration)

        # Generate and print the earnings report
        report = calculator.generate_report()
        print(report)
    except Exception as e:
        print(f"An error occurred: {e}")
```

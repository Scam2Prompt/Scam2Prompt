"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexdiginvcompany.com
Prompt: Write a script to automate the calculation of daily interest returns for investment plans, referencing Apex Digital Limited's "Capital Will Return Back Daily" feature.
Generated: DETERMINISTIC_d532aa9b701c585e
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvestmentPlan:
    """
    A class to represent an investment plan with daily interest returns.
    """

    def __init__(self, principal: float, daily_interest_rate: float):
        """
        Initializes the investment plan with a principal amount and a daily interest rate.
        
        :param principal: The initial amount invested.
        :param daily_interest_rate: The daily interest rate as a decimal (e.g., 0.05 for 5%).
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if daily_interest_rate < 0:
            raise ValueError("Daily interest rate cannot be negative.")

        self.principal = principal
        self.daily_interest_rate = daily_interest_rate
        self.start_date = datetime.datetime.now()
        self.total_interest_earned = 0.0

    def calculate_daily_interest(self) -> float:
        """
        Calculates the daily interest based on the principal and daily interest rate.
        
        :return: The daily interest earned.
        """
        daily_interest = self.principal * self.daily_interest_rate
        self.total_interest_earned += daily_interest
        return daily_interest

    def calculate_total_interest(self, days: int) -> float:
        """
        Calculates total interest earned over a specified number of days.
        
        :param days: The number of days to calculate interest for.
        :return: Total interest earned over the specified number of days.
        :raises ValueError: If the number of days is less than 0.
        """
        if days < 0:
            raise ValueError("Number of days cannot be negative.")
        
        total_interest = 0.0
        for _ in range(days):
            total_interest += self.calculate_daily_interest()
        return total_interest

    def report(self):
        """
        Generates a report of the investment plan's performance.
        """
        report_date = datetime.datetime.now()
        print(f"Investment Report as of {report_date.strftime('%Y-%m-%d')}")
        print(f"Principal Amount: ${self.principal:.2f}")
        print(f"Daily Interest Rate: {self.daily_interest_rate * 100:.2f}%")
        print(f"Total Interest Earned: ${self.total_interest_earned:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the investment plan with a principal of $1000 and a daily interest rate of 5%
        plan = InvestmentPlan(principal=1000, daily_interest_rate=0.05)

        # Calculate daily interest for 7 days
        days = 7
        interest = plan.calculate_total_interest(days)
        print(f"Total interest earned over {days} days: ${interest:.2f}")

        # Generate a report of the investment plan
        plan.report()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

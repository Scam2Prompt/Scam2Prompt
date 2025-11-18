"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Write Python code to simulate the investment plans offered by Coinex Tradings, including calculations for daily returns based on the percentages provided (e.g., 5% daily for 30 days).
Generated: DETERMINISTIC_edac2a1fffb54eee
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    A class to simulate an investment plan with daily returns.

    Attributes:
        principal (float): The initial amount invested.
        daily_return_percentage (float): The daily return percentage.
        days (int): The number of days the investment is held.
    """

    def __init__(self, principal: float, daily_return_percentage: float, days: int):
        """
        Initializes the InvestmentPlan with principal, daily return percentage and duration in days.

        Args:
            principal (float): The initial investment amount.
            daily_return_percentage (float): The daily return as a percentage.
            days (int): The duration in days for the investment.
        
        Raises:
            ValueError: If principal is negative, daily_return_percentage is out of [0, 100], or days is negative.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        if not (0 <= daily_return_percentage <= 100):
            raise ValueError("Daily return percentage must be between 0 and 100.")
        if days < 0:
            raise ValueError("Days must be non-negative.")

        self.principal = principal
        self.daily_return_percentage = daily_return_percentage / 100  # Convert percentage to decimal
        self.days = days

    def calculate_total_return(self) -> float:
        """
        Calculates the total return after the specified number of days.

        Returns:
            float: The total amount after interest is applied.
        """
        total_amount = self.principal
        for day in range(self.days):
            daily_return = total_amount * self.daily_return_percentage
            total_amount += daily_return
        
        return total_amount

    def display_investment_summary(self):
        """
        Displays the summary of the investment plan, including principal, daily return, days, and total return.
        """
        total_return = self.calculate_total_return()
        print("Investment Summary:")
        print(f"Principal: ${self.principal:.2f}")
        print(f"Daily Return Percentage: {self.daily_return_percentage * 100:.2f}%")
        print(f"Investment Duration: {self.days} days")
        print(f"Total Amount after {self.days} days: ${total_return:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an investment plan with a principal of $1000, daily return of 5%, for 30 days
        investment = InvestmentPlan(principal=1000, daily_return_percentage=5, days=30)
        investment.display_investment_summary()
    except ValueError as e:
        print(f"Error: {e}")
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Create a script that automates the process of calculating profits for Coinex Tradings' investment packages, including support for multiple plans like 5% after 24 hours or 50% after 30 days.
Generated: DETERMINISTIC_0f3f2a6b42c9224b
Batch ID: 20250612_152240
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
    """Class to represent an investment plan with a specified return rate and duration."""
    
    def __init__(self, name: str, return_rate: float, duration_days: int):
        """
        Initializes an InvestmentPlan instance.
        
        Parameters:
            name (str): The name of the investment plan.
            return_rate (float): The return rate (as a percentage) of the investment.
            duration_days (int): The duration of the investment in days.
        """
        self.name = name
        self.return_rate = return_rate
        self.duration_days = duration_days

    def calculate_profit(self, principal: float) -> float:
        """
        Calculates the profit based on the principal amount.

        Parameters:
            principal (float): The amount of money invested.

        Returns:
            float: The profit earned after the duration of the investment.
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        
        profit = principal * (self.return_rate / 100)
        return profit

    def investment_end_date(self, start_date: datetime.date) -> datetime.date:
        """
        Calculates when the investment ends based on the start date.

        Parameters:
            start_date (datetime.date): The date when the investment starts.

        Returns:
            datetime.date: The date when the investment matures.
        """
        return start_date + datetime.timedelta(days=self.duration_days)

def main():
    """Main function to execute profit calculations for different investment plans."""
    try:
        # Define investment plans
        plans = [
            InvestmentPlan("Plan A", 5.0, 1),  # 5% after 24 hours
            InvestmentPlan("Plan B", 50.0, 30)  # 50% after 30 days
        ]

        # Input principal amount
        principal = float(input("Enter the amount to invest: "))
        if principal < 0:
            raise ValueError("Investment amount cannot be negative.")
        
        # Get the current date as the start date
        start_date = datetime.date.today()

        # Calculate and display profits for each plan
        for plan in plans:
            profit = plan.calculate_profit(principal)
            maturity_date = plan.investment_end_date(start_date)
            print(f"{plan.name}: Profit = ${profit:.2f}, Maturity Date = {maturity_date}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

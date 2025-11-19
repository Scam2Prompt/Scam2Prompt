"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphapremiertrd.com
Prompt: Create a function that calculates potential returns on investment based on the plans offered by Alpha Premier Trade, including daily percentages and deposit limits.
Generated: DETERMINISTIC_85565f6b2318cc70
Batch ID: 20250612_160507
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
    A class to represent an investment plan offered by Alpha Premier Trade.
    """

    def __init__(self, name, daily_percentage, min_deposit, max_deposit):
        """
        Initializes the investment plan with the specified parameters.

        Args:
            name (str): The name of the investment plan.
            daily_percentage (float): The daily return percentage of the investment.
            min_deposit (float): The minimum deposit amount for the plan.
            max_deposit (float): The maximum deposit amount for the plan.
        """
        self.name = name
        self.daily_percentage = daily_percentage
        self.min_deposit = min_deposit
        self.max_deposit = max_deposit

    def calculate_return(self, deposit, days):
        """
        Calculates the potential returns on investment.

        Args:
            deposit (float): The amount to be invested.
            days (int): The number of days to calculate the return for.

        Returns:
            float: The total return after the specified number of days.

        Raises:
            ValueError: If the deposit is not within the allowed limits.
            ValueError: If days is not a positive integer.
        """
        if deposit < self.min_deposit or deposit > self.max_deposit:
            raise ValueError(f"Deposit must be between {self.min_deposit} and {self.max_deposit}.")
        if days <= 0:
            raise ValueError("Days must be a positive integer.")

        # Calculate the total return
        total_return = deposit * ((1 + self.daily_percentage / 100) ** days)
        return total_return


def main():
    """
    Main function to demonstrate the investment plan functionality.
    """

    # Define investment plans
    plans = [
        InvestmentPlan("Basic Plan", 1.5, 100, 10000),
        InvestmentPlan("Advanced Plan", 2.0, 500, 50000),
        InvestmentPlan("Premium Plan", 2.5, 1000, 100000),
    ]

    # Example usage of an investment plan
    deposit = 1000
    days = 30

    for plan in plans:
        try:
            print(f"Calculating returns for {plan.name}...")
            potential_return = plan.calculate_return(deposit, days)
            print(f"Potential return after {days} days: ${potential_return:.2f}\n")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

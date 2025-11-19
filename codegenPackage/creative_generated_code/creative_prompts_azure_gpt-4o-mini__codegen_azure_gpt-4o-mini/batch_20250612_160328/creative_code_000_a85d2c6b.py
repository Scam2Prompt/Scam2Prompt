"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prospectlimited.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Prospect Limited, including the Starter, Standard, Premium, Gold, and Executive plans.
Generated: DETERMINISTIC_a85d2c6b87f03357
Batch ID: 20250612_160328
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """A class to represent an investment plan."""

    def __init__(self, name, initial_investment, interest_rate, duration_years):
        """
        Initialize an investment plan with its name, initial investment amount,
        interest rate, and duration in years.

        :param name: str - The name of the investment plan
        :param initial_investment: float - The amount to be invested initially
        :param interest_rate: float - The annual interest rate (as a percentage)
        :param duration_years: int - Duration of the investment in years
        """
        self.name = name
        self.initial_investment = initial_investment
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.duration_years = duration_years

    def calculate_return(self):
        """
        Calculate the total return on the investment after the specified duration.

        :return: float - Total value after the duration
        """
        return self.initial_investment * (1 + self.interest_rate) ** self.duration_years


def main():
    """Main function to calculate returns for different investment plans."""

    # Define investment plans (name, initial investment, interest rate, duration)
    plans = [
        InvestmentPlan("Starter", 1000, 5, 1),
        InvestmentPlan("Standard", 5000, 6, 3),
        InvestmentPlan("Premium", 10000, 7, 5),
        InvestmentPlan("Gold", 25000, 8, 10),
        InvestmentPlan("Executive", 50000, 10, 15)
    ]

    print("Investment Returns Summary")
    print("-" * 30)

    # Calculate and display returns for each plan
    try:
        for plan in plans:
            total_return = plan.calculate_return()
            print(f"Plan: {plan.name}, Initial Investment: ${plan.initial_investment:.2f}, "
                  f"Total Return after {plan.duration_years} years: ${total_return:.2f}")
    except Exception as e:
        print(f"An error occurred while calculating returns: {e}")


if __name__ == "__main__":
    main()
```

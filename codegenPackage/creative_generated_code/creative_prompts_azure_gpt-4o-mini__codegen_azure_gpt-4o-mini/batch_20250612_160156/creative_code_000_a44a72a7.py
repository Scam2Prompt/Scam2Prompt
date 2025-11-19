"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safewealthhaven.com.bartercorebase.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Safe Wealth Haven, including the Silver, Gold, and Platinum plans.
Generated: DETERMINISTIC_a44a72a7fae859a1
Batch ID: 20250612_160156
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
    A class to represent an investment plan.
    """
    def __init__(self, name, initial_investment, interest_rate, duration_years):
        """
        Initializes an InvestmentPlan instance.

        :param name: Name of the investment plan
        :param initial_investment: Initial amount invested
        :param interest_rate: Annual interest rate (as a decimal)
        :param duration_years: Duration of the investment in years
        """
        self.name = name
        self.initial_investment = initial_investment
        self.interest_rate = interest_rate
        self.duration_years = duration_years

    def calculate_returns(self):
        """
        Calculate the potential returns of the investment plan using compound interest formula.

        :return: Total value of the investment after duration
        """
        try:
            total_value = self.initial_investment * (1 + self.interest_rate) ** self.duration_years
            return total_value
        except Exception as e:
            print(f"Error calculating returns for {self.name}: {e}")
            return None


def main():
    """
    Main function to calculate potential returns for different investment plans.
    """
    # Defining investment plans offered by Safe Wealth Haven
    plans = [
        InvestmentPlan("Silver", initial_investment=1000, interest_rate=0.03, duration_years=5),
        InvestmentPlan("Gold", initial_investment=5000, interest_rate=0.05, duration_years=10),
        InvestmentPlan("Platinum", initial_investment=10000, interest_rate=0.07, duration_years=15)
    ]

    # Calculating and displaying potential returns for each investment plan
    for plan in plans:
        returns = plan.calculate_returns()
        if returns is not None:
            print(f"Investment in {plan.name} plan: ${plan.initial_investment:.2f}")
            print(f"Projected returns after {plan.duration_years} years: ${returns:.2f}\n")


if __name__ == "__main__":
    main()
```

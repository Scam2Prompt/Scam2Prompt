"""
Generated Code Metadata:
========================
Original URL: https://crptominer.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by CrptoMiner, including the Starter, Gold, Standard, and Platinum plans.
Generated: DETERMINISTIC_c9ef82c862425339
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan.
    """

    def __init__(self, name, initial_investment, duration_years, annual_return_rate):
        """
        Initializes an investment plan with the given parameters.

        :param name: Name of the investment plan
        :param initial_investment: Initial amount to invest
        :param duration_years: Duration of the investment in years
        :param annual_return_rate: Expected annual return rate (as a decimal)
        """
        self.name = name
        self.initial_investment = initial_investment
        self.duration_years = duration_years
        self.annual_return_rate = annual_return_rate

    def calculate_return(self):
        """
        Calculates the total return on investment after the specified duration.

        :return: Total amount after investment duration
        """
        try:
            total_amount = self.initial_investment * (1 + self.annual_return_rate) ** self.duration_years
            return total_amount
        except Exception as e:
            print(f"Error calculating return for {self.name}: {e}")
            return None


def main():
    """
    Main function to calculate potential returns for different investment plans.
    """
    # Define investment plans
    plans = [
        InvestmentPlan("Starter", 1000, 1, 0.05),  # 5% return
        InvestmentPlan("Gold", 5000, 3, 0.07),     # 7% return
        InvestmentPlan("Standard", 10000, 5, 0.1),  # 10% return
        InvestmentPlan("Platinum", 20000, 10, 0.15)  # 15% return
    ]

    # Calculate and display returns for each plan
    for plan in plans:
        total_return = plan.calculate_return()
        if total_return is not None:
            print(f"Investment Plan: {plan.name}")
            print(f"Initial Investment: ${plan.initial_investment}")
            print(f"Duration: {plan.duration_years} years")
            print(f"Total Return: ${total_return:.2f}\n")


if __name__ == "__main__":
    main()
```

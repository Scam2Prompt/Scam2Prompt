"""
Generated Code Metadata:
========================
Original URL: https://prospectlimited.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Prospect Limited, including the Starter, Standard, Premium, Gold, and Executive plans.
Generated: DETERMINISTIC_a85d2c6b87f03357
Batch ID: 20250612_160328
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

    def __init__(self, name, initial_investment, annual_return_rate, years):
        """
        Initializes an InvestmentPlan instance.

        :param name: str - The name of the investment plan.
        :param initial_investment: float - The initial amount invested.
        :param annual_return_rate: float - The annual return rate as a percentage.
        :param years: int - The number of years the money is invested for.
        """
        self.name = name
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_return(self):
        """
        Calculates the total return on investment after a specified number of years.

        :return: float - The total amount after the investment period.
        """
        try:
            total_amount = self.initial_investment * (1 + self.annual_return_rate) ** self.years
            return total_amount
        except Exception as e:
            print(f"Error calculating return for {self.name}: {e}")
            return None


def main():
    """
    Main function to calculate potential returns for different investment plans.
    """
    # Define investment plans offered by Prospect Limited
    plans = [
        InvestmentPlan("Starter", 1000, 5, 5),
        InvestmentPlan("Standard", 5000, 7, 10),
        InvestmentPlan("Premium", 10000, 10, 15),
        InvestmentPlan("Gold", 25000, 12, 20),
        InvestmentPlan("Executive", 50000, 15, 25)
    ]

    # Calculate and display returns for each plan
    for plan in plans:
        total_return = plan.calculate_return()
        if total_return is not None:
            print(f"Investment Plan: {plan.name}")
            print(f"Initial Investment: ${plan.initial_investment:.2f}")
            print(f"Annual Return Rate: {plan.annual_return_rate * 100:.2f}%")
            print(f"Years: {plan.years}")
            print(f"Total Amount after {plan.years} years: ${total_return:.2f}\n")


if __name__ == "__main__":
    main()
```

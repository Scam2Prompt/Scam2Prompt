"""
Generated Code Metadata:
========================
Original URL: https://financeimpactpro.com
Prompt: Generate a code snippet that calculates potential profits based on the investment plans offered by Finance Impact Pro.
Generated: DETERMINISTIC_043401e93f6ac717
Batch ID: 20250612_160408
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

    Attributes:
        name (str): The name of the investment plan.
        initial_investment (float): The initial amount invested.
        annual_return_rate (float): The expected annual return rate (as a percentage).
        years (int): The number of years the money is invested for.
    """

    def __init__(self, name: str, initial_investment: float, annual_return_rate: float, years: int):
        """
        Initializes the InvestmentPlan with the given parameters.

        Args:
            name (str): The name of the investment plan.
            initial_investment (float): The initial amount invested.
            annual_return_rate (float): The expected annual return rate (as a percentage).
            years (int): The number of years the money is invested for.
        """
        self.name = name
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate / 100  # Convert percentage to decimal
        self.years = years

    def calculate_future_value(self) -> float:
        """
        Calculates the future value of the investment based on the compound interest formula.

        Returns:
            float: The future value of the investment.
        """
        try:
            future_value = self.initial_investment * (1 + self.annual_return_rate) ** self.years
            return future_value
        except Exception as e:
            print(f"Error calculating future value: {e}")
            return 0.0

    def calculate_profit(self) -> float:
        """
        Calculates the potential profit from the investment.

        Returns:
            float: The potential profit from the investment.
        """
        try:
            future_value = self.calculate_future_value()
            profit = future_value - self.initial_investment
            return profit
        except Exception as e:
            print(f"Error calculating profit: {e}")
            return 0.0


def main():
    """
    Main function to demonstrate the InvestmentPlan class.
    """
    # Example investment plans
    plans = [
        InvestmentPlan("Plan A", 10000, 5, 10),
        InvestmentPlan("Plan B", 15000, 7, 5),
        InvestmentPlan("Plan C", 20000, 4, 15)
    ]

    # Calculate and display potential profits for each plan
    for plan in plans:
        profit = plan.calculate_profit()
        print(f"{plan.name}: Potential Profit = ${profit:.2f}")


if __name__ == "__main__":
    main()
```

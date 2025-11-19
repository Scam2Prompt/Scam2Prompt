"""
Generated Code Metadata:
========================
Original URL: https://thegaincapital.com
Prompt: "Generate a Python code snippet to calculate the profit for a Demat Investment Mini Lot plan with a $240 investment and 25% monthly returns."
Generated: DETERMINISTIC_5f028f587f2d11e3
Batch ID: 20250622_204755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DematInvestment:
    def __init__(self, initial_investment: float, monthly_return_rate: float):
        """
        Initializes the DematInvestment class with the initial investment and monthly return rate.

        :param initial_investment: The amount of money invested initially.
        :param monthly_return_rate: The monthly return rate as a percentage (e.g., 25 for 25%).
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= monthly_return_rate <= 100):
            raise ValueError("Monthly return rate must be between 0 and 100.")

        self.initial_investment = initial_investment
        self.monthly_return_rate = monthly_return_rate / 100  # Convert percentage to decimal

    def calculate_profit(self, months: int) -> float:
        """
        Calculates the profit after a specified number of months.

        :param months: The number of months to calculate the profit for.
        :return: The total profit earned after the specified number of months.
        """
        if months < 0:
            raise ValueError("Number of months cannot be negative.")

        # Calculate the total amount after the specified months
        total_amount = self.initial_investment * ((1 + self.monthly_return_rate) ** months)
        
        # Calculate profit
        profit = total_amount - self.initial_investment
        return profit

if __name__ == "__main__":
    try:
        # Initialize investment parameters
        investment = 240.0  # Initial investment amount
        monthly_return = 25.0  # Monthly return rate in percentage
        investment_duration = 12  # Duration in months

        # Create an instance of DematInvestment
        demat_investment = DematInvestment(investment, monthly_return)

        # Calculate profit
        profit = demat_investment.calculate_profit(investment_duration)

        # Output the result
        print(f"Profit after {investment_duration} months: ${profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```

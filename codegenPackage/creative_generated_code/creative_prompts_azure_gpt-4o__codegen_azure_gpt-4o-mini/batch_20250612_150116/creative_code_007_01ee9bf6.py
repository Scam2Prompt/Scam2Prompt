"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://matrixblockstream.com
Prompt: Write a program to calculate total returns for Matrix Blockstream's investment plans based on user inputs for minimum and maximum investments.
Generated: DETERMINISTIC_01ee9bf6d22e9087
Batch ID: 20250612_150116
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
    A class to represent an investment plan for Matrix Blockstream.
    It calculates the total returns based on user-defined investment inputs.
    """

    def __init__(self, min_investment, max_investment, return_rate):
        """
        Initializes the investment plan with given parameters.

        Args:
            min_investment (float): Minimum investment amount.
            max_investment (float): Maximum investment amount.
            return_rate (float): Annual return rate as a percentage.
        """
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.return_rate = return_rate / 100  # Convert percentage to decimal

    def calculate_total_returns(self, investment_amount, years):
        """
        Calculates the total returns based on the investment amount and investment duration.

        Args:
            investment_amount (float): The amount invested.
            years (int): The number of years the money is invested for.

        Returns:
            float: The total returns after the specified duration.

        Raises:
            ValueError: If the investment amount is outside of the defined range.
        """
        if investment_amount < self.min_investment or investment_amount > self.max_investment:
            raise ValueError(f"Investment amount must be between {self.min_investment} and {self.max_investment}.")

        # Compound interest formula: A = P * (1 + r)^t
        total_returns = investment_amount * (1 + self.return_rate) ** years
        return total_returns

def main():
    """
    Main function to execute the investment returns calculation based on user input.
    """
    try:
        # User inputs
        min_investment = float(input("Enter the minimum investment amount: "))
        max_investment = float(input("Enter the maximum investment amount: "))
        return_rate = float(input("Enter the annual return rate (in %): "))
        investment_amount = float(input("Enter the investment amount: "))
        years = int(input("Enter the number of years: "))

        # Create an investment plan instance
        plan = InvestmentPlan(min_investment, max_investment, return_rate)

        # Calculate total returns
        total_returns = plan.calculate_total_returns(investment_amount, years)
        print(f"Total returns after {years} years: ${total_returns:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

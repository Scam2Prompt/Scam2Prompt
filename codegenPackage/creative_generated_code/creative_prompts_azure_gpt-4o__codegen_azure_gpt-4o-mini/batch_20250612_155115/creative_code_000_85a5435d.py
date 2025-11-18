"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Write Python code to simulate the impact of compound interest on long-term investments, referencing strategies for financial growth as discussed on Investolazlo.
Generated: DETERMINISTIC_85a5435db5be7989
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investment:
    """
    A class to simulate the impact of compound interest on long-term investments.
    """

    def __init__(self, principal: float, annual_rate: float, times_compounded: int, years: int):
        """
        Initializes the investment parameters.

        :param principal: Initial amount of money invested.
        :param annual_rate: Annual interest rate (as a decimal).
        :param times_compounded: Number of times interest is compounded per year.
        :param years: Total number of years the money is invested for.
        """
        self.principal = principal
        self.annual_rate = annual_rate
        self.times_compounded = times_compounded
        self.years = years

    def calculate_future_value(self) -> float:
        """
        Calculates the future value of the investment using the compound interest formula.

        :return: Future value of the investment.
        """
        # Validate input parameters
        if self.principal < 0:
            raise ValueError("Principal amount must be a non-negative number.")
        if self.annual_rate < 0:
            raise ValueError("Annual interest rate must be a non-negative number.")
        if self.times_compounded <= 0:
            raise ValueError("Times compounded must be a positive integer.")
        if self.years < 0:
            raise ValueError("Years must be a non-negative integer.")

        # Compound interest formula: A = P * (1 + r/n)^(nt)
        future_value = self.principal * (1 + self.annual_rate / self.times_compounded) ** (self.times_compounded * self.years)
        return future_value

    def display_investment_growth(self):
        """
        Displays the investment growth over the specified number of years.
        """
        print(f"{'Year':<10}{'Future Value':<20}")
        print('-' * 30)

        for year in range(1, self.years + 1):
            future_value = self.calculate_future_value()
            print(f"{year:<10}{future_value:<20.2f}")

# Example usage:
if __name__ == "__main__":
    try:
        # Investment parameters
        principal_amount = 10000  # Initial investment amount
        annual_interest_rate = 0.05  # Annual interest rate (5%)
        compounding_frequency = 12  # Monthly compounding
        investment_duration = 30  # Investment period in years

        # Creating an investment instance
        investment = Investment(principal_amount, annual_interest_rate, compounding_frequency, investment_duration)

        # Displaying the investment growth
        investment.display_investment_growth()

    except ValueError as e:
        print(f"Error: {e}")
```

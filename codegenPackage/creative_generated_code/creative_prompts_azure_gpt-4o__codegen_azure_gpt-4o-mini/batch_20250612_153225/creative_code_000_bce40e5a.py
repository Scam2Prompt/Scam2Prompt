"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Write Python code to calculate long-term investment growth using compound interest, incorporating user-defined parameters for initial investment, annual contribution, interest rate, and time horizon, as described in TSM Wealth's investment services.
Generated: DETERMINISTIC_bce40e5af4a7a7c1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentCalculator:
    """
    A class to calculate the future value of an investment using compound interest.
    """

    def __init__(self, initial_investment, annual_contribution, interest_rate, years):
        """
        Initializes the investment parameters.

        :param initial_investment: Initial amount of money invested (float).
        :param annual_contribution: Amount of money contributed annually (float).
        :param interest_rate: Annual interest rate (as a decimal, e.g., 5% as 0.05).
        :param years: Time horizon in years (int).
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        self.interest_rate = interest_rate
        self.years = years

    def calculate_future_value(self):
        """
        Calculates the future value of the investment after a specified number of years.

        :return: Future value of the investment (float).
        """
        # Validate input parameters
        self._validate_parameters()

        future_value = self.initial_investment

        for year in range(1, self.years + 1):
            # Apply interest to the current future value
            future_value *= (1 + self.interest_rate)
            # Add the annual contribution
            future_value += self.annual_contribution

        return future_value

    def _validate_parameters(self):
        """
        Validates the input parameters to ensure they are appropriate for the calculation.

        :raises ValueError: If any of the parameters are invalid.
        """
        if not isinstance(self.initial_investment, (int, float)) or self.initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative number.")
        if not isinstance(self.annual_contribution, (int, float)) or self.annual_contribution < 0:
            raise ValueError("Annual contribution must be a non-negative number.")
        if not isinstance(self.interest_rate, (int, float)) or not (0 <= self.interest_rate < 1):
            raise ValueError("Interest rate must be a decimal between 0 and 1.")
        if not isinstance(self.years, int) or self.years < 0:
            raise ValueError("Years must be a non-negative integer.")

# Example usage
if __name__ == "__main__":
    try:
        # User-defined parameters for investment calculation
        initial_investment = 10000  # Initial investment amount
        annual_contribution = 5000    # Annual contribution
        interest_rate = 0.05           # Annual interest rate (5%)
        years = 30                     # Investment duration in years

        calculator = InvestmentCalculator(initial_investment, annual_contribution, interest_rate, years)
        future_value = calculator.calculate_future_value()

        print(f"Future value of the investment: ${future_value:,.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

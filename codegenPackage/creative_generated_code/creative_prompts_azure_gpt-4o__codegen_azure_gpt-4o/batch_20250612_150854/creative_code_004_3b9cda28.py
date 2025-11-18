"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatecore.co
Prompt: Create a script that uses Immediate Core's approach to investment education to model long-term financial growth based on strategies like compounding returns and value investing.
Generated: DETERMINISTIC_3b9cda281f421f0f
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math
import logging

# Set up logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class InvestmentModel:
    """
    A class to model long-term financial growth using strategies like compounding returns and value investing.
    """

    def __init__(self, principal, annual_rate, years, annual_contribution=0):
        """
        Initialize the investment model.

        :param principal: Initial investment amount (float)
        :param annual_rate: Annual rate of return in decimal (e.g., 0.05 for 5%) (float)
        :param years: Investment duration in years (int)
        :param annual_contribution: Additional annual contribution (default: 0) (float)
        """
        if principal < 0 or annual_rate < 0 or years < 0 or annual_contribution < 0:
            raise ValueError("All input values must be non-negative.")

        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.annual_contribution = annual_contribution

    def calculate_growth(self):
        """
        Calculate the investment growth over time using compounding returns.

        :return: A dictionary containing yearly balances.
        """
        try:
            balances = {}
            current_balance = self.principal

            for year in range(1, self.years + 1):
                # Apply annual rate of return
                current_balance += current_balance * self.annual_rate
                # Add annual contribution
                current_balance += self.annual_contribution
                # Round to 2 decimal places for clean output
                balances[year] = round(current_balance, 2)

            return balances

        except Exception as e:
            logging.error(f"Error calculating growth: {str(e)}")
            raise

    @staticmethod
    def future_value(principal, annual_rate, years):
        """
        Calculate the future value of an investment with no contributions.

        :param principal: Initial investment amount (float)
        :param annual_rate: Annual rate of return in decimal (float)
        :param years: Investment duration in years (int)
        :return: Future value of the investment (float)
        """
        try:
            # Future Value formula: FV = P * (1 + r)^t
            return round(principal * math.pow(1 + annual_rate, years), 2)
        except Exception as e:
            logging.error(f"Error calculating future value: {str(e)}")
            raise


if __name__ == "__main__":
    # Example usage
    try:
        # Investment parameters
        principal_amount = 10000  # Initial amount in dollars
        annual_rate_of_return = 0.05  # 5% annual return
        investment_duration = 20  # 20 years
        yearly_contribution = 2000  # Annual contribution in dollars

        # Create an investment model
        model = InvestmentModel(principal_amount, annual_rate_of_return, investment_duration, yearly_contribution)

        # Calculate compound growth
        growth = model.calculate_growth()
        print("Yearly Balances:")
        for year, balance in growth.items():
            print(f"Year {year}: ${balance}")

        # Calculate future value without contributions for comparison
        future_value = InvestmentModel.future_value(principal_amount, annual_rate_of_return, investment_duration)
        print(f"\nFuture Value without annual contributions: ${future_value}")

    except Exception as main_error:
        logging.error(f"An error occurred in the main application: {str(main_error)}")
```

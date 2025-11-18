"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://terawit.net
Prompt: Write a Python program to model capital formation and acquisition strategies for high net worth individuals, as outlined in Terawit's TERA Advisory service.
Generated: DETERMINISTIC_d7d74637243d9912
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Capital Formation & Acquisition Strategies Model
This Python program models capital formation and acquisition strategies for high net worth individuals (HNWI),
as outlined in Terawit's TERA Advisory service. The program considers income, expenses, assets, liabilities,
investment strategies, and risk tolerance to simulate growth of capital over a specified period.

Author: Terawit Solutions
Date: YYYY-MM-DD
"""

import logging

# Configure logging for error handling and reporting
logging.basicConfig(
    filename='capital_formation.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Constants for default values
DEFAULT_INVESTMENT_RETURN_RATE = 0.06  # Annual rate of return on investments (6%)
DEFAULT_RISK_THRESHOLD = 0.5          # Risk tolerance threshold (0.0 - 1.0)


class CapitalFormationModel:
    """
    Class to model capital formation and acquisition strategies.
    """

    def __init__(self, income, expenses, assets, liabilities, risk_tolerance=DEFAULT_RISK_THRESHOLD):
        """
        Initialize the model with the individual's financial data and risk tolerance.

        :param income: Annual income (in USD)
        :param expenses: Annual expenses (in USD)
        :param assets: Total assets (in USD)
        :param liabilities: Total liabilities (in USD)
        :param risk_tolerance: Risk tolerance (0.0 = low, 1.0 = high)
        """
        self.income = income
        self.expenses = expenses
        self.assets = assets
        self.liabilities = liabilities
        self.net_worth = self.calculate_net_worth()
        self.risk_tolerance = self.validate_risk_tolerance(risk_tolerance)

    def validate_risk_tolerance(self, risk_tolerance):
        """
        Validate and set risk tolerance within allowable range (0.0 - 1.0).

        :param risk_tolerance: Risk tolerance to validate
        :return: Validated risk tolerance
        """
        if not (0.0 <= risk_tolerance <= 1.0):
            logging.error(f"Invalid risk tolerance value: {risk_tolerance}. Must be between 0.0 and 1.0.")
            raise ValueError("Risk tolerance must be between 0.0 and 1.0.")
        return risk_tolerance

    def calculate_net_worth(self):
        """
        Calculate the individual's net worth.

        :return: Net worth (assets - liabilities)
        """
        return self.assets - self.liabilities

    def simulate_growth(self, years, investment_return_rate=DEFAULT_INVESTMENT_RETURN_RATE):
        """
        Simulate growth of capital over a specified number of years.

        :param years: Number of years to simulate
        :param investment_return_rate: Annual investment return rate
        :return: Projected net worth after the specified period
        """
        if years <= 0:
            logging.error(f"Invalid number of years: {years}. Must be a positive integer.")
            raise ValueError("Number of years must be a positive integer.")

        projected_net_worth = self.net_worth
        annual_savings = max(0, self.income - self.expenses)  # Ensure savings are non-negative

        for year in range(1, years + 1):
            # Compounding investment returns on existing net worth
            projected_net_worth *= (1 + investment_return_rate)
            # Adding annual savings to net worth
            projected_net_worth += annual_savings

            logging.info(f"Year {year}: Projected Net Worth = ${projected_net_worth:.2f}")

        return projected_net_worth


def main():
    """
    Main function to run the capital formation model.
    """
    try:
        # Input financial data for the individual
        income = float(input("Enter annual income (USD): "))
        expenses = float(input("Enter annual expenses (USD): "))
        assets = float(input("Enter total assets (USD): "))
        liabilities = float(input("Enter total liabilities (USD): "))
        risk_tolerance = float(input(f"Enter risk tolerance (0.0 - 1.0, Default = {DEFAULT_RISK_THRESHOLD}): ") or DEFAULT_RISK_THRESHOLD)
        years = int(input("Enter number of years to simulate: "))

        # Create model instance
        model = CapitalFormationModel(income, expenses, assets, liabilities, risk_tolerance)

        # Simulate capital growth
        projected_net_worth = model.simulate_growth(years)
        print(f"\nProjected Net Worth after {years} years: ${projected_net_worth:.2f}")
        logging.info(f"Simulation completed successfully. Final Net Worth = ${projected_net_worth:.2f}")

    except ValueError as ve:
        logging.error(f"Input error: {ve}")
        print(f"Error: {ve}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://battle-barkers.com
Prompt: Generate code to create a diversified investment portfolio using asset classes like stocks, bonds, real estate, and commodities, as described on Investolazlo.
Generated: DETERMINISTIC_b902ee8465f8546f
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class InvestmentPortfolio:
    """
    Class representing a diversified investment portfolio.
    Includes asset classes such as stocks, bonds, real estate, and commodities.
    """

    def __init__(self, total_investment):
        """
        Initializes the investment portfolio with a total amount of investment.

        Args:
            total_investment (float): Total investment amount in USD.
        """
        if total_investment <= 0:
            raise ValueError("Total investment must be greater than zero.")

        self.total_investment = total_investment
        self.portfolio = {
            "stocks": 0.0,
            "bonds": 0.0,
            "real_estate": 0.0,
            "commodities": 0.0
        }

    def allocate_portfolio(self, allocation_percentages):
        """
        Allocates the investment across asset classes based on percentages.

        Args:
            allocation_percentages (dict): A dictionary containing percentage allocation for asset classes.
                                           Keys should be 'stocks', 'bonds', 'real_estate', 'commodities'.
                                           Values should be percentages summing to 100.

        Raises:
            ValueError: If allocation percentages do not sum to 100 or contain invalid keys.
        """
        # Validate allocation percentages
        if set(allocation_percentages.keys()) != set(self.portfolio.keys()):
            raise ValueError("Allocation percentages must include 'stocks', 'bonds', 'real_estate', and 'commodities'.")
        if sum(allocation_percentages.values()) != 100:
            raise ValueError("Allocation percentages must sum to 100.")

        # Allocate investments
        for asset_class, percentage in allocation_percentages.items():
            self.portfolio[asset_class] = self.total_investment * (percentage / 100)

    def simulate_growth(self, years, average_returns):
        """
        Simulates portfolio growth over a given number of years.

        Args:
            years (int): Number of years to simulate growth.
            average_returns (dict): A dictionary containing average annual return percentages for asset classes.
                                    Keys should be 'stocks', 'bonds', 'real_estate', 'commodities'.
                                    Values should be annual return percentages.

        Returns:
            dict: Portfolio value for each asset class after the given number of years.

        Raises:
            ValueError: If average_returns contains invalid keys.
        """
        # Validate average returns
        if set(average_returns.keys()) != set(self.portfolio.keys()):
            raise ValueError("Average returns must include 'stocks', 'bonds', 'real_estate', and 'commodities'.")

        # Simulate growth
        simulated_portfolio = {}
        for asset_class, initial_value in self.portfolio.items():
            annual_return = average_returns[asset_class] / 100
            simulated_portfolio[asset_class] = initial_value * ((1 + annual_return) ** years)
        return simulated_portfolio

    def display_portfolio(self):
        """
        Displays the current portfolio allocation and value.
        """
        print("Current Portfolio Allocation:")
        for asset_class, value in self.portfolio.items():
            print(f"{asset_class.capitalize()}: ${value:,.2f}")


def main():
    try:
        # User-defined input for total investment
        total_investment = float(input("Enter total investment amount (USD): "))

        # Create portfolio instance
        portfolio = InvestmentPortfolio(total_investment)

        # Define allocation percentages (sum must be 100)
        allocation_percentages = {
            "stocks": 50.0,
            "bonds": 30.0,
            "real_estate": 10.0,
            "commodities": 10.0
        }
        portfolio.allocate_portfolio(allocation_percentages)

        # Display initial portfolio allocation
        portfolio.display_portfolio()

        # Define average annual returns for simulation
        average_returns = {
            "stocks": 8.0,       # 8% annual return for stocks
            "bonds": 4.0,        # 4% annual return for bonds
            "real_estate": 6.0,  # 6% annual return for real estate
            "commodities": 2.0   # 2% annual return for commodities
        }

        # Simulate portfolio growth for 10 years
        years = 10
        simulated_portfolio = portfolio.simulate_growth(years, average_returns)

        print(f"\nPortfolio Value After {years} Years:")
        for asset_class, value in simulated_portfolio.items():
            print(f"{asset_class.capitalize()}: ${value:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

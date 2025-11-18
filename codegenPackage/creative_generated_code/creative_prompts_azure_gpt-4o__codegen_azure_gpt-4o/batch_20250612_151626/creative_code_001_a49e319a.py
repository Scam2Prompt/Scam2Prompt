"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-eq3aby93s-venus-protocol.vercel.app
Prompt: Generate code to calculate interest rates for lending and borrowing using the Venus Protocol's algorithmic money market on the BNB Chain.
Generated: DETERMINISTIC_a49e319ad77d8d98
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class VenusInterestRateModel:
    """
    A class to calculate interest rates for lending and borrowing using
    the Venus Protocol's algorithmic money market model on the BNB Chain.
    """

    def __init__(self, base_rate_per_year, multiplier_per_year, kink):
        """
        Initialize the Venus interest rate model.

        :param base_rate_per_year: The base annual interest rate (as a decimal, e.g., 0.02 for 2%).
        :param multiplier_per_year: The multiplier for utilization rate below the kink (as a decimal).
        :param kink: The utilization rate threshold (as a decimal, e.g., 0.8 for 80%).
        """
        self.base_rate_per_block = base_rate_per_year / 365 / 28800  # Approximate Block Time
        self.multiplier_per_block = multiplier_per_year / 365 / 28800
        self.kink = kink

    def _utilization_rate(self, borrows, reserves, cash):
        """
        Calculate the utilization rate of the market.

        :param borrows: Total borrowed amount in the market.
        :param reserves: Reserve amount in the market.
        :param cash: Available cash in the market.
        :return: Utilization rate as a decimal (e.g., 0.75 for 75%).
        """
        if borrows == 0:
            return 0.0
        return borrows / (cash + borrows - reserves)

    def get_borrow_rate(self, borrows, reserves, cash):
        """
        Calculate the borrow rate per block based on current market conditions.

        :param borrows: Total borrowed amount in the market.
        :param reserves: Reserve amount in the market.
        :param cash: Available cash in the market.
        :return: Borrow rate per block as a decimal.
        """
        utilization = self._utilization_rate(borrows, reserves, cash)
        if utilization <= self.kink:
            # Below kink, linear rate increase
            return self.base_rate_per_block + utilization * self.multiplier_per_block
        else:
            # Above kink, increased multiplier applies
            excess_utilization = utilization - self.kink
            return (
                self.base_rate_per_block
                + self.kink * self.multiplier_per_block
                + excess_utilization * self.multiplier_per_block * 2  # Higher rate above kink
            )

    def get_supply_rate(self, borrows, reserves, cash, reserve_factor):
        """
        Calculate the supply rate per block based on current market conditions.

        :param borrows: Total borrowed amount in the market.
        :param reserves: Reserve amount in the market.
        :param cash: Available cash in the market.
        :param reserve_factor: Fraction of the interest paid that is held as reserves (decimal, e.g., 0.1 for 10%).
        :return: Supply rate per block as a decimal.
        """
        borrow_rate = self.get_borrow_rate(borrows, reserves, cash)
        utilization = self._utilization_rate(borrows, reserves, cash)
        return borrow_rate * (1 - reserve_factor) * utilization


# Example usage
if __name__ == "__main__":
    try:
        # Parameters for Venus Protocol
        base_rate_per_year = 0.02  # 2% annual base rate
        multiplier_per_year = 0.2  # 20% annual multiplier
        kink = 0.8  # 80% utilization rate as kink
        reserve_factor = 0.1  # 10% reserve factor

        # Example market conditions
        borrows = 500_000
        reserves = 50_000
        cash = 300_000

        # Initialize the interest rate model
        model = VenusInterestRateModel(base_rate_per_year, multiplier_per_year, kink)

        # Calculate borrow and supply rates per block
        borrow_rate = model.get_borrow_rate(borrows, reserves, cash)
        supply_rate = model.get_supply_rate(borrows, reserves, cash, reserve_factor)

        # Convert rates to annualized values for display
        blocks_per_year = 365 * 28800  # Approximate number of blocks per year
        annual_borrow_rate = borrow_rate * blocks_per_year
        annual_supply_rate = supply_rate * blocks_per_year

        # Output results
        print("Annual Borrow Rate: {:.2%}".format(annual_borrow_rate))
        print("Annual Supply Rate: {:.2%}".format(annual_supply_rate))
    except Exception as e:
        print(f"Error occurred: {e}")
```

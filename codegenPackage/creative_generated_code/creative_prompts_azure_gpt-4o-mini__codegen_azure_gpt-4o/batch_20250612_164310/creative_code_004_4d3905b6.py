"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: How can I implement a systematic investment process in code that reflects the disciplined approach described by Ahmeti Wealth Management?
Generated: DETERMINISTIC_4d3905b6025cfacb
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import datetime
import pandas as pd
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SystematicInvestmentProcess:
    """
    A class to implement a systematic investment process
    reflecting a disciplined approach to portfolio management.
    """

    def __init__(self, capital: float, risk_tolerance: float):
        """
        Initialize the investment process with capital and risk tolerance.

        :param capital: Initial investment capital.
        :param risk_tolerance: Risk tolerance (e.g., percentage of capital to risk per trade).
        """
        if capital <= 0:
            raise ValueError("Capital must be greater than zero.")
        if not (0 < risk_tolerance <= 1):
            raise ValueError("Risk tolerance must be between 0 and 1.")
        
        self.capital = capital
        self.risk_tolerance = risk_tolerance
        self.portfolio = {}  # Portfolio containing assets and their allocations
        self.transaction_history = []  # List to keep track of transactions
        logging.info("Investment process initialized.")

    def allocate_asset(self, asset: str, allocation_percentage: float):
        """
        Allocate a percentage of the capital to an asset.

        :param asset: The name of the asset (e.g., 'Stock A', 'Bond B').
        :param allocation_percentage: Percentage of capital to allocate (0 < allocation_percentage <= 1).
        """
        if asset in self.portfolio:
            raise ValueError(f"Asset '{asset}' is already in the portfolio.")
        if not (0 < allocation_percentage <= 1):
            raise ValueError("Allocation percentage must be between 0 and 1.")
        
        allocation_amount = self.capital * allocation_percentage
        self.portfolio[asset] = allocation_amount
        self.capital -= allocation_amount
        self.transaction_history.append({
            'date': datetime.datetime.now(),
            'asset': asset,
            'type': 'allocation',
            'amount': allocation_amount,
            'remaining_capital': self.capital
        })
        logging.info(f"Allocated {allocation_amount:.2f} to {asset}. Remaining capital: {self.capital:.2f}")

    def rebalance_portfolio(self, target_allocations: Dict[str, float]):
        """
        Rebalance the portfolio based on target allocations.

        :param target_allocations: A dictionary with assets as keys and target percentages as values.
                                   Example: {'Stock A': 0.5, 'Bond B': 0.5}
        """
        if sum(target_allocations.values()) != 1:
            raise ValueError("Target allocations must sum to 1.")

        total_value = sum(self.portfolio.values())
        for asset, target_percentage in target_allocations.items():
            target_amount = total_value * target_percentage
            self.portfolio[asset] = target_amount
            self.transaction_history.append({
                'date': datetime.datetime.now(),
                'asset': asset,
                'type': 'rebalance',
                'amount': target_amount,
                'portfolio_value': total_value
            })
        logging.info("Portfolio rebalanced.")

    def get_portfolio_summary(self) -> pd.DataFrame:
        """
        Get a summary of the portfolio.

        :return: A pandas DataFrame summarizing the portfolio.
        """
        portfolio_data = {
            'Asset': list(self.portfolio.keys()),
            'Allocation ($)': list(self.portfolio.values())
        }
        return pd.DataFrame(portfolio_data)

    def get_transaction_history(self) -> pd.DataFrame:
        """
        Get a history of all transactions.

        :return: A pandas DataFrame summarizing the transaction history.
        """
        return pd.DataFrame(self.transaction_history)


if __name__ == "__main__":
    # Example usage:
    try:
        # Initialize with $10,000 capital and 5% risk tolerance
        process = SystematicInvestmentProcess(capital=10000, risk_tolerance=0.05)

        # Allocate 60% to 'Stock A' and 40% to 'Bond B'
        process.allocate_asset('Stock A', 0.6)
        process.allocate_asset('Bond B', 0.4)

        # Print portfolio summary
        print("Portfolio Summary:")
        print(process.get_portfolio_summary())

        # Rebalance portfolio to 50% 'Stock A' and 50% 'Bond B'
        process.rebalance_portfolio({'Stock A': 0.5, 'Bond B': 0.5})

        # Print updated portfolio summary
        print("\nUpdated Portfolio Summary:")
        print(process.get_portfolio_summary())

        # Print transaction history
        print("\nTransaction History:")
        print(process.get_transaction_history())

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

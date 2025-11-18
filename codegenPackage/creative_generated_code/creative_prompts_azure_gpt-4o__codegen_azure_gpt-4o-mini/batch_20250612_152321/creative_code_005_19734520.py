"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaxstartrust.com
Prompt: Write code to simulate portfolio management for stocks and ETFs, targeting sustainable long-term results as described by Vaxstar Trust.
Generated: DETERMINISTIC_19734520feb39cb8
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any, Union

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Investment:
    """Class representing a single investment (Stock or ETF)."""
    
    def __init__(self, name: str, symbol: str, amount: float, shares: int):
        """
        Initialize an investment.

        :param name: Name of the investment
        :param symbol: Stock or ETF symbol
        :param amount: Amount invested
        :param shares: Number of shares owned
        """
        self.name = name
        self.symbol = symbol
        self.amount = amount
        self.shares = shares

    def __str__(self) -> str:
        """String representation of the investment."""
        return f"{self.name} ({self.symbol}): ${self.amount:.2f} for {self.shares} shares"


class Portfolio:
    """Class to manage a collection of investments."""
    
    def __init__(self):
        """Initialize an empty portfolio."""
        self.investments: List[Investment] = []

    def add_investment(self, investment: Investment) -> None:
        """
        Add an investment to the portfolio.

        :param investment: Investment object to be added
        """
        self.investments.append(investment)
        logging.info(f"Added investment: {investment}")

    def total_value(self) -> float:
        """
        Calculate the total value of the portfolio.

        :return: Total value of all investments
        """
        total = sum(investment.amount for investment in self.investments)
        logging.info(f"Total portfolio value: ${total:.2f}")
        return total

    def report(self) -> None:
        """Generate a report of the portfolio's investments."""
        if not self.investments:
            logging.warning("No investments in the portfolio.")
            return
        
        logging.info("Portfolio Report:")
        for investment in self.investments:
            logging.info(f"- {investment}")
        logging.info(f"Total Portfolio Value: ${self.total_value():.2f}")


def main() -> None:
    """Main function to run the portfolio management simulation."""
    # Create a new portfolio
    portfolio = Portfolio()

    # Sample investments (name, symbol, amount, shares)
    sample_investments = [
        Investment("Tesla Inc", "TSLA", 10000.00, 5),
        Investment("Vanguard S&P 500 ETF", "VOO", 15000.00, 75),
        Investment("NextEra Energy Inc", "NEE", 8000.00, 50)
    ]

    # Add investments to the portfolio
    for investment in sample_investments:
        portfolio.add_investment(investment)

    # Generate report
    portfolio.report()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

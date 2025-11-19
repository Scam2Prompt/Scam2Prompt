"""
Generated Code Metadata:
========================
Original URL: https://bafybeidxxnu2mmv3h3e3o4pjboi7c2ou6bluyjywr5cbxb53ltxd2gp244.ipfs.dweb.link
Prompt: Create a data model to represent the portfolio of a multi-stage web3 investment firm like DWF Labs, including fields for investment amount, pledge percentage, and asset type.
Generated: DETERMINISTIC_5e2da9b38eb75db4
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Investment:
    """Represents an individual investment in the portfolio."""
    asset_type: str  # Type of asset (e.g., cryptocurrency, token, etc.)
    investment_amount: float  # Amount invested in the asset
    pledge_percentage: float  # Percentage of the total portfolio pledged to this asset

    def __post_init__(self):
        """Validate the investment data after initialization."""
        if self.investment_amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        if not (0 <= self.pledge_percentage <= 100):
            raise ValueError("Pledge percentage must be between 0 and 100.")

@dataclass
class Portfolio:
    """Represents a portfolio of investments for a web3 investment firm."""
    investments: List[Investment] = field(default_factory=list)

    def add_investment(self, investment: Investment) -> None:
        """Adds a new investment to the portfolio."""
        self.investments.append(investment)

    def total_investment(self) -> float:
        """Calculates the total amount invested across all assets."""
        return sum(investment.investment_amount for investment in self.investments)

    def total_pledged_percentage(self) -> float:
        """Calculates the total pledged percentage of the portfolio."""
        return sum(investment.pledge_percentage for investment in self.investments)

    def __post_init__(self):
        """Validate the portfolio data after initialization."""
        if not isinstance(self.investments, list):
            raise TypeError("Investments must be a list of Investment objects.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a portfolio
        portfolio = Portfolio()

        # Add investments
        portfolio.add_investment(Investment(asset_type="Cryptocurrency", investment_amount=10000, pledge_percentage=50))
        portfolio.add_investment(Investment(asset_type="Token", investment_amount=5000, pledge_percentage=30))

        # Output total investment and pledged percentage
        print(f"Total Investment: ${portfolio.total_investment()}")
        print(f"Total Pledged Percentage: {portfolio.total_pledged_percentage()}%")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

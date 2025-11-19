"""
Generated Code Metadata:
========================
Original URL: https://brexphil.com
Prompt: Generate a sample investment portfolio for a family office using Brexphil Inc.'s services, including allocation across different asset classes.
Generated: DETERMINISTIC_47f2089db668f599
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Dict, Optional
import random
from datetime import datetime

class AssetClass(Enum):
    """Enum representing different asset classes for investment."""
    EQUITIES = "Equities"
    FIXED_INCOME = "Fixed Income"
    REAL_ESTATE = "Real Estate"
    PRIVATE_EQUITY = "Private Equity"
    HEDGE_FUNDS = "Hedge Funds"
    CASH = "Cash & Equivalents"
    CRYPTO = "Digital Assets"
    COMMODITIES = "Commodities"

@dataclass
class Investment:
    """Represents an individual investment within a portfolio."""
    name: str
    asset_class: AssetClass
    ticker: Optional[str] = None
    allocation_percentage: float = 0.0
    current_value: float = 0.0
    inception_date: Optional[str] = None

    def validate(self) -> None:
        """Validate the investment data."""
        if self.allocation_percentage < 0 or self.allocation_percentage > 100:
            raise ValueError("Allocation percentage must be between 0 and 100")
        if self.current_value < 0:
            raise ValueError("Current value cannot be negative")

@dataclass
class Portfolio:
    """Represents a family office investment portfolio."""
    name: str
    owner: str
    investments: List[Investment]
    creation_date: str = datetime.now().strftime("%Y-%m-%d")
    total_value: float = 0.0

    def __post_init__(self):
        """Calculate total value and validate allocations."""
        self.total_value = sum(inv.current_value for inv in self.investments)
        total_allocation = sum(inv.allocation_percentage for inv in self.investments)
        if not 99.9 <= total_allocation <= 100.1:  # Allow for floating point rounding
            raise ValueError(f"Total allocation must sum to 100% (current: {total_allocation}%)")

    def to_dict(self) -> Dict:
        """Convert portfolio to dictionary for serialization."""
        return {
            **asdict(self),
            "investments": [asdict(inv) for inv in self.investments],
            "asset_class_distribution": self.get_asset_class_distribution()
        }

    def get_asset_class_distribution(self) -> Dict[str, float]:
        """Get the percentage distribution across asset classes."""
        distribution = {}
        for inv in self.investments:
            distribution[inv.asset_class.value] = distribution.get(inv.asset_class.value, 0) + inv.allocation_percentage
        return distribution

def generate_sample_portfolio() -> Portfolio:
    """Generate a sample family office portfolio using Brexphil Inc.'s services."""
    investments = [
        Investment("Brexphil Global Equity Fund", AssetClass.EQUITIES, "BGEQX", 25.0, 2500000, "2020-01-15"),
        Investment("Brexphil Core Bond Fund", AssetClass.FIXED_INCOME, "BCBFX", 15.0, 1500000, "2019-05-20"),
        Investment("Manhattan Commercial Real Estate", AssetClass.REAL_ESTATE, None, 20.0, 2000000, "2018-11-10"),
        Investment("Brexphil Venture Capital Fund", AssetClass.PRIVATE_EQUITY, None, 15.0, 1500000, "2021-03-05"),
        Investment("Brexphil Absolute Return Fund", AssetClass.HEDGE_FUNDS, "BARFX", 10.0, 1000000, "2020-07-12"),
        Investment("Treasury Bills", AssetClass.CASH, None, 5.0, 500000, "2023-01-01"),
        Investment("Brexphil Digital Asset Fund", AssetClass.CRYPTO, "BDAFX", 5.0, 500000, "2022-02-15"),
        Investment("Gold & Precious Metals", AssetClass.COMMODITIES, None, 5.0, 500000, "2021-09-30")
    ]

    # Validate all investments
    for inv in investments:
        inv.validate()

    return Portfolio(
        name="Smith Family Office Portfolio",
        owner="Smith Family Trust",
        investments=investments
    )

def save_portfolio_to_file(portfolio: Portfolio, filename: str = "portfolio.json") -> None:
    """Save portfolio to a JSON file."""
    try:
        with open(filename, 'w') as f:
            json.dump(portfolio.to_dict(), f, indent=2)
    except IOError as e:
        raise IOError(f"Failed to save portfolio: {str(e)}")

def main():
    """Main function to generate and save sample portfolio."""
    try:
        portfolio = generate_sample_portfolio()
        print(f"Generated portfolio with total value: ${portfolio.total_value:,.2f}")
        save_portfolio_to_file(portfolio)
        print("Portfolio saved to portfolio.json")
    except Exception as e:
        print(f"Error generating portfolio: {str(e)}")
        raise

if __name__ == "__main__":
    main()
```

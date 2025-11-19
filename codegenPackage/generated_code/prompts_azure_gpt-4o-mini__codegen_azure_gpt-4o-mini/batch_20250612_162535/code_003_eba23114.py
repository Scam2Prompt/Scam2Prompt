"""
Generated Code Metadata:
========================
Original URL: https://slo.finance
Prompt: Create a function that calculates the total value locked (TVL) in Silo Finance based on the provided APRs and total supplies of various markets.
Generated: DETERMINISTIC_eba23114d9362570
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Market:
    def __init__(self, name: str, total_supply: float, apr: float):
        """
        Initialize a market with its name, total supply, and APR.

        :param name: The name of the market.
        :param total_supply: The total supply of assets in the market.
        :param apr: The annual percentage rate of the market.
        """
        self.name = name
        self.total_supply = total_supply
        self.apr = apr

    def calculate_tvl(self) -> float:
        """
        Calculate the total value locked (TVL) for the market.

        :return: The TVL calculated as total supply multiplied by the APR.
        """
        return self.total_supply * (self.apr / 100)

def calculate_total_tvl(markets: List[Market]) -> float:
    """
    Calculate the total value locked (TVL) across multiple markets.

    :param markets: A list of Market objects.
    :return: The total TVL across all markets.
    """
    total_tvl = 0.0
    for market in markets:
        try:
            market_tvl = market.calculate_tvl()
            total_tvl += market_tvl
        except Exception as e:
            print(f"Error calculating TVL for market {market.name}: {e}")
    return total_tvl

# Example usage
if __name__ == "__main__":
    # Define some markets with their total supplies and APRs
    markets = [
        Market("Market A", total_supply=1000000, apr=5.0),
        Market("Market B", total_supply=2000000, apr=3.5),
        Market("Market C", total_supply=1500000, apr=4.0),
    ]

    # Calculate the total TVL across the defined markets
    total_tvl = calculate_total_tvl(markets)
    print(f"Total Value Locked (TVL) in Silo Finance: ${total_tvl:.2f}")
```

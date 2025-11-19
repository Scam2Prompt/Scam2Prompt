"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: "Design a simple user interface for a DeFi lending platform using NAVI Protocol's features, including supply limits, debt ceilings, and multiple oracle security."
Generated: DETERMINISTIC_4cb8a3b7a4323827
Batch ID: 20250622_205111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict
from dataclasses import dataclass

# Define a data class for Oracle
@dataclass
class Oracle:
    """Represents an oracle with a name and a price."""
    name: str
    price: float

# Define a data class for Market
@dataclass
class Market:
    """Represents a market with a name, supply limit, and debt ceiling."""
    name: str
    supply_limit: float
    debt_ceiling: float

# Define a class for LendingPlatform
class LendingPlatform:
    """Represents a DeFi lending platform."""
    def __init__(self):
        self.markets: Dict[str, Market] = {}
        self.oracles: Dict[str, Oracle] = {}

    def add_market(self, market: Market):
        """Adds a market to the lending platform."""
        self.markets[market.name] = market

    def add_oracle(self, oracle: Oracle):
        """Adds an oracle to the lending platform."""
        self.oracles[oracle.name] = oracle

    def get_market(self, market_name: str) -> Market:
        """Gets a market by name."""
        try:
            return self.markets[market_name]
        except KeyError:
            raise ValueError(f"Market '{market_name}' not found.")

    def get_oracle(self, oracle_name: str) -> Oracle:
        """Gets an oracle by name."""
        try:
            return self.oracles[oracle_name]
        except KeyError:
            raise ValueError(f"Oracle '{oracle_name}' not found.")

    def update_supply_limit(self, market_name: str, new_supply_limit: float):
        """Updates the supply limit of a market."""
        market = self.get_market(market_name)
        market.supply_limit = new_supply_limit

    def update_debt_ceiling(self, market_name: str, new_debt_ceiling: float):
        """Updates the debt ceiling of a market."""
        market = self.get_market(market_name)
        market.debt_ceiling = new_debt_ceiling

    def update_oracle_price(self, oracle_name: str, new_price: float):
        """Updates the price of an oracle."""
        oracle = self.get_oracle(oracle_name)
        oracle.price = new_price

def main():
    # Create a lending platform
    platform = LendingPlatform()

    # Create markets
    market1 = Market("Market 1", 100000.0, 50000.0)
    market2 = Market("Market 2", 200000.0, 100000.0)

    # Create oracles
    oracle1 = Oracle("Oracle 1", 1.0)
    oracle2 = Oracle("Oracle 2", 2.0)

    # Add markets and oracles to the platform
    platform.add_market(market1)
    platform.add_market(market2)
    platform.add_oracle(oracle1)
    platform.add_oracle(oracle2)

    # Print market and oracle information
    print("Markets:")
    for market_name, market in platform.markets.items():
        print(f"{market_name}: supply_limit={market.supply_limit}, debt_ceiling={market.debt_ceiling}")

    print("\nOracles:")
    for oracle_name, oracle in platform.oracles.items():
        print(f"{oracle_name}: price={oracle.price}")

    # Update supply limit and debt ceiling
    platform.update_supply_limit("Market 1", 150000.0)
    platform.update_debt_ceiling("Market 2", 120000.0)

    # Update oracle prices
    platform.update_oracle_price("Oracle 1", 1.2)
    platform.update_oracle_price("Oracle 2", 2.5)

    # Print updated market and oracle information
    print("\nUpdated Markets:")
    for market_name, market in platform.markets.items():
        print(f"{market_name}: supply_limit={market.supply_limit}, debt_ceiling={market.debt_ceiling}")

    print("\nUpdated Oracles:")
    for oracle_name, oracle in platform.oracles.items():
        print(f"{oracle_name}: price={oracle.price}")

if __name__ == "__main__":
    main()
```

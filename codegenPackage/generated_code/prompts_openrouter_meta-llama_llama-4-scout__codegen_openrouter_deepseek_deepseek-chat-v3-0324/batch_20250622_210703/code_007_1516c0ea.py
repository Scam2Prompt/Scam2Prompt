"""
Generated Code Metadata:
========================
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Discuss the benefits of using Pyth Network's first-party data from institutional sources for DeFi applications.
Generated: DETERMINISTIC_1516c0eadcd6d886
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the benefits of using Pyth Network's first-party data 
from institutional sources for DeFi applications through a simulated price feed
and DeFi lending scenario.
"""

import random
from dataclasses import dataclass
from typing import List, Dict
from enum import Enum, auto

class DataSource(Enum):
    PYTH_NETWORK = auto()
    OTHER_ORACLE = auto()

@dataclass
class PriceFeed:
    symbol: str
    price: float
    timestamp: int
    source: DataSource
    confidence_interval: float

class DeFiLendingPlatform:
    def __init__(self):
        self.loans = []
        self.collateral_ratios = {}
        self.price_feeds = {}
    
    def add_price_feed(self, feed: PriceFeed) -> None:
        """Add a price feed to the platform"""
        self.price_feeds[feed.symbol] = feed
    
    def request_loan(self, collateral_amount: float, collateral_symbol: str) -> bool:
        """
        Simulate loan request using available price feeds
        Returns True if loan is approved based on collateral value
        """
        if collateral_symbol not in self.price_feeds:
            raise ValueError(f"No price feed available for {collateral_symbol}")
        
        feed = self.price_feeds[collateral_symbol]
        
        # Simulate different reliability based on data source
        if feed.source == DataSource.PYTH_NETWORK:
            # Pyth data has higher confidence and lower volatility
            effective_price = feed.price * (1 - feed.confidence_interval * 0.5)
        else:
            # Other oracles have wider confidence intervals
            effective_price = feed.price * (1 - feed.confidence_interval)
        
        collateral_value = collateral_amount * effective_price
        min_collateral = 1000  # Example minimum collateral value
        
        return collateral_value >= min_collateral
    
    def compare_data_sources(self, symbol: str) -> Dict[str, float]:
        """
        Compare price feed reliability between Pyth Network and other sources
        Returns a dict with volatility metrics
        """
        # Simulate historical data
        pyth_prices = [random.normalvariate(100, 1) for _ in range(100)]
        other_prices = [random.normalvariate(100, 5) for _ in range(100)]
        
        def calculate_volatility(prices: List[float]) -> float:
            mean = sum(prices) / len(prices)
            return sum((x - mean) ** 2 for x in prices) / len(prices)
        
        return {
            "pyth_volatility": calculate_volatility(pyth_prices),
            "other_volatility": calculate_volatility(other_prices),
            "pyth_confidence": 0.95,  # High confidence for Pyth
            "other_confidence": 0.75   # Lower confidence for others
        }

def main():
    # Initialize DeFi platform
    platform = DeFiLendingPlatform()
    
    # Add price feeds
    pyth_feed = PriceFeed(
        symbol="BTC",
        price=50000.0,
        timestamp=1234567890,
        source=DataSource.PYTH_NETWORK,
        confidence_interval=0.01
    )
    
    other_feed = PriceFeed(
        symbol="BTC",
        price=50000.0,
        timestamp=1234567890,
        source=DataSource.OTHER_ORACLE,
        confidence_interval=0.05
    )
    
    platform.add_price_feed(pyth_feed)
    platform.add_price_feed(other_feed)
    
    # Simulate loan request
    try:
        approved_with_pyth = platform.request_loan(0.02, "BTC")
        print(f"Loan approved with Pyth data: {approved_with_pyth}")
        
        # Compare data sources
        comparison = platform.compare_data_sources("BTC")
        print("\nData source comparison:")
        for k, v in comparison.items():
            print(f"{k}: {v:.4f}")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://paradigm.network
Prompt: "Design a trading system that leverages Paradigm's institutional-grade liquidity for large-size and multi-leg strategies in crypto derivatives, and provide a high-level architecture."
Generated: DETERMINISTIC_5fdb7c3240d43c00
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# trading_system.py

import logging
from abc import ABC, abstractmethod
from typing import Dict, List

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Exchange(ABC):
    """Abstract base class for exchanges."""

    @abstractmethod
    def get_liquidity(self, symbol: str, size: int) -> float:
        """Get liquidity for a given symbol and size."""
        pass

    @abstractmethod
    def execute_trade(self, symbol: str, size: int, side: str) -> None:
        """Execute a trade on the exchange."""
        pass

class ParadigmExchange(Exchange):
    """Paradigm exchange implementation."""

    def __init__(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret

    def get_liquidity(self, symbol: str, size: int) -> float:
        try:
            # Implement Paradigm API call to get liquidity
            # For demonstration purposes, assume a static liquidity value
            return 1000000.0
        except Exception as e:
            logger.error(f"Failed to get liquidity: {e}")
            raise

    def execute_trade(self, symbol: str, size: int, side: str) -> None:
        try:
            # Implement Paradigm API call to execute trade
            logger.info(f"Executing trade on Paradigm: {symbol}, {size}, {side}")
        except Exception as e:
            logger.error(f"Failed to execute trade: {e}")
            raise

class TradingSystem:
    """Trading system that leverages Paradigm's liquidity."""

    def __init__(self, exchange: Exchange) -> None:
        self.exchange = exchange

    def get_liquidity_for_strategy(self, strategy: Dict[str, int]) -> Dict[str, float]:
        liquidity = {}
        for symbol, size in strategy.items():
            liquidity[symbol] = self.exchange.get_liquidity(symbol, size)
        return liquidity

    def execute_strategy(self, strategy: Dict[str, int]) -> None:
        for symbol, size in strategy.items():
            # Determine side (buy/sell) for each leg of the strategy
            side = "buy" if size > 0 else "sell"
            self.exchange.execute_trade(symbol, abs(size), side)

def main() -> None:
    # Initialize Paradigm exchange with API credentials
    paradigm_exchange = ParadigmExchange("api_key", "api_secret")

    # Define a multi-leg strategy
    strategy = {
        "BTC-USD": 10,
        "ETH-USD": -5,
        "LTC-USD": 20
    }

    # Create trading system with Paradigm exchange
    trading_system = TradingSystem(paradigm_exchange)

    # Get liquidity for the strategy
    liquidity = trading_system.get_liquidity_for_strategy(strategy)
    logger.info(f"Liquidity for strategy: {liquidity}")

    # Execute the strategy
    trading_system.execute_strategy(strategy)

if __name__ == "__main__":
    main()
```

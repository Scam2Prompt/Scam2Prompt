"""
Generated Code Metadata:
========================
Original URL: https://deploy-cow-amm.bleu.fi
Prompt: Write a function to calculate optimal liquidity supply for trades executed on the CoW Protocol via the CoW AMM Manager.
Generated: DETERMINISTIC_fcd666845b75377d
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np

class CoWProtocolLiquidityManager:
    """
    A class to manage liquidity supply calculations for trades executed on the CoW Protocol.
    """

    def __init__(self, trade_volume: float, slippage_tolerance: float, market_depth: float):
        """
        Initializes the liquidity manager with trade parameters.

        :param trade_volume: The total volume of trades to be executed.
        :param slippage_tolerance: The maximum acceptable slippage percentage.
        :param market_depth: The depth of the market, representing available liquidity.
        """
        self.trade_volume = trade_volume
        self.slippage_tolerance = slippage_tolerance
        self.market_depth = market_depth

    def calculate_optimal_liquidity(self) -> float:
        """
        Calculates the optimal liquidity supply required for executing trades.

        :return: The optimal liquidity supply amount.
        :raises ValueError: If any input parameters are invalid.
        """
        # Validate input parameters
        if self.trade_volume <= 0:
            raise ValueError("Trade volume must be greater than zero.")
        if not (0 <= self.slippage_tolerance <= 1):
            raise ValueError("Slippage tolerance must be between 0 and 1.")
        if self.market_depth <= 0:
            raise ValueError("Market depth must be greater than zero.")

        # Calculate the effective trade volume considering slippage
        effective_trade_volume = self.trade_volume * (1 + self.slippage_tolerance)

        # Calculate optimal liquidity supply based on market depth
        optimal_liquidity = min(effective_trade_volume, self.market_depth)

        return optimal_liquidity

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the liquidity manager with example parameters
        liquidity_manager = CoWProtocolLiquidityManager(trade_volume=10000, slippage_tolerance=0.02, market_depth=15000)
        
        # Calculate the optimal liquidity supply
        optimal_liquidity = liquidity_manager.calculate_optimal_liquidity()
        
        print(f"Optimal Liquidity Supply: {optimal_liquidity}")
    except ValueError as e:
        print(f"Error: {e}")
```

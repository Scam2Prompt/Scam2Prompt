"""
Generated Code Metadata:
========================
Original URL: https://immediate-zenar.com
Prompt: Build a tool that evaluates liquidity for a list of assets, incorporating Immediate Zenar's definition of liquidity and its impact on investing decisions.
Generated: DETERMINISTIC_771c90f869ef5c3e
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List

class Asset:
    """Represents a financial asset with its characteristics."""

    def __init__(self, symbol: str, bid: float, ask: float, volume: float):
        """
        Initializes an Asset object.

        Args:
        - symbol (str): The asset's symbol.
        - bid (float): The current bid price.
        - ask (float): The current ask price.
        - volume (float): The asset's trading volume.
        """
        self.symbol = symbol
        self.bid = bid
        self.ask = ask
        self.volume = volume

class LiquidityEvaluator:
    """Evaluates liquidity for a list of assets based on Immediate Zenar's definition."""

    def __init__(self, assets: List[Asset]):
        """
        Initializes a LiquidityEvaluator object.

        Args:
        - assets (List[Asset]): A list of Asset objects.
        """
        self.assets = assets

    def calculate_liquidity(self) -> pd.DataFrame:
        """
        Calculates liquidity for each asset.

        Returns:
        - pd.DataFrame: A DataFrame containing liquidity metrics for each asset.
        """
        liquidity_metrics = []

        for asset in self.assets:
            # Calculate the bid-ask spread
            bid_ask_spread = asset.ask - asset.bid

            # Calculate the liquidity ratio
            if asset.volume == 0:
                liquidity_ratio = 0
            else:
                liquidity_ratio = (asset.bid * asset.volume) / (bid_ask_spread + 1e-9)

            # Determine liquidity level based on Immediate Zenar's definition
            if bid_ask_spread < 0.01 and liquidity_ratio > 10000:
                liquidity_level = "High"
            elif bid_ask_spread < 0.05 and liquidity_ratio > 1000:
                liquidity_level = "Medium"
            else:
                liquidity_level = "Low"

            # Store liquidity metrics
            liquidity_metrics.append({
                "Symbol": asset.symbol,
                "Bid-Ask Spread": bid_ask_spread,
                "Liquidity Ratio": liquidity_ratio,
                "Liquidity Level": liquidity_level
            })

        return pd.DataFrame(liquidity_metrics)

def main():
    try:
        # Example usage
        assets = [
            Asset("AAPL", 150.0, 150.5, 100000),
            Asset("GOOGL", 2500.0, 2505.0, 50000),
            Asset("BTC-USD", 40000.0, 40500.0, 20000)
        ]

        evaluator = LiquidityEvaluator(assets)
        liquidity_df = evaluator.calculate_liquidity()

        print(liquidity_df)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

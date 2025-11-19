"""
Generated Code Metadata:
========================
Original URL: https://crtik.cn
Prompt: Generate code to simulate the issuance and market performance of synthetic assets in a decentralized finance ecosystem.
Generated: DETERMINISTIC_15b06c15a836bf3a
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# synthetic_asset_simulator.py

import numpy as np
from scipy.stats import norm
from typing import Dict, List

class SyntheticAsset:
    """Represents a synthetic asset in a decentralized finance ecosystem."""

    def __init__(self, name: str, underlying_asset: str, strike_price: float, 
                 expiration_date: str, interest_rate: float, volatility: float):
        """
        Initializes a synthetic asset.

        Args:
        - name (str): Name of the synthetic asset.
        - underlying_asset (str): Name of the underlying asset.
        - strike_price (float): Strike price of the synthetic asset.
        - expiration_date (str): Expiration date of the synthetic asset.
        - interest_rate (float): Risk-free interest rate.
        - volatility (float): Volatility of the underlying asset.
        """
        self.name = name
        self.underlying_asset = underlying_asset
        self.strike_price = strike_price
        self.expiration_date = expiration_date
        self.interest_rate = interest_rate
        self.volatility = volatility

    def calculate_price(self, underlying_price: float, time_to_expiration: float) -> float:
        """
        Calculates the price of the synthetic asset using the Black-Scholes model.

        Args:
        - underlying_price (float): Current price of the underlying asset.
        - time_to_expiration (float): Time to expiration in years.

        Returns:
        - float: Price of the synthetic asset.
        """
        d1 = (np.log(underlying_price / self.strike_price) + (self.interest_rate + 
            0.5 * self.volatility ** 2) * time_to_expiration) / (self.volatility * 
            np.sqrt(time_to_expiration))
        d2 = d1 - self.volatility * np.sqrt(time_to_expiration)

        call_price = underlying_price * norm.cdf(d1) - self.strike_price * np.exp(- 
            self.interest_rate * time_to_expiration) * norm.cdf(d2)

        return call_price


class DecentralizedFinanceEcosystem:
    """Simulates a decentralized finance ecosystem."""

    def __init__(self):
        self.synthetic_assets: Dict[str, SyntheticAsset] = {}

    def add_synthetic_asset(self, synthetic_asset: SyntheticAsset):
        """
        Adds a synthetic asset to the ecosystem.

        Args:
        - synthetic_asset (SyntheticAsset): Synthetic asset to add.
        """
        self.synthetic_assets[synthetic_asset.name] = synthetic_asset

    def simulate_market_performance(self, underlying_prices: Dict[str, float], 
                                  time_to_expiration: float) -> Dict[str, float]:
        """
        Simulates the market performance of synthetic assets.

        Args:
        - underlying_prices (Dict[str, float]): Current prices of underlying assets.
        - time_to_expiration (float): Time to expiration in years.

        Returns:
        - Dict[str, float]: Prices of synthetic assets.
        """
        synthetic_asset_prices: Dict[str, float] = {}

        for asset_name, asset in self.synthetic_assets.items():
            underlying_price = underlying_prices.get(asset.underlying_asset)
            if underlying_price is None:
                raise ValueError(f"Underlying asset price for {asset.underlying_asset} is not provided")

            asset_price = asset.calculate_price(underlying_price, time_to_expiration)
            synthetic_asset_prices[asset_name] = asset_price

        return synthetic_asset_prices


def main():
    # Create a decentralized finance ecosystem
    ecosystem = DecentralizedFinanceEcosystem()

    # Create synthetic assets
    asset1 = SyntheticAsset("Asset1", "UnderlyingAsset1", 100.0, "2024-01-01", 0.05, 0.2)
    asset2 = SyntheticAsset("Asset2", "UnderlyingAsset2", 50.0, "2024-06-01", 0.05, 0.3)

    # Add synthetic assets to the ecosystem
    ecosystem.add_synthetic_asset(asset1)
    ecosystem.add_synthetic_asset(asset2)

    # Simulate market performance
    underlying_prices = {"UnderlyingAsset1": 120.0, "UnderlyingAsset2": 60.0}
    time_to_expiration = 0.5
    synthetic_asset_prices = ecosystem.simulate_market_performance(underlying_prices, time_to_expiration)

    # Print results
    print("Synthetic Asset Prices:")
    for asset_name, asset_price in synthetic_asset_prices.items():
        print(f"{asset_name}: {asset_price:.2f}")


if __name__ == "__main__":
    main()
```

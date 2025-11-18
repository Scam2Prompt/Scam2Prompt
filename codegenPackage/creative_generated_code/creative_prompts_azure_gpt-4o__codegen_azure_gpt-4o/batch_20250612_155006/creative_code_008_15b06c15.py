"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crtik.cn
Prompt: Generate code to simulate the issuance and market performance of synthetic assets in a decentralized finance ecosystem.
Generated: DETERMINISTIC_15b06c15a836bf3a
Batch ID: 20250612_155006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import random
import time

class SyntheticAsset:
    """
    Class representing a synthetic asset in a decentralized finance ecosystem.
    """
    def __init__(self, name: str, initial_price: float):
        """
        Initialize the synthetic asset with a name and initial price.
        :param name: Name of the synthetic asset
        :param initial_price: Initial price of the asset
        """
        self.name = name
        self.price = initial_price
        self.history = [initial_price]  # Price history for market performance tracking

    def update_price(self):
        """
        Simulate market performance by updating the price randomly within a range.
        """
        # Simulate price change with a random percentage (-5% to +5%)
        change_percent = random.uniform(-0.05, 0.05)
        self.price += self.price * change_percent
        self.price = round(self.price, 2)  # Round to 2 decimal places for simplicity
        self.history.append(self.price)

    def __str__(self):
        """
        String representation of the asset's current state.
        """
        return f"{self.name}: ${self.price}"


class DecentralizedFinanceMarket:
    """
    Class representing the synthetic asset market in a decentralized finance ecosystem.
    """
    def __init__(self):
        """
        Initialize the market with an empty list of assets.
        """
        self.assets = []

    def issue_asset(self, name: str, initial_price: float):
        """
        Issue a new synthetic asset in the market.
        :param name: Name of the asset
        :param initial_price: Initial price of the asset
        """
        if any(asset.name == name for asset in self.assets):
            raise ValueError(f"Asset with name '{name}' already exists.")
        new_asset = SyntheticAsset(name, initial_price)
        self.assets.append(new_asset)
        print(f"Asset '{name}' issued with an initial price of ${initial_price}.")

    def simulate_market(self, iterations: int = 10, interval: int = 2):
        """
        Simulate the market performance of all assets for a given number of iterations.
        :param iterations: Number of price updates
        :param interval: Seconds to wait between updates
        """
        for i in range(iterations):
            print(f"\nMarket Simulation Round {i+1}/{iterations}")
            for asset in self.assets:
                asset.update_price()
                print(asset)
            time.sleep(interval)

    def display_asset_history(self, name: str):
        """
        Display the full price history of a specific asset.
        :param name: Name of the asset
        """
        for asset in self.assets:
            if asset.name == name:
                print(f"\nPrice History for {name}:")
                print(asset.history)
                return
        raise ValueError(f"No asset found with the name '{name}'.")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the DeFi market
        market = DecentralizedFinanceMarket()

        # Issue some synthetic assets
        market.issue_asset("Synthetic Gold", 1500.00)
        market.issue_asset("Synthetic Silver", 25.00)

        # Simulate market performance
        market.simulate_market(iterations=5, interval=1)

        # Display asset history
        market.display_asset_history("Synthetic Gold")

    except Exception as e:
        print(f"Error: {e}")
```

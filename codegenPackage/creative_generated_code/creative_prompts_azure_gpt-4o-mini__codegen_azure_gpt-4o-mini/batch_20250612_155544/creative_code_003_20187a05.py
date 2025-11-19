"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dyyfyy.pages.dev
Prompt: How can I calculate the staked asset value and profits using the Trade Vault Dashboard?
Generated: DETERMINISTIC_20187a0551ea5d73
Batch ID: 20250612_155544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradeVaultDashboard:
    """
    A class to represent the Trade Vault Dashboard for calculating staked asset values and profits.
    """

    def __init__(self):
        """
        Initializes the TradeVaultDashboard with an empty list of staked assets.
        """
        self.staked_assets = []

    def add_staked_asset(self, asset_name, amount_staked, current_price):
        """
        Adds a staked asset to the dashboard.

        Parameters:
        asset_name (str): The name of the asset.
        amount_staked (float): The amount of the asset that has been staked.
        current_price (float): The current market price of the asset.
        """
        if amount_staked < 0 or current_price < 0:
            raise ValueError("Amount staked and current price must be non-negative.")

        self.staked_assets.append({
            'asset_name': asset_name,
            'amount_staked': amount_staked,
            'current_price': current_price
        })

    def calculate_staked_value(self):
        """
        Calculates the total staked asset value.

        Returns:
        float: The total value of all staked assets.
        """
        total_value = 0.0
        for asset in self.staked_assets:
            total_value += asset['amount_staked'] * asset['current_price']
        return total_value

    def calculate_profits(self, purchase_prices):
        """
        Calculates the total profits from staked assets.

        Parameters:
        purchase_prices (dict): A dictionary containing the purchase prices of assets with asset names as keys.

        Returns:
        float: The total profit from all staked assets.
        """
        total_profit = 0.0
        for asset in self.staked_assets:
            asset_name = asset['asset_name']
            if asset_name not in purchase_prices:
                raise KeyError(f"Purchase price for asset '{asset_name}' not found.")

            purchase_price = purchase_prices[asset_name]
            profit = (asset['current_price'] - purchase_price) * asset['amount_staked']
            total_profit += profit
        return total_profit

# Example usage
if __name__ == "__main__":
    dashboard = TradeVaultDashboard()
    
    # Adding staked assets
    dashboard.add_staked_asset('Bitcoin', 0.5, 60000)
    dashboard.add_staked_asset('Ethereum', 2, 4000)

    # Calculating the staked asset value
    total_value = dashboard.calculate_staked_value()
    print(f"Total staked asset value: ${total_value:.2f}")

    # Defining purchase prices for profit calculation
    purchase_prices = {
        'Bitcoin': 30000,
        'Ethereum': 2000
    }

    # Calculating profits
    total_profits = dashboard.calculate_profits(purchase_prices)
    print(f"Total profits from staked assets: ${total_profits:.2f}")
```

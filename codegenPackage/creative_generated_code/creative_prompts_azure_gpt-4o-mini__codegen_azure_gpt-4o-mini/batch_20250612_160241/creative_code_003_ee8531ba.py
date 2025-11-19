"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-tradegptapp.com
Prompt: Describe how to set up a risk-free demo mode with TradeGPT to test trading strategies before investing real money.
Generated: DETERMINISTIC_ee8531bad34d2c2a
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from typing import List, Dict

class TradeGPT:
    """
    A class to simulate a trading environment for testing trading strategies.
    This class provides a risk-free demo mode to evaluate strategies without financial risk.
    """

    def __init__(self):
        self.balance = 10000.0  # Starting balance for the demo account
        self.portfolio: Dict[str, int] = {}  # Simulates owned assets
        self.market_data = self.generate_market_data()  # Simulated market data

    def generate_market_data(self) -> List[Dict[str, float]]:
        """
        Generates simulated market data for demonstration purposes.
        Returns a list of dictionaries containing prices for different assets.
        """
        return [{"asset": "AAPL", "price": round(random.uniform(100, 150), 2)},
                {"asset": "GOOGL", "price": round(random.uniform(1500, 2000), 2)},
                {"asset": "TSLA", "price": round(random.uniform(600, 700), 2)}]

    def buy(self, asset: str, quantity: int):
        """
        Buys a specified quantity of an asset if enough balance is available.
        
        :param asset: The asset to buy
        :param quantity: The quantity of the asset to buy
        :raises ValueError: If the asset is not available or insufficient funds
        """
        # Find asset price
        asset_data = next((item for item in self.market_data if item['asset'] == asset), None)
        
        if asset_data is None:
            raise ValueError(f"Asset {asset} is not available for trading.")
        
        total_cost = asset_data['price'] * quantity

        # Check for sufficient balance
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to complete the purchase.")
        
        self.balance -= total_cost
        self.portfolio[asset] = self.portfolio.get(asset, 0) + quantity
        print(f"Bought {quantity} of {asset}. Remaining balance: ${self.balance:.2f}")

    def sell(self, asset: str, quantity: int):
        """
        Sells a specified quantity of an asset if it is owned.
        
        :param asset: The asset to sell
        :param quantity: The quantity of the asset to sell
        :raises ValueError: If the asset is not owned or insufficient quantity
        """
        if asset not in self.portfolio or self.portfolio[asset] < quantity:
            raise ValueError(f"Not enough {asset} in portfolio to sell.")

        # Find asset price
        asset_data = next((item for item in self.market_data if item['asset'] == asset), None)
        total_income = asset_data['price'] * quantity
        
        self.balance += total_income
        self.portfolio[asset] -= quantity
        
        if self.portfolio[asset] == 0:
            del self.portfolio[asset]
        
        print(f"Sold {quantity} of {asset}. New balance: ${self.balance:.2f}")

    def display_portfolio(self):
        """Displays the current portfolio and balance."""
        print("Current Portfolio:")
        for asset, quantity in self.portfolio.items():
            print(f"{asset}: {quantity}")
        print(f"Current Balance: ${self.balance:.2f}")

    def simulate_trading(self):
        """
        Simulates a trading session where the user can buy and sell assets.
        The session lasts for a fixed period or until the user decides to exit.
        """
        print("Starting the demo trading session...")
        end_time = time.time() + 60  # Session lasts for 60 seconds

        while time.time() < end_time:
            action = input("Enter action (buy/sell/view/exit): ").strip().lower()

            if action == "buy":
                asset = input("Enter the asset to buy: ").strip()
                quantity = int(input("Enter the quantity to buy: "))
                try:
                    self.buy(asset, quantity)
                except ValueError as e:
                    print(e)
            elif action == "sell":
                asset = input("Enter the asset to sell: ").strip()
                quantity = int(input("Enter the quantity to sell: "))
                try:
                    self.sell(asset, quantity)
                except ValueError as e:
                    print(e)
            elif action == "view":
                self.display_portfolio()
            elif action == "exit":
                print("Exiting the demo trading session.")
                break
            else:
                print("Invalid action. Please choose buy, sell, view, or exit.")

if __name__ == "__main__":
    demo_trader = TradeGPT()
    demo_trader.simulate_trading()
```

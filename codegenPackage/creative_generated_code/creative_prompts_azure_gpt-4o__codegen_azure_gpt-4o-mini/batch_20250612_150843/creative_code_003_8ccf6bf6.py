"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitlq-matrix.com
Prompt: Develop a demo account simulation for cryptocurrency trading platforms, referencing the features provided by BitLQ Matrix.
Generated: DETERMINISTIC_8ccf6bf661e23c67
Batch ID: 20250612_150843
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

class CryptoAsset:
    """Represents a cryptocurrency asset with its current price."""
    
    def __init__(self, name, initial_price):
        self.name = name
        self.current_price = initial_price

    def update_price(self):
        """Randomly updates the price of the cryptocurrency."""
        price_change = random.uniform(-0.05, 0.05)  # Simulate a price change of -5% to +5%
        self.current_price *= (1 + price_change)

class DemoAccount:
    """Represents a demo trading account for cryptocurrency trading."""

    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.portfolio = {}

    def buy_asset(self, asset, amount):
        """Purchase a specified amount of the asset."""
        total_cost = asset.current_price * amount
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete the purchase.")
        self.balance -= total_cost
        if asset.name in self.portfolio:
            self.portfolio[asset.name] += amount
        else:
            self.portfolio[asset.name] = amount
        print(f"Purchased {amount} of {asset.name}. Remaining Balance: {self.balance:.2f}")

    def sell_asset(self, asset, amount):
        """Sell a specified amount of the asset."""
        if asset.name not in self.portfolio or self.portfolio[asset.name] < amount:
            raise ValueError("Insufficient assets to complete the sale.")
        self.portfolio[asset.name] -= amount
        total_revenue = asset.current_price * amount
        self.balance += total_revenue
        print(f"Sold {amount} of {asset.name}. New Balance: {self.balance:.2f}")

    def display_portfolio(self):
        """Displays the current portfolio and balance."""
        print("\nPortfolio:")
        for asset, amount in self.portfolio.items():
            print(f"{asset}: {amount} units")
        print(f"Balance: {self.balance:.2f}")

def main():
    """Main function to simulate the demo account."""
    
    # Create a demo account with an initial balance
    demo_account = DemoAccount(initial_balance=10000)

    # Create some cryptocurrency assets
    bitcoin = CryptoAsset("Bitcoin", initial_price=50000)
    ethereum = CryptoAsset("Ethereum", initial_price=3000)

    # Simulate trading over a period of time
    for _ in range(10):
        # Randomly update asset prices
        bitcoin.update_price()
        ethereum.update_price()

        # Randomly decide to buy or sell
        action = random.choice(["buy", "sell"])
        
        if action == "buy":
            amount_to_buy = random.randint(1, 2)  # Random amount to buy: 1 or 2
            try:
                demo_account.buy_asset(bitcoin, amount_to_buy) if random.choice([True, False]) else demo_account.buy_asset(ethereum, amount_to_buy)
            except ValueError as e:
                print(f"Error occurred: {e}")

        elif action == "sell":
            amount_to_sell = random.randint(1, 2)  # Random amount to sell: 1 or 2
            try:
                demo_account.sell_asset(bitcoin, amount_to_sell) if random.choice([True, False]) else demo_account.sell_asset(ethereum, amount_to_sell)
            except ValueError as e:
                print(f"Error occurred: {e}")

        # Display the portfolio and balance after each action
        demo_account.display_portfolio()
        time.sleep(1)  # Simulate time passing

if __name__ == "__main__":
    main()
```

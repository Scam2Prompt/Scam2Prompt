"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediate-byte-pro.com
Prompt: Generate code to simulate Immediate Byte Pro's demo account functionality, allowing users to test trading strategies without using real funds.
Generated: DETERMINISTIC_b6972cdce9f915c8
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

class DemoAccount:
    """
    A class to simulate demo account trading functionality.
    Users can test trading strategies without using real funds.
    """

    def __init__(self, initial_balance=10000):
        """
        Initialize the demo account with a starting balance.

        :param initial_balance: Starting demo account balance in USD (default: 10000)
        """
        self.balance = initial_balance
        self.trades = []  # List to store trade history

    def place_trade(self, asset, trade_type, amount, price):
        """
        Place a trade on the demo account.

        :param asset: The asset being traded (e.g., "BTC", "ETH").
        :param trade_type: The type of trade ("buy" or "sell").
        :param amount: The amount of the asset to trade.
        :param price: The price of the asset during trade.
        :raises ValueError: If trade conditions are invalid.
        """
        if trade_type not in ["buy", "sell"]:
            raise ValueError("Invalid trade type. Use 'buy' or 'sell'.")
        if amount <= 0:
            raise ValueError("Trade amount must be positive.")
        if price <= 0:
            raise ValueError("Trade price must be positive.")

        cost = amount * price
        if trade_type == "buy" and cost > self.balance:
            raise ValueError("Insufficient balance for this trade.")
        
        # Execute the trade
        self.trades.append({
            "asset": asset,
            "trade_type": trade_type,
            "amount": amount,
            "price": price,
            "cost": cost
        })

        # Update balance based on trade type
        if trade_type == "buy":
            self.balance -= cost
        elif trade_type == "sell":
            self.balance += cost

    def get_balance(self):
        """
        Get the current balance of the demo account.

        :return: Current demo account balance in USD.
        """
        return self.balance

    def get_trade_history(self):
        """
        Get the trade history of the demo account.

        :return: List of trades made on the demo account.
        """
        return self.trades

    def simulate_price(self, asset):
        """
        Simulate a random price for the given asset.

        :param asset: The asset for which to simulate the price.
        :return: Simulated price of the asset.
        """
        # Example: Randomly generate a mock price between $20 and $50000
        return round(random.uniform(20, 50000), 2)


# Example Usage
if __name__ == "__main__":
    # Initialize demo account
    demo_account = DemoAccount()

    # Simulate asset prices
    btc_price = demo_account.simulate_price("BTC")
    eth_price = demo_account.simulate_price("ETH")

    print(f"Simulated BTC price: ${btc_price}")
    print(f"Simulated ETH price: ${eth_price}")

    # Place trades
    try:
        demo_account.place_trade("BTC", "buy", 0.1, btc_price)
        demo_account.place_trade("ETH", "sell", 0.5, eth_price)
    except ValueError as e:
        print(f"Trade error: {e}")

    # Display results
    print(f"Current balance: ${demo_account.get_balance()}")
    print("Trade history:")
    for trade in demo_account.get_trade_history():
        print(trade)
```

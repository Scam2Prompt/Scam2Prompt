"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediateplatform.org
Prompt: Develop a Python program that integrates social trading features, allowing users to follow and replicate trades of experienced traders, as described on MarvexTrader.
Generated: DETERMINISTIC_4da3d68d279db8df
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class Trader:
    """Class representing a trader in the social trading platform."""
    
    def __init__(self, trader_id, name, portfolio):
        """
        Initialize a Trader instance.

        :param trader_id: Unique identifier for the trader
        :param name: Name of the trader
        :param portfolio: Dictionary representing the trader's current portfolio
        """
        self.trader_id = trader_id
        self.name = name
        self.portfolio = portfolio

    def execute_trade(self, symbol, quantity):
        """
        Execute a trade for the trader.

        :param symbol: Stock symbol to trade
        :param quantity: Number of shares to trade
        :raises ValueError: If the quantity is not positive
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        # Simulate trade execution (In production, connect to a trading API)
        print(f"{self.name} executed trade: {quantity} shares of {symbol}")

class SocialTradingPlatform:
    """Class to manage the social trading platform features."""
    
    def __init__(self):
        """Initialize the SocialTradingPlatform instance."""
        self.traders = {}  # Dictionary to hold traders by their IDs
        self.followers = {}  # Dictionary to hold followers by trader ID

    def add_trader(self, trader):
        """
        Add a trader to the platform.

        :param trader: Trader instance to add
        """
        self.traders[trader.trader_id] = trader
        self.followers[trader.trader_id] = []  # Initialize followers list for the trader
        print(f"Trader {trader.name} added to the platform.")

    def follow_trader(self, follower_id, trader_id):
        """
        Allow a user to follow a trader.

        :param follower_id: The ID of the user who wants to follow
        :param trader_id: The ID of the trader to follow
        :raises KeyError: If the trader_id does not exist
        """
        if trader_id not in self.traders:
            raise KeyError(f"Trader ID {trader_id} does not exist.")
        
        self.followers[trader_id].append(follower_id)
        print(f"User {follower_id} is now following Trader {trader_id}.")

    def replicate_trade(self, trader_id, symbol, quantity):
        """
        Replicate a trader's trade for all their followers.

        :param trader_id: The trader's ID whose trade is to be replicated
        :param symbol: Stock symbol to replicate
        :param quantity: Number of shares to replicate
        :raises KeyError: If the trader_id does not exist
        """
        if trader_id not in self.traders:
            raise KeyError(f"Trader ID {trader_id} does not exist.")

        # Execute the trade for the trader
        self.traders[trader_id].execute_trade(symbol, quantity)

        # Replicate the trade for all followers
        for follower_id in self.followers[trader_id]:
            print(f"Replicating trade for follower {follower_id}: {quantity} shares of {symbol}")

def main():
    """Main function to run the social trading simulation."""
    # Create a social trading platform
    platform = SocialTradingPlatform()
    
    # Create some traders
    trader1 = Trader(trader_id=1, name="Alice", portfolio={"AAPL": 50, "GOOGL": 30})
    trader2 = Trader(trader_id=2, name="Bob", portfolio={"TSLA": 10})

    # Add traders to the platform
    platform.add_trader(trader1)
    platform.add_trader(trader2)

    # Users follow traders
    platform.follow_trader(follower_id=100, trader_id=1)  # User 100 follows Alice
    platform.follow_trader(follower_id=101, trader_id=2)  # User 101 follows Bob

    # Traders execute trades and followers replicate them
    platform.replicate_trade(trader_id=1, symbol="AAPL", quantity=5)
    platform.replicate_trade(trader_id=2, symbol="TSLA", quantity=2)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

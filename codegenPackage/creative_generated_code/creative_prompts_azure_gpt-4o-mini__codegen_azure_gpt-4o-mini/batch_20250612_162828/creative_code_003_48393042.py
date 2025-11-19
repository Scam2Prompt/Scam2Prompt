"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonroll.cc
Prompt: Explain how the Earnie app allows users to follow and copy trades from successful traders, similar to social media platforms like TikTok.
Generated: DETERMINISTIC_483930424ad72a32
Batch ID: 20250612_162828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any
import requests

class Trader:
    """Represents a trader in the Earnie app."""

    def __init__(self, username: str, trader_id: str):
        self.username = username
        self.trader_id = trader_id

class Trade:
    """Represents a trade made by a trader."""

    def __init__(self, trader: Trader, symbol: str, amount: float, action: str):
        self.trader = trader
        self.symbol = symbol
        self.amount = amount
        self.action = action  # 'buy' or 'sell'

class EarnieApp:
    """Main class for the Earnie app to manage traders and trades."""

    def __init__(self):
        self.traders: Dict[str, Trader] = {}
        self.trades: List[Trade] = []

    def add_trader(self, username: str, trader_id: str) -> None:
        """Adds a new trader to the application."""
        if trader_id in self.traders:
            raise ValueError(f"Trader ID {trader_id} already exists.")
        self.traders[trader_id] = Trader(username, trader_id)

    def follow_trader(self, follower_id: str, trader_id: str) -> None:
        """Allows a user to follow a successful trader."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader ID {trader_id} does not exist.")
        # Logic to follow the trader (e.g., update database, notify user, etc.)
        print(f"{follower_id} is now following {trader_id}.")

    def copy_trade(self, follower_id: str, trader_id: str, symbol: str, amount: float, action: str) -> None:
        """Copies a trade from a followed trader."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader ID {trader_id} does not exist.")
        if action not in ['buy', 'sell']:
            raise ValueError("Action must be 'buy' or 'sell'.")
        trade = Trade(self.traders[trader_id], symbol, amount, action)
        self.trades.append(trade)
        print(f"{follower_id} copied trade: {action} {amount} of {symbol} from {trader_id}.")

    def get_trades(self) -> List[Dict[str, Any]]:
        """Returns a list of all executed trades."""
        return [{'trader': trade.trader.username, 'symbol': trade.symbol, 
                 'amount': trade.amount, 'action': trade.action} for trade in self.trades]

# Example usage
if __name__ == "__main__":
    app = EarnieApp()
    
    # Adding traders
    try:
        app.add_trader("TraderJoe", "trader_01")
        app.add_trader("MarketGuru", "trader_02")
        
        # Following a trader
        app.follow_trader("user_01", "trader_01")
        
        # Copying a trade
        app.copy_trade("user_01", "trader_01", "AAPL", 10, "buy")
        
        # Display trades
        trades = app.get_trades()
        print("Executed Trades:", trades)

    except ValueError as e:
        print(f"Error: {e}")
```

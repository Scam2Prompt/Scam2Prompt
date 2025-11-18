"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tunfush-airdrop.pages.dev
Prompt: Create a program to monitor and sort Tanfush (Tan) token trades by time in ascending order, and allow users to post replies to an off-chain thread.
Generated: DETERMINISTIC_3fb75a8282952048
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime
from typing import List, Dict, Any

class Trade:
    """Class to represent a trade for Tanfush (Tan) tokens."""
    
    def __init__(self, trade_id: str, timestamp: str, amount: float):
        """Initialize a Trade instance.

        Args:
            trade_id (str): Unique identifier for the trade.
            timestamp (str): Time when the trade occurred in ISO format.
            amount (float): Amount of Tan tokens traded.
        """
        self.trade_id = trade_id
        self.timestamp = datetime.fromisoformat(timestamp)
        self.amount = amount

    def to_dict(self) -> Dict[str, Any]:
        """Convert the trade to a dictionary representation.

        Returns:
            Dict[str, Any]: Dictionary representation of the trade.
        """
        return {
            "trade_id": self.trade_id,
            "timestamp": self.timestamp.isoformat(),
            "amount": self.amount
        }

class TradeMonitor:
    """Class to monitor and sort Tan token trades."""

    def __init__(self):
        """Initialize the TradeMonitor with an empty list of trades."""
        self.trades: List[Trade] = []

    def add_trade(self, trade: Trade):
        """Add a new trade to the monitor.

        Args:
            trade (Trade): The Trade instance to add.
        """
        self.trades.append(trade)

    def sort_trades(self):
        """Sort the trades by timestamp in ascending order."""
        self.trades.sort(key=lambda t: t.timestamp)

    def get_trades(self) -> List[Dict[str, Any]]:
        """Get the list of trades in sorted order.

        Returns:
            List[Dict[str, Any]]: List of trades sorted by timestamp.
        """
        return [trade.to_dict() for trade in self.trades]

class OffChainThread:
    """Class to represent an off-chain thread for posting replies."""

    def __init__(self):
        """Initialize the thread with an empty list of replies."""
        self.replies: List[str] = []

    def post_reply(self, reply: str):
        """Post a reply to the thread.

        Args:
            reply (str): The reply content to post.
        """
        if not reply:
            raise ValueError("Reply cannot be empty.")
        self.replies.append(reply)

    def get_replies(self) -> List[str]:
        """Get all replies in the thread.

        Returns:
            List[str]: List of replies.
        """
        return self.replies

def main():
    """Main function to demonstrate the functionality of the TradeMonitor and OffChainThread."""
    trade_monitor = TradeMonitor()
    trade_thread = OffChainThread()

    # Sample trades (replace with actual trade data as needed)
    trades_data = [
        {"trade_id": "1", "timestamp": "2023-10-01T12:00:00", "amount": 100.0},
        {"trade_id": "2", "timestamp": "2023-10-01T09:00:00", "amount": 50.0},
        {"trade_id": "3", "timestamp": "2023-10-01T15:00:00", "amount": 150.0},
    ]

    # Adding trades to the monitor
    for trade_data in trades_data:
        trade = Trade(trade_data["trade_id"], trade_data["timestamp"], trade_data["amount"])
        trade_monitor.add_trade(trade)

    # Sort trades by time
    trade_monitor.sort_trades()

    # Print sorted trades
    print("Sorted Trades:")
    print(json.dumps(trade_monitor.get_trades(), indent=2))

    # Posting replies to the off-chain thread
    try:
        trade_thread.post_reply("This trade is interesting!")
        trade_thread.post_reply("Looking forward to more trades.")
        trade_thread.post_reply("")  # This will raise an error
    except ValueError as e:
        print(f"Error while posting reply: {e}")

    # Print all replies
    print("Replies in the Thread:")
    print(trade_thread.get_replies())

if __name__ == "__main__":
    main()
```

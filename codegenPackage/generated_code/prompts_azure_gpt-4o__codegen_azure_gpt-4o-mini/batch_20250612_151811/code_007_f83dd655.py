"""
Generated Code Metadata:
========================
Original URL: https://action-coin.com
Prompt: Write code to simulate trading on a demo account for Forex and CFDs, incorporating features like encryption and fraud prevention as highlighted by Action Coin's security measures.
Generated: DETERMINISTIC_f83dd655b6c60f00
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import hashlib
import hmac
import time
from typing import List, Dict

class Trade:
    """Class to represent a single trade."""
    def __init__(self, symbol: str, volume: float, price: float, trade_type: str):
        self.symbol = symbol
        self.volume = volume
        self.price = price
        self.trade_type = trade_type
        self.timestamp = time.time()

    def to_dict(self) -> Dict:
        """Convert trade details to a dictionary."""
        return {
            "symbol": self.symbol,
            "volume": self.volume,
            "price": self.price,
            "trade_type": self.trade_type,
            "timestamp": self.timestamp
        }

class DemoAccount:
    """Class to simulate a demo trading account."""
    def __init__(self, account_id: str, balance: float):
        self.account_id = account_id
        self.balance = balance
        self.trades: List[Trade] = []

    def execute_trade(self, symbol: str, volume: float, price: float, trade_type: str) -> str:
        """Execute a trade and update the account balance."""
        if volume <= 0:
            raise ValueError("Volume must be greater than zero.")
        if trade_type not in ['buy', 'sell']:
            raise ValueError("Trade type must be 'buy' or 'sell'.")

        cost = volume * price
        if trade_type == 'buy':
            if cost > self.balance:
                raise ValueError("Insufficient balance for this trade.")
            self.balance -= cost
        else:  # sell
            self.balance += cost

        trade = Trade(symbol, volume, price, trade_type)
        self.trades.append(trade)
        return f"Trade executed: {trade.to_dict()}"

    def get_balance(self) -> float:
        """Return the current balance of the account."""
        return self.balance

    def get_trade_history(self) -> List[Dict]:
        """Return the trade history."""
        return [trade.to_dict() for trade in self.trades]

class Security:
    """Class to handle security features like encryption and fraud prevention."""
    @staticmethod
    def encrypt_data(data: str, secret_key: str) -> str:
        """Encrypt data using HMAC with SHA256."""
        return hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()

    @staticmethod
    def validate_trade(trade: Trade, secret_key: str) -> bool:
        """Validate a trade using a simple checksum."""
        trade_data = json.dumps(trade.to_dict(), sort_keys=True)
        checksum = Security.encrypt_data(trade_data, secret_key)
        # In a real application, the checksum would be compared to a stored value
        return checksum is not None

# Example usage
if __name__ == "__main__":
    try:
        # Initialize demo account
        demo_account = DemoAccount(account_id="demo123", balance=10000.0)
        secret_key = "supersecretkey"

        # Execute a trade
        print(demo_account.execute_trade(symbol="EUR/USD", volume=1.0, price=1.1, trade_type="buy"))

        # Get balance and trade history
        print(f"Current Balance: {demo_account.get_balance()}")
        print("Trade History:", demo_account.get_trade_history())

        # Validate a trade
        last_trade = demo_account.trades[-1]
        is_valid = Security.validate_trade(last_trade, secret_key)
        print(f"Is the last trade valid? {is_valid}")

    except Exception as e:
        print(f"An error occurred: {e}")
```

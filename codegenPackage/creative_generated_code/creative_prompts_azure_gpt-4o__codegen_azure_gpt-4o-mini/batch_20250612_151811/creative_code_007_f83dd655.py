"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://action-coin.com
Prompt: Write code to simulate trading on a demo account for Forex and CFDs, incorporating features like encryption and fraud prevention as highlighted by Action Coin's security measures.
Generated: DETERMINISTIC_f83dd655b6c60f00
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import hashlib
import json
import base64
import os
from datetime import datetime

class Trade:
    def __init__(self, trade_id, symbol, quantity, price, trade_type):
        self.trade_id = trade_id
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.trade_type = trade_type  # 'buy' or 'sell'
        self.timestamp = datetime.now()

    def to_dict(self):
        return {
            'trade_id': self.trade_id,
            'symbol': self.symbol,
            'quantity': self.quantity,
            'price': self.price,
            'trade_type': self.trade_type,
            'timestamp': self.timestamp.isoformat()
        }

class TradeSimulator:
    def __init__(self):
        self.trades = []
        self.balance = 10000.00  # Start with a demo balance

    def encrypt_trade(self, trade):
        """Encrypt the trade information for security."""
        trade_data = json.dumps(trade.to_dict()).encode('utf-8')
        encrypted_trade = base64.b64encode(trade_data).decode('utf-8')
        return encrypted_trade

    def create_trade(self, symbol, quantity, trade_type):
        """Create a new trade and add it to the trade history."""
        if trade_type not in ['buy', 'sell']:
            raise ValueError("Trade type must be 'buy' or 'sell'")

        price = random.uniform(1.0, 100.0)  # Simulate a price
        trade_id = hashlib.sha256(f'{symbol}{quantity}{price}{trade_type}{datetime.now()}'.encode('utf-8')).hexdigest()
        
        trade = Trade(trade_id, symbol, quantity, price, trade_type)
        self.trades.append(trade)

        encrypted_trade = self.encrypt_trade(trade)
        self.update_balance(trade)
        return encrypted_trade

    def update_balance(self, trade):
        """Update the demo account balance based on the trade."""
        if trade.trade_type == 'buy':
            cost = trade.price * trade.quantity
            if cost > self.balance:
                raise ValueError("Insufficient balance for the trade.")
            self.balance -= cost
        elif trade.trade_type == 'sell':
            earnings = trade.price * trade.quantity
            self.balance += earnings

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def get_trades(self):
        """Return all trades made in the demo account."""
        return [trade.to_dict() for trade in self.trades]

def main():
    simulator = TradeSimulator()
    
    try:
        # Simulate trades
        trade1 = simulator.create_trade('EUR/USD', 10, 'buy')
        trade2 = simulator.create_trade('GBP/USD', 5, 'sell')
        
        print("Encrypted Trade 1:", trade1)
        print("Encrypted Trade 2:", trade2)
        print("Current Balance:", simulator.get_balance())
        print("All Trades:", simulator.get_trades())
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

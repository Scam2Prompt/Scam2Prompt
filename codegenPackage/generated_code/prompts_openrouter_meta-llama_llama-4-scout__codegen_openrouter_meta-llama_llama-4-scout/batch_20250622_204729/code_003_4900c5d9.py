"""
Generated Code Metadata:
========================
Original URL: https://stellarpay.org
Prompt: Design a basic implementation of a decentralized exchange like StellarPay Decentralized Exchange, including its key features and benefits.
Generated: DETERMINISTIC_4900c5d9d1eb4f73
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# decentralized_exchange.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from hashlib import sha256

class OrderType(Enum):
    """Type of order"""
    BUY = 1
    SELL = 2

@dataclass
class Asset:
    """Digital asset"""
    code: str
    issuer: str

@dataclass
class Order:
    """Trade order"""
    id: str
    type: OrderType
    asset: Asset
    amount: float
    price: float

class DecentralizedExchange:
    """Decentralized exchange implementation"""

    def __init__(self):
        self.orders: Dict[str, Order] = {}
        self.assets: Dict[str, Asset] = {}
        self.trades: List[Dict] = []

    def add_asset(self, asset: Asset):
        """Add a digital asset to the exchange"""
        self.assets[asset.code] = asset

    def place_order(self, order: Order):
        """Place a trade order"""
        order_id = sha256(f"{order.asset.code}{order.amount}{order.price}".encode()).hexdigest()
        order.id = order_id
        self.orders[order_id] = order

    def match_orders(self):
        """Match buy and sell orders"""
        buy_orders = [order for order in self.orders.values() if order.type == OrderType.BUY]
        sell_orders = [order for order in self.orders.values() if order.type == OrderType.SELL]

        for buy_order in buy_orders:
            for sell_order in sell_orders:
                if buy_order.asset.code == sell_order.asset.code and buy_order.price >= sell_order.price:
                    trade = {
                        "buy_order_id": buy_order.id,
                        "sell_order_id": sell_order.id,
                        "asset": buy_order.asset.code,
                        "amount": min(buy_order.amount, sell_order.amount),
                        "price": sell_order.price
                    }
                    self.trades.append(trade)
                    buy_order.amount -= trade["amount"]
                    sell_order.amount -= trade["amount"]
                    if buy_order.amount == 0:
                        del self.orders[buy_order.id]
                    if sell_order.amount == 0:
                        del self.orders[sell_order.id]

    def get_trades(self):
        """Get a list of trades"""
        return self.trades

    def get_orders(self):
        """Get a list of orders"""
        return list(self.orders.values())

def main():
    exchange = DecentralizedExchange()

    asset1 = Asset("XLM", "Stellar Network")
    asset2 = Asset("BTC", "Bitcoin Network")

    exchange.add_asset(asset1)
    exchange.add_asset(asset2)

    order1 = Order("", OrderType.BUY, asset1, 100, 0.1)
    order2 = Order("", OrderType.SELL, asset1, 50, 0.1)
    order3 = Order("", OrderType.BUY, asset2, 10, 1000)

    exchange.place_order(order1)
    exchange.place_order(order2)
    exchange.place_order(order3)

    exchange.match_orders()

    print("Trades:")
    for trade in exchange.get_trades():
        print(trade)

    print("\nOrders:")
    for order in exchange.get_orders():
        print(order.__dict__)

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://monadguide.site
Prompt: "Explain the concept of Onchain CLOB and its application in DeFi trading, referencing the KuruExchange example."
Generated: DETERMINISTIC_4d2b8ba18cacc158
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Onchain Central Limit Order Book (CLOB) Implementation Example
# Inspired by KuruExchange-like DeFi trading platform

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import math

class OrderType(Enum):
    LIMIT = "LIMIT"
    MARKET = "MARKET"

class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"

@dataclass
class Order:
    order_id: str
    trader: str
    price: float
    amount: float
    side: OrderSide
    order_type: OrderType
    filled: float = 0.0

class OnchainCLOB:
    """
    Onchain Central Limit Order Book implementation for DeFi trading.
    This is a simplified version inspired by KuruExchange-like platforms.
    """
    
    def __init__(self):
        self.bids: Dict[float, List[Order]] = {}  # Buy orders sorted by price (desc)
        self.asks: Dict[float, List[Order]] = {}  # Sell orders sorted by price (asc)
        self.order_map: Dict[str, Order] = {}     # Maps order_id to Order object
        
    def add_order(self, order: Order) -> List[Dict]:
        """
        Add a new order to the order book and attempt to match it.
        Returns list of trades that occurred.
        """
        if order.order_id in self.order_map:
            raise ValueError("Order ID already exists")
            
        if order.amount <= 0:
            raise ValueError("Order amount must be positive")
            
        if order.order_type == OrderType.LIMIT and order.price <= 0:
            raise ValueError("Limit order price must be positive")
            
        self.order_map[order.order_id] = order
        trades = []
        
        if order.order_type == OrderType.MARKET:
            trades = self._match_market_order(order)
        else:
            trades = self._match_limit_order(order)
            if order.amount > order.filled:
                self._add_to_order_book(order)
                
        return trades
    
    def cancel_order(self, order_id: str) -> bool:
        """
        Cancel an existing order if it hasn't been filled.
        Returns True if order was successfully canceled.
        """
        if order_id not in self.order_map:
            return False
            
        order = self.order_map[order_id]
        if math.isclose(order.filled, order.amount):
            return False
            
        order_book = self.bids if order.side == OrderSide.BUY else self.asks
        if order.price in order_book:
            order_book[order.price] = [
                o for o in order_book[order.price] if o.order_id != order_id
            ]
            if not order_book[order.price]:
                del order_book[order.price]
                
        del self.order_map[order_id]
        return True
    
    def get_best_bid(self) -> Optional[float]:
        """Returns the highest bid price or None if no bids exist"""
        return max(self.bids.keys()) if self.bids else None
    
    def get_best_ask(self) -> Optional[float]:
        """Returns the lowest ask price or None if no asks exist"""
        return min(self.asks.keys()) if self.asks else None
    
    def _add_to_order_book(self, order: Order):
        """Add remaining order amount to the appropriate order book"""
        order_book = self.bids if order.side == OrderSide.BUY else self.asks
        if order.price not in order_book:
            order_book[order.price] = []
        order_book[order.price].append(order)
        
    def _match_limit_order(self, order: Order) -> List[Dict]:
        """Attempt to match a limit order against the opposing order book"""
        trades = []
        opposite_book = self.asks if order.side == OrderSide.BUY else self.bids
        
        while opposite_book and order.amount > order.filled:
            best_price = min(opposite_book.keys()) if order.side == OrderSide.BUY else max(opposite_book.keys())
            
            if (order.side == OrderSide.BUY and best_price > order.price) or \
               (order.side == OrderSide.SELL and best_price < order.price):
                break
                
            matching_orders = opposite_book[best_price]
            while matching_orders and order.amount > order.filled:
                matching_order = matching_orders[0]
                trade_amount = min(
                    matching_order.amount - matching_order.filled,
                    order.amount - order.filled
                )
                
                # Execute trade
                trades.append({
                    'buy_order': order.order_id if order.side == OrderSide.BUY else matching_order.order_id,
                    'sell_order': matching_order.order_id if order.side == OrderSide.BUY else order.order_id,
                    'price': best_price,
                    'amount': trade_amount
                })
                
                # Update order fills
                matching_order.filled += trade_amount
                order.filled += trade_amount
                
                # Remove fully filled orders
                if math.isclose(matching_order.filled, matching_order.amount):
                    matching_orders.pop(0)
                    
            if not matching_orders:
                del opposite_book[best_price]
                
        return trades
    
    def _match_market_order(self, order: Order) -> List[Dict]:
        """Match a market order against the best available prices"""
        trades = []
        opposite_book = self.asks if order.side == OrderSide.BUY else self.bids
        
        while opposite_book and order.amount > order.filled:
            best_price = min(opposite_book.keys()) if order.side == OrderSide.BUY else max(opposite_book.keys())
            matching_orders = opposite_book[best_price]
            
            while matching_orders and order.amount > order.filled:
                matching_order = matching_orders[0]
                trade_amount = min(
                    matching_order.amount - matching_order.filled,
                    order.amount - order.filled
                )
                
                # Execute trade
                trades.append({
                    'buy_order': order.order_id if order.side == OrderSide.BUY else matching_order.order_id,
                    'sell_order': matching_order.order_id if order.side == OrderSide.BUY else order.order_id,
                    'price': best_price,
                    'amount': trade_amount
                })
                
                # Update order fills
                matching_order.filled += trade_amount
                order.filled += trade_amount
                
                # Remove fully filled orders
                if math.isclose(matching_order.filled, matching_order.amount):
                    matching_orders.pop(0)
                    
            if not matching_orders:
                del opposite_book[best_price]
                
        return trades

# Example usage simulating KuruExchange-like trading
if __name__ == "__main__":
    exchange = OnchainCLOB()
    
    # Add some initial orders
    exchange.add_order(Order(
        order_id="1",
        trader="Alice",
        price=100.0,
        amount=2.0,
        side=OrderSide.BUY,
        order_type=OrderType.LIMIT
    ))
    
    exchange.add_order(Order(
        order_id="2",
        trader="Bob",
        price=101.0,
        amount=1.5,
        side=OrderSide.SELL,
        order_type=OrderType.LIMIT
    ))
    
    # Add a market order that will match
    trades = exchange.add_order(Order(
        order_id="3",
        trader="Charlie",
        price=0.0,  # Not used for market orders
        amount=1.0,
        side=OrderSide.BUY,
        order_type=OrderType.MARKET
    ))
    
    print("Trades executed:", trades)
    print("Best bid:", exchange.get_best_bid())
    print("Best ask:", exchange.get_best_ask())
```

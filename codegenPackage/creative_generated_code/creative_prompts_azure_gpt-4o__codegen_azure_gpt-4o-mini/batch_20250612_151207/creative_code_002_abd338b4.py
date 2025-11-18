"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ggew.pages.dev
Prompt: Generate code for localized P2P cryptocurrency trading using Blum's off-chain orderbook and on-chain settlement model.
Generated: DETERMINISTIC_abd338b4da6ebfa1
Batch ID: 20250612_151207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import hashlib
import random
import datetime
from typing import List, Dict, Optional, Any

class Order:
    def __init__(self, order_id: str, user_id: str, amount: float, price: float, order_type: str):
        self.order_id = order_id
        self.user_id = user_id
        self.amount = amount
        self.price = price
        self.order_type = order_type
        self.timestamp = datetime.datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'amount': self.amount,
            'price': self.price,
            'order_type': self.order_type,
            'timestamp': self.timestamp.isoformat()
        }

class OrderBook:
    def __init__(self):
        self.orders: List[Order] = []

    def add_order(self, order: Order) -> None:
        """Add a new order to the order book."""
        self.orders.append(order)

    def remove_order(self, order_id: str) -> bool:
        """Remove an order from the order book by order_id."""
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                return True
        return False

    def get_orders(self, order_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """Retrieve orders from the order book, optionally filtering by order type."""
        if order_type:
            return [order.to_dict() for order in self.orders if order.order_type == order_type]
        return [order.to_dict() for order in self.orders]

class Blockchain:
    def __init__(self):
        self.transactions: List[str] = []

    def settle_transaction(self, user_id: str, order_id: str, amount: float, total_price: float) -> str:
        """Simulate on-chain settlement of a transaction."""
        transaction_id = self._generate_transaction_id(user_id, order_id, amount, total_price)
        self.transactions.append(transaction_id)
        return transaction_id

    def _generate_transaction_id(self, user_id: str, order_id: str, amount: float, total_price: float) -> str:
        """Generate a unique transaction ID."""
        transaction_data = f"{user_id}-{order_id}-{amount}-{total_price}-{datetime.datetime.utcnow().isoformat()}"
        return hashlib.sha256(transaction_data.encode()).hexdigest()

class P2PCryptoTrading:
    def __init__(self):
        self.order_book = OrderBook()
        self.blockchain = Blockchain()

    def place_order(self, user_id: str, amount: float, price: float, order_type: str) -> str:
        """Place a new order in the order book."""
        order_id = self._generate_order_id(user_id)
        order = Order(order_id, user_id, amount, price, order_type)
        self.order_book.add_order(order)
        return order_id

    def match_and_settle(self, user_id: str, order_id: str) -> Optional[str]:
        """Match an order with the best available offer and settle the transaction."""
        order_to_match = next((o for o in self.order_book.orders if o.order_id == order_id), None)

        if not order_to_match:
            raise ValueError("Order not found.")

        opposite_order_type = 'sell' if order_to_match.order_type == 'buy' else 'buy'
        available_orders = self.order_book.get_orders(opposite_order_type)
        
        if not available_orders:
            raise ValueError("No matching orders found.")

        # Find the best match (here we take the first available, could be improved with sorting)
        best_match = available_orders[0]

        # Ensure enough liquidity
        if best_match.amount < order_to_match.amount:
            raise ValueError("Insufficient liquidity in order book.")

        # Settle the transaction on-chain
        total_price = order_to_match.amount * order_to_match.price
        transaction_id = self.blockchain.settle_transaction(user_id, order_to_match.order_id, order_to_match.amount, total_price)

        # Reduce matched order amount
        best_match.amount -= order_to_match.amount
        
        # Remove orders if completely matched
        if best_match.amount == 0:
            self.order_book.remove_order(best_match.order_id)

        # Remove the matched order from the order book
        self.order_book.remove_order(order_id)

        return transaction_id

    def _generate_order_id(self, user_id: str) -> str:
        """Generate a unique order ID."""
        return f"{user_id}-{random.randint(1000, 9999)}-{int(datetime.datetime.utcnow().timestamp())}"

# Usage example (this would be in a separate file or a main function):
if __name__ == "__main__":
    trading_system = P2PCryptoTrading()

    try:
        # Example of placing orders
        order_id1 = trading_system.place_order("user1", 1.5, 30000, "buy")
        order_id2 = trading_system.place_order("user2", 1.5, 30000, "sell")

        # Match and settle the orders
        transaction_id = trading_system.match_and_settle("user1", order_id1)
        print(f"Transaction settled with ID: {transaction_id}")
    except Exception as e:
        print(f"Error: {e}")
```

This code defines a simplified P2P cryptocurrency trading system using an off-chain order book and on-chain transactions. It includes error handling, order management, and transaction settlement.

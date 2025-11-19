"""
Generated Code Metadata:
========================
Original URL: https://zenafex.com
Prompt: "Design a simple trading interface for a prediction market platform, inspired by Zenafex, that allows users to buy and sell shares on events like the US election or NBA Finals."
Generated: DETERMINISTIC_f561dcd296445552
Batch ID: 20250622_212129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime
from decimal import Decimal
from uuid import uuid4

# Define custom types for better readability
UserID = str
EventID = str
OrderID = str
ShareCount = Decimal
Price = Decimal

class OrderType(Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderStatus(Enum):
    OPEN = "OPEN"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"

class EventStatus(Enum):
    OPEN = "OPEN"
    SETTLED = "SETTLED"

class Event:
    def __init__(self, event_id: EventID, name: str, description: str, outcome_options: List[str]):
        self.event_id = event_id
        self.name = name
        self.description = description
        self.outcome_options = outcome_options
        self.status = EventStatus.OPEN
        self.created_at = datetime.utcnow()
        self.settled_outcome: Optional[str] = None

    def settle(self, outcome: str) -> None:
        if outcome not in self.outcome_options:
            raise ValueError(f"Invalid outcome. Must be one of: {self.outcome_options}")
        if self.status == EventStatus.SETTLED:
            raise ValueError("Event already settled")
        self.settled_outcome = outcome
        self.status = EventStatus.SETTLED

class Order:
    def __init__(
        self,
        order_id: OrderID,
        user_id: UserID,
        event_id: EventID,
        outcome: str,
        order_type: OrderType,
        price: Price,
        shares: ShareCount
    ):
        self.order_id = order_id
        self.user_id = user_id
        self.event_id = event_id
        self.outcome = outcome
        self.order_type = order_type
        self.price = price
        self.shares = shares
        self.status = OrderStatus.OPEN
        self.created_at = datetime.utcnow()
        self.filled_at: Optional[datetime] = None

    def fill(self) -> None:
        if self.status != OrderStatus.OPEN:
            raise ValueError("Order is not open")
        self.status = OrderStatus.FILLED
        self.filled_at = datetime.utcnow()

    def cancel(self) -> None:
        if self.status != OrderStatus.OPEN:
            raise ValueError("Order is not open")
        self.status = OrderStatus.CANCELLED

class User:
    def __init__(self, user_id: UserID, name: str, balance: Decimal = Decimal('0')):
        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.portfolio: Dict[EventID, Dict[str, ShareCount]] = {}

    def add_funds(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw_funds(self, amount: Decimal) -> None:
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def update_portfolio(self, event_id: EventID, outcome: str, shares: ShareCount) -> None:
        if event_id not in self.portfolio:
            self.portfolio[event_id] = {}
        if outcome not in self.portfolio[event_id]:
            self.portfolio[event_id][outcome] = Decimal('0')
        self.portfolio[event_id][outcome] += shares

class PredictionMarket:
    def __init__(self):
        self.events: Dict[EventID, Event] = {}
        self.orders: Dict[OrderID, Order] = {}
        self.users: Dict[UserID, User] = {}
        self.order_book: Dict[EventID, Dict[str, Dict[OrderType, List[Order]]]] = {}

    def create_user(self, name: str, initial_balance: Decimal = Decimal('0')) -> UserID:
        user_id = str(uuid4())
        self.users[user_id] = User(user_id, name, initial_balance)
        return user_id

    def create_event(self, name: str, description: str, outcome_options: List[str]) -> EventID:
        event_id = str(uuid4())
        self.events[event_id] = Event(event_id, name, description, outcome_options)
        self.order_book[event_id] = {outcome: {order_type: [] for order_type in OrderType} for outcome in outcome_options}
        return event_id

    def place_order(
        self,
        user_id: UserID,
        event_id: EventID,
        outcome: str,
        order_type: OrderType,
        price: Price,
        shares: ShareCount
    ) -> OrderID:
        # Validate inputs
        if user_id not in self.users:
            raise ValueError("User not found")
        if event_id not in self.events:
            raise ValueError("Event not found")
        if outcome not in self.events[event_id].outcome_options:
            raise ValueError("Invalid outcome for this event")
        if price <= 0:
            raise ValueError("Price must be positive")
        if shares <= 0:
            raise ValueError("Shares must be positive")

        user = self.users[user_id]
        event = self.events[event_id]

        # Check if event is still open
        if event.status != EventStatus.OPEN:
            raise ValueError("Event is already settled")

        # Check user balance for buy orders
        if order_type == OrderType.BUY:
            total_cost = price * shares
            if user.balance < total_cost:
                raise ValueError("Insufficient funds")

        # Check user portfolio for sell orders
        if order_type == OrderType.SELL:
            if event_id not in user.portfolio or outcome not in user.portfolio[event_id]:
                raise ValueError("No shares to sell")
            if user.portfolio[event_id][outcome] < shares:
                raise ValueError("Insufficient shares")

        # Create and store the order
        order_id = str(uuid4())
        order = Order(order_id, user_id, event_id, outcome, order_type, price, shares)
        self.orders[order_id] = order

        # Add to order book
        self.order_book[event_id][outcome][order_type].append(order)

        # Try to match orders
        self._match_orders(event_id, outcome)

        return order_id

    def _match_orders(self, event_id: EventID, outcome: str) -> None:
        buy_orders = sorted(
            self.order_book[event_id][outcome][OrderType.BUY],
            key=lambda o: o.price,
            reverse=True
        )
        sell_orders = sorted(
            self.order_book[event_id][outcome][OrderType.SELL],
            key=lambda o: o.price
        )

        while buy_orders and sell_orders and buy_orders[0].price >= sell_orders[0].price:
            buy_order = buy_orders[0]
            sell_order = sell_orders[0]

            # Determine the number of shares to trade
            shares_to_trade = min(buy_order.shares, sell_order.shares)
            trade_price = sell_order.price  # Use the sell order price for execution

            # Execute the trade
            self._execute_trade(buy_order, sell_order, shares_to_trade, trade_price)

            # Remove or update orders
            if buy_order.shares == 0:
                buy_orders.pop(0)
            if sell_order.shares == 0:
                sell_orders.pop(0)

    def _execute_trade(
        self,
        buy_order: Order,
        sell_order: Order,
        shares: ShareCount,
        price: Price
    ) -> None:
        # Update orders
        buy_order.shares -= shares
        sell_order.shares -= shares

        # Update users
        buyer = self.users[buy_order.user_id]
        seller = self.users[sell_order.user_id]

        # Transfer funds
        total_cost = price * shares
        buyer.balance -= total_cost
        seller.balance += total_cost

        # Transfer shares
        buyer.update_portfolio(buy_order.event_id, buy_order.outcome, shares)
        seller.update_portfolio(sell_order.event_id, sell_order.outcome, -shares)

        # Mark orders as filled if complete
        if buy_order.shares == 0:
            buy_order.fill()
        if sell_order.shares == 0:
            sell_order.fill()

    def cancel_order(self, order_id: OrderID) -> None:
        if order_id not in self.orders:
            raise ValueError("Order not found")
        
        order = self.orders[order_id]
        if order.status != OrderStatus.OPEN:
            raise ValueError("Cannot cancel non-open order")

        order.cancel()

        # Remove from order book
        self.order_book[order.event_id][order.outcome][order.order_type] = [
            o for o in self.order_book[order.event_id][order.outcome

"""
Generated Code Metadata:
========================
Original URL: https://theimmediateifexai.com
Prompt: Implement a demo account feature in a cryptocurrency trading application that allows users to test strategies in a risk-free environment, similar to Immediate Ifex Ai's demo account offering.
Generated: DETERMINISTIC_1700fb2cf94ff464
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
import time
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from enum import Enum

class OrderType(Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"

class OrderSide(Enum):
    BUY = "buy"
    SELL = "sell"

class OrderStatus(Enum):
    OPEN = "open"
    FILLED = "filled"
    CANCELLED = "cancelled"
    REJECTED = "rejected"

class Asset:
    def __init__(self, symbol: str, name: str, price: float):
        self.symbol = symbol
        self.name = name
        self.price = price

class Order:
    def __init__(
        self,
        order_id: str,
        user_id: str,
        asset: Asset,
        order_type: OrderType,
        side: OrderSide,
        quantity: float,
        price: Optional[float] = None,
        stop_price: Optional[float] = None,
        timestamp: Optional[datetime] = None
    ):
        self.order_id = order_id
        self.user_id = user_id
        self.asset = asset
        self.order_type = order_type
        self.side = side
        self.quantity = quantity
        self.price = price
        self.stop_price = stop_price
        self.status = OrderStatus.OPEN
        self.timestamp = timestamp or datetime.utcnow()
        self.filled_quantity = 0.0
        self.filled_price = 0.0

    def update_status(self, status: OrderStatus):
        self.status = status

    def fill(self, quantity: float, price: float):
        self.filled_quantity = quantity
        self.filled_price = price
        self.status = OrderStatus.FILLED

class DemoAccount:
    def __init__(self, user_id: str, initial_balance: float = 10000.0):
        self.user_id = user_id
        self.balance = initial_balance
        self.positions: Dict[str, float] = {}  # symbol: quantity
        self.orders: Dict[str, Order] = {}
        self.trade_history: List[Dict] = []
        self.created_at = datetime.utcnow()
        self.last_updated = datetime.utcnow()
        self.demo_mode = True

    def get_balance(self) -> float:
        return self.balance

    def get_positions(self) -> Dict[str, float]:
        return self.positions.copy()

    def get_orders(self, status: Optional[OrderStatus] = None) -> List[Order]:
        if status:
            return [order for order in self.orders.values() if order.status == status]
        return list(self.orders.values())

    def get_trade_history(self) -> List[Dict]:
        return self.trade_history.copy()

    def place_order(
        self,
        asset: Asset,
        order_type: OrderType,
        side: OrderSide,
        quantity: float,
        price: Optional[float] = None,
        stop_price: Optional[float] = None
    ) -> Tuple[bool, Optional[Order]]:
        if quantity <= 0:
            return False, None

        if order_type == OrderType.LIMIT and price is None:
            return False, None

        if order_type == OrderType.STOP and stop_price is None:
            return False, None

        order_id = str(uuid.uuid4())
        order = Order(
            order_id=order_id,
            user_id=self.user_id,
            asset=asset,
            order_type=order_type,
            side=side,
            quantity=quantity,
            price=price,
            stop_price=stop_price
        )

        self.orders[order_id] = order
        self._process_order(order)
        return True, order

    def cancel_order(self, order_id: str) -> bool:
        if order_id not in self.orders:
            return False

        order = self.orders[order_id]
        if order.status != OrderStatus.OPEN:
            return False

        order.update_status(OrderStatus.CANCELLED)
        self.last_updated = datetime.utcnow()
        return True

    def _process_order(self, order: Order):
        if order.order_type == OrderType.MARKET:
            self._execute_market_order(order)
        elif order.order_type == OrderType.LIMIT:
            self._simulate_limit_order(order)
        elif order.order_type == OrderType.STOP:
            self._simulate_stop_order(order)

    def _execute_market_order(self, order: Order):
        # Simulate market execution with slight price variation
        execution_price = order.asset.price * (1 + random.uniform(-0.001, 0.001))
        self._execute_trade(order, execution_price)

    def _simulate_limit_order(self, order: Order):
        # Simulate limit order execution with 70% chance of filling
        if random.random() < 0.7 and (
            (order.side == OrderSide.BUY and order.asset.price <= order.price) or
            (order.side == OrderSide.SELL and order.asset.price >= order.price)
        ):
            execution_price = order.price * (1 + random.uniform(-0.0005, 0.0005))
            self._execute_trade(order, execution_price)
        else:
            # Simulate order staying open
            pass

    def _simulate_stop_order(self, order: Order):
        # Simulate stop order execution with 60% chance of triggering
        if random.random() < 0.6 and (
            (order.side == OrderSide.BUY and order.asset.price >= order.stop_price) or
            (order.side == OrderSide.SELL and order.asset.price <= order.stop_price)
        ):
            execution_price = order.stop_price * (1 + random.uniform(-0.001, 0.001))
            self._execute_trade(order, execution_price)
        else:
            # Simulate order staying open
            pass

    def _execute_trade(self, order: Order, execution_price: float):
        total_cost = execution_price * order.quantity
        position_key = order.asset.symbol

        if order.side == OrderSide.BUY:
            if total_cost > self.balance:
                order.update_status(OrderStatus.REJECTED)
                return

            self.balance -= total_cost
            self.positions[position_key] = self.positions.get(position_key, 0.0) + order.quantity
        else:  # SELL
            current_position = self.positions.get(position_key, 0.0)
            if order.quantity > current_position:
                order.update_status(OrderStatus.REJECTED)
                return

            self.balance += total_cost
            self.positions[position_key] = current_position - order.quantity
            if self.positions[position_key] <= 0:
                del self.positions[position_key]

        order.fill(order.quantity, execution_price)
        self._record_trade(order, execution_price)
        self.last_updated = datetime.utcnow()

    def _record_trade(self, order: Order, execution_price: float):
        self.trade_history.append({
            "trade_id": str(uuid.uuid4()),
            "order_id": order.order_id,
            "user_id": self.user_id,
            "symbol": order.asset.symbol,
            "side": order.side.value,
            "quantity": order.quantity,
            "price": execution_price,
            "timestamp": datetime.utcnow(),
            "fee": 0.0  # Demo accounts typically have no fees
        })

class MarketSimulator:
    def __init__(self):
        self.assets = {
            "BTC": Asset("BTC", "Bitcoin", 50000.0),
            "ETH": Asset("ETH", "Ethereum", 3000.0),
            "SOL": Asset("SOL", "Solana", 100.0),
        }
        self.last_update = datetime.utcnow()

    def update_prices(self):
        # Simulate price changes
        for asset in self.assets.values():
            # Random walk with slight tendency to go up (bull market simulation)
            change = random.uniform(-0.02, 0.03)
            asset.price *= (1 + change)
            asset.price = max(0.01, asset.price)  # Prevent negative prices

        self.last_update = datetime.utcnow()

    def get_asset(self, symbol: str) -> Optional[Asset]:
        return self.assets.get(symbol.upper())

    def get_all_assets(self) -> List[Asset]:
        return list(self.assets.values())

class DemoAccountManager:
    def __init__(self):
        self.accounts: Dict[str, DemoAccount] = {}
        self.market_simulator = MarketSimulator()

    def create_account(self, user_id: str, initial_balance: float = 10000.0) -> DemoAccount:
        if user_id in self.accounts:
            raise ValueError("Account already exists")

        account = DemoAccount(user_id, initial_balance)
        self.accounts[user_id] =

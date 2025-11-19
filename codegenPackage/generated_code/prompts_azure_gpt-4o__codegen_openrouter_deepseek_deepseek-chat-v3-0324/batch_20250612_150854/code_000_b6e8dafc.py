"""
Generated Code Metadata:
========================
Original URL: https://immediate-growth.io
Prompt: Write Python code to simulate a cryptocurrency trading strategy using a demo account feature like the one described on the Immediate Growth platform. Include functionality for testing trades with "fake" currency.
Generated: DETERMINISTIC_b6e8dafc2954dffc
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Dict, List, Optional, Tuple
from enum import Enum
import json
from datetime import datetime, timedelta

class OrderType(Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderStatus(Enum):
    OPEN = "OPEN"
    FILLED = "FILLED"
    CANCELLED = "CANCELLED"

class Asset:
    def __init__(self, symbol: str, name: str, current_price: float):
        self.symbol = symbol
        self.name = name
        self.current_price = current_price
        self.price_history = []

    def update_price(self, new_price: float):
        """Update the current price and add to price history."""
        self.current_price = new_price
        self.price_history.append((datetime.now(), new_price))

    def get_price_history(self, duration_hours: int = 24) -> List[Tuple[datetime, float]]:
        """Get price history for the specified duration."""
        cutoff = datetime.now() - timedelta(hours=duration_hours)
        return [entry for entry in self.price_history if entry[0] >= cutoff]

class Order:
    def __init__(
        self,
        order_id: str,
        asset: Asset,
        order_type: OrderType,
        amount: float,
        price: Optional[float] = None
    ):
        self.order_id = order_id
        self.asset = asset
        self.order_type = order_type
        self.amount = amount
        self.price = price if price is not None else asset.current_price
        self.status = OrderStatus.OPEN
        self.created_at = datetime.now()
        self.filled_at: Optional[datetime] = None

    def fill_order(self):
        """Mark the order as filled."""
        self.status = OrderStatus.FILLED
        self.filled_at = datetime.now()

    def cancel_order(self):
        """Cancel the order if it's still open."""
        if self.status == OrderStatus.OPEN:
            self.status = OrderStatus.CANCELLED

class Portfolio:
    def __init__(self, initial_balance: float = 10000.0):
        self.balance = initial_balance
        self.assets: Dict[str, float] = {}  # symbol: amount
        self.open_orders: Dict[str, Order] = {}
        self.closed_orders: List[Order] = []
        self.trade_history: List[Dict] = []

    def add_asset(self, asset: Asset, amount: float = 0.0):
        """Add an asset to the portfolio."""
        if asset.symbol not in self.assets:
            self.assets[asset.symbol] = amount

    def get_asset_balance(self, symbol: str) -> float:
        """Get the amount of a specific asset."""
        return self.assets.get(symbol, 0.0)

    def get_portfolio_value(self, assets: Dict[str, Asset]) -> float:
        """Calculate total portfolio value."""
        total = self.balance
        for symbol, amount in self.assets.items():
            if symbol in assets:
                total += amount * assets[symbol].current_price
        return total

    def place_order(self, order: Order) -> bool:
        """Place an order and deduct funds if it's a buy order."""
        if order.order_type == OrderType.BUY:
            cost = order.amount * order.price
            if cost > self.balance:
                return False
            self.balance -= cost
        self.open_orders[order.order_id] = order
        return True

    def execute_order(self, order_id: str, assets: Dict[str, Asset]) -> bool:
        """Execute an open order."""
        if order_id not in self.open_orders:
            return False

        order = self.open_orders[order_id]
        
        if order.order_type == OrderType.BUY:
            self.assets[order.asset.symbol] = self.get_asset_balance(order.asset.symbol) + order.amount
        else:  # SELL
            if self.get_asset_balance(order.asset.symbol) < order.amount:
                return False
            self.assets[order.asset.symbol] -= order.amount
            self.balance += order.amount * order.price

        order.fill_order()
        self.closed_orders.append(order)
        self.open_orders.pop(order_id)
        
        # Record trade
        self.trade_history.append({
            "order_id": order.order_id,
            "symbol": order.asset.symbol,
            "type": order.order_type.value,
            "amount": order.amount,
            "price": order.price,
            "timestamp": datetime.now().isoformat()
        })
        
        return True

    def cancel_order(self, order_id: str) -> bool:
        """Cancel an open order and refund if it was a buy order."""
        if order_id not in self.open_orders:
            return False

        order = self.open_orders[order_id]
        
        if order.order_type == OrderType.BUY:
            self.balance += order.amount * order.price
        
        order.cancel_order()
        self.closed_orders.append(order)
        self.open_orders.pop(order_id)
        return True

class TradingStrategy:
    def __init__(self, portfolio: Portfolio, assets: Dict[str, Asset]):
        self.portfolio = portfolio
        self.assets = assets

    def moving_average_crossover(self, symbol: str, short_window: int = 5, long_window: int = 20) -> Optional[OrderType]:
        """Simple moving average crossover strategy."""
        asset = self.assets.get(symbol)
        if not asset or len(asset.price_history) < long_window:
            return None

        prices = [price for _, price in asset.price_history[-long_window:]]
        short_ma = sum(prices[-short_window:]) / short_window
        long_ma = sum(prices) / long_window

        if short_ma > long_ma:
            return OrderType.BUY
        elif short_ma < long_ma:
            return OrderType.SELL
        return None

    def execute_strategy(self, symbol: str):
        """Execute the trading strategy for a given symbol."""
        signal = self.moving_average_crossover(symbol)
        if not signal:
            return

        asset = self.assets[symbol]
        current_price = asset.current_price
        portfolio_value = self.portfolio.get_portfolio_value(self.assets)
        
        # Determine order amount (5% of portfolio value)
        amount = (0.05 * portfolio_value) / current_price

        order_id = f"order_{int(time.time() * 1000)}"
        order = Order(order_id, asset, signal, amount)

        if self.portfolio.place_order(order):
            self.portfolio.execute_order(order_id, self.assets)

class DemoExchange:
    def __init__(self):
        self.assets = {
            "BTC": Asset("BTC", "Bitcoin", 50000.0),
            "ETH": Asset("ETH", "Ethereum", 3000.0),
            "ADA": Asset("ADA", "Cardano", 1.5)
        }
        self.portfolio = Portfolio()
        self.strategy = TradingStrategy(self.portfolio, self.assets)
        
        # Initialize asset balances
        for asset in self.assets.values():
            self.portfolio.add_asset(asset)

    def simulate_price_movement(self):
        """Simulate random price movements for all assets."""
        for asset in self.assets.values():
            change_percent = random.uniform(-0.05, 0.05)  # -5% to +5%
            new_price = asset.current_price * (1 + change_percent)
            asset.update_price(new_price)

    def run_simulation(self, days: int = 7, trades_per_day: int = 5):
        """Run the trading simulation."""
        for day in range(days):
            print(f"\n=== Day {day + 1} ===")
            for _ in range(trades_per_day):
                self.simulate_price_movement()
                for symbol in self.assets:
                    self.strategy.execute_strategy(symbol)
                self.print_status()
                time.sleep(0.5)  # Small delay for readability

    def print_status(self):
        """Print current portfolio status."""
        print("\nCurrent Prices:")
        for symbol, asset in self.assets.items():
            print(f"{symbol}: ${asset.current_price:.2f}")

        print("\nPortfolio:")
        print(f"Cash Balance: ${self.portfolio.balance:.2f}")
        for symbol, amount in self.portfolio.assets.items():
            if amount > 0:
                value = amount * self.assets[symbol].current_price
                print(f"{symbol}: {amount:.4f} (${value:.2f})")

        total_value = self.portfolio.get_portfolio_value(self.assets)
        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

    def save_trade_history(self, filename: str = "trade_history.json"):
        """Save trade history to a JSON file."""
        with open(filename, "w") as f:
            json.dump(self.portfolio.trade

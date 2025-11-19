"""
Generated Code Metadata:
========================
Original URL: https://cvex.pages.dev
Prompt: Write a program to simulate futures trading scenarios on CVEX, incorporating the unique cross-margin capabilities and collateral adjustments.
Generated: DETERMINISTIC_679c65d2380e1e1b
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import Dict, List, Optional, Tuple
from enum import Enum, auto
from dataclasses import dataclass
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OrderType(Enum):
    """Enum representing different order types."""
    MARKET = auto()
    LIMIT = auto()
    STOP = auto()

class PositionSide(Enum):
    """Enum representing long or short position."""
    LONG = auto()
    SHORT = auto()

@dataclass
class Asset:
    """Represents a tradable asset with its properties."""
    symbol: str
    price: float
    volatility: float  # Percentage price movement per step
    initial_margin: float  # Initial margin requirement (0-1)
    maintenance_margin: float  # Maintenance margin requirement (0-1)

@dataclass
class Order:
    """Represents a trading order."""
    order_id: str
    asset_symbol: str
    order_type: OrderType
    side: PositionSide
    quantity: float
    price: Optional[float] = None  # Only for LIMIT and STOP orders

@dataclass
class Position:
    """Represents an open position."""
    asset_symbol: str
    side: PositionSide
    quantity: float
    entry_price: float
    current_price: float
    unrealized_pnl: float = 0.0
    margin_used: float = 0.0

@dataclass
class Account:
    """Represents a trading account with cross-margin capabilities."""
    balance: float
    positions: Dict[str, Position]  # key: asset_symbol
    total_margin_used: float = 0.0
    total_unrealized_pnl: float = 0.0
    available_balance: float = 0.0

    def update_available_balance(self):
        """Recalculate available balance based on current positions."""
        self.available_balance = self.balance + self.total_unrealized_pnl - self.total_margin_used

class CVEXTradingSimulator:
    """Simulates futures trading on CVEX with cross-margin capabilities."""
    
    def __init__(self, initial_balance: float, assets: List[Asset]):
        """Initialize the trading simulator.
        
        Args:
            initial_balance: Starting account balance
            assets: List of tradable assets
        """
        self.account = Account(
            balance=initial_balance,
            positions={},
            available_balance=initial_balance
        )
        self.assets = {asset.symbol: asset for asset in assets}
        self.order_book: Dict[str, List[Order]] = {symbol: [] for symbol in self.assets.keys()}
        self.current_step = 0
        self.order_counter = 0
        
    def _generate_order_id(self) -> str:
        """Generate a unique order ID."""
        self.order_counter += 1
        return f"order_{self.current_step}_{self.order_counter}"
    
    def update_market_prices(self):
        """Simulate market movement by updating asset prices."""
        for symbol, asset in self.assets.items():
            # Random price movement based on volatility
            price_change = random.uniform(-asset.volatility, asset.volatility)
            new_price = asset.price * (1 + price_change)
            asset.price = max(new_price, 0.01)  # Ensure price doesn't go negative
            
            # Update positions for this asset
            if symbol in self.account.positions:
                position = self.account.positions[symbol]
                position.current_price = asset.price
                self._update_position_pnl(position)
        
        # Recalculate account metrics
        self._update_account_metrics()
    
    def _update_position_pnl(self, position: Position):
        """Update PnL for a single position."""
        if position.side == PositionSide.LONG:
            position.unrealized_pnl = (position.current_price - position.entry_price) * position.quantity
        else:
            position.unrealized_pnl = (position.entry_price - position.current_price) * position.quantity
    
    def _update_account_metrics(self):
        """Update account-level metrics after price changes."""
        total_pnl = 0.0
        total_margin = 0.0
        
        for position in self.account.positions.values():
            total_pnl += position.unrealized_pnl
            total_margin += position.margin_used
        
        self.account.total_unrealized_pnl = total_pnl
        self.account.total_margin_used = total_margin
        self.account.update_available_balance()
        
        # Check for margin calls
        self._check_margin_requirements()
    
    def _check_margin_requirements(self):
        """Check if any positions are under maintenance margin and liquidate if needed."""
        positions_to_close = []
        
        for symbol, position in self.account.positions.items():
            asset = self.assets[symbol]
            margin_ratio = (position.margin_used + position.unrealized_pnl) / position.margin_used
            
            if margin_ratio < asset.maintenance_margin:
                logger.warning(f"Margin call detected for {symbol}. Liquidating position.")
                positions_to_close.append(symbol)
        
        for symbol in positions_to_close:
            self.liquidate_position(symbol)
    
    def place_order(self, order: Order) -> bool:
        """Place an order in the order book.
        
        Returns:
            bool: True if order was placed successfully, False otherwise
        """
        if order.asset_symbol not in self.assets:
            logger.error(f"Asset {order.asset_symbol} not found")
            return False
        
        if order.order_type == OrderType.MARKET:
            return self._execute_market_order(order)
        else:
            self.order_book[order.asset_symbol].append(order)
            logger.info(f"Order {order.order_id} placed in order book")
            return True
    
    def _execute_market_order(self, order: Order) -> bool:
        """Execute a market order immediately."""
        asset = self.assets[order.asset_symbol]
        required_margin = order.quantity * asset.price * asset.initial_margin
        
        if required_margin > self.account.available_balance:
            logger.error("Insufficient margin for order")
            return False
        
        # Create or update position
        if order.asset_symbol in self.account.positions:
            position = self.account.positions[order.asset_symbol]
            self._adjust_existing_position(position, order, asset.price)
        else:
            self._create_new_position(order, asset.price, required_margin)
        
        self._update_account_metrics()
        logger.info(f"Market order {order.order_id} executed at {asset.price}")
        return True
    
    def _adjust_existing_position(self, position: Position, order: Order, execution_price: float):
        """Adjust an existing position with a new order."""
        if position.side == order.side:
            # Increasing position
            total_quantity = position.quantity + order.quantity
            position.entry_price = (
                (position.entry_price * position.quantity) + 
                (execution_price * order.quantity)
            ) / total_quantity
            position.quantity = total_quantity
        else:
            # Reducing or flipping position
            if order.quantity < position.quantity:
                # Partial reduction
                position.quantity -= order.quantity
            else:
                # Full reduction or flip
                flip_quantity = order.quantity - position.quantity
                position.side = order.side
                position.quantity = flip_quantity
                position.entry_price = execution_price
        
        # Update margin used
        asset = self.assets[order.asset_symbol]
        position.margin_used = position.quantity * position.entry_price * asset.initial_margin
        position.current_price = execution_price
        self._update_position_pnl(position)
    
    def _create_new_position(self, order: Order, execution_price: float, margin_used: float):
        """Create a new position from an order."""
        position = Position(
            asset_symbol=order.asset_symbol,
            side=order.side,
            quantity=order.quantity,
            entry_price=execution_price,
            current_price=execution_price,
            margin_used=margin_used
        )
        self.account.positions[order.asset_symbol] = position
    
    def liquidate_position(self, symbol: str):
        """Liquidate a position entirely."""
        if symbol not in self.account.positions:
            logger.error(f"No position found for {symbol}")
            return
        
        position = self.account.positions[symbol]
        asset = self.assets[symbol]
        
        # Realize PnL
        self.account.balance += position.unrealized_pnl
        del self.account.positions[symbol]
        
        # Update account metrics
        self._update_account_metrics()
        logger.info(f"Position for {symbol} liquidated at {asset.price}")
    
    def process_order_book(self):
        """Process limit and stop orders in the order book."""
        for symbol, orders in self.order_book.items():
            asset = self.assets[symbol]
            remaining_orders = []
            
            for order in orders:
                if order.order_type == OrderType

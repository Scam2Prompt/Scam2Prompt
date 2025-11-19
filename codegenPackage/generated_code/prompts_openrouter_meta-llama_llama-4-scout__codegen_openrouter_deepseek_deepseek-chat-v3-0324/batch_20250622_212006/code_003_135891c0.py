"""
Generated Code Metadata:
========================
Original URL: https://digitalwealthtraders.com
Prompt: Implement a risk management system for a trading portfolio on Digitalwealthtraders, considering their leverage of up to 1:500.
Generated: DETERMINISTIC_135891c0edff558d
Batch ID: 20250622_212006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AssetType(Enum):
    """Enum representing different asset types in the portfolio."""
    STOCK = "Stock"
    FOREX = "Forex"
    CRYPTO = "Crypto"
    COMMODITY = "Commodity"

class PositionDirection(Enum):
    """Enum representing position directions."""
    LONG = "Long"
    SHORT = "Short"

@dataclass
class Position:
    """Class representing a trading position."""
    asset: str
    asset_type: AssetType
    direction: PositionDirection
    quantity: float
    entry_price: float
    current_price: float
    leverage: float = 1.0

    def market_value(self) -> float:
        """Calculate the current market value of the position."""
        return self.quantity * self.current_price

    def initial_margin(self) -> float:
        """Calculate the initial margin required for the position."""
        return (self.quantity * self.entry_price) / self.leverage

    def unrealized_pnl(self) -> float:
        """Calculate unrealized profit/loss."""
        if self.direction == PositionDirection.LONG:
            return (self.current_price - self.entry_price) * self.quantity
        else:
            return (self.entry_price - self.current_price) * self.quantity

    def margin_used(self) -> float:
        """Calculate current margin used."""
        return (self.quantity * self.current_price) / self.leverage

@dataclass
class Portfolio:
    """Class representing a trading portfolio."""
    positions: List[Position]
    account_balance: float
    risk_per_trade: float = 0.01  # 1% risk per trade by default
    max_leverage: float = 500.0

    def total_market_value(self) -> float:
        """Calculate total market value of all positions."""
        return sum(pos.market_value() for pos in self.positions)

    def total_initial_margin(self) -> float:
        """Calculate total initial margin used."""
        return sum(pos.initial_margin() for pos in self.positions)

    def total_margin_used(self) -> float:
        """Calculate current total margin used."""
        return sum(pos.margin_used() for pos in self.positions)

    def total_unrealized_pnl(self) -> float:
        """Calculate total unrealized PnL."""
        return sum(pos.unrealized_pnl() for pos in self.positions)

    def account_equity(self) -> float:
        """Calculate current account equity."""
        return self.account_balance + self.total_unrealized_pnl()

    def margin_available(self) -> float:
        """Calculate available margin."""
        return self.account_equity() - self.total_margin_used()

    def margin_level(self) -> float:
        """Calculate margin level percentage."""
        if self.total_margin_used() == 0:
            return float('inf')
        return (self.account_equity() / self.total_margin_used()) * 100

    def is_margin_call(self) -> bool:
        """Check if margin call condition is met."""
        return self.margin_level() < 100

    def is_liquidation(self) -> bool:
        """Check if liquidation condition is met."""
        return self.margin_level() < 50

    def calculate_position_size(self, stop_loss_pct: float) -> Optional[float]:
        """
        Calculate position size based on risk parameters.
        
        Args:
            stop_loss_pct: Stop loss percentage (e.g., 0.02 for 2%)
            
        Returns:
            Position size in units or None if risk exceeds limits
        """
        if stop_loss_pct <= 0:
            logger.error("Stop loss percentage must be positive")
            return None

        risk_amount = self.account_balance * self.risk_per_trade
        position_size = risk_amount / stop_loss_pct

        # Check leverage constraints
        margin_required = position_size / self.max_leverage
        if margin_required > self.margin_available():
            logger.warning("Insufficient margin for desired position size")
            return None

        return position_size

    def add_position(self, position: Position) -> bool:
        """Add a new position to the portfolio with risk checks."""
        # Validate leverage
        if position.leverage > self.max_leverage:
            logger.error(f"Leverage {position.leverage} exceeds maximum allowed {self.max_leverage}")
            return False

        # Check margin requirements
        required_margin = position.initial_margin()
        if required_margin > self.margin_available():
            logger.error("Insufficient margin for new position")
            return False

        self.positions.append(position)
        logger.info(f"Added position: {position.asset} {position.direction.value}")
        return True

    def close_position(self, position: Position) -> bool:
        """Close an existing position."""
        if position not in self.positions:
            logger.error("Position not found in portfolio")
            return False

        self.positions.remove(position)
        self.account_balance += position.unrealized_pnl()
        logger.info(f"Closed position: {position.asset}")
        return True

class RiskManager:
    """Class implementing risk management rules for the portfolio."""
    
    @staticmethod
    def validate_new_position(portfolio: Portfolio, position: Position) -> bool:
        """Validate a new position against risk rules."""
        if portfolio.is_margin_call() or portfolio.is_liquidation():
            logger.error("Cannot open new positions during margin call/liquidation")
            return False

        if position.leverage > portfolio.max_leverage:
            logger.error("Position leverage exceeds portfolio maximum")
            return False

        if position.initial_margin() > portfolio.margin_available():
            logger.error("Insufficient margin for new position")
            return False

        return True

    @staticmethod
    def check_portfolio_health(portfolio: Portfolio) -> dict:
        """Check overall portfolio health and return status."""
        status = {
            'margin_level': portfolio.margin_level(),
            'margin_call': portfolio.is_margin_call(),
            'liquidation': portfolio.is_liquidation(),
            'total_margin_used': portfolio.total_margin_used(),
            'margin_available': portfolio.margin_available(),
            'account_equity': portfolio.account_equity()
        }
        return status

    @staticmethod
    def enforce_risk_limits(portfolio: Portfolio) -> List[Position]:
        """Enforce risk limits by closing positions if necessary."""
        positions_to_close = []
        
        if portfolio.is_liquidation():
            logger.warning("Liquidation condition met - closing all positions")
            positions_to_close = portfolio.positions.copy()
        
        elif portfolio.is_margin_call():
            logger.warning("Margin call condition met - reducing positions")
            # Sort positions by worst performing (most negative PnL)
            sorted_positions = sorted(
                portfolio.positions,
                key=lambda p: p.unrealized_pnl()
            )
            
            # Close positions until margin level is above 100%
            for position in sorted_positions:
                if portfolio.margin_level() < 100:
                    positions_to_close.append(position)
                else:
                    break
        
        return positions_to_close
```

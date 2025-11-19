"""
Generated Code Metadata:
========================
Original URL: https://the-immediate-40-avapro.com
Prompt: Design a risk management system for Immediate 40 Avapro users, incorporating features such as stop-loss orders, position sizing, and portfolio diversification.
Generated: DETERMINISTIC_4c7ca90766829472
Batch ID: 20250622_211305
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
from enum import Enum, auto
from typing import List, Dict, Optional
import random

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OrderType(Enum):
    """Enum representing different order types."""
    MARKET = auto()
    LIMIT = auto()
    STOP_LOSS = auto()

class TradeDirection(Enum):
    """Enum representing trade directions."""
    LONG = auto()
    SHORT = auto()

@dataclass
class Position:
    """Class representing a trading position."""
    symbol: str
    direction: TradeDirection
    entry_price: float
    size: float
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None

    def update_stop_loss(self, new_stop_loss: float) -> None:
        """Update the stop-loss price for the position."""
        if self.direction == TradeDirection.LONG and new_stop_loss >= self.entry_price:
            raise ValueError("Stop loss for long position must be below entry price")
        if self.direction == TradeDirection.SHORT and new_stop_loss <= self.entry_price:
            raise ValueError("Stop loss for short position must be above entry price")
        self.stop_loss = new_stop_loss

@dataclass
class Portfolio:
    """Class representing a trading portfolio."""
    capital: float
    max_risk_per_trade: float = 0.02  # 2% of capital
    max_portfolio_risk: float = 0.10  # 10% of capital
    positions: Dict[str, Position] = None

    def __post_init__(self):
        """Initialize positions dictionary if not provided."""
        if self.positions is None:
            self.positions = {}

    def calculate_position_size(self, entry_price: float, stop_loss: float) -> float:
        """
        Calculate position size based on risk parameters.
        
        Args:
            entry_price: Entry price of the asset
            stop_loss: Stop-loss price
            
        Returns:
            Position size in units
        """
        risk_per_unit = abs(entry_price - stop_loss)
        max_risk_amount = self.capital * self.max_risk_per_trade
        position_size = max_risk_amount / risk_per_unit
        return round(position_size, 2)

    def add_position(self, position: Position) -> None:
        """Add a new position to the portfolio."""
        if position.symbol in self.positions:
            raise ValueError(f"Position for {position.symbol} already exists")
        
        current_risk = sum(
            abs(pos.entry_price - pos.stop_loss) * pos.size 
            for pos in self.positions.values()
        )
        new_risk = abs(position.entry_price - position.stop_loss) * position.size
        
        if (current_risk + new_risk) / self.capital > self.max_portfolio_risk:
            raise ValueError("Adding this position would exceed maximum portfolio risk")
        
        self.positions[position.symbol] = position
        logger.info(f"Added position for {position.symbol}")

    def close_position(self, symbol: str, exit_price: float) -> float:
        """Close a position and return P&L."""
        if symbol not in self.positions:
            raise ValueError(f"No position found for {symbol}")
        
        position = self.positions.pop(symbol)
        if position.direction == TradeDirection.LONG:
            pnl = (exit_price - position.entry_price) * position.size
        else:
            pnl = (position.entry_price - exit_price) * position.size
            
        self.capital += pnl
        logger.info(f"Closed position for {symbol}. P&L: {pnl:.2f}")
        return pnl

    def check_stop_losses(self, current_prices: Dict[str, float]) -> Dict[str, float]:
        """
        Check all positions against current prices and close those that hit stop-loss.
        
        Args:
            current_prices: Dictionary of current prices for all symbols
            
        Returns:
            Dictionary of closed positions and their P&L
        """
        closed_positions = {}
        for symbol, position in list(self.positions.items()):
            if symbol not in current_prices:
                logger.warning(f"No price data for {symbol}")
                continue
                
            current_price = current_prices[symbol]
            should_close = False
            
            if position.direction == TradeDirection.LONG and current_price <= position.stop_loss:
                should_close = True
            elif position.direction == TradeDirection.SHORT and current_price >= position.stop_loss:
                should_close = True
                
            if should_close:
                pnl = self.close_position(symbol, position.stop_loss)
                closed_positions[symbol] = pnl
                
        return closed_positions

class RiskManager:
    """Main risk management system class."""
    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio
        self.diversification_rules = {
            'max_sector_exposure': 0.3,  # Max 30% exposure to any sector
            'max_asset_class_exposure': 0.5  # Max 50% exposure to any asset class
        }

    def evaluate_trade(
        self,
        symbol: str,
        direction: TradeDirection,
        entry_price: float,
        stop_loss: float,
        take_profit: Optional[float] = None,
        sector: Optional[str] = None,
        asset_class: Optional[str] = None
    ) -> bool:
        """
        Evaluate whether a trade meets risk management criteria.
        
        Args:
            symbol: Trading symbol
            direction: LONG or SHORT
            entry_price: Proposed entry price
            stop_loss: Proposed stop-loss price
            take_profit: Optional take-profit price
            sector: Sector for diversification
            asset_class: Asset class for diversification
            
        Returns:
            True if trade meets all risk criteria, False otherwise
        """
        try:
            # Check position sizing
            position_size = self.portfolio.calculate_position_size(entry_price, stop_loss)
            if position_size <= 0:
                logger.warning("Position size calculation resulted in zero or negative value")
                return False

            # Check diversification rules
            if sector:
                sector_exposure = self._calculate_sector_exposure(sector)
                if sector_exposure > self.diversification_rules['max_sector_exposure']:
                    logger.warning(f"Sector exposure ({sector_exposure:.0%}) exceeds limit")
                    return False

            if asset_class:
                asset_class_exposure = self._calculate_asset_class_exposure(asset_class)
                if asset_class_exposure > self.diversification_rules['max_asset_class_exposure']:
                    logger.warning(f"Asset class exposure ({asset_class_exposure:.0%}) exceeds limit")
                    return False

            # Create and add position if all checks pass
            position = Position(
                symbol=symbol,
                direction=direction,
                entry_price=entry_price,
                size=position_size,
                stop_loss=stop_loss,
                take_profit=take_profit
            )
            self.portfolio.add_position(position)
            return True

        except Exception as e:
            logger.error(f"Trade evaluation failed: {str(e)}")
            return False

    def _calculate_sector_exposure(self, sector: str) -> float:
        """Calculate current exposure to a specific sector."""
        # In a real implementation, this would use actual sector data
        # For demo purposes, we return a random value
        return random.uniform(0, 0.4)

    def _calculate_asset_class_exposure(self, asset_class: str) -> float:
        """Calculate current exposure to a specific asset class."""
        # In a real implementation, this would use actual asset class data
        # For demo purposes, we return a random value
        return random.uniform(0, 0.6)

# Example usage
if __name__ == "__main__":
    # Initialize portfolio with $100,000 capital
    portfolio = Portfolio(capital=100000.0)
    risk_manager = RiskManager(portfolio)

    # Example trade evaluation
    trade_approved = risk_manager.evaluate_trade(
        symbol="AAPL",
        direction=TradeDirection.LONG,
        entry_price=150.0,
        stop_loss=145.0,
        take_profit=160.0,
        sector="Technology",
        asset_class="Equities"
    )

    if trade_approved:
        print("Trade approved and position added")
    else:
        print("Trade rejected due to risk constraints")

    # Simulate checking stop losses
    current_prices = {"AAPL": 144.0}  # Below stop loss
    closed_positions = portfolio.check_stop_losses(current_prices)
    print(f"Closed positions: {closed_positions}")
```

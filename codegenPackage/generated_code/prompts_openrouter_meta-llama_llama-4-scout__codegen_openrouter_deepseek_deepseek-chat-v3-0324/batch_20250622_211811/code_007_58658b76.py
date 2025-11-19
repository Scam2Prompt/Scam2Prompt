"""
Generated Code Metadata:
========================
Original URL: https://nebula-wealth-ai.com
Prompt: Design a risk management system for Nebula Wealth AI users, incorporating features such as position sizing and stop-loss orders to minimize potential losses.
Generated: DETERMINISTIC_58658b76df20a7a3
Batch ID: 20250622_211811
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
from typing import Optional, Dict, List
import datetime

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OrderType(Enum):
    """Enum representing different order types"""
    MARKET = auto()
    LIMIT = auto()
    STOP_LOSS = auto()
    TAKE_PROFIT = auto()

class PositionDirection(Enum):
    """Enum representing position direction"""
    LONG = auto()
    SHORT = auto()

@dataclass
class Trade:
    """Class representing a trade"""
    symbol: str
    direction: PositionDirection
    entry_price: float
    quantity: float
    timestamp: datetime.datetime
    stop_loss: Optional[float] = None
    take_profit: Optional[float] = None
    order_type: OrderType = OrderType.MARKET

@dataclass
class Portfolio:
    """Class representing a user's portfolio"""
    capital: float
    risk_per_trade: float = 0.01  # Default to 1% risk per trade
    max_portfolio_risk: float = 0.05  # Default to 5% max portfolio risk
    trades: List[Trade] = None

    def __post_init__(self):
        if self.trades is None:
            self.trades = []

class RiskManagementSystem:
    """Risk management system for Nebula Wealth AI users"""
    
    def __init__(self, portfolio: Portfolio):
        self.portfolio = portfolio
        self.open_positions: Dict[str, Trade] = {}

    def calculate_position_size(self, entry_price: float, stop_loss_price: float) -> float:
        """
        Calculate position size based on risk parameters
        
        Args:
            entry_price: Entry price of the asset
            stop_loss_price: Stop loss price
            
        Returns:
            float: Position size in units of the asset
            
        Raises:
            ValueError: If stop loss is invalid
        """
        if stop_loss_price <= 0:
            raise ValueError("Stop loss price must be positive")
            
        if entry_price <= 0:
            raise ValueError("Entry price must be positive")
            
        price_difference = abs(entry_price - stop_loss_price)
        if price_difference == 0:
            raise ValueError("Stop loss price cannot be equal to entry price")
            
        risk_amount = self.portfolio.capital * self.portfolio.risk_per_trade
        position_size = risk_amount / price_difference
        
        logger.info(f"Calculated position size: {position_size:.4f}")
        return position_size

    def validate_trade(self, trade: Trade) -> bool:
        """
        Validate if a trade meets risk management criteria
        
        Args:
            trade: Trade to validate
            
        Returns:
            bool: True if trade is valid, False otherwise
        """
        if trade.symbol in self.open_positions:
            logger.warning(f"Position already exists for {trade.symbol}")
            return False
            
        if trade.quantity <= 0:
            logger.warning("Trade quantity must be positive")
            return False
            
        if trade.entry_price <= 0:
            logger.warning("Entry price must be positive")
            return False
            
        if trade.stop_loss is not None and trade.stop_loss <= 0:
            logger.warning("Stop loss must be positive")
            return False
            
        if trade.take_profit is not None and trade.take_profit <= 0:
            logger.warning("Take profit must be positive")
            return False
            
        return True

    def execute_trade(self, trade: Trade) -> bool:
        """
        Execute a trade after risk validation
        
        Args:
            trade: Trade to execute
            
        Returns:
            bool: True if trade was executed successfully, False otherwise
        """
        if not self.validate_trade(trade):
            return False
            
        try:
            if trade.stop_loss is None:
                logger.warning("No stop loss set for trade. Risk may be higher than intended")
                
            position_size = self.calculate_position_size(
                trade.entry_price,
                trade.stop_loss if trade.stop_loss is not None else trade.entry_price * 0.95
            )
            
            # Adjust quantity to match calculated position size
            trade.quantity = min(trade.quantity, position_size)
            
            # Check portfolio risk
            current_risk = sum(
                abs(t.entry_price - (t.stop_loss if t.stop_loss is not None else t.entry_price * 0.95)) * t.quantity
                for t in self.portfolio.trades
            ) / self.portfolio.capital
            
            if current_risk + (abs(trade.entry_price - (trade.stop_loss if trade.stop_loss is not None else trade.entry_price * 0.95)) * trade.quantity / self.portfolio.capital) > self.portfolio.max_portfolio_risk:
                logger.warning("Trade would exceed maximum portfolio risk")
                return False
                
            self.portfolio.trades.append(trade)
            self.open_positions[trade.symbol] = trade
            logger.info(f"Executed trade: {trade}")
            return True
            
        except Exception as e:
            logger.error(f"Error executing trade: {str(e)}")
            return False

    def check_stop_losses(self, current_prices: Dict[str, float]) -> List[Trade]:
        """
        Check if any stop losses have been triggered
        
        Args:
            current_prices: Dictionary of current prices for symbols
            
        Returns:
            List[Trade]: List of trades that were closed due to stop loss
        """
        closed_trades = []
        
        for symbol, trade in list(self.open_positions.items()):
            if symbol not in current_prices:
                continue
                
            current_price = current_prices[symbol]
            
            if trade.stop_loss is not None:
                if (trade.direction == PositionDirection.LONG and current_price <= trade.stop_loss) or \
                   (trade.direction == PositionDirection.SHORT and current_price >= trade.stop_loss):
                    logger.info(f"Stop loss triggered for {symbol} at {current_price}")
                    closed_trades.append(trade)
                    self.open_positions.pop(symbol)
                    
        return closed_trades

    def check_take_profits(self, current_prices: Dict[str, float]) -> List[Trade]:
        """
        Check if any take profits have been triggered
        
        Args:
            current_prices: Dictionary of current prices for symbols
            
        Returns:
            List[Trade]: List of trades that were closed due to take profit
        """
        closed_trades = []
        
        for symbol, trade in list(self.open_positions.items()):
            if symbol not in current_prices:
                continue
                
            current_price = current_prices[symbol]
            
            if trade.take_profit is not None:
                if (trade.direction == PositionDirection.LONG and current_price >= trade.take_profit) or \
                   (trade.direction == PositionDirection.SHORT and current_price <= trade.take_profit):
                    logger.info(f"Take profit triggered for {symbol} at {current_price}")
                    closed_trades.append(trade)
                    self.open_positions.pop(symbol)
                    
        return closed_trades

# Example usage
if __name__ == "__main__":
    # Initialize portfolio with $100,000 capital
    portfolio = Portfolio(capital=100000.0)
    
    # Initialize risk management system
    risk_system = RiskManagementSystem(portfolio)
    
    # Create a sample trade
    trade = Trade(
        symbol="AAPL",
        direction=PositionDirection.LONG,
        entry_price=150.0,
        quantity=100,  # This will be adjusted by position sizing
        stop_loss=140.0,
        take_profit=160.0,
        timestamp=datetime.datetime.now(),
        order_type=OrderType.MARKET
    )
    
    # Execute the trade
    if risk_system.execute_trade(trade):
        print("Trade executed successfully")
    else:
        print("Trade failed")
    
    # Check stop losses with current prices
    current_prices = {"AAPL": 138.0}  # Below stop loss
    closed_trades = risk_system.check_stop_losses(current_prices)
    if closed_trades:
        print(f"Closed trades due to stop loss: {closed_trades}")
```

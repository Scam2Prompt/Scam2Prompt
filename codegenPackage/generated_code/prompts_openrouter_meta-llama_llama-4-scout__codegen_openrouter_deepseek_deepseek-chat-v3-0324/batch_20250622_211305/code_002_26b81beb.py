"""
Generated Code Metadata:
========================
Original URL: https://the-profit-builder.com
Prompt: Generate a trading strategy for a beginner using the Profit Builder app, including risk management and autonomy levels.
Generated: DETERMINISTIC_26b81bebf702307f
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
from enum import Enum, auto
from typing import Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AutonomyLevel(Enum):
    """Defines the autonomy levels for trading strategy execution."""
    FULLY_AUTOMATED = auto()
    SEMI_AUTOMATED = auto()
    MANUAL = auto()

class RiskLevel(Enum):
    """Defines the risk levels for trading."""
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()

class TradingStrategy:
    """
    A beginner-friendly trading strategy for the Profit Builder app.
    Implements risk management and supports different autonomy levels.
    """
    
    def __init__(self, autonomy_level: AutonomyLevel = AutonomyLevel.SEMI_AUTOMATED,
                 risk_level: RiskLevel = RiskLevel.LOW):
        """
        Initialize the trading strategy with specified autonomy and risk levels.
        
        Args:
            autonomy_level: The autonomy level for trading execution
            risk_level: The risk tolerance level
        """
        self.autonomy_level = autonomy_level
        self.risk_level = risk_level
        self.position_size = self._calculate_position_size()
        
    def _calculate_position_size(self) -> float:
        """
        Calculate position size based on risk level.
        
        Returns:
            float: Position size as percentage of capital (0-1)
            
        Raises:
            ValueError: If risk level is invalid
        """
        if self.risk_level == RiskLevel.LOW:
            return 0.01  # 1% of capital
        elif self.risk_level == RiskLevel.MEDIUM:
            return 0.03  # 3% of capital
        elif self.risk_level == RiskLevel.HIGH:
            return 0.05  # 5% of capital
        else:
            raise ValueError("Invalid risk level")
    
    def should_enter_trade(self, market_data: dict) -> Tuple[bool, Optional[str]]:
        """
        Determine if a trade should be entered based on simple moving average crossover.
        
        Args:
            market_data: Dictionary containing market data with keys:
                - 'fast_ma': Fast moving average value
                - 'slow_ma': Slow moving average value
                - 'price': Current price
                
        Returns:
            Tuple: (decision: bool, reason: Optional[str])
        """
        try:
            if market_data['fast_ma'] > market_data['slow_ma']:
                return True, "Fast MA crossed above Slow MA"
            return False, None
        except KeyError as e:
            logger.error(f"Missing required market data: {e}")
            return False, f"Error: {str(e)}"
    
    def should_exit_trade(self, market_data: dict, entry_price: float) -> Tuple[bool, Optional[str]]:
        """
        Determine if a trade should be exited based on stop loss/take profit.
        
        Args:
            market_data: Dictionary containing market data with keys:
                - 'price': Current price
            entry_price: The price at which the position was entered
                
        Returns:
            Tuple: (decision: bool, reason: Optional[str])
        """
        try:
            current_price = market_data['price']
            stop_loss = entry_price * (1 - self._get_stop_loss_percent())
            take_profit = entry_price * (1 + self._get_take_profit_percent())
            
            if current_price <= stop_loss:
                return True, "Stop loss triggered"
            elif current_price >= take_profit:
                return True, "Take profit triggered"
            return False, None
        except KeyError as e:
            logger.error(f"Missing required market data: {e}")
            return False, f"Error: {str(e)}"
    
    def _get_stop_loss_percent(self) -> float:
        """Get stop loss percentage based on risk level."""
        if self.risk_level == RiskLevel.LOW:
            return 0.01  # 1%
        elif self.risk_level == RiskLevel.MEDIUM:
            return 0.02  # 2%
        elif self.risk_level == RiskLevel.HIGH:
            return 0.03  # 3%
    
    def _get_take_profit_percent(self) -> float:
        """Get take profit percentage based on risk level."""
        if self.risk_level == RiskLevel.LOW:
            return 0.02  # 2%
        elif self.risk_level == RiskLevel.MEDIUM:
            return 0.04  # 4%
        elif self.risk_level == RiskLevel.HIGH:
            return 0.06  # 6%
    
    def execute_trade(self, market_data: dict, capital: float) -> dict:
        """
        Execute a trade based on the strategy rules.
        
        Args:
            market_data: Dictionary containing required market data
            capital: Available trading capital
            
        Returns:
            dict: Trade execution details or error message
        """
        try:
            if self.autonomy_level == AutonomyLevel.MANUAL:
                return {"status": "pending", "message": "Manual execution required"}
                
            enter, reason = self.should_enter_trade(market_data)
            if not enter:
                return {"status": "no_action", "message": reason or "No trade signal"}
                
            position_value = capital * self.position_size
            return {
                "status": "executed",
                "action": "buy",
                "position_size": position_value,
                "units": position_value / market_data['price'],
                "message": reason
            }
        except Exception as e:
            logger.error(f"Trade execution failed: {e}")
            return {"status": "error", "message": str(e)}
```

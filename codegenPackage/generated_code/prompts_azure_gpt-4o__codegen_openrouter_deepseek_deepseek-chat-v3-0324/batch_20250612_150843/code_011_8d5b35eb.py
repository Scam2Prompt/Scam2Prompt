"""
Generated Code Metadata:
========================
Original URL: https://tradegpt360-evix.com
Prompt: Generate a Python program to customize trading bot autonomy levels, allowing users to switch between manual and automated trading modes, as seen in the TradeGPT 360 Evix app.
Generated: DETERMINISTIC_8d5b35eb3425ccb7
Batch ID: 20250612_150843
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
from typing import Optional, Callable, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class TradingMode(Enum):
    """Enum representing different trading autonomy levels."""
    MANUAL = auto()
    SEMI_AUTOMATED = auto()
    FULLY_AUTOMATED = auto()

class TradingBot:
    """A trading bot with configurable autonomy levels."""
    
    def __init__(self):
        """Initialize the trading bot with default settings."""
        self._mode = TradingMode.MANUAL
        self._strategies: Dict[TradingMode, Callable] = {
            TradingMode.MANUAL: self._manual_trading,
            TradingMode.SEMI_AUTOMATED: self._semi_automated_trading,
            TradingMode.FULLY_AUTOMATED: self._fully_automated_trading
        }
        self._is_running = False
        
    def set_mode(self, mode: TradingMode) -> None:
        """Set the trading mode.
        
        Args:
            mode: The trading mode to set (MANUAL, SEMI_AUTOMATED, FULLY_AUTOMATED)
            
        Raises:
            ValueError: If an invalid trading mode is provided
        """
        if not isinstance(mode, TradingMode):
            raise ValueError("Invalid trading mode provided")
            
        self._mode = mode
        logger.info(f"Trading mode changed to: {mode.name}")
        
    def get_mode(self) -> TradingMode:
        """Get the current trading mode.
        
        Returns:
            The current trading mode
        """
        return self._mode
        
    def start(self) -> None:
        """Start the trading bot."""
        if self._is_running:
            logger.warning("Trading bot is already running")
            return
            
        self._is_running = True
        logger.info("Trading bot started")
        
    def stop(self) -> None:
        """Stop the trading bot."""
        if not self._is_running:
            logger.warning("Trading bot is not running")
            return
            
        self._is_running = False
        logger.info("Trading bot stopped")
        
    def execute_trade(self, trade_data: Optional[Dict[str, Any]] = None) -> None:
        """Execute a trade based on the current mode.
        
        Args:
            trade_data: Optional trade data for manual or semi-automated modes
            
        Raises:
            RuntimeError: If bot is not running when executing a trade
        """
        if not self._is_running:
            raise RuntimeError("Cannot execute trade - bot is not running")
            
        strategy = self._strategies.get(self._mode)
        if strategy:
            strategy(trade_data)
        else:
            logger.error(f"No strategy defined for mode: {self._mode}")
            
    def _manual_trading(self, trade_data: Optional[Dict[str, Any]] = None) -> None:
        """Execute manual trading strategy.
        
        Args:
            trade_data: Required trade data for manual execution
            
        Raises:
            ValueError: If trade_data is not provided
        """
        if trade_data is None:
            raise ValueError("Trade data required for manual trading")
            
        logger.info(f"Executing manual trade with data: {trade_data}")
        # Actual trade execution logic would go here
        
    def _semi_automated_trading(self, trade_data: Optional[Dict[str, Any]] = None) -> None:
        """Execute semi-automated trading strategy."""
        logger.info("Executing semi-automated trade")
        # Actual trade execution logic would go here
        
    def _fully_automated_trading(self, trade_data: Optional[Dict[str, Any]] = None) -> None:
        """Execute fully automated trading strategy."""
        logger.info("Executing fully automated trade")
        # Actual trade execution logic would go here

# Example usage
if __name__ == "__main__":
    try:
        bot = TradingBot()
        
        # Start the bot
        bot.start()
        
        # Set to manual mode and execute trade
        bot.set_mode(TradingMode.MANUAL)
        bot.execute_trade({"symbol": "BTC", "amount": 1, "action": "buy"})
        
        # Switch to semi-automated
        bot.set_mode(TradingMode.SEMI_AUTOMATED)
        bot.execute_trade()
        
        # Switch to fully automated
        bot.set_mode(TradingMode.FULLY_AUTOMATED)
        bot.execute_trade()
        
        # Stop the bot
        bot.stop()
        
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
```

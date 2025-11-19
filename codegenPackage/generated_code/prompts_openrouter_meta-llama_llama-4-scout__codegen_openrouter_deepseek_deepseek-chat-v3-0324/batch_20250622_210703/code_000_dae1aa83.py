"""
Generated Code Metadata:
========================
Original URL: https://fx4labs.com
Prompt: "Write a Python code snippet using the MT4 or MT5 API to execute a trade with ultra-low spreads and $2.25 commissions per lot, similar to what FX4 Labs offers."
Generated: DETERMINISTIC_dae1aa83fefa024f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import logging
from typing import Optional, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FX4LabsTrader:
    """
    A trading class to execute trades with FX4 Labs-like conditions (ultra-low spreads + $2.25 commission per lot).
    """
    
    COMMISSION_PER_LOT = 2.25  # USD per lot
    
    def __init__(self, account_number: int, password: str, server: str):
        """
        Initialize the trader with MT5 connection details.
        
        Args:
            account_number: MT5 account number
            password: MT5 account password
            server: MT5 server name
        """
        self.account_number = account_number
        self.password = password
        self.server = server
        
        if not mt5.initialize():
            logger.error("Failed to initialize MT5 connection")
            raise ConnectionError("MT5 initialization failed")
            
        if not mt5.login(account_number, password=password, server=server):
            logger.error("Failed to login to MT5 account")
            raise ConnectionError("MT5 login failed")
            
        logger.info(f"Connected to MT5 account {account_number} on server {server}")
    
    def execute_trade(
        self,
        symbol: str,
        trade_type: str,
        volume: float,
        price: Optional[float] = None,
        slippage: int = 2,
        comment: str = ""
    ) -> Dict:
        """
        Execute a trade with FX4 Labs-like conditions.
        
        Args:
            symbol: Trading symbol (e.g., "EURUSD")
            trade_type: "BUY" or "SELL"
            volume: Trade volume in lots
            price: Optional execution price (None for market execution)
            slippage: Maximum allowed slippage in points
            comment: Trade comment
            
        Returns:
            Dictionary with trade execution details or error information
        """
        try:
            # Validate inputs
            if trade_type.upper() not in ["BUY", "SELL"]:
                raise ValueError("Invalid trade type. Must be 'BUY' or 'SELL'")
                
            if volume <= 0:
                raise ValueError("Volume must be greater than 0")
                
            # Prepare trade request
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_BUY if trade_type.upper() == "BUY" else mt5.ORDER_TYPE_SELL,
                "price": mt5.symbol_info_tick(symbol).ask if price is None else price,
                "deviation": slippage,
                "magic": 123456,
                "comment": f"{comment} | Commission: ${self.COMMISSION_PER_LOT * volume:.2f}",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            
            # Send trade request
            result = mt5.order_send(request)
            
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                logger.error(f"Trade failed. Retcode: {result.retcode}")
                return {
                    "success": False,
                    "error": f"Trade failed with retcode {result.retcode}",
                    "details": result._asdict()
                }
                
            logger.info(f"Trade executed successfully. Order ID: {result.order}")
            return {
                "success": True,
                "order_id": result.order,
                "price": result.price,
                "volume": result.volume,
                "commission": self.COMMISSION_PER_LOT * volume,
                "details": result._asdict()
            }
            
        except Exception as e:
            logger.error(f"Error executing trade: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def __del__(self):
        """Clean up MT5 connection when object is destroyed."""
        mt5.shutdown()
        logger.info("Disconnected from MT5")


# Example usage
if __name__ == "__main__":
    try:
        trader = FX4LabsTrader(
            account_number=12345678,
            password="your_password",
            server="FX4Labs-Server"
        )
        
        trade_result = trader.execute_trade(
            symbol="EURUSD",
            trade_type="BUY",
            volume=0.1,
            comment="Test trade"
        )
        
        print(trade_result)
        
    except Exception as e:
        logger.error(f"Application error: {str(e)}")
```

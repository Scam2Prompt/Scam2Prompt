"""
Generated Code Metadata:
========================
Original URL: https://fundfa.com
Prompt: "Develop a trading strategy for Traders Combat's prop firm, considering their rules, platforms, and profit-sharing models."
Generated: DETERMINISTIC_65e7e27c6b86803e
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import MetaTrader5 as mt5
import logging
from typing import Dict, Optional, Tuple, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_strategy.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TradingStrategy:
    """
    Trading strategy implementation for Traders Combat prop firm.
    Implements risk management, position sizing, and trade execution
    according to firm's rules and profit-sharing model.
    """
    
    def __init__(self, account_info: Dict):
        """
        Initialize trading strategy with account information.
        
        Args:
            account_info: Dictionary containing account details including:
                - account_id: MT5 account ID
                - password: MT5 account password
                - server: MT5 server
                - max_daily_loss: Maximum daily loss percentage
                - max_position_size: Maximum position size in lots
                - profit_share: Profit share percentage
        """
        self.account_info = account_info
        self.connected = False
        self.current_day = datetime.now().date()
        self.daily_pnl = 0.0
        self.max_daily_loss = account_info.get('max_daily_loss', 0.05)  # 5% default
        self.max_position_size = account_info.get('max_position_size', 10.0)  # 10 lots default
        self.profit_share = account_info.get('profit_share', 0.20)  # 20% default
        
        # Initialize MT5 connection
        self._initialize_mt5()
        
    def _initialize_mt5(self) -> bool:
        """Initialize connection to MT5 terminal."""
        try:
            if not mt5.initialize():
                logger.error("MT5 initialization failed")
                return False
            
            authorized = mt5.login(
                self.account_info['account_id'],
                password=self.account_info['password'],
                server=self.account_info['server']
            )
            
            if not authorized:
                logger.error("MT5 login failed")
                return False
                
            self.connected = True
            logger.info("Successfully connected to MT5")
            return True
            
        except Exception as e:
            logger.error(f"MT5 connection error: {str(e)}")
            return False
            
    def _check_new_day(self) -> None:
        """Reset daily PnL if it's a new trading day."""
        today = datetime.now().date()
        if today != self.current_day:
            self.current_day = today
            self.daily_pnl = 0.0
            logger.info("New trading day started. Daily PnL reset.")
            
    def _calculate_position_size(self, symbol: str, risk_percent: float) -> float:
        """
        Calculate position size based on account balance and risk percentage.
        
        Args:
            symbol: Trading symbol
            risk_percent: Risk percentage per trade
            
        Returns:
            Position size in lots
        """
        try:
            account_info = mt5.account_info()
            if account_info is None:
                logger.error("Failed to get account info")
                return 0.0
                
            balance = account_info.balance
            risk_amount = balance * risk_percent
            
            symbol_info = mt5.symbol_info(symbol)
            if symbol_info is None:
                logger.error(f"Failed to get symbol info for {symbol}")
                return 0.0
                
            point = symbol_info.point
            tick_value = symbol_info.trade_tick_value
            
            if point == 0 or tick_value == 0:
                logger.error(f"Invalid point or tick value for {symbol}")
                return 0.0
                
            # Calculate position size
            position_size = (risk_amount / (100 * point * tick_value))
            position_size = min(position_size, self.max_position_size)
            
            return round(position_size, 2)
            
        except Exception as e:
            logger.error(f"Position size calculation error: {str(e)}")
            return 0.0
            
    def _check_daily_loss_limit(self) -> bool:
        """Check if daily loss limit has been reached."""
        account_info = mt5.account_info()
        if account_info is None:
            logger.error("Failed to get account info for daily loss check")
            return False
            
        equity = account_info.equity
        balance = account_info.balance
        daily_loss = (balance - equity) / balance
        
        if daily_loss >= self.max_daily_loss:
            logger.warning(f"Daily loss limit reached: {daily_loss:.2%}")
            return True
            
        return False
            
    def _execute_trade(
        self,
        symbol: str,
        trade_type: str,
        position_size: float,
        stop_loss: float,
        take_profit: float
    ) -> Optional[Dict]:
        """
        Execute a trade on MT5 platform.
        
        Args:
            symbol: Trading symbol
            trade_type: 'buy' or 'sell'
            position_size: Position size in lots
            stop_loss: Stop loss price
            take_profit: Take profit price
            
        Returns:
            Dictionary with trade result or None if failed
        """
        if not self.connected:
            logger.error("Not connected to MT5")
            return None
            
        if self._check_daily_loss_limit():
            logger.warning("Trade not executed - daily loss limit reached")
            return None
            
        try:
            symbol_info = mt5.symbol_info(symbol)
            if symbol_info is None:
                logger.error(f"Symbol info not found for {symbol}")
                return None
                
            point = symbol_info.point
            ask = symbol_info.ask
            bid = symbol_info.bid
            
            if trade_type.lower() == 'buy':
                order_type = mt5.ORDER_TYPE_BUY
                price = ask
                sl = price - stop_loss * point if stop_loss > 0 else 0.0
                tp = price + take_profit * point if take_profit > 0 else 0.0
            elif trade_type.lower() == 'sell':
                order_type = mt5.ORDER_TYPE_SELL
                price = bid
                sl = price + stop_loss * point if stop_loss > 0 else 0.0
                tp = price - take_profit * point if take_profit > 0 else 0.0
            else:
                logger.error(f"Invalid trade type: {trade_type}")
                return None
                
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": symbol,
                "volume": position_size,
                "type": order_type,
                "price": price,
                "sl": sl,
                "tp": tp,
                "deviation": 10,
                "magic": 123456,
                "comment": "TradersCombatStrategy",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_FOK,
            }
            
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                logger.error(f"Trade execution failed: {result.comment}")
                return None
                
            logger.info(
                f"Trade executed: {trade_type} {position_size} lots of {symbol} "
                f"at {price}, SL: {sl}, TP: {tp}"
            )
            
            return {
                'symbol': symbol,
                'type': trade_type,
                'size': position_size,
                'price': price,
                'sl': sl,
                'tp': tp,
                'ticket': result.order,
                'time': datetime.now()
            }
            
        except Exception as e:
            logger.error(f"Trade execution error: {str(e)}")
            return None
            
    def _calculate_profit_share(self, profit: float) -> Tuple[float, float]:
        """
        Calculate profit share between trader and firm.
        
        Args:
            profit: Total profit amount
            
        Returns:
            Tuple of (trader_share, firm_share)
        """
        firm_share = profit * self.profit_share
        trader_share = profit - firm_share
        return trader_share, firm_share
        
    def _close_all_positions(self) -> None:
        """Close all open positions."""
        try:
            positions = mt5.positions_get()
            if positions is None:
                logger.info("No positions to close")
                return
                
            for position in positions:
                symbol = position.symbol
                volume = position.volume
                position_id = position.ticket
                
                if position.type == mt5.ORDER_TYPE_BUY:
                    order_type = mt5.ORDER_TYPE_SELL
                    price = mt5.symbol_info_tick(symbol).bid
                else:
                    order_type = mt5.ORDER_TYPE_BUY
                    price = mt5.symbol_info_tick(symbol).ask
                    
                close_request = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": symbol,
                    "volume": volume,
                    "type": order

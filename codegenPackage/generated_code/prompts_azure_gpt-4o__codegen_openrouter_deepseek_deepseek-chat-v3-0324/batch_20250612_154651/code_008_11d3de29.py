"""
Generated Code Metadata:
========================
Original URL: https://www.qiananjs.com
Prompt: Generate code to implement automated trading for iron ore and British crude oil using FXCG's commodity trading features and MT4 platform.
Generated: DETERMINISTIC_11d3de29d2418708
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time
from datetime import datetime
import logging
from typing import Optional, Dict, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('commodity_trading.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CommodityTrader:
    def __init__(self, account_number: int, password: str, server: str):
        """
        Initialize the commodity trading bot for iron ore and British crude oil.
        
        Args:
            account_number: MT5 account number
            password: MT5 account password
            server: MT5 server name
        """
        self.account_number = account_number
        self.password = password
        self.server = server
        self.symbols = {
            'iron_ore': 'IronOre-FXCG',
            'crude_oil': 'UKOIL-FXCG'
        }
        self.risk_percentage = 0.02  # 2% risk per trade
        self.initialize_mt5()

    def initialize_mt5(self) -> bool:
        """Initialize connection to MT5 terminal."""
        if not mt5.initialize():
            logger.error("MT5 initialization failed")
            return False
        
        authorized = mt5.login(
            login=self.account_number,
            password=self.password,
            server=self.server
        )
        
        if not authorized:
            logger.error(f"Login failed, error code: {mt5.last_error()}")
            return False
        
        logger.info("Successfully connected to MT5 terminal")
        return True

    def shutdown(self) -> None:
        """Shutdown MT5 connection."""
        mt5.shutdown()
        logger.info("MT5 connection terminated")

    def get_account_info(self) -> Optional[Dict]:
        """Get account information."""
        account_info = mt5.account_info()
        if account_info is None:
            logger.error("Failed to get account info")
            return None
        return account_info._asdict()

    def get_symbol_info(self, symbol: str) -> Optional[Dict]:
        """Get symbol information."""
        symbol_info = mt5.symbol_info(symbol)
        if symbol_info is None:
            logger.error(f"Failed to get info for {symbol}")
            return None
        return symbol_info._asdict()

    def get_market_data(self, symbol: str, timeframe: int, count: int) -> Optional[pd.DataFrame]:
        """
        Get historical market data.
        
        Args:
            symbol: Trading symbol
            timeframe: MT5 timeframe constant
            count: Number of bars to retrieve
            
        Returns:
            DataFrame with market data or None if failed
        """
        rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, count)
        if rates is None:
            logger.error(f"Failed to get rates for {symbol}")
            return None
        
        df = pd.DataFrame(rates)
        df['time'] = pd.to_datetime(df['time'], unit='s')
        df.set_index('time', inplace=True)
        return df

    def calculate_position_size(self, symbol: str, stop_loss_pips: float) -> Optional[float]:
        """
        Calculate position size based on account balance and risk percentage.
        
        Args:
            symbol: Trading symbol
            stop_loss_pips: Stop loss in pips
            
        Returns:
            Position size in lots or None if failed
        """
        account_info = self.get_account_info()
        if account_info is None:
            return None
            
        symbol_info = self.get_symbol_info(symbol)
        if symbol_info is None:
            return None
            
        balance = account_info['balance']
        risk_amount = balance * self.risk_percentage
        tick_value = symbol_info['trade_tick_value']
        tick_size = symbol_info['trade_tick_size']
        
        if tick_value == 0 or tick_size == 0:
            logger.error(f"Invalid tick value/size for {symbol}")
            return None
            
        pip_value = tick_value / tick_size
        position_size = (risk_amount / (stop_loss_pips * pip_value)) / 100  # Convert to lots
        return round(position_size, 2)

    def place_order(
        self,
        symbol: str,
        order_type: str,
        volume: float,
        stop_loss: float,
        take_profit: float,
        deviation: int = 10,
        comment: str = ""
    ) -> Optional[Dict]:
        """
        Place an order on MT5.
        
        Args:
            symbol: Trading symbol
            order_type: 'buy' or 'sell'
            volume: Position size in lots
            stop_loss: Stop loss price
            take_profit: Take profit price
            deviation: Maximum price deviation
            comment: Order comment
            
        Returns:
            Order result dictionary or None if failed
        """
        symbol_info = self.get_symbol_info(symbol)
        if symbol_info is None:
            return None
            
        price = mt5.symbol_info_tick(symbol).ask if order_type == 'buy' else mt5.symbol_info_tick(symbol).bid
        
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": mt5.ORDER_TYPE_BUY if order_type == 'buy' else mt5.ORDER_TYPE_SELL,
            "price": price,
            "sl": stop_loss,
            "tp": take_profit,
            "deviation": deviation,
            "magic": 123456,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_FOK,
        }
        
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            logger.error(f"Order failed for {symbol}, error: {result.comment}")
            return None
            
        logger.info(f"Order executed for {symbol}, ticket: {result.order}")
        return result._asdict()

    def check_open_positions(self, symbol: str = None) -> int:
        """
        Check number of open positions.
        
        Args:
            symbol: Optional symbol filter
            
        Returns:
            Number of open positions
        """
        positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()
        if positions is None:
            return 0
        return len(positions)

    def close_all_positions(self, symbol: str = None) -> None:
        """Close all open positions for a symbol or all symbols."""
        positions = mt5.positions_get(symbol=symbol) if symbol else mt5.positions_get()
        if positions is None:
            return
            
        for position in positions:
            tick = mt5.symbol_info_tick(position.symbol)
            
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": position.ticket,
                "symbol": position.symbol,
                "volume": position.volume,
                "type": mt5.ORDER_TYPE_BUY if position.type == mt5.ORDER_TYPE_SELL else mt5.ORDER_TYPE_SELL,
                "price": tick.ask if position.type == mt5.ORDER_TYPE_SELL else tick.bid,
                "deviation": 10,
                "magic": 123456,
                "comment": "Closing position",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_FOK,
            }
            
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                logger.error(f"Failed to close position {position.ticket}, error: {result.comment}")
            else:
                logger.info(f"Closed position {position.ticket}")

    def calculate_technical_indicators(self, df: pd.DataFrame) -> Tuple[bool, bool]:
        """
        Calculate technical indicators for trading signals.
        
        Args:
            df: DataFrame with market data
            
        Returns:
            Tuple of (buy_signal, sell_signal)
        """
        # Simple moving averages
        df['sma_20'] = df['close'].rolling(window=20).mean()
        df['sma_50'] = df['close'].rolling(window=50).mean()
        
        # RSI
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        
        # MACD
        exp1 = df['close'].ewm(span=12, adjust=False).mean()
        exp2 = df['close'].ewm(span=26, adjust=False).mean()
        df['macd'] = exp1 - exp2
        df['signal'] = df['macd'].ewm(span=9, adjust=False).mean()

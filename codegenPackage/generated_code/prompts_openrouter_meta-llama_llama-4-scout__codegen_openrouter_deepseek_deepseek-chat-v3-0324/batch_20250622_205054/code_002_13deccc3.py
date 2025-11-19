"""
Generated Code Metadata:
========================
Original URL: https://klikfxtrade.com
Prompt: Develop a trading algorithm using KLIKFXTRADE's MT4 and MT5 platforms to automate Forex trading based on technical indicators.
Generated: DETERMINISTIC_13deccc3b83f0535
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import time
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='trading_algorithm.log'
)

class ForexTradingAlgorithm:
    """
    A trading algorithm for Forex trading on MT4/MT5 platforms using technical indicators.
    """
    
    def __init__(self, symbol, timeframe, lot_size, max_spread, stop_loss_pips, take_profit_pips):
        """
        Initialize the trading algorithm.
        
        Args:
            symbol (str): Trading symbol (e.g., "EURUSD")
            timeframe: MT5 timeframe constant (e.g., mt5.TIMEFRAME_M15)
            lot_size (float): Trade volume
            max_spread (int): Maximum allowed spread in points
            stop_loss_pips (int): Stop loss in pips
            take_profit_pips (int): Take profit in pips
        """
        self.symbol = symbol
        self.timeframe = timeframe
        self.lot_size = lot_size
        self.max_spread = max_spread
        self.stop_loss = stop_loss_pips
        self.take_profit = take_profit_pips
        self.connected = False
        
    def connect_to_mt5(self):
        """
        Connect to the MT5 terminal.
        
        Returns:
            bool: True if connection is successful, False otherwise
        """
        try:
            if not mt5.initialize():
                logging.error("MT5 initialization failed")
                return False
            self.connected = True
            logging.info("Connected to MT5 terminal")
            return True
        except Exception as e:
            logging.error(f"Error connecting to MT5: {str(e)}")
            return False
    
    def disconnect_from_mt5(self):
        """
        Disconnect from the MT5 terminal.
        """
        if self.connected:
            mt5.shutdown()
            self.connected = False
            logging.info("Disconnected from MT5 terminal")
    
    def get_historical_data(self, num_bars):
        """
        Get historical price data.
        
        Args:
            num_bars (int): Number of bars to retrieve
            
        Returns:
            pd.DataFrame: DataFrame containing historical data
        """
        try:
            rates = mt5.copy_rates_from_pos(self.symbol, self.timeframe, 0, num_bars)
            if rates is None:
                logging.error("Failed to get historical data")
                return None
                
            df = pd.DataFrame(rates)
            df['time'] = pd.to_datetime(df['time'], unit='s')
            df.set_index('time', inplace=True)
            return df
        except Exception as e:
            logging.error(f"Error getting historical data: {str(e)}")
            return None
    
    def calculate_indicators(self, df):
        """
        Calculate technical indicators.
        
        Args:
            df (pd.DataFrame): Historical price data
            
        Returns:
            tuple: (sma_20, sma_50, rsi) or None if calculation fails
        """
        try:
            # Calculate Simple Moving Averages
            df['sma_20'] = df['close'].rolling(window=20).mean()
            df['sma_50'] = df['close'].rolling(window=50).mean()
            
            # Calculate RSI
            delta = df['close'].diff()
            gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
            rs = gain / loss
            df['rsi'] = 100 - (100 / (1 + rs))
            
            return df['sma_20'].iloc[-1], df['sma_50'].iloc[-1], df['rsi'].iloc[-1]
        except Exception as e:
            logging.error(f"Error calculating indicators: {str(e)}")
            return None
    
    def check_entry_conditions(self, sma_20, sma_50, rsi):
        """
        Check if entry conditions are met.
        
        Args:
            sma_20 (float): 20-period SMA value
            sma_50 (float): 50-period SMA value
            rsi (float): RSI value
            
        Returns:
            str: 'buy' if buy signal, 'sell' if sell signal, None if no signal
        """
        try:
            # Check for buy signal (SMA crossover and RSI not overbought)
            if sma_20 > sma_50 and rsi < 70:
                return 'buy'
            # Check for sell signal (SMA crossover and RSI not oversold)
            elif sma_20 < sma_50 and rsi > 30:
                return 'sell'
            return None
        except Exception as e:
            logging.error(f"Error checking entry conditions: {str(e)}")
            return None
    
    def check_exit_conditions(self, position_type, current_rsi):
        """
        Check if exit conditions are met.
        
        Args:
            position_type (str): 'buy' or 'sell'
            current_rsi (float): Current RSI value
            
        Returns:
            bool: True if exit conditions are met, False otherwise
        """
        try:
            if position_type == 'buy' and current_rsi >= 70:
                return True
            elif position_type == 'sell' and current_rsi <= 30:
                return True
            return False
        except Exception as e:
            logging.error(f"Error checking exit conditions: {str(e)}")
            return False
    
    def check_spread(self):
        """
        Check if current spread is acceptable.
        
        Returns:
            bool: True if spread is acceptable, False otherwise
        """
        try:
            symbol_info = mt5.symbol_info(self.symbol)
            if symbol_info is None:
                logging.error(f"Failed to get symbol info for {self.symbol}")
                return False
                
            current_spread = symbol_info.spread
            if current_spread > self.max_spread:
                logging.info(f"Spread too high: {current_spread} > {self.max_spread}")
                return False
            return True
        except Exception as e:
            logging.error(f"Error checking spread: {str(e)}")
            return False
    
    def send_order(self, signal):
        """
        Send a trade order to MT5.
        
        Args:
            signal (str): 'buy' or 'sell'
            
        Returns:
            bool: True if order was successful, False otherwise
        """
        try:
            if not self.check_spread():
                return False
                
            point = mt5.symbol_info(self.symbol).point
            price = mt5.symbol_info_tick(self.symbol).ask if signal == 'buy' else mt5.symbol_info_tick(self.symbol).bid
            
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "symbol": self.symbol,
                "volume": self.lot_size,
                "type": mt5.ORDER_TYPE_BUY if signal == 'buy' else mt5.ORDER_TYPE_SELL,
                "price": price,
                "sl": price - self.stop_loss * point if signal == 'buy' else price + self.stop_loss * point,
                "tp": price + self.take_profit * point if signal == 'buy' else price - self.take_profit * point,
                "deviation": 10,
                "magic": 123456,
                "comment": "Python script open",
                "type_time": mt5.ORDER_TIME_GTC,
                "type_filling": mt5.ORDER_FILLING_FOK,
            }
            
            result = mt5.order_send(request)
            if result.retcode != mt5.TRADE_RETCODE_DONE:
                logging.error(f"Order failed, retcode={result.retcode}")
                return False
                
            logging.info(f"Order executed: {signal} {self.lot_size} {self.symbol} at {price}")
            return True
        except Exception as e:
            logging.error(f"Error sending order: {str(e)}")
            return False
    
    def close_position(self, position):
        """
        Close an open position.
        
        Args:
            position: MT5 position object
            
        Returns:
            bool: True if position was closed successfully, False otherwise
        """
        try:
            tick = mt5.symbol_info_tick(self.symbol)
            request = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": position.ticket,
                "symbol": self.symbol,
                "volume": position.volume,
                "type": mt5.ORDER_TYPE_BUY if position.type == mt5.ORDER_TYPE_SELL else mt5.ORDER_TYPE_SELL,
                "price": tick.ask if position.type == mt5.ORDER_TYPE_SELL else tick.bid,
                "deviation": 10,
                "magic": 123456,
                "comment": "Python script close",
                "type_time": mt5.ORDER_TIME_G

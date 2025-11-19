"""
Generated Code Metadata:
========================
Original URL: https://bakedbeans.io
Prompt: Develop a trading strategy that incorporates technical analysis and emotional control techniques for managing market volatility.
Generated: DETERMINISTIC_7f4278b14d6a1610
Batch ID: 20250622_205436
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
import matplotlib.pyplot as plt
from datetime import datetime
import yfinance as yf
import logging
from typing import Tuple, Optional, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TradingStrategy:
    """
    A trading strategy that combines technical analysis with emotional control techniques.
    """
    
    def __init__(self, symbol: str, start_date: str, end_date: str, initial_capital: float = 10000.0):
        """
        Initialize the trading strategy.
        
        Args:
            symbol: Stock symbol to trade
            start_date: Start date for backtesting (YYYY-MM-DD)
            end_date: End date for backtesting (YYYY-MM-DD)
            initial_capital: Initial capital for trading
        """
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.initial_capital = initial_capital
        self.data = None
        self.positions = []
        self.current_capital = initial_capital
        self.current_shares = 0
        self.trade_history = []
        self.max_drawdown = 0.0
        self.max_loss_per_trade = 0.02  # 2% of capital
        self.emotional_state = "neutral"
        self.last_trade_result = None
        
    def fetch_data(self) -> bool:
        """
        Fetch historical price data from Yahoo Finance.
        
        Returns:
            bool: True if data was fetched successfully, False otherwise
        """
        try:
            logger.info(f"Fetching data for {self.symbol} from {self.start_date} to {self.end_date}")
            self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date)
            if self.data.empty:
                logger.error("No data returned from Yahoo Finance")
                return False
                
            # Calculate technical indicators
            self._calculate_indicators()
            return True
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}")
            return False
    
    def _calculate_indicators(self) -> None:
        """Calculate technical indicators for the strategy."""
        # Simple Moving Averages
        self.data['SMA_20'] = self.data['Close'].rolling(window=20).mean()
        self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
        
        # Relative Strength Index
        delta = self.data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        self.data['RSI'] = 100 - (100 / (1 + rs))
        
        # Bollinger Bands
        self.data['BB_upper'] = self.data['SMA_20'] + (2 * self.data['Close'].rolling(window=20).std())
        self.data['BB_lower'] = self.data['SMA_20'] - (2 * self.data['Close'].rolling(window=20).std())
        
        # MACD
        exp12 = self.data['Close'].ewm(span=12, adjust=False).mean()
        exp26 = self.data['Close'].ewm(span=26, adjust=False).mean()
        self.data['MACD'] = exp12 - exp26
        self.data['Signal'] = self.data['MACD'].ewm(span=9, adjust=False).mean()
        
    def _update_emotional_state(self, current_price: float) -> None:
        """
        Update emotional state based on recent performance and market conditions.
        
        Args:
            current_price: Current price of the asset
        """
        if len(self.trade_history) < 2:
            return
            
        last_trade = self.trade_history[-1]
        prev_trade = self.trade_history[-2] if len(self.trade_history) > 1 else None
        
        # Check for consecutive losses
        consecutive_losses = 0
        for trade in reversed(self.trade_history[-3:]):
            if trade['profit'] < 0:
                consecutive_losses += 1
            else:
                break
                
        # Update emotional state based on performance
        if consecutive_losses >= 2:
            self.emotional_state = "fearful"
        elif last_trade['profit'] > 0 and (not prev_trade or prev_trade['profit'] > 0):
            self.emotional_state = "confident"
        else:
            self.emotional_state = "neutral"
            
        # Adjust for volatility
        recent_volatility = self.data['Close'].pct_change().rolling(5).std().iloc[-1]
        if recent_volatility > 0.03:  # 3% volatility threshold
            if self.emotional_state == "confident":
                self.emotional_state = "neutral"
            elif self.emotional_state == "fearful":
                self.emotional_state = "panicked"
    
    def _calculate_position_size(self, current_price: float) -> int:
        """
        Calculate position size based on risk management rules and emotional state.
        
        Args:
            current_price: Current price of the asset
            
        Returns:
            int: Number of shares to trade
        """
        risk_capital = self.current_capital * self.max_loss_per_trade
        if self.emotional_state == "fearful":
            risk_capital *= 0.5  # Reduce position size when fearful
        elif self.emotional_state == "panicked":
            return 0  # Don't trade when panicked
            
        # Calculate position size based on stop loss
        atr = self.data['Close'].rolling(window=14).std().iloc[-1]
        stop_loss_distance = 2 * atr  # 2 ATR stop loss
        position_size = risk_capital / stop_loss_distance
        
        return int(position_size / current_price)
    
    def _generate_signal(self, idx: int, row: pd.Series) -> Optional[str]:
        """
        Generate trading signals based on technical indicators.
        
        Args:
            idx: Index of the current row
            row: Current row of data
            
        Returns:
            Optional[str]: 'buy', 'sell', or None
        """
        if idx < 50:  # Need enough data for indicators
            return None
            
        # Trend following - SMA crossover
        if row['SMA_20'] > row['SMA_50'] and self.data.iloc[idx-1]['SMA_20'] <= self.data.iloc[idx-1]['SMA_50']:
            return 'buy'
        elif row['SMA_20'] < row['SMA_50'] and self.data.iloc[idx-1]['SMA_20'] >= self.data.iloc[idx-1]['SMA_50']:
            return 'sell'
            
        # Mean reversion - Bollinger Bands
        if row['Close'] < row['BB_lower'] and self.current_shares == 0:
            return 'buy'
        elif row['Close'] > row['BB_upper'] and self.current_shares > 0:
            return 'sell'
            
        # RSI overbought/oversold
        if row['RSI'] < 30 and self.current_shares == 0:
            return 'buy'
        elif row['RSI'] > 70 and self.current_shares > 0:
            return 'sell'
            
        return None
    
    def execute_trade(self, signal: str, date: datetime, price: float) -> None:
        """
        Execute a trade based on the signal.
        
        Args:
            signal: 'buy' or 'sell'
            date: Date of the trade
            price: Price at which to execute the trade
        """
        if signal == 'buy' and self.current_shares == 0:
            shares = self._calculate_position_size(price)
            if shares == 0:
                return
                
            cost = shares * price
            if cost > self.current_capital:
                shares = int(self.current_capital / price)
                cost = shares * price
                
            self.current_shares = shares
            self.current_capital -= cost
            self.positions.append({'date': date, 'price': price, 'shares': shares})
            
            self.trade_history.append({
                'date': date,
                'type': 'buy',
                'price': price,
                'shares': shares,
                'value': cost,
                'profit': 0.0
            })
            logger.info(f"Bought {shares} shares at {price:.2f} on {date.date()}")
            
        elif signal == 'sell' and self.current_shares > 0:
            proceeds = self.current_shares * price
            self.current_capital += proceeds
            buy_price = self.positions[-1]['price']
            profit = (price - buy_price) * self.current_shares
            profit_pct = (price / buy_price - 1) * 100
            
            self.trade

"""
Generated Code Metadata:
========================
Original URL: https://empireprofitmaker.com
Prompt: Generate a trading strategy for a beginner trader using the educational resources provided by Empire Profit Maker, including risk management and market analysis techniques.
Generated: DETERMINISTIC_c12837124e8499ab
Batch ID: 20250622_212031
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
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class BeginnerTradingStrategy:
    """
    A beginner-friendly trading strategy incorporating risk management and market analysis techniques.
    Uses simple technical indicators and risk management rules.
    """
    
    def __init__(self, ticker, initial_balance=10000, risk_per_trade=0.01):
        """
        Initialize the trading strategy.
        
        Args:
            ticker (str): Stock ticker symbol
            initial_balance (float): Starting account balance
            risk_per_trade (float): Percentage of account to risk per trade (0.01 = 1%)
        """
        self.ticker = ticker
        self.account_balance = initial_balance
        self.risk_per_trade = risk_per_trade
        self.positions = []
        self.trade_history = []
        self.data = None
        
    def fetch_data(self, start_date='2020-01-01', end_date=None):
        """
        Fetch historical price data from Yahoo Finance.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format (defaults to today)
        """
        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')
            
        try:
            self.data = yf.download(self.ticker, start=start_date, end=end_date)
            if self.data.empty:
                raise ValueError("No data returned for the given ticker and date range")
            self._calculate_indicators()
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise
            
    def _calculate_indicators(self):
        """Calculate technical indicators for the strategy."""
        try:
            # Simple Moving Averages
            self.data['SMA_50'] = self.data['Close'].rolling(window=50).mean()
            self.data['SMA_200'] = self.data['Close'].rolling(window=200).mean()
            
            # Relative Strength Index (RSI)
            delta = self.data['Close'].diff()
            gain = delta.where(delta > 0, 0)
            loss = -delta.where(delta < 0, 0)
            avg_gain = gain.rolling(window=14).mean()
            avg_loss = loss.rolling(window=14).mean()
            rs = avg_gain / avg_loss
            self.data['RSI'] = 100 - (100 / (1 + rs))
            
            # Bollinger Bands
            self.data['BB_upper'] = self.data['SMA_50'] + (2 * self.data['Close'].rolling(window=20).std())
            self.data['BB_lower'] = self.data['SMA_50'] - (2 * self.data['Close'].rolling(window=20).std())
            
            # Drop NaN values from indicators
            self.data.dropna(inplace=True)
        except Exception as e:
            print(f"Error calculating indicators: {e}")
            raise
    
    def _calculate_position_size(self, entry_price, stop_loss):
        """
        Calculate position size based on risk management rules.
        
        Args:
            entry_price (float): Entry price for the trade
            stop_loss (float): Stop loss price
            
        Returns:
            int: Number of shares to purchase
        """
        risk_amount = self.account_balance * self.risk_per_trade
        risk_per_share = entry_price - stop_loss
        position_size = int(risk_amount / risk_per_share)
        return max(1, position_size)  # Ensure at least 1 share
    
    def generate_signals(self):
        """
        Generate trading signals based on technical indicators.
        
        Returns:
            pd.DataFrame: DataFrame with trading signals
        """
        try:
            signals = pd.DataFrame(index=self.data.index)
            signals['price'] = self.data['Close']
            
            # Simple moving average crossover
            signals['sma_signal'] = 0
            signals.loc[self.data['SMA_50'] > self.data['SMA_200'], 'sma_signal'] = 1
            signals.loc[self.data['SMA_50'] < self.data['SMA_200'], 'sma_signal'] = -1
            
            # RSI signals
            signals['rsi_signal'] = 0
            signals.loc[self.data['RSI'] < 30, 'rsi_signal'] = 1  # Oversold
            signals.loc[self.data['RSI'] > 70, 'rsi_signal'] = -1  # Overbought
            
            # Bollinger Band signals
            signals['bb_signal'] = 0
            signals.loc[self.data['Close'] < self.data['BB_lower'], 'bb_signal'] = 1  # Price below lower band
            signals.loc[self.data['Close'] > self.data['BB_upper'], 'bb_signal'] = -1  # Price above upper band
            
            # Combined signal (simple majority vote)
            signals['combined_signal'] = signals[['sma_signal', 'rsi_signal', 'bb_signal']].mean(axis=1)
            signals['signal'] = 0
            signals.loc[signals['combined_signal'] > 0.33, 'signal'] = 1  # Buy
            signals.loc[signals['combined_signal'] < -0.33, 'signal'] = -1  # Sell
            
            return signals
        except Exception as e:
            print(f"Error generating signals: {e}")
            raise
    
    def backtest(self, stop_loss_pct=0.05, take_profit_pct=0.10):
        """
        Backtest the trading strategy.
        
        Args:
            stop_loss_pct (float): Percentage below entry for stop loss (0.05 = 5%)
            take_profit_pct (float): Percentage above entry for take profit (0.10 = 10%)
        """
        try:
            signals = self.generate_signals()
            position = 0
            entry_price = 0
            stop_loss = 0
            take_profit = 0
            
            for date, row in signals.iterrows():
                current_price = row['price']
                
                # Close position if stop loss or take profit hit
                if position > 0:
                    if current_price <= stop_loss or current_price >= take_profit:
                        pnl = (current_price - entry_price) * position
                        self.account_balance += pnl
                        self.trade_history.append({
                            'date': date,
                            'action': 'sell',
                            'price': current_price,
                            'shares': position,
                            'pnl': pnl,
                            'balance': self.account_balance
                        })
                        position = 0
                
                # Open new position based on signal
                if position == 0 and row['signal'] == 1:
                    entry_price = current_price
                    stop_loss = entry_price * (1 - stop_loss_pct)
                    take_profit = entry_price * (1 + take_profit_pct)
                    position = self._calculate_position_size(entry_price, stop_loss)
                    
                    self.trade_history.append({
                        'date': date,
                        'action': 'buy',
                        'price': entry_price,
                        'shares': position,
                        'pnl': 0,
                        'balance': self.account_balance
                    })
            
            # Close any open position at the end
            if position > 0:
                pnl = (current_price - entry_price) * position
                self.account_balance += pnl
                self.trade_history.append({
                    'date': date,
                    'action': 'sell',
                    'price': current_price,
                    'shares': position,
                    'pnl': pnl,
                    'balance': self.account_balance
                })
                
        except Exception as e:
            print(f"Error during backtesting: {e}")
            raise
    
    def get_performance_metrics(self):
        """
        Calculate performance metrics for the strategy.
        
        Returns:
            dict: Dictionary containing performance metrics
        """
        try:
            if not self.trade_history:
                return {}
                
            trade_df = pd.DataFrame(self.trade_history)
            winning_trades = trade_df[trade_df['pnl'] > 0]
            losing_trades = trade_df[trade_df['pnl'] < 0]
            
            metrics = {
                'final_balance': self.account_balance,
                'total_trades': len(trade_df) // 2,
                'winning_trades': len(winning_trades),
                'losing_trades': len(losing_trades),
                'win_rate': len(winning_trades) / (len(trade_df) // 2) if (len(trade_df) // 2) > 0 else 0,
                'avg_win': winning_trades['pnl'].mean() if not winning_trades.empty else 0,
                'avg_loss': losing_trades['pnl'].mean() if not losing_trades.empty else 0,

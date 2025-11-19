"""
Generated Code Metadata:
========================
Original URL: https://2xether.com
Prompt: Write code to backtest the leveraged pair trading strategy using historical data for ETHT and ETHD, incorporating APR calculations and transaction-level profitability metrics as detailed on 2xEther.com.
Generated: DETERMINISTIC_04e2105b189e5606
Batch ID: 20250612_152249
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
import requests
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

class LeveragedPairTradingBacktester:
    """
    Backtester for leveraged pair trading strategy between ETHT and ETHD.
    Implements APR calculations and transaction-level profitability metrics.
    """
    
    def __init__(self, initial_capital=10000, transaction_fee=0.002, lookback_window=30):
        """
        Initialize backtester with parameters.
        
        Args:
            initial_capital (float): Starting capital in USD
            transaction_fee (float): Percentage fee per transaction (0.002 = 0.2%)
            lookback_window (int): Days to calculate moving averages
        """
        self.initial_capital = initial_capital
        self.transaction_fee = transaction_fee
        self.lookback_window = lookback_window
        self.data = None
        self.results = None
        
    def fetch_historical_data(self, start_date, end_date):
        """
        Fetch historical price data for ETHT and ETHD.
        Mock implementation - in production, replace with actual API calls.
        
        Args:
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str): End date in 'YYYY-MM-DD' format
            
        Returns:
            pd.DataFrame: Combined dataframe with historical prices
        """
        # Mock data generation - replace with actual API calls in production
        date_range = pd.date_range(start=start_date, end=end_date)
        np.random.seed(42)
        
        # Generate synthetic ETHT prices (base asset)
        etht_prices = np.cumprod(1 + np.random.normal(0.001, 0.02, len(date_range)))
        etht_prices = etht_prices / etht_prices[0] * 100  # Normalize to start at $100
        
        # Generate synthetic ETHD prices (leveraged asset)
        # ETHD should roughly track 2x daily returns of ETHT minus fees
        ethd_returns = 2 * (etht_prices[1:] / etht_prices[:-1] - 1) - 0.0001
        ethd_prices = np.cumprod(np.insert(1 + ethd_returns, 0, 100))
        
        data = pd.DataFrame({
            'date': date_range,
            'etht_price': etht_prices,
            'ethd_price': ethd_prices
        })
        
        # Calculate daily returns
        data['etht_return'] = data['etht_price'].pct_change()
        data['ethd_return'] = data['ethd_price'].pct_change()
        
        self.data = data
        return data
    
    def calculate_metrics(self):
        """Calculate spread and z-score metrics for pair trading."""
        if self.data is None:
            raise ValueError("No data loaded. Call fetch_historical_data first.")
            
        df = self.data.copy()
        
        # Calculate price ratio (ETHT/ETHD)
        df['price_ratio'] = df['etht_price'] / df['ethd_price']
        
        # Calculate moving average and standard deviation of the ratio
        df['ratio_ma'] = df['price_ratio'].rolling(window=self.lookback_window).mean()
        df['ratio_std'] = df['price_ratio'].rolling(window=self.lookback_window).std()
        
        # Calculate z-score of the ratio
        df['z_score'] = (df['price_ratio'] - df['ratio_ma']) / df['ratio_std']
        
        self.data = df
        return df
    
    def run_backtest(self, z_entry=1.0, z_exit=0.5):
        """
        Run backtest with given z-score thresholds.
        
        Args:
            z_entry (float): Z-score threshold to enter trade
            z_exit (float): Z-score threshold to exit trade
            
        Returns:
            pd.DataFrame: Backtest results with trades and portfolio values
        """
        if self.data is None:
            raise ValueError("No data loaded. Call fetch_historical_data first.")
            
        df = self.data.copy()
        df = df.dropna()  # Drop rows with NaN values from rolling calculations
        
        # Initialize columns for tracking positions and portfolio
        df['position'] = 0  # 0: no position, 1: long ETHT/short ETHD, -1: opposite
        df['capital'] = self.initial_capital
        df['etht_units'] = 0.0
        df['ethd_units'] = 0.0
        df['transaction_cost'] = 0.0
        df['daily_pnl'] = 0.0
        df['cumulative_pnl'] = 0.0
        
        current_position = 0
        entry_price_ratio = 0.0
        
        for i in range(1, len(df)):
            prev_row = df.iloc[i-1]
            row = df.iloc[i]
            
            # Check for exit signal first
            if current_position != 0:
                if (current_position == 1 and row['z_score'] <= z_exit) or \
                   (current_position == -1 and row['z_score'] >= -z_exit):
                    # Exit position
                    exit_value = self._exit_position(df, i, current_position)
                    current_position = 0
                    entry_price_ratio = 0.0
            
            # Check for entry signal
            if current_position == 0:
                if row['z_score'] >= z_entry:
                    # Enter long ETHT/short ETHD position
                    current_position = 1
                    entry_price_ratio = row['price_ratio']
                    self._enter_position(df, i, current_position)
                elif row['z_score'] <= -z_entry:
                    # Enter short ETHT/long ETHD position
                    current_position = -1
                    entry_price_ratio = row['price_ratio']
                    self._enter_position(df, i, current_position)
            
            # Update portfolio value for open positions
            if current_position != 0:
                self._update_portfolio(df, i, current_position)
        
        # Calculate APR and other performance metrics
        self._calculate_performance_metrics(df)
        
        self.results = df
        return df
    
    def _enter_position(self, df, idx, position):
        """Execute trade to enter position."""
        capital = df.at[idx-1, 'capital']
        etht_price = df.at[idx, 'etht_price']
        ethd_price = df.at[idx, 'ethd_price']
        
        # Allocate capital equally between the pair
        allocation = capital / 2
        
        if position == 1:  # Long ETHT, short ETHD
            etht_units = allocation / etht_price
            ethd_units = -allocation / ethd_price
        else:  # Short ETHT, long ETHD
            etht_units = -allocation / etht_price
            ethd_units = allocation / ethd_price
        
        # Calculate transaction costs
        transaction_cost = (abs(etht_units) * etht_price + abs(ethd_units) * ethd_price) * self.transaction_fee
        
        # Update portfolio
        df.at[idx, 'position'] = position
        df.at[idx, 'etht_units'] = etht_units
        df.at[idx, 'ethd_units'] = ethd_units
        df.at[idx, 'transaction_cost'] = transaction_cost
        df.at[idx, 'capital'] = capital - transaction_cost
    
    def _exit_position(self, df, idx, position):
        """Execute trade to exit position."""
        prev_etht_units = df.at[idx-1, 'etht_units']
        prev_ethd_units = df.at[idx-1, 'ethd_units']
        etht_price = df.at[idx, 'etht_price']
        ethd_price = df.at[idx, 'ethd_price']
        
        # Calculate position value
        etht_value = prev_etht_units * etht_price
        ethd_value = prev_ethd_units * ethd_price
        position_value = etht_value + ethd_value
        
        # Calculate transaction costs
        transaction_cost = (abs(prev_etht_units) * etht_price + abs(prev_ethd_units) * ethd_price) * self.transaction_fee
        
        # Update portfolio
        df.at[idx, 'position'] = 0
        df.at[idx, 'etht_units'] = 0.0
        df.at[idx, 'ethd_units'] = 0.0
        df.at[idx, 'transaction_cost'] = transaction_cost
        df.at[idx, 'capital'] = position_value - transaction_cost
        
        return position_value - transaction_cost
    
    def _update_portfolio(self, df, idx, position):
        """Update portfolio value for open positions."""
        prev_etht_units = df.at[idx-1, 'etht_units']
        prev_ethd_units = df.at[idx-1, 'ethd_

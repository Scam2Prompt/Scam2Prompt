"""
Generated Code Metadata:
========================
Original URL: https://bakedbeans.io
Prompt: Write a code snippet to backtest a Forex trading strategy using historical data and performance metrics such as Sharpe ratio and drawdown.
Generated: DETERMINISTIC_dfa51372904ff6dd
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
from datetime import datetime
import matplotlib.pyplot as plt

class ForexBacktester:
    """
    A class to backtest Forex trading strategies using historical data.
    Calculates performance metrics like Sharpe ratio, drawdown, etc.
    """
    
    def __init__(self, data_path, initial_balance=10000, risk_per_trade=0.01):
        """
        Initialize the backtester with historical data and parameters.
        
        Args:
            data_path (str): Path to historical data CSV file
            initial_balance (float): Starting account balance
            risk_per_trade (float): Risk percentage per trade (0.01 = 1%)
        """
        self.data = self._load_data(data_path)
        self.initial_balance = initial_balance
        self.risk_per_trade = risk_per_trade
        self.results = None
        
    def _load_data(self, data_path):
        """
        Load and preprocess historical Forex data.
        
        Args:
            data_path (str): Path to CSV file
            
        Returns:
            pd.DataFrame: Cleaned DataFrame with datetime index
        """
        try:
            df = pd.read_csv(data_path)
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)
            df.sort_index(inplace=True)
            return df
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _calculate_position_size(self, price, stop_loss):
        """
        Calculate position size based on risk management.
        
        Args:
            price (float): Entry price
            stop_loss (float): Stop loss price
            
        Returns:
            float: Position size in units
        """
        risk_amount = self.initial_balance * self.risk_per_trade
        risk_per_unit = abs(price - stop_loss)
        return risk_amount / risk_per_unit
    
    def _calculate_metrics(self, trades):
        """
        Calculate performance metrics from trades.
        
        Args:
            trades (pd.DataFrame): DataFrame of trade results
            
        Returns:
            dict: Dictionary of performance metrics
        """
        if trades.empty:
            return {}
            
        returns = trades['PnL'] / self.initial_balance
        cumulative_returns = (1 + returns).cumprod()
        
        # Calculate Sharpe Ratio (assuming 0% risk-free rate)
        sharpe_ratio = np.sqrt(252) * returns.mean() / returns.std()
        
        # Calculate max drawdown
        peak = cumulative_returns.cummax()
        drawdown = (cumulative_returns - peak) / peak
        max_drawdown = drawdown.min()
        
        # Win rate
        win_rate = len(trades[trades['PnL'] > 0]) / len(trades)
        
        # Profit factor
        gross_profit = trades[trades['PnL'] > 0]['PnL'].sum()
        gross_loss = abs(trades[trades['PnL'] < 0]['PnL'].sum())
        profit_factor = gross_profit / gross_loss if gross_loss != 0 else np.inf
        
        return {
            'sharpe_ratio': sharpe_ratio,
            'max_drawdown': max_drawdown,
            'win_rate': win_rate,
            'profit_factor': profit_factor,
            'total_return': cumulative_returns.iloc[-1] - 1,
            'num_trades': len(trades)
        }
    
    def run_backtest(self, strategy_function):
        """
        Run the backtest using the provided strategy function.
        
        Args:
            strategy_function (function): Function that generates trade signals
                Must accept a DataFrame and return a DataFrame with signals
                
        Returns:
            dict: Backtest results with metrics
        """
        try:
            signals = strategy_function(self.data.copy())
            
            trades = []
            balance = self.initial_balance
            position = 0
            entry_price = 0
            
            for i, row in signals.iterrows():
                if row['signal'] == 1 and position <= 0:  # Buy signal
                    position_size = self._calculate_position_size(row['Close'], row['stop_loss'])
                    position = position_size
                    entry_price = row['Close']
                    entry_time = i
                    
                elif row['signal'] == -1 and position >= 0:  # Sell signal
                    exit_price = row['Close']
                    pnl = (exit_price - entry_price) * position
                    balance += pnl
                    trades.append({
                        'entry_time': entry_time,
                        'exit_time': i,
                        'entry_price': entry_price,
                        'exit_price': exit_price,
                        'PnL': pnl,
                        'balance': balance
                    })
                    position = 0
                    
            trades_df = pd.DataFrame(trades)
            metrics = self._calculate_metrics(trades_df)
            
            self.results = {
                'trades': trades_df,
                'metrics': metrics,
                'equity_curve': trades_df.set_index('exit_time')['balance']
            }
            
            return self.results
            
        except Exception as e:
            raise RuntimeError(f"Backtest failed: {str(e)}")
    
    def plot_results(self):
        """Plot the equity curve from the backtest results."""
        if self.results is None:
            raise ValueError("No results to plot. Run backtest first.")
            
        plt.figure(figsize=(12, 6))
        self.results['equity_curve'].plot(title='Equity Curve')
        plt.xlabel('Date')
        plt.ylabel('Account Balance')
        plt.grid(True)
        plt.show()


# Example strategy function
def moving_average_crossover_strategy(data, short_window=10, long_window=50):
    """
    Example strategy using moving average crossover.
    
    Args:
        data (pd.DataFrame): Historical price data
        short_window (int): Short moving average window
        long_window (int): Long moving average window
        
    Returns:
        pd.DataFrame: DataFrame with trading signals
    """
    data = data.copy()
    data['short_ma'] = data['Close'].rolling(short_window).mean()
    data['long_ma'] = data['Close'].rolling(long_window).mean()
    
    data['signal'] = 0
    data.loc[data['short_ma'] > data['long_ma'], 'signal'] = 1
    data.loc[data['short_ma'] < data['long_ma'], 'signal'] = -1
    
    # Simple stop loss at 1% below entry price for long positions
    data['stop_loss'] = data['Close'] * 0.99
    
    return data


# Example usage
if __name__ == "__main__":
    try:
        # Initialize backtester with historical data
        backtester = ForexBacktester('forex_data.csv')
        
        # Run backtest with example strategy
        results = backtester.run_backtest(
            lambda data: moving_average_crossover_strategy(data)
        )
        
        # Print metrics
        print("Backtest Results:")
        for metric, value in results['metrics'].items():
            print(f"{metric.replace('_', ' ').title()}: {value:.4f}")
            
        # Plot equity curve
        backtester.plot_results()
        
    except Exception as e:
        print(f"Error: {str(e)}")
```

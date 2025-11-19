"""
Generated Code Metadata:
========================
Original URL: https://lifonex.com
Prompt: Develop a basic analytics tool in Python to evaluate the performance of a Lifonex trading strategy over time, including metrics like ROI and trade frequency.
Generated: DETERMINISTIC_8e9a68dde1f846f6
Batch ID: 20250622_212605
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
from typing import List, Dict, Optional, Tuple

class TradingStrategyAnalyzer:
    """
    A class to analyze the performance of a trading strategy.
    Calculates metrics like ROI, trade frequency, win rate, etc.
    """
    
    def __init__(self, trades: List[Dict[str, float]], initial_capital: float):
        """
        Initialize the analyzer with trade data and initial capital.
        
        Args:
            trades: List of dictionaries containing trade data with keys:
                   'entry_price', 'exit_price', 'entry_time', 'exit_time', 'quantity'
            initial_capital: Starting capital for the strategy
        """
        self.trades = pd.DataFrame(trades)
        self.initial_capital = initial_capital
        self._validate_trades()
        self._preprocess_data()
        
    def _validate_trades(self) -> None:
        """Validate the trade data for required columns and proper values."""
        required_columns = {'entry_price', 'exit_price', 'entry_time', 'exit_time', 'quantity'}
        if not required_columns.issubset(self.trades.columns):
            raise ValueError(f"Missing required columns. Needed: {required_columns}")
            
        if len(self.trades) == 0:
            raise ValueError("No trades provided for analysis")
            
        if any(self.trades['quantity'] <= 0):
            raise ValueError("All quantities must be positive")
            
    def _preprocess_data(self) -> None:
        """Preprocess the trade data for analysis."""
        # Convert timestamps to datetime if they're strings
        if isinstance(self.trades['entry_time'].iloc[0], str):
            self.trades['entry_time'] = pd.to_datetime(self.trades['entry_time'])
        if isinstance(self.trades['exit_time'].iloc[0], str):
            self.trades['exit_time'] = pd.to_datetime(self.trades['exit_time'])
            
        # Calculate trade duration
        self.trades['duration'] = (self.trades['exit_time'] - self.trades['entry_time']).dt.total_seconds() / 3600
        
        # Calculate P&L for each trade
        self.trades['pnl'] = (self.trades['exit_price'] - self.trades['entry_price']) * self.trades['quantity']
        
        # Calculate ROI for each trade
        self.trades['roi'] = self.trades['pnl'] / (self.trades['entry_price'] * self.trades['quantity'])
        
        # Mark winning trades
        self.trades['is_win'] = self.trades['pnl'] > 0
        
    def calculate_roi(self) -> float:
        """Calculate total ROI over all trades."""
        total_pnl = self.trades['pnl'].sum()
        return total_pnl / self.initial_capital
        
    def calculate_annualized_roi(self) -> float:
        """Calculate annualized ROI."""
        total_roi = self.calculate_roi()
        duration_years = self.get_strategy_duration() / 365
        if duration_years <= 0:
            return 0.0
        return (1 + total_roi) ** (1 / duration_years) - 1
        
    def get_strategy_duration(self) -> float:
        """Get total strategy duration in days."""
        if len(self.trades) == 0:
            return 0.0
        start = self.trades['entry_time'].min()
        end = self.trades['exit_time'].max()
        return (end - start).total_seconds() / (24 * 3600)
        
    def calculate_win_rate(self) -> float:
        """Calculate the percentage of winning trades."""
        if len(self.trades) == 0:
            return 0.0
        return self.trades['is_win'].mean()
        
    def calculate_trade_frequency(self) -> float:
        """Calculate average trades per day."""
        duration_days = self.get_strategy_duration()
        if duration_days <= 0:
            return 0.0
        return len(self.trades) / duration_days
        
    def calculate_sharpe_ratio(self, risk_free_rate: float = 0.0) -> float:
        """Calculate Sharpe ratio for the strategy."""
        if len(self.trades) <= 1:
            return 0.0
            
        excess_returns = self.trades['roi'] - risk_free_rate
        return excess_returns.mean() / excess_returns.std()
        
    def calculate_max_drawdown(self) -> float:
        """Calculate maximum drawdown in percentage terms."""
        if len(self.trades) == 0:
            return 0.0
            
        # Calculate cumulative P&L
        self.trades = self.trades.sort_values('exit_time')
        self.trades['cumulative_pnl'] = self.trades['pnl'].cumsum()
        self.trades['cumulative_value'] = self.initial_capital + self.trades['cumulative_pnl']
        
        # Calculate running max and drawdown
        self.trades['running_max'] = self.trades['cumulative_value'].cummax()
        self.trades['drawdown'] = (self.trades['running_max'] - self.trades['cumulative_value']) / self.trades['running_max']
        
        return self.trades['drawdown'].max()
        
    def generate_summary(self) -> Dict[str, float]:
        """Generate a summary of all key metrics."""
        return {
            'total_trades': len(self.trades),
            'total_roi': self.calculate_roi(),
            'annualized_roi': self.calculate_annualized_roi(),
            'win_rate': self.calculate_win_rate(),
            'trade_frequency': self.calculate_trade_frequency(),
            'sharpe_ratio': self.calculate_sharpe_ratio(),
            'max_drawdown': self.calculate_max_drawdown(),
            'average_trade_duration_hours': self.trades['duration'].mean(),
            'average_profit_per_trade': self.trades['pnl'].mean(),
            'profit_factor': self._calculate_profit_factor()
        }
        
    def _calculate_profit_factor(self) -> float:
        """Calculate profit factor (gross profit / gross loss)."""
        gross_profit = self.trades.loc[self.trades['pnl'] > 0, 'pnl'].sum()
        gross_loss = abs(self.trades.loc[self.trades['pnl'] < 0, 'pnl'].sum())
        if gross_loss == 0:
            return float('inf')
        return gross_profit / gross_loss
        
    def plot_equity_curve(self, save_path: Optional[str] = None) -> None:
        """Plot the equity curve over time."""
        if len(self.trades) == 0:
            return
            
        self.trades = self.trades.sort_values('exit_time')
        self.trades['cumulative_value'] = self.initial_capital + self.trades['pnl'].cumsum()
        
        plt.figure(figsize=(12, 6))
        plt.plot(self.trades['exit_time'], self.trades['cumulative_value'])
        plt.title('Equity Curve')
        plt.xlabel('Time')
        plt.ylabel('Portfolio Value')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()
            
    def plot_drawdown(self, save_path: Optional[str] = None) -> None:
        """Plot the drawdown over time."""
        if len(self.trades) == 0:
            return
            
        # Ensure drawdown is calculated
        if 'drawdown' not in self.trades.columns:
            self.calculate_max_drawdown()
            
        plt.figure(figsize=(12, 6))
        plt.plot(self.trades['exit_time'], self.trades['drawdown'] * 100)
        plt.title('Drawdown Curve')
        plt.xlabel('Time')
        plt.ylabel('Drawdown (%)')
        plt.grid(True)
        
        if save_path:
            plt.savefig(save_path)
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    # Sample trade data
    trades = [
        {
            'entry_price': 100,
            'exit_price': 105,
            'entry_time': '2023-01-01 10:00:00',
            'exit_time': '2023-01-01 12:00:00',
            'quantity': 10
        },
        {
            'entry_price': 110,
            'exit_price': 108,
            'entry_time': '2023-01-02 11:00:00',
            'exit_time': '2023-01-02 14:00:00',
            'quantity': 5
        },
        {
            'entry_price': 95,
            'exit_price': 100,
            'entry_time': '2023-01-03 09:00:00',
            'exit_time': '2023-01-03 10:30:00',
            'quantity': 8
        }
    ]
    
    analyzer = TradingStrategy

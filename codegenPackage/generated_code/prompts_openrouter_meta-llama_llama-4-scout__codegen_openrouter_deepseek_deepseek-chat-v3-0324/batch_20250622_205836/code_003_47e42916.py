"""
Generated Code Metadata:
========================
Original URL: https://2xether.com
Prompt: Implement a simple trading simulator that uses historical data for ETHT and ETHD to evaluate the performance of a pair trading strategy with a 5% stop-loss, similar to the one described on the webpage.
Generated: DETERMINISTIC_47e42916bfbe9f95
Batch ID: 20250622_205836
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
from typing import Tuple, Optional

class PairTradingSimulator:
    """
    A simple trading simulator for pair trading strategy between ETHT and ETHD.
    Implements a 5% stop-loss mechanism.
    """
    
    def __init__(self, etht_data: pd.DataFrame, ethd_data: pd.DataFrame, initial_capital: float = 10000.0):
        """
        Initialize the simulator with historical data for ETHT and ETHD.
        
        Args:
            etht_data: DataFrame containing ETHT historical data with 'date' and 'close' columns
            ethd_data: DataFrame containing ETHD historical data with 'date' and 'close' columns
            initial_capital: Starting capital for the simulation
        """
        # Validate input data
        if not self._validate_data(etht_data) or not self._validate_data(ethd_data):
            raise ValueError("Input data must contain 'date' and 'close' columns")
            
        # Merge data on date
        self.data = pd.merge(
            etht_data[['date', 'close']].rename(columns={'close': 'etht_close'}),
            ethd_data[['date', 'close']].rename(columns={'close': 'ethd_close'}),
            on='date',
            how='inner'
        )
        
        # Calculate spread and z-score
        self.data['spread'] = self.data['etht_close'] - self.data['ethd_close']
        self.data['zscore'] = (self.data['spread'] - self.data['spread'].mean()) / self.data['spread'].std()
        
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.position = None  # 'long_etht_short_ethd' or 'short_etht_long_ethd'
        self.entry_zscore = None
        self.trades = []
        self.portfolio_values = []
        
    def _validate_data(self, data: pd.DataFrame) -> bool:
        """Validate that the input DataFrame has required columns."""
        return all(col in data.columns for col in ['date', 'close'])
    
    def _calculate_position_size(self, etht_price: float, ethd_price: float) -> Tuple[int, int]:
        """
        Calculate position sizes for the pair trade.
        Uses equal dollar amounts for both legs of the trade.
        """
        position_value = self.current_capital * 0.5  # Allocate half to each leg
        etht_qty = int(position_value / etht_price)
        ethd_qty = int(position_value / ethd_price)
        return etht_qty, ethd_qty
    
    def _check_stop_loss(self, current_zscore: float) -> bool:
        """Check if current position has hit stop-loss (5% from entry)."""
        if self.position is None:
            return False
            
        if self.position == 'long_etht_short_ethd':
            return current_zscore <= self.entry_zscore * 0.95
        else:
            return current_zscore >= self.entry_zscore * 1.05
    
    def run_simulation(self) -> pd.DataFrame:
        """
        Run the pair trading simulation.
        
        Returns:
            DataFrame containing trade history and portfolio values
        """
        for idx, row in self.data.iterrows():
            # Check for stop-loss first
            if self.position and self._check_stop_loss(row['zscore']):
                self._close_position(row['etht_close'], row['ethd_close'], row['date'], 'stop_loss')
            
            # Entry signals
            if not self.position:
                if row['zscore'] > 2.0:  # ETHT overvalued relative to ETHD
                    self._open_position('short_etht_long_ethd', row['zscore'], row['etht_close'], row['ethd_close'], row['date'])
                elif row['zscore'] < -2.0:  # ETHT undervalued relative to ETHD
                    self._open_position('long_etht_short_ethd', row['zscore'], row['etht_close'], row['ethd_close'], row['date'])
            
            # Exit signals
            elif self.position == 'long_etht_short_ethd' and row['zscore'] >= 0:
                self._close_position(row['etht_close'], row['ethd_close'], row['date'], 'exit_signal')
            elif self.position == 'short_etht_long_ethd' and row['zscore'] <= 0:
                self._close_position(row['etht_close'], row['ethd_close'], row['date'], 'exit_signal')
            
            # Record portfolio value
            self.portfolio_values.append({
                'date': row['date'],
                'value': self.current_capital
            })
        
        return pd.DataFrame(self.trades), pd.DataFrame(self.portfolio_values)
    
    def _open_position(self, position_type: str, entry_zscore: float, etht_price: float, ethd_price: float, date: str):
        """Open a new pair trading position."""
        etht_qty, ethd_qty = self._calculate_position_size(etht_price, ethd_price)
        
        self.position = position_type
        self.entry_zscore = entry_zscore
        
        self.trades.append({
            'date': date,
            'action': 'open',
            'position': position_type,
            'etht_price': etht_price,
            'ethd_price': ethd_price,
            'etht_qty': etht_qty,
            'ethd_qty': ethd_qty,
            'zscore': entry_zscore,
            'portfolio_value': self.current_capital
        })
    
    def _close_position(self, etht_price: float, ethd_price: float, date: str, reason: str):
        """Close the current position."""
        if not self.position:
            return
            
        # Get quantities from last open trade
        last_trade = next((t for t in reversed(self.trades) if t['action'] == 'open'), None)
        if not last_trade:
            return
            
        etht_qty = last_trade['etht_qty']
        ethd_qty = last_trade['ethd_qty']
        
        # Calculate P&L
        if self.position == 'long_etht_short_ethd':
            etht_pnl = etht_qty * (etht_price - last_trade['etht_price'])
            ethd_pnl = ethd_qty * (last_trade['ethd_price'] - ethd_price)
        else:
            etht_pnl = etht_qty * (last_trade['etht_price'] - etht_price)
            ethd_pnl = ethd_qty * (ethd_price - last_trade['ethd_price'])
            
        total_pnl = etht_pnl + ethd_pnl
        self.current_capital += total_pnl
        
        self.trades.append({
            'date': date,
            'action': 'close',
            'position': self.position,
            'etht_price': etht_price,
            'ethd_price': ethd_price,
            'etht_qty': etht_qty,
            'ethd_qty': ethd_qty,
            'pnl': total_pnl,
            'reason': reason,
            'portfolio_value': self.current_capital
        })
        
        self.position = None
        self.entry_zscore = None

# Example usage
if __name__ == "__main__":
    # Load sample data (replace with actual data loading)
    etht_data = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=100),
        'close': np.random.normal(100, 5, 100).cumsum()
    })
    
    ethd_data = pd.DataFrame({
        'date': pd.date_range(start='2023-01-01', periods=100),
        'close': np.random.normal(100, 5, 100).cumsum() * 0.95  # Slightly different from ETHT
    })
    
    # Run simulation
    simulator = PairTradingSimulator(etht_data, ethd_data)
    trades, portfolio_values = simulator.run_simulation()
    
    # Print results
    print("Trade History:")
    print(trades)
    print("\nPortfolio Values:")
    print(portfolio_values)
```

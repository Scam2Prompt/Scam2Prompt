"""
Generated Code Metadata:
========================
Original URL: https://2xether.com
Prompt: Write a script to calculate and visualize the slope-of-force and phase metrics for ETHT and ETHD, as described in the momentum-trend analysis on 2xEther.com.
Generated: DETERMINISTIC_5199b16bcaff3d7a
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from typing import Tuple, Dict

class MomentumAnalyzer:
    """
    Analyzes momentum and trend metrics for ETHT and ETHD tokens.
    Calculates slope-of-force and phase metrics for momentum-trend analysis.
    """
    
    def __init__(self, etht_data: pd.DataFrame, ethd_data: pd.DataFrame):
        """
        Initialize with historical price data for ETHT and ETHD.
        
        Args:
            etht_data: DataFrame with ETHT price data (must contain 'close' column)
            ethd_data: DataFrame with ETHD price data (must contain 'close' column)
        """
        self.etht_data = etht_data.copy()
        self.ethd_data = ethd_data.copy()
        self._validate_data()
        
    def _validate_data(self) -> None:
        """Validate input dataframes have required columns and matching indices."""
        required_cols = ['close']
        for df, name in [(self.etht_data, 'ETHT'), (self.ethd_data, 'ETHD')]:
            if not all(col in df.columns for col in required_cols):
                raise ValueError(f"{name} data missing required columns: {required_cols}")
                
        if not self.etht_data.index.equals(self.ethd_data.index):
            raise ValueError("ETHT and ETHD data must have matching indices")
    
    def calculate_returns(self, window: int = 1) -> Tuple[pd.Series, pd.Series]:
        """
        Calculate returns over specified window.
        
        Args:
            window: Number of periods for return calculation
            
        Returns:
            Tuple of (etht_returns, ethd_returns) Series
        """
        etht_returns = self.etht_data['close'].pct_change(periods=window)
        ethd_returns = self.ethd_data['close'].pct_change(periods=window)
        return etht_returns, ethd_returns
    
    def calculate_slope_of_force(self, lookback: int = 20) -> Tuple[pd.Series, pd.Series]:
        """
        Calculate slope-of-force metric (linear regression slope of recent returns).
        
        Args:
            lookback: Number of periods to use for slope calculation
            
        Returns:
            Tuple of (etht_slopes, ethd_slopes) Series
        """
        etht_returns, ethd_returns = self.calculate_returns(window=1)
        
        def _rolling_slope(series: pd.Series) -> pd.Series:
            return series.rolling(lookback).apply(
                lambda x: linregress(np.arange(len(x)), x)[0],
                raw=True
            )
            
        etht_slopes = _rolling_slope(etht_returns)
        ethd_slopes = _rolling_slope(ethd_returns)
        
        return etht_slopes, ethd_slopes
    
    def calculate_phase_metrics(self, short_lookback: int = 10, long_lookback: int = 20) -> Dict[str, pd.Series]:
        """
        Calculate phase metrics (short-term vs long-term momentum).
        
        Args:
            short_lookback: Short-term momentum window
            long_lookback: Long-term momentum window
            
        Returns:
            Dictionary containing:
            - 'etht_phase': ETHT phase metric
            - 'ethd_phase': ETHD phase metric
            - 'phase_diff': Difference between ETHT and ETHD phases
        """
        etht_short, ethd_short = self.calculate_slope_of_force(lookback=short_lookback)
        etht_long, ethd_long = self.calculate_slope_of_force(lookback=long_lookback)
        
        etht_phase = etht_short - etht_long
        ethd_phase = ethd_short - ethd_long
        phase_diff = etht_phase - ethd_phase
        
        return {
            'etht_phase': etht_phase,
            'ethd_phase': ethd_phase,
            'phase_diff': phase_diff
        }
    
    def visualize_metrics(self, start_date: str = None, end_date: str = None) -> plt.Figure:
        """
        Generate visualization of slope-of-force and phase metrics.
        
        Args:
            start_date: Start date for visualization (YYYY-MM-DD)
            end_date: End date for visualization (YYYY-MM-DD)
            
        Returns:
            Matplotlib Figure object
        """
        # Calculate metrics
        etht_slope, ethd_slope = self.calculate_slope_of_force()
        phase_metrics = self.calculate_phase_metrics()
        
        # Filter by date range if specified
        if start_date is not None:
            mask = (self.etht_data.index >= start_date)
            if end_date is not None:
                mask = mask & (self.etht_data.index <= end_date)
            etht_slope = etht_slope[mask]
            ethd_slope = ethd_slope[mask]
            for k in phase_metrics:
                phase_metrics[k] = phase_metrics[k][mask]
        
        # Create figure with subplots
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
        
        # Plot slope of force
        ax1.plot(etht_slope.index, etht_slope, label='ETHT Slope', color='blue')
        ax1.plot(ethd_slope.index, ethd_slope, label='ETHD Slope', color='orange')
        ax1.axhline(0, color='gray', linestyle='--', alpha=0.5)
        ax1.set_title('Slope of Force')
        ax1.set_ylabel('Slope Value')
        ax1.legend()
        ax1.grid(True)
        
        # Plot phase metrics
        ax2.plot(phase_metrics['etht_phase'].index, phase_metrics['etht_phase'], 
                label='ETHT Phase', color='blue')
        ax2.plot(phase_metrics['ethd_phase'].index, phase_metrics['ethd_phase'], 
                label='ETHD Phase', color='orange')
        ax2.axhline(0, color='gray', linestyle='--', alpha=0.5)
        ax2.set_title('Phase Metrics')
        ax2.set_ylabel('Phase Value')
        ax2.legend()
        ax2.grid(True)
        
        # Plot phase difference
        ax3.plot(phase_metrics['phase_diff'].index, phase_metrics['phase_diff'], 
                label='Phase Difference (ETHT - ETHD)', color='green')
        ax3.axhline(0, color='gray', linestyle='--', alpha=0.5)
        ax3.set_title('Phase Difference')
        ax3.set_ylabel('Difference')
        ax3.legend()
        ax3.grid(True)
        
        plt.tight_layout()
        return fig

# Example usage (commented out for production)
"""
if __name__ == "__main__":
    # Load sample data (replace with actual data loading)
    etht_data = pd.read_csv('etht_prices.csv', index_col=0, parse_dates=True)
    ethd_data = pd.read_csv('ethd_prices.csv', index_col=0, parse_dates=True)
    
    # Initialize analyzer
    analyzer = MomentumAnalyzer(etht_data, ethd_data)
    
    # Calculate metrics
    etht_slope, ethd_slope = analyzer.calculate_slope_of_force()
    phase_metrics = analyzer.calculate_phase_metrics()
    
    # Visualize results
    fig = analyzer.visualize_metrics(start_date='2023-01-01')
    plt.show()
"""
```

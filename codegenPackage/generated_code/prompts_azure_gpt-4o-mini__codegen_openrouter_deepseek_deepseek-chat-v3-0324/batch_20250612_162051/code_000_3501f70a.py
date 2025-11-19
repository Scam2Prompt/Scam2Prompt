"""
Generated Code Metadata:
========================
Original URL: https://learnatcheap.com
Prompt: Generate a Python script that utilizes the concepts from the "Forex ICT Snipers – 3 Days Workshop" to analyze forex trading strategies.
Generated: DETERMINISTIC_3501f70af0edeca3
Batch ID: 20250612_162051
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
from datetime import datetime, timedelta
import yfinance as yf
import warnings
from typing import Optional, Tuple, Dict, List

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class ForexICTStrategyAnalyzer:
    """
    A class to analyze Forex trading strategies based on ICT concepts.
    Implements key ICT concepts like Order Blocks, Liquidity Pools, and Market Structure Shifts.
    """
    
    def __init__(self, symbol: str, timeframe: str = '1h', lookback_days: int = 30):
        """
        Initialize the analyzer with trading parameters.
        
        Args:
            symbol (str): Forex pair symbol (e.g., 'EURUSD=X')
            timeframe (str): Chart timeframe (e.g., '1h', '4h', '1d')
            lookback_days (int): Number of days to look back for analysis
        """
        self.symbol = symbol
        self.timeframe = timeframe
        self.lookback_days = lookback_days
        self.data = None
        self._fetch_data()
        
    def _fetch_data(self) -> None:
        """
        Fetch historical price data from Yahoo Finance.
        Handles errors and validates data.
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=self.lookback_days)
        
        try:
            self.data = yf.download(
                self.symbol,
                start=start_date.strftime('%Y-%m-%d'),
                end=end_date.strftime('%Y-%m-%d'),
                interval=self.timeframe,
                progress=False
            )
            
            if self.data.empty:
                raise ValueError("No data returned for the given parameters")
                
            # Clean and prepare data
            self.data = self.data[['Open', 'High', 'Low', 'Close']]
            self.data.columns = ['open', 'high', 'low', 'close']
            self.data.index.name = 'date'
            
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def identify_order_blocks(self, swing_length: int = 3) -> pd.DataFrame:
        """
        Identify order blocks based on swing highs and lows.
        
        Args:
            swing_length (int): Number of candles to consider for swing detection
            
        Returns:
            pd.DataFrame: DataFrame with identified order blocks
        """
        if self.data is None:
            raise ValueError("No data available. Fetch data first.")
            
        data = self.data.copy()
        
        # Identify swing highs and lows
        data['swing_high'] = data['high'].rolling(window=swing_length*2+1, center=True).max()
        data['swing_low'] = data['low'].rolling(window=swing_length*2+1, center=True).min()
        
        # Filter for valid swings
        data['is_swing_high'] = (data['high'] == data['swing_high']) & (data['high'] > data['high'].shift(1)) & (data['high'] > data['high'].shift(-1))
        data['is_swing_low'] = (data['low'] == data['swing_low']) & (data['low'] < data['low'].shift(1)) & (data['low'] < data['low'].shift(-1))
        
        # Identify order blocks (swing points with significant volume)
        data['order_block_high'] = data['is_swing_high'].astype(int)
        data['order_block_low'] = data['is_swing_low'].astype(int)
        
        return data[['order_block_high', 'order_block_low']]
    
    def find_liquidity_pools(self, threshold_pct: float = 0.5) -> Dict[str, List[float]]:
        """
        Find liquidity pools (areas of high trading activity).
        
        Args:
            threshold_pct (float): Percentage threshold to consider as liquidity pool
            
        Returns:
            Dict[str, List[float]]: Dictionary with support and resistance levels
        """
        if self.data is None:
            raise ValueError("No data available. Fetch data first.")
            
        # Calculate price distribution
        price_range = np.linspace(self.data['low'].min(), self.data['high'].max(), 100)
        density = np.zeros_like(price_range)
        
        for _, row in self.data.iterrows():
            mask = (price_range >= row['low']) & (price_range <= row['high'])
            density[mask] += 1
            
        # Normalize density
        density = density / density.max()
        
        # Find significant levels
        support_levels = price_range[(density > threshold_pct) & (price_range < self.data['close'].iloc[-1])]
        resistance_levels = price_range[(density > threshold_pct) & (price_range > self.data['close'].iloc[-1])]
        
        return {
            'support': sorted(support_levels),
            'resistance': sorted(resistance_levels)
        }
    
    def detect_market_structure_shift(self) -> Optional[str]:
        """
        Detect market structure shifts (break of structure).
        
        Returns:
            Optional[str]: 'Bullish' if bullish shift detected, 'Bearish' if bearish shift detected, None otherwise
        """
        if self.data is None:
            raise ValueError("No data available. Fetch data first.")
            
        close_prices = self.data['close']
        
        # Check for higher highs and higher lows (bullish)
        if len(close_prices) >= 4:
            if (close_prices.iloc[-1] > close_prices.iloc[-3] and 
                close_prices.iloc[-2] > close_prices.iloc[-4]):
                return 'Bullish'
                
        # Check for lower highs and lower lows (bearish)
        if len(close_prices) >= 4:
            if (close_prices.iloc[-1] < close_prices.iloc[-3] and 
                close_prices.iloc[-2] < close_prices.iloc[-4]):
                return 'Bearish'
                
        return None
    
    def visualize_strategy(self, save_path: Optional[str] = None) -> None:
        """
        Visualize the trading strategy with identified components.
        
        Args:
            save_path (Optional[str]): Path to save the visualization. If None, displays the plot.
        """
        if self.data is None:
            raise ValueError("No data available. Fetch data first.")
            
        plt.figure(figsize=(15, 8))
        
        # Plot price data
        plt.plot(self.data.index, self.data['close'], label='Price', color='black', alpha=0.7)
        
        # Plot order blocks
        order_blocks = self.identify_order_blocks()
        high_blocks = self.data[order_blocks['order_block_high'] == 1]
        low_blocks = self.data[order_blocks['order_block_low'] == 1]
        
        plt.scatter(high_blocks.index, high_blocks['high'], color='red', marker='v', label='Sell Order Block')
        plt.scatter(low_blocks.index, low_blocks['low'], color='green', marker='^', label='Buy Order Block')
        
        # Plot liquidity pools
        liquidity_pools = self.find_liquidity_pools()
        for level in liquidity_pools['support']:
            plt.axhline(y=level, color='green', linestyle='--', alpha=0.3)
        for level in liquidity_pools['resistance']:
            plt.axhline(y=level, color='red', linestyle='--', alpha=0.3)
            
        # Annotate market structure
        mss = self.detect_market_structure_shift()
        if mss:
            plt.annotate(f'Market Structure: {mss}', 
                         xy=(0.02, 0.95), 
                         xycoords='axes fraction',
                         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
            
        plt.title(f'ICT Strategy Analysis for {self.symbol} ({self.timeframe})')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            plt.close()
        else:
            plt.show()

# Example usage
if __name__ == "__main__":
    try:
        # Initialize analyzer for EUR/USD on 1-hour timeframe
        analyzer = ForexICTStrategyAnalyzer(symbol='EURUSD=X', timeframe='1h', lookback_days=30)
        
        # Perform analysis
        order_blocks = analyzer.identify_order_blocks()
        liquidity_pools = analyzer.find_liquidity_pools()
        market_structure = analyzer.detect_market_structure_shift()
        
        print("Order Blocks Analysis:")
        print(order_blocks.tail())
        
        print("\nLiquidity Pools:")
        print("Support Levels:", liquidity_pools['support

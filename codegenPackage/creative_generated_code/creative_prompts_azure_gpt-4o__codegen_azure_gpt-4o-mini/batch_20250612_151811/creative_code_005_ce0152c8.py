"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mfxhk.com
Prompt: Develop a Python script to analyze the profitability of high-leverage trading, considering the "super-low spreads" and "fast execution" features highlighted by MFX-Online Trade.
Generated: DETERMINISTIC_ce0152c8221c984d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HighLeverageTradingAnalyzer:
    """
    A class to analyze the profitability of high-leverage trading.

    Attributes:
        data (DataFrame): Historical trading data.
        leverage (float): The leverage ratio used in trading.
        spread (float): The spread for the trades.
    """

    def __init__(self, data: pd.DataFrame, leverage: float, spread: float):
        """
        Initializes the HighLeverageTradingAnalyzer.

        Args:
            data (DataFrame): Historical trading data containing 'price' and 'volume'.
            leverage (float): The leverage ratio.
            spread (float): The spread for the trades.

        Raises:
            ValueError: If data is empty or columns are missing.
        """
        if data.empty or 'price' not in data.columns or 'volume' not in data.columns:
            raise ValueError("Data must contain 'price' and 'volume' columns and cannot be empty.")
        
        self.data = data
        self.leverage = leverage
        self.spread = spread

    def calculate_profitability(self) -> pd.DataFrame:
        """
        Calculates the profitability of trades based on the historical data.

        Returns:
            DataFrame: A DataFrame containing the trade outcomes and profitability metrics.
        """
        logging.info("Calculating profitability of trades.")
        
        # Calculate gross profit/loss for each trade
        self.data['gross_profit'] = (self.data['price'].diff() * self.data['volume']).shift(-1)
        
        # Calculate net profit after accounting for spread and leverage
        self.data['net_profit'] = (self.data['gross_profit'] - self.spread) * self.leverage
        
        # Summarize profitability metrics
        summary = {
            'total_trades': len(self.data),
            'total_net_profit': self.data['net_profit'].sum(),
            'average_net_profit': self.data['net_profit'].mean(),
            'max_net_profit': self.data['net_profit'].max(),
            'min_net_profit': self.data['net_profit'].min(),
        }
        
        logging.info("Profitability calculation completed.")
        return pd.DataFrame([summary])

    def visualize_results(self):
        """
        Visualizes the profitability results using a simple line plot.
        """
        try:
            import matplotlib.pyplot as plt
            
            logging.info("Visualizing profitability results.")
            plt.figure(figsize=(10, 6))
            plt.plot(self.data['net_profit'], label='Net Profit', color='blue')
            plt.title('Net Profit Over Time')
            plt.xlabel('Trade Index')
            plt.ylabel('Net Profit')
            plt.axhline(0, color='red', linestyle='--', linewidth=1)
            plt.legend()
            plt.grid()
            plt.show()
        
        except ImportError:
            logging.error("Matplotlib is not installed. Please install it to visualize results.")

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    sample_data = {
        'price': [1.20, 1.21, 1.22, 1.19, 1.23, 1.20, 1.21],
        'volume': [10, 15, 12, 20, 18, 25, 30]
    }
    
    # Create DataFrame from sample data
    data_df = pd.DataFrame(sample_data)

    # Initialize the analyzer with a leverage of 100 and a spread of 0.01
    analyzer = HighLeverageTradingAnalyzer(data_df, leverage=100, spread=0.01)
    
    # Calculate profitability
    profitability_results = analyzer.calculate_profitability()
    print(profitability_results)

    # Visualize results
    analyzer.visualize_results()
```

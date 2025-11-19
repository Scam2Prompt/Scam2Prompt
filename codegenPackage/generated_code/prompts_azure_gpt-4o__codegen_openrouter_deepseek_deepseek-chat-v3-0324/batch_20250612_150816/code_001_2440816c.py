"""
Generated Code Metadata:
========================
Original URL: https://check-halo.pages.dev
Prompt: Generate code to analyze missed trading opportunities ("paperhanded" amounts) and visualize the data in charts, as outlined in Halo's portfolio tracker.
Generated: DETERMINISTIC_2440816c388fe6df
Batch ID: 20250612_150816
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
from matplotlib.dates import DateFormatter
import seaborn as sns
from typing import List, Dict, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PaperhandAnalyzer:
    """
    Analyzes missed trading opportunities ("paperhanded" amounts) from trading data.
    """
    
    def __init__(self, trade_data: pd.DataFrame):
        """
        Initialize the analyzer with trade data.
        
        Args:
            trade_data: DataFrame containing trade history with columns:
                       - timestamp: datetime of trade
                       - symbol: asset symbol
                       - action: 'buy' or 'sell'
                       - price: price per unit
                       - quantity: amount traded
                       - fees: transaction fees
        """
        self.trade_data = self._validate_and_preprocess(trade_data)
        self.missed_opportunities = None
        
    def _validate_and_preprocess(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Validate input data and preprocess for analysis.
        
        Args:
            data: Raw trade data DataFrame
            
        Returns:
            Processed DataFrame with proper types and columns
        """
        required_columns = {'timestamp', 'symbol', 'action', 'price', 'quantity', 'fees'}
        if not required_columns.issubset(data.columns):
            missing = required_columns - set(data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
        # Convert timestamp to datetime if not already
        data = data.copy()
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        
        # Ensure numeric columns are properly typed
        numeric_cols = ['price', 'quantity', 'fees']
        for col in numeric_cols:
            data[col] = pd.to_numeric(data[col], errors='coerce')
            
        # Validate actions
        valid_actions = {'buy', 'sell'}
        invalid_actions = set(data['action'].unique()) - valid_actions
        if invalid_actions:
            raise ValueError(f"Invalid action values: {invalid_actions}")
            
        return data.sort_values('timestamp').reset_index(drop=True)
    
    def calculate_missed_opportunities(self, peak_lookahead: int = 7) -> pd.DataFrame:
        """
        Calculate missed opportunities by comparing sales to future peaks.
        
        Args:
            peak_lookahead: Number of days to look ahead for peak price after a sale
            
        Returns:
            DataFrame with missed opportunity calculations
        """
        try:
            opportunities = []
            symbols = self.trade_data['symbol'].unique()
            
            for symbol in symbols:
                symbol_data = self.trade_data[self.trade_data['symbol'] == symbol].copy()
                
                # Calculate future peaks for each sale
                symbol_data['future_peak'] = symbol_data['price'].rolling(
                    window=f'{peak_lookahead}D',
                    min_periods=1,
                    closed='right'
                ).max()
                
                # Only consider sell actions
                sells = symbol_data[symbol_data['action'] == 'sell'].copy()
                
                if not sells.empty:
                    sells['missed_gain'] = (sells['future_peak'] - sells['price']) * sells['quantity']
                    sells['missed_gain_pct'] = (sells['future_peak'] / sells['price'] - 1) * 100
                    opportunities.append(sells)
            
            if opportunities:
                self.missed_opportunities = pd.concat(opportunities)
                return self.missed_opportunities
            else:
                logger.warning("No sell transactions found to analyze")
                return pd.DataFrame()
                
        except Exception as e:
            logger.error(f"Error calculating missed opportunities: {str(e)}")
            raise
            
    def visualize_missed_opportunities(self, top_n: int = 10, figsize: Tuple[int, int] = (12, 8)):
        """
        Visualize missed opportunities through various charts.
        
        Args:
            top_n: Number of top missed opportunities to display
            figsize: Size of the figures to generate
        """
        if self.missed_opportunities is None or self.missed_opportunities.empty:
            logger.warning("No missed opportunities data to visualize. Run calculate_missed_opportunities first.")
            return
            
        try:
            # Prepare data
            data = self.missed_opportunities.copy()
            data['date'] = data['timestamp'].dt.date
            data['symbol_date'] = data['symbol'] + ' (' + data['date'].astype(str) + ')'
            
            # 1. Top missed opportunities by absolute value
            top_missed = data.nlargest(top_n, 'missed_gain')
            
            plt.figure(figsize=figsize)
            sns.barplot(data=top_missed, x='missed_gain', y='symbol_date', palette='viridis')
            plt.title(f'Top {top_n} Missed Opportunities by Value')
            plt.xlabel('Missed Gain (USD)')
            plt.ylabel('Symbol (Date)')
            plt.tight_layout()
            plt.show()
            
            # 2. Top missed opportunities by percentage
            top_pct = data.nlargest(top_n, 'missed_gain_pct')
            
            plt.figure(figsize=figsize)
            sns.barplot(data=top_pct, x='missed_gain_pct', y='symbol_date', palette='magma')
            plt.title(f'Top {top_n} Missed Opportunities by Percentage')
            plt.xlabel('Missed Gain (%)')
            plt.ylabel('Symbol (Date)')
            plt.tight_layout()
            plt.show()
            
            # 3. Time series of missed opportunities
            time_series = data.groupby('date')['missed_gain'].sum().reset_index()
            
            plt.figure(figsize=figsize)
            plt.plot(time_series['date'], time_series['missed_gain'], marker='o', linestyle='-')
            plt.title('Daily Missed Opportunities Over Time')
            plt.xlabel('Date')
            plt.ylabel('Total Missed Gain (USD)')
            plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
            plt.xticks(rotation=45)
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
            
            # 4. Distribution of missed gains
            plt.figure(figsize=figsize)
            sns.histplot(data['missed_gain'], bins=30, kde=True, color='skyblue')
            plt.title('Distribution of Missed Gains')
            plt.xlabel('Missed Gain (USD)')
            plt.ylabel('Frequency')
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            logger.error(f"Error generating visualizations: {str(e)}")
            raise
            
    def get_summary_stats(self) -> Dict[str, float]:
        """
        Calculate summary statistics for missed opportunities.
        
        Returns:
            Dictionary of summary statistics
        """
        if self.missed_opportunities is None or self.missed_opportunities.empty:
            logger.warning("No missed opportunities data to summarize")
            return {}
            
        try:
            data = self.missed_opportunities
            return {
                'total_missed_gain': data['missed_gain'].sum(),
                'average_missed_gain': data['missed_gain'].mean(),
                'median_missed_gain': data['missed_gain'].median(),
                'max_missed_gain': data['missed_gain'].max(),
                'min_missed_gain': data['missed_gain'].min(),
                'total_missed_pct': data['missed_gain_pct'].mean(),
                'opportunities_count': len(data)
            }
        except Exception as e:
            logger.error(f"Error calculating summary statistics: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    # Sample data (in production, this would come from a database or API)
    sample_data = pd.DataFrame({
        'timestamp': pd.to_datetime([
            '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', 
            '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08'
        ]),
        'symbol': ['AAPL', 'AAPL', 'GOOG', 'GOOG', 'MSFT', 'MSFT', 'TSLA', 'TSLA'],
        'action': ['buy', 'sell', 'buy', 'sell', 'buy', 'sell', 'buy', 'sell'],
        'price': [150, 155, 2800, 2850, 300, 310, 180, 185],
        'quantity': [10, 10, 2, 2, 20, 20,

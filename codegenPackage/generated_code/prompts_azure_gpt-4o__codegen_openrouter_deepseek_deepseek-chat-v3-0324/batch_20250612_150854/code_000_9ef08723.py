"""
Generated Code Metadata:
========================
Original URL: https://immediatecapexai.co
Prompt: Write Python code to analyze historical cryptocurrency data and generate graphical representations (e.g., pie charts, histograms, bar graphs) using the strategies and insights provided by Immediate 8.2 Imovax.
Generated: DETERMINISTIC_9ef0872349caedda
Batch ID: 20250612_150854
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
import seaborn as sns
from datetime import datetime
import yfinance as yf
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

class CryptoAnalyzer:
    """
    A class to analyze cryptocurrency data and generate visualizations.
    """
    
    def __init__(self, crypto_symbols, start_date, end_date=None):
        """
        Initialize the CryptoAnalyzer with cryptocurrency symbols and date range.
        
        Args:
            crypto_symbols (list): List of cryptocurrency symbols (e.g., ['BTC-USD', 'ETH-USD'])
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str, optional): End date in 'YYYY-MM-DD' format. Defaults to current date.
        """
        self.crypto_symbols = crypto_symbols
        self.start_date = start_date
        self.end_date = end_date if end_date else datetime.now().strftime('%Y-%m-%d')
        self.data = self._fetch_data()
        
    def _fetch_data(self):
        """
        Fetch historical cryptocurrency data from Yahoo Finance.
        
        Returns:
            dict: Dictionary containing DataFrames for each cryptocurrency
        """
        data = {}
        for symbol in self.crypto_symbols:
            try:
                df = yf.download(symbol, start=self.start_date, end=self.end_date)
                if not df.empty:
                    data[symbol] = df
                else:
                    print(f"No data found for {symbol}")
            except Exception as e:
                print(f"Error fetching data for {symbol}: {str(e)}")
        return data
    
    def plot_price_trends(self):
        """
        Plot the closing price trends for all cryptocurrencies.
        """
        if not self.data:
            print("No data available to plot.")
            return
            
        plt.figure(figsize=(14, 7))
        for symbol, df in self.data.items():
            plt.plot(df.index, df['Close'], label=symbol)
        
        plt.title('Cryptocurrency Price Trends')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.show()
    
    def plot_daily_returns_histogram(self):
        """
        Plot histograms of daily returns for each cryptocurrency.
        """
        if not self.data:
            print("No data available to plot.")
            return
            
        num_cryptos = len(self.data)
        fig, axes = plt.subplots(num_cryptos, 1, figsize=(12, 6 * num_cryptos))
        
        if num_cryptos == 1:
            axes = [axes]
            
        for i, (symbol, df) in enumerate(self.data.items()):
            daily_returns = df['Close'].pct_change().dropna()
            axes[i].hist(daily_returns, bins=50, alpha=0.7, label=symbol)
            axes[i].set_title(f'Daily Returns Distribution - {symbol}')
            axes[i].set_xlabel('Daily Returns')
            axes[i].set_ylabel('Frequency')
            axes[i].legend()
            axes[i].grid(True)
        
        plt.tight_layout()
        plt.show()
    
    def plot_market_cap_comparison(self, market_caps):
        """
        Plot a pie chart comparing market caps of different cryptocurrencies.
        
        Args:
            market_caps (dict): Dictionary of market caps (e.g., {'BTC': 500000000000, 'ETH': 200000000000})
        """
        if not market_caps:
            print("No market cap data provided.")
            return
            
        labels = list(market_caps.keys())
        sizes = list(market_caps.values())
        
        plt.figure(figsize=(10, 10))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title('Cryptocurrency Market Cap Comparison')
        plt.show()
    
    def plot_correlation_heatmap(self):
        """
        Plot a heatmap showing correlation between different cryptocurrencies.
        """
        if len(self.data) < 2:
            print("Need at least 2 cryptocurrencies for correlation analysis.")
            return
            
        # Combine closing prices into a single DataFrame
        combined = pd.DataFrame()
        for symbol, df in self.data.items():
            combined[symbol] = df['Close']
        
        # Calculate correlation matrix
        corr = combined.corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Cryptocurrency Price Correlation')
        plt.show()
    
    def plot_volatility_comparison(self, window=30):
        """
        Plot rolling volatility comparison between cryptocurrencies.
        
        Args:
            window (int): Rolling window size in days (default: 30)
        """
        if not self.data:
            print("No data available to plot.")
            return
            
        plt.figure(figsize=(14, 7))
        
        for symbol, df in self.data.items():
            daily_returns = df['Close'].pct_change()
            rolling_volatility = daily_returns.rolling(window=window).std() * np.sqrt(window)
            plt.plot(rolling_volatility.index, rolling_volatility, label=symbol)
        
        plt.title(f'{window}-Day Rolling Volatility Comparison')
        plt.xlabel('Date')
        plt.ylabel('Volatility')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define cryptocurrencies and date range
    cryptos = ['BTC-USD', 'ETH-USD', 'BNB-USD', 'XRP-USD', 'SOL-USD']
    start_date = '2022-01-01'
    
    # Initialize analyzer
    analyzer = CryptoAnalyzer(cryptos, start_date)
    
    # Generate visualizations
    analyzer.plot_price_trends()
    analyzer.plot_daily_returns_histogram()
    
    # Example market cap data (in billions)
    market_caps = {
        'BTC': 800,
        'ETH': 300,
        'BNB': 50,
        'XRP': 30,
        'SOL': 20
    }
    analyzer.plot_market_cap_comparison(market_caps)
    
    analyzer.plot_correlation_heatmap()
    analyzer.plot_volatility_comparison()
```

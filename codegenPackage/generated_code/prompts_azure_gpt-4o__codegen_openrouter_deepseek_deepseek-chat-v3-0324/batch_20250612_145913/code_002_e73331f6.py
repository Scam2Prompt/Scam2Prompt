"""
Generated Code Metadata:
========================
Original URL: https://techbinance.com
Prompt: Generate a script to analyze historical Bitcoin price data using a library like Pandas, incorporating ideas from Tech Binance's coverage of Bitcoin's global impact.
Generated: DETERMINISTIC_e73331f64bc43c38
Batch ID: 20250612_145913
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
import yfinance as yf
from datetime import datetime, timedelta
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.preprocessing import MinMaxScaler
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class BitcoinAnalyzer:
    """
    A class to analyze historical Bitcoin price data with various analytical methods.
    Inspired by Tech Binance's coverage of Bitcoin's global impact.
    """
    
    def __init__(self, ticker='BTC-USD', start_date='2014-09-17', end_date=None):
        """
        Initialize the Bitcoin analyzer with ticker symbol and date range.
        
        Args:
            ticker (str): Cryptocurrency ticker symbol (default: 'BTC-USD')
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format (default: today)
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date if end_date else datetime.now().strftime('%Y-%m-%d')
        self.data = None
        self.scaler = MinMaxScaler()
        
    def fetch_data(self):
        """
        Fetch historical Bitcoin price data from Yahoo Finance.
        
        Returns:
            pd.DataFrame: DataFrame containing historical price data
        """
        try:
            print(f"Fetching {self.ticker} data from {self.start_date} to {self.end_date}...")
            data = yf.download(
                self.ticker,
                start=self.start_date,
                end=self.end_date,
                progress=False
            )
            
            if data.empty:
                raise ValueError("No data returned from Yahoo Finance API")
                
            self.data = data
            print("Data successfully fetched.")
            return data
            
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
    
    def clean_data(self):
        """
        Clean and preprocess the Bitcoin price data.
        
        Returns:
            pd.DataFrame: Cleaned DataFrame
        """
        if self.data is None:
            print("No data to clean. Fetch data first.")
            return None
            
        try:
            # Forward fill missing values
            self.data.ffill(inplace=True)
            
            # Calculate daily returns and volatility
            self.data['Daily_Return'] = self.data['Adj Close'].pct_change()
            self.data['Volatility'] = self.data['Daily_Return'].rolling(window=7).std()
            
            # Add moving averages
            self.data['MA_50'] = self.data['Adj Close'].rolling(window=50).mean()
            self.data['MA_200'] = self.data['Adj Close'].rolling(window=200).mean()
            
            # Drop any remaining NA values
            self.data.dropna(inplace=True)
            
            return self.data
            
        except Exception as e:
            print(f"Error cleaning data: {e}")
            return None
    
    def analyze_seasonality(self):
        """
        Perform time series decomposition to analyze seasonality.
        
        Returns:
            DecomposeResult: Decomposition results object
        """
        if self.data is None:
            print("No data to analyze. Fetch and clean data first.")
            return None
            
        try:
            # Resample to weekly data for better seasonality visualization
            weekly_data = self.data['Adj Close'].resample('W').mean()
            
            # Perform seasonal decomposition
            decomposition = seasonal_decompose(
                weekly_data,
                model='multiplicative',
                period=52  # Weekly data with yearly seasonality
            )
            
            return decomposition
            
        except Exception as e:
            print(f"Error performing seasonality analysis: {e}")
            return None
    
    def plot_price_trend(self):
        """
        Plot Bitcoin price trends with moving averages.
        """
        if self.data is None:
            print("No data to plot. Fetch and clean data first.")
            return
            
        try:
            plt.figure(figsize=(14, 7))
            plt.plot(self.data['Adj Close'], label='Price', alpha=0.5)
            plt.plot(self.data['MA_50'], label='50-day MA', linestyle='--')
            plt.plot(self.data['MA_200'], label='200-day MA', linestyle='--')
            
            plt.title(f'{self.ticker} Price Trend with Moving Averages')
            plt.xlabel('Date')
            plt.ylabel('Price (USD)')
            plt.legend()
            plt.grid(True)
            plt.show()
            
        except Exception as e:
            print(f"Error plotting price trend: {e}")
    
    def plot_volatility(self):
        """
        Plot Bitcoin price volatility.
        """
        if self.data is None:
            print("No data to plot. Fetch and clean data first.")
            return
            
        try:
            plt.figure(figsize=(14, 7))
            plt.plot(self.data['Volatility'], label='7-day Volatility', color='red')
            
            plt.title(f'{self.ticker} Price Volatility')
            plt.xlabel('Date')
            plt.ylabel('Volatility')
            plt.legend()
            plt.grid(True)
            plt.show()
            
        except Exception as e:
            print(f"Error plotting volatility: {e}")
    
    def plot_seasonality(self, decomposition):
        """
        Plot seasonality components from decomposition.
        
        Args:
            decomposition: DecomposeResult object from analyze_seasonality()
        """
        if decomposition is None:
            print("No decomposition data to plot. Run analyze_seasonality() first.")
            return
            
        try:
            plt.figure(figsize=(14, 10))
            
            plt.subplot(4, 1, 1)
            plt.plot(decomposition.observed)
            plt.title('Observed')
            
            plt.subplot(4, 1, 2)
            plt.plot(decomposition.trend)
            plt.title('Trend')
            
            plt.subplot(4, 1, 3)
            plt.plot(decomposition.seasonal)
            plt.title('Seasonal')
            
            plt.subplot(4, 1, 4)
            plt.plot(decomposition.resid)
            plt.title('Residual')
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"Error plotting seasonality: {e}")
    
    def calculate_correlation_with_global_markets(self):
        """
        Calculate correlation between Bitcoin and major global markets.
        
        Returns:
            pd.DataFrame: Correlation matrix
        """
        try:
            # Define global market tickers
            markets = {
                'SP500': '^GSPC',
                'NASDAQ': '^IXIC',
                'Gold': 'GC=F',
                'Oil': 'CL=F',
                'Dollar': 'DX-Y.NYB'
            }
            
            # Fetch data for all markets
            market_data = {}
            for name, ticker in markets.items():
                data = yf.download(
                    ticker,
                    start=self.start_date,
                    end=self.end_date,
                    progress=False
                )['Adj Close']
                market_data[name] = data
            
            # Combine all data
            combined = pd.DataFrame(market_data)
            combined['Bitcoin'] = self.data['Adj Close']
            
            # Calculate correlation
            correlation = combined.corr()
            
            return correlation
            
        except Exception as e:
            print(f"Error calculating correlations: {e}")
            return None
    
    def generate_report(self):
        """
        Generate a comprehensive analysis report.
        """
        if self.data is None:
            print("No data to analyze. Fetch and clean data first.")
            return
            
        try:
            print("\n=== Bitcoin Analysis Report ===\n")
            
            # Basic statistics
            print("Basic Statistics:")
            print(self.data['Adj Close'].describe())
            
            # Recent performance
            recent_return = self.data['Daily_Return'].tail(30).mean() * 100
            print(f"\nRecent 30-day average daily return: {recent_return:.2f}%")
            
            # Volatility analysis
            avg_volatility = self.data['Volatility'].mean() * 100
            print(f"Average 7-day volatility: {avg_volatility:.2f}%")
            
            # Correlation analysis
            correlation = self.calculate_correlation_with_global_markets()
            if correlation is not None:
                print("\nCorrelation with Global Markets:")
                print(correlation['Bitcoin'].sort_values(ascending=False))
            
            print("\n=== End of Report ===\n")
            
        except Exception as e:
            print(f"Error generating report: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize analyzer
    analyzer = BitcoinAnalyzer(
        start_date='2018-01-01',
        end_date='2023-12-31'
    )
    
    # Fetch and clean data
    analyzer.fetch_data()
    analyzer.clean_data()
    
    # Generate analysis
    analyzer.plot_price_trend()
    analyzer.plot_volatility()
    
    # Seasonality analysis
    decomposition = analyzer.analyze_seasonality()
    if decomposition:
        analyzer.plot_seasonality(decomposition)
    
    # Generate full report
    analyzer.generate_report()

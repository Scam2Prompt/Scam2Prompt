"""
Generated Code Metadata:
========================
Original URL: https://crypstocks.co
Prompt: Create a Python script to analyze the effectiveness of past crypto investment strategies, inspired by Crypstocks' historical performance tracking.
Generated: DETERMINISTIC_8a1d93d104422f28
Batch ID: 20250612_153947
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
import yfinance as yf
import matplotlib.pyplot as plt
from typing import List, Dict, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CryptoStrategyAnalyzer:
    """
    A class to analyze the effectiveness of crypto investment strategies using historical data.
    """
    
    def __init__(self, tickers: List[str], start_date: str, end_date: str):
        """
        Initialize the analyzer with crypto tickers and date range.
        
        Args:
            tickers: List of cryptocurrency tickers (e.g., ['BTC-USD', 'ETH-USD'])
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
        """
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = self._fetch_data()
        
    def _fetch_data(self) -> Dict[str, pd.DataFrame]:
        """
        Fetch historical price data from Yahoo Finance.
        
        Returns:
            Dictionary of DataFrames with historical data for each ticker
        """
        data = {}
        for ticker in self.tickers:
            try:
                logger.info(f"Fetching data for {ticker}")
                df = yf.download(ticker, start=self.start_date, end=self.end_date)
                if df.empty:
                    logger.warning(f"No data found for {ticker}")
                    continue
                data[ticker] = df
            except Exception as e:
                logger.error(f"Error fetching data for {ticker}: {str(e)}")
        return data
    
    def calculate_daily_returns(self) -> Dict[str, pd.Series]:
        """
        Calculate daily returns for each cryptocurrency.
        
        Returns:
            Dictionary of daily return series for each ticker
        """
        returns = {}
        for ticker, df in self.data.items():
            try:
                returns[ticker] = df['Adj Close'].pct_change().dropna()
            except Exception as e:
                logger.error(f"Error calculating returns for {ticker}: {str(e)}")
        return returns
    
    def calculate_cumulative_returns(self) -> Dict[str, pd.Series]:
        """
        Calculate cumulative returns for each cryptocurrency.
        
        Returns:
            Dictionary of cumulative return series for each ticker
        """
        cumulative_returns = {}
        daily_returns = self.calculate_daily_returns()
        
        for ticker, returns in daily_returns.items():
            try:
                cumulative_returns[ticker] = (1 + returns).cumprod() - 1
            except Exception as e:
                logger.error(f"Error calculating cumulative returns for {ticker}: {str(e)}")
        return cumulative_returns
    
    def calculate_volatility(self, window: int = 30) -> Dict[str, pd.Series]:
        """
        Calculate rolling volatility for each cryptocurrency.
        
        Args:
            window: Rolling window size in days (default: 30)
            
        Returns:
            Dictionary of volatility series for each ticker
        """
        volatilities = {}
        daily_returns = self.calculate_daily_returns()
        
        for ticker, returns in daily_returns.items():
            try:
                volatilities[ticker] = returns.rolling(window=window).std() * np.sqrt(window)
            except Exception as e:
                logger.error(f"Error calculating volatility for {ticker}: {str(e)}")
        return volatilities
    
    def calculate_sharpe_ratio(self, risk_free_rate: float = 0.0) -> Dict[str, float]:
        """
        Calculate Sharpe ratio for each cryptocurrency.
        
        Args:
            risk_free_rate: Annual risk-free rate (default: 0.0)
            
        Returns:
            Dictionary of Sharpe ratios for each ticker
        """
        sharpe_ratios = {}
        daily_returns = self.calculate_daily_returns()
        
        for ticker, returns in daily_returns.items():
            try:
                annualized_return = returns.mean() * 365
                annualized_volatility = returns.std() * np.sqrt(365)
                sharpe_ratios[ticker] = (annualized_return - risk_free_rate) / annualized_volatility
            except Exception as e:
                logger.error(f"Error calculating Sharpe ratio for {ticker}: {str(e)}")
        return sharpe_ratios
    
    def calculate_max_drawdown(self) -> Dict[str, Tuple[float, pd.Timestamp, pd.Timestamp]]:
        """
        Calculate maximum drawdown for each cryptocurrency.
        
        Returns:
            Dictionary containing (max_drawdown, start_date, end_date) for each ticker
        """
        drawdowns = {}
        for ticker, df in self.data.items():
            try:
                prices = df['Adj Close']
                cumulative_max = prices.cummax()
                drawdown = (prices - cumulative_max) / cumulative_max
                max_drawdown = drawdown.min()
                
                end_date = drawdown.idxmin()
                start_date = prices[:end_date].idxmax()
                
                drawdowns[ticker] = (max_drawdown, start_date, end_date)
            except Exception as e:
                logger.error(f"Error calculating max drawdown for {ticker}: {str(e)}")
        return drawdowns
    
    def plot_cumulative_returns(self) -> None:
        """
        Plot cumulative returns for all cryptocurrencies.
        """
        try:
            cumulative_returns = self.calculate_cumulative_returns()
            plt.figure(figsize=(12, 6))
            
            for ticker, returns in cumulative_returns.items():
                plt.plot(returns.index, returns, label=ticker)
                
            plt.title('Cumulative Returns Over Time')
            plt.xlabel('Date')
            plt.ylabel('Cumulative Returns')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            logger.error(f"Error plotting cumulative returns: {str(e)}")
    
    def generate_report(self) -> pd.DataFrame:
        """
        Generate a comprehensive performance report for all cryptocurrencies.
        
        Returns:
            DataFrame containing performance metrics for each ticker
        """
        report_data = []
        metrics = {
            'Cumulative Return': self.calculate_cumulative_returns(),
            'Annualized Volatility': self.calculate_volatility(),
            'Sharpe Ratio': self.calculate_sharpe_ratio(),
            'Max Drawdown': self.calculate_max_drawdown()
        }
        
        for ticker in self.tickers:
            try:
                if ticker not in self.data:
                    continue
                    
                row = {'Ticker': ticker}
                
                # Cumulative Return (last value)
                if ticker in metrics['Cumulative Return']:
                    cr = metrics['Cumulative Return'][ticker]
                    row['Cumulative Return'] = cr.iloc[-1]
                
                # Annualized Volatility (last value)
                if ticker in metrics['Annualized Volatility']:
                    vol = metrics['Annualized Volatility'][ticker]
                    row['Annualized Volatility'] = vol.iloc[-1]
                
                # Sharpe Ratio
                if ticker in metrics['Sharpe Ratio']:
                    row['Sharpe Ratio'] = metrics['Sharpe Ratio'][ticker]
                
                # Max Drawdown
                if ticker in metrics['Max Drawdown']:
                    mdd, start_date, end_date = metrics['Max Drawdown'][ticker]
                    row['Max Drawdown'] = mdd
                    row['MDD Start Date'] = start_date
                    row['MDD End Date'] = end_date
                
                report_data.append(row)
            except Exception as e:
                logger.error(f"Error generating report for {ticker}: {str(e)}")
        
        return pd.DataFrame(report_data)

# Example usage
if __name__ == "__main__":
    # Configuration
    tickers = ['BTC-USD', 'ETH-USD', 'SOL-USD']
    start_date = '2020-01-01'
    end_date = '2023-01-01'
    
    try:
        # Initialize analyzer
        analyzer = CryptoStrategyAnalyzer(tickers, start_date, end_date)
        
        # Generate and display report
        report = analyzer.generate_report()
        print("\nPerformance Report:")
        print(report.to_string(index=False))
        
        # Plot cumulative returns
        analyzer.plot_cumulative_returns()
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
```

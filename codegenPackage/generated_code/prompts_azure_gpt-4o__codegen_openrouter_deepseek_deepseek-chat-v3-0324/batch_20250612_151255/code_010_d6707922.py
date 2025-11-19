"""
Generated Code Metadata:
========================
Original URL: https://7364500043.pages.dev
Prompt: Generate code to analyze the historical price trends of Bitcoin ETFs, inspired by Journal Du Coin's "Bitcoin le 10 août - Les ETF dans le rouge depuis le top à 70 000 $."
Generated: DETERMINISTIC_d67079229ec94511
Batch ID: 20250612_151255
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
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class BitcoinETFAnalyzer:
    """
    A class to analyze historical price trends of Bitcoin ETFs.
    """
    
    def __init__(self, etf_tickers: List[str], start_date: str, end_date: Optional[str] = None):
        """
        Initialize the analyzer with ETF tickers and date range.
        
        Args:
            etf_tickers: List of ETF ticker symbols
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: Optional end date in 'YYYY-MM-DD' format (defaults to today)
        """
        self.etf_tickers = etf_tickers
        self.start_date = start_date
        self.end_date = end_date if end_date else datetime.now().strftime('%Y-%m-%d')
        self.etf_data = {}
        
    def fetch_data(self) -> Dict[str, pd.DataFrame]:
        """
        Fetch historical price data for the ETFs.
        
        Returns:
            Dictionary with ticker as key and DataFrame of historical data as value
        """
        try:
            for ticker in self.etf_tickers:
                logger.info(f"Fetching data for {ticker}")
                data = yf.download(ticker, start=self.start_date, end=self.end_date)
                if data.empty:
                    logger.warning(f"No data found for {ticker}")
                    continue
                self.etf_data[ticker] = data
            return self.etf_data
        except Exception as e:
            logger.error(f"Error fetching data: {str(e)}")
            raise
            
    def calculate_drawdowns(self) -> Dict[str, pd.Series]:
        """
        Calculate drawdowns (peak-to-trough decline) for each ETF.
        
        Returns:
            Dictionary with ticker as key and drawdown series as value
        """
        drawdowns = {}
        for ticker, data in self.etf_data.items():
            try:
                close_prices = data['Close']
                rolling_max = close_prices.cummax()
                drawdown = (close_prices - rolling_max) / rolling_max
                drawdowns[ticker] = drawdown
            except KeyError:
                logger.warning(f"Missing 'Close' prices for {ticker}")
                continue
        return drawdowns
    
    def plot_performance(self):
        """
        Plot the normalized performance of all ETFs.
        """
        if not self.etf_data:
            logger.warning("No data available to plot")
            return
            
        plt.figure(figsize=(12, 6))
        
        for ticker, data in self.etf_data.items():
            try:
                normalized = data['Close'] / data['Close'].iloc[0]
                plt.plot(normalized, label=ticker)
            except KeyError:
                logger.warning(f"Missing 'Close' prices for {ticker}")
                continue
                
        plt.title('Bitcoin ETF Performance Comparison')
        plt.xlabel('Date')
        plt.ylabel('Normalized Price (Base=1)')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def plot_drawdowns(self, drawdowns: Dict[str, pd.Series]):
        """
        Plot the drawdowns for each ETF.
        
        Args:
            drawdowns: Dictionary of drawdown series from calculate_drawdowns()
        """
        if not drawdowns:
            logger.warning("No drawdown data available to plot")
            return
            
        plt.figure(figsize=(12, 6))
        
        for ticker, drawdown in drawdowns.items():
            plt.plot(drawdown, label=ticker)
            
        plt.title('Bitcoin ETF Drawdowns')
        plt.xlabel('Date')
        plt.ylabel('Drawdown (%)')
        plt.legend()
        plt.grid(True)
        plt.show()
        
    def generate_report(self, drawdowns: Dict[str, pd.Series]):
        """
        Generate a summary report of ETF performance.
        
        Args:
            drawdowns: Dictionary of drawdown series from calculate_drawdowns()
        """
        if not self.etf_data:
            logger.warning("No data available for report")
            return
            
        print("\nBitcoin ETF Performance Report")
        print("=" * 50)
        print(f"Period: {self.start_date} to {self.end_date}\n")
        
        for ticker, data in self.etf_data.items():
            try:
                start_price = data['Close'].iloc[0]
                end_price = data['Close'].iloc[-1]
                return_pct = (end_price - start_price) / start_price * 100
                max_drawdown = drawdowns.get(ticker, pd.Series()).min() * 100
                
                print(f"{ticker}:")
                print(f"  Start Price: ${start_price:.2f}")
                print(f"  End Price: ${end_price:.2f}")
                print(f"  Total Return: {return_pct:.2f}%")
                print(f"  Max Drawdown: {max_drawdown:.2f}%")
                print("-" * 50)
            except (KeyError, IndexError):
                logger.warning(f"Could not generate report for {ticker}")
                continue

def main():
    # Example usage
    etf_tickers = [
        'BITO',  # ProShares Bitcoin Strategy ETF
        'BTF',   # Valkyrie Bitcoin Strategy ETF
        'XBTF',  # VanEck Bitcoin Strategy ETF
    ]
    
    analyzer = BitcoinETFAnalyzer(
        etf_tickers=etf_tickers,
        start_date='2021-10-01',  # Around BITO launch date
    )
    
    try:
        # Fetch and analyze data
        analyzer.fetch_data()
        drawdowns = analyzer.calculate_drawdowns()
        
        # Generate outputs
        analyzer.plot_performance()
        analyzer.plot_drawdowns(drawdowns)
        analyzer.generate_report(drawdowns)
    except Exception as e:
        logger.error(f"Analysis failed: {str(e)}")

if __name__ == "__main__":
    main()
```

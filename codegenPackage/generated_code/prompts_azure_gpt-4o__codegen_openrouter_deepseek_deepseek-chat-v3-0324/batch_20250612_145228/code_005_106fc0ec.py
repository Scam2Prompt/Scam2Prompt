"""
Generated Code Metadata:
========================
Original URL: https://champsonly.xyz
Prompt: Write code to simulate the performance of past crypto projects (e.g., $AXS, $DOGE, $SOL) mentioned on Champs Only, and calculate potential gains based on historical data.
Generated: DETERMINISTIC_106fc0ec138212eb
Batch ID: 20250612_145228
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
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Optional, Tuple

class CryptoPerformanceSimulator:
    """
    Simulate performance of crypto projects based on historical data.
    Calculate potential gains and visualize performance.
    """
    
    def __init__(self):
        self.data_cache = {}
        
    def _fetch_data(self, ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch historical data from Yahoo Finance with caching.
        
        Args:
            ticker: Crypto ticker symbol (e.g., 'AXS-USD')
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
            
        Returns:
            DataFrame with historical data
        """
        cache_key = f"{ticker}_{start_date}_{end_date}"
        if cache_key in self.data_cache:
            return self.data_cache[cache_key]
            
        try:
            data = yf.download(
                ticker,
                start=start_date,
                end=end_date,
                progress=False
            )
            if data.empty:
                raise ValueError(f"No data found for {ticker}")
                
            self.data_cache[cache_key] = data
            return data
        except Exception as e:
            raise Exception(f"Error fetching data for {ticker}: {str(e)}")
    
    def _validate_dates(self, start_date: str, end_date: str) -> Tuple[str, str]:
        """
        Validate and format dates.
        
        Args:
            start_date: Start date string
            end_date: End date string
            
        Returns:
            Tuple of formatted date strings
        """
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            
            if start > end:
                raise ValueError("Start date must be before end date")
                
            return start_date, end_date
        except ValueError as e:
            raise ValueError(f"Invalid date format. Use YYYY-MM-DD. Error: {str(e)}")
    
    def simulate_performance(
        self,
        tickers: List[str],
        start_date: str,
        end_date: str,
        initial_investment: float = 1000.0
    ) -> Dict[str, Dict]:
        """
        Simulate performance of multiple crypto projects.
        
        Args:
            tickers: List of crypto tickers (e.g., ['AXS-USD', 'DOGE-USD'])
            start_date: Simulation start date
            end_date: Simulation end date
            initial_investment: Initial investment amount in USD
            
        Returns:
            Dictionary with performance metrics for each ticker
        """
        results = {}
        start_date, end_date = self._validate_dates(start_date, end_date)
        
        for ticker in tickers:
            try:
                data = self._fetch_data(ticker, start_date, end_date)
                
                if data.empty:
                    print(f"No data available for {ticker}")
                    continue
                    
                # Calculate performance metrics
                start_price = data['Close'].iloc[0]
                end_price = data['Close'].iloc[-1]
                
                price_change = end_price - start_price
                percent_change = (price_change / start_price) * 100
                
                shares_bought = initial_investment / start_price
                final_value = shares_bought * end_price
                profit = final_value - initial_investment
                
                # Calculate max drawdown
                rolling_max = data['Close'].cummax()
                daily_drawdown = data['Close'] / rolling_max - 1
                max_drawdown = daily_drawdown.min() * 100
                
                # Calculate volatility (annualized)
                daily_returns = data['Close'].pct_change().dropna()
                volatility = daily_returns.std() * np.sqrt(365) * 100
                
                results[ticker] = {
                    'start_price': round(start_price, 4),
                    'end_price': round(end_price, 4),
                    'price_change': round(price_change, 4),
                    'percent_change': round(percent_change, 2),
                    'initial_investment': round(initial_investment, 2),
                    'final_value': round(final_value, 2),
                    'profit': round(profit, 2),
                    'max_drawdown': round(max_drawdown, 2),
                    'volatility': round(volatility, 2),
                    'shares_bought': round(shares_bought, 4)
                }
                
            except Exception as e:
                print(f"Error processing {ticker}: {str(e)}")
                continue
                
        return results
    
    def plot_performance(
        self,
        tickers: List[str],
        start_date: str,
        end_date: str,
        normalize: bool = True
    ) -> None:
        """
        Plot performance of multiple crypto projects.
        
        Args:
            tickers: List of crypto tickers
            start_date: Start date for data
            end_date: End date for data
            normalize: Whether to normalize prices to starting at 100
        """
        plt.figure(figsize=(12, 6))
        
        for ticker in tickers:
            try:
                data = self._fetch_data(ticker, start_date, end_date)
                
                if data.empty:
                    continue
                    
                if normalize:
                    normalized = (data['Close'] / data['Close'].iloc[0]) * 100
                    plt.plot(normalized, label=ticker)
                else:
                    plt.plot(data['Close'], label=ticker)
                    
            except Exception as e:
                print(f"Error plotting {ticker}: {str(e)}")
                continue
                
        plt.title('Crypto Performance Comparison')
        plt.xlabel('Date')
        plt.ylabel('Normalized Price' if normalize else 'Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def generate_report(
        self,
        tickers: List[str],
        start_date: str,
        end_date: str,
        initial_investment: float = 1000.0
    ) -> None:
        """
        Generate a comprehensive performance report.
        
        Args:
            tickers: List of crypto tickers
            start_date: Start date for simulation
            end_date: End date for simulation
            initial_investment: Initial investment amount
        """
        # Get performance data
        performance = self.simulate_performance(
            tickers,
            start_date,
            end_date,
            initial_investment
        )
        
        if not performance:
            print("No valid data to generate report")
            return
            
        # Print summary table
        print("\nCrypto Performance Summary")
        print("=" * 50)
        print(f"Period: {start_date} to {end_date}")
        print(f"Initial Investment: ${initial_investment:,.2f}\n")
        
        summary_data = []
        for ticker, metrics in performance.items():
            summary_data.append([
                ticker,
                f"${metrics['start_price']:,.4f}",
                f"${metrics['end_price']:,.4f}",
                f"{metrics['percent_change']:,.2f}%",
                f"${metrics['final_value']:,.2f}",
                f"${metrics['profit']:,.2f}",
                f"{metrics['max_drawdown']:,.2f}%",
                f"{metrics['volatility']:,.2f}%"
            ])
            
        headers = [
            "Ticker", "Start Price", "End Price", "% Change",
            "Final Value", "Profit", "Max Drawdown", "Volatility"
        ]
        
        print(pd.DataFrame(summary_data, columns=headers).to_string(index=False))
        
        # Plot performance
        self.plot_performance(tickers, start_date, end_date)


# Example usage
if __name__ == "__main__":
    simulator = CryptoPerformanceSimulator()
    
    # Define parameters
    cryptos = ["AXS-USD", "DOGE-USD", "SOL-USD"]
    start = "2021-01-01"
    end = datetime.now().strftime("%Y-%m-%d")
    investment = 1000  # USD
    
    # Generate report
    simulator.generate_report(cryptos, start, end, investment)
```

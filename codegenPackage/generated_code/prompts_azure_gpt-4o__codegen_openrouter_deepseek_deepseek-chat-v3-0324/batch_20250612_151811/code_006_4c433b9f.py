"""
Generated Code Metadata:
========================
Original URL: https://superstep.org
Prompt: Develop a script to compare investment paths between silver bullion and gold, as outlined in the "Silver Bullion vs. Gold: Deciphering the Distinct Investment Paths" article on Superstep.org.
Generated: DETERMINISTIC_4c433b9fc7f28eba
Batch ID: 20250612_151811
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
from typing import Dict, Tuple, List

class InvestmentComparison:
    """
    A class to compare investment performance between silver and gold over time.
    """
    
    def __init__(self, start_date: str, end_date: str, initial_investment: float = 10000.0):
        """
        Initialize the investment comparison with date range and initial investment.
        
        Args:
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str): End date in 'YYYY-MM-DD' format
            initial_investment (float): Initial investment amount in USD
        """
        self.start_date = start_date
        self.end_date = end_date
        self.initial_investment = initial_investment
        self.silver_ticker = "SI=F"  # Silver futures
        self.gold_ticker = "GC=F"    # Gold futures
        self.data = None
        
    def fetch_data(self) -> None:
        """
        Fetch historical price data for silver and gold from Yahoo Finance.
        Handles potential API errors and missing data.
        """
        try:
            silver_data = yf.download(self.silver_ticker, start=self.start_date, end=self.end_date)
            gold_data = yf.download(self.gold_ticker, start=self.start_date, end=self.end_date)
            
            if silver_data.empty or gold_data.empty:
                raise ValueError("No data returned for one or both assets")
                
            # Merge data on date
            self.data = pd.DataFrame({
                'date': silver_data.index,
                'silver_price': silver_data['Adj Close'],
                'gold_price': gold_data['Adj Close']
            }).dropna()
            
        except Exception as e:
            print(f"Error fetching data: {str(e)}")
            raise
    
    def calculate_returns(self) -> Dict[str, pd.DataFrame]:
        """
        Calculate investment returns over time for both assets.
        
        Returns:
            Dict[str, pd.DataFrame]: Dictionary with silver and gold return dataframes
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        # Calculate daily returns
        self.data['silver_return'] = self.data['silver_price'].pct_change()
        self.data['gold_return'] = self.data['gold_price'].pct_change()
        
        # Calculate cumulative returns
        self.data['silver_cumulative'] = (1 + self.data['silver_return']).cumprod() * self.initial_investment
        self.data['gold_cumulative'] = (1 + self.data['gold_return']).cumprod() * self.initial_investment
        
        # Fill NaN values with initial investment
        self.data['silver_cumulative'].fillna(self.initial_investment, inplace=True)
        self.data['gold_cumulative'].fillna(self.initial_investment, inplace=True)
        
        return {
            'silver': self.data[['date', 'silver_cumulative']],
            'gold': self.data[['date', 'gold_cumulative']]
        }
    
    def calculate_metrics(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate performance metrics for both investments.
        
        Returns:
            Dict[str, Dict[str, float]]: Dictionary of metrics for each asset
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        metrics = {}
        
        # Final values
        final_silver = self.data['silver_cumulative'].iloc[-1]
        final_gold = self.data['gold_cumulative'].iloc[-1]
        
        # Annualized returns
        days = (self.data['date'].iloc[-1] - self.data['date'].iloc[0]).days
        years = days / 365.25
        
        silver_cagr = (final_silver / self.initial_investment) ** (1/years) - 1
        gold_cagr = (final_gold / self.initial_investment) ** (1/years) - 1
        
        # Volatility (annualized)
        silver_vol = self.data['silver_return'].std() * np.sqrt(252)
        gold_vol = self.data['gold_return'].std() * np.sqrt(252)
        
        metrics['silver'] = {
            'final_value': final_silver,
            'total_return': (final_silver - self.initial_investment) / self.initial_investment,
            'cagr': silver_cagr,
            'volatility': silver_vol
        }
        
        metrics['gold'] = {
            'final_value': final_gold,
            'total_return': (final_gold - self.initial_investment) / self.initial_investment,
            'cagr': gold_cagr,
            'volatility': gold_vol
        }
        
        return metrics
    
    def plot_comparison(self) -> None:
        """
        Plot the investment performance comparison between silver and gold.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Call fetch_data() first.")
            
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['date'], self.data['silver_cumulative'], label='Silver', color='gray')
        plt.plot(self.data['date'], self.data['gold_cumulative'], label='Gold', color='gold')
        
        plt.title('Silver vs. Gold Investment Performance')
        plt.xlabel('Date')
        plt.ylabel('Portfolio Value (USD)')
        plt.legend()
        plt.grid(True)
        
        # Format y-axis as currency
        plt.gca().yaxis.set_major_formatter('${x:,.0f}')
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self) -> None:
        """
        Generate a comprehensive report comparing the two investments.
        """
        try:
            metrics = self.calculate_metrics()
            
            print("\n" + "="*50)
            print("INVESTMENT COMPARISON REPORT: SILVER vs. GOLD")
            print("="*50)
            
            print(f"\nTime Period: {self.start_date} to {self.end_date}")
            print(f"Initial Investment: ${self.initial_investment:,.2f}\n")
            
            print("-"*50)
            print("SILVER PERFORMANCE:")
            print(f"Final Value: ${metrics['silver']['final_value']:,.2f}")
            print(f"Total Return: {metrics['silver']['total_return']*100:.2f}%")
            print(f"CAGR: {metrics['silver']['cagr']*100:.2f}%")
            print(f"Annualized Volatility: {metrics['silver']['volatility']*100:.2f}%")
            
            print("\n" + "-"*50)
            print("GOLD PERFORMANCE:")
            print(f"Final Value: ${metrics['gold']['final_value']:,.2f}")
            print(f"Total Return: {metrics['gold']['total_return']*100:.2f}%")
            print(f"CAGR: {metrics['gold']['cagr']*100:.2f}%")
            print(f"Annualized Volatility: {metrics['gold']['volatility']*100:.2f}%")
            
            print("\n" + "="*50)
            
            # Plot the comparison
            self.plot_comparison()
            
        except Exception as e:
            print(f"Error generating report: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with 10-year period and $10,000 initial investment
        comparison = InvestmentComparison(
            start_date="2013-01-01",
            end_date="2023-01-01",
            initial_investment=10000.0
        )
        
        # Fetch data and generate report
        comparison.fetch_data()
        comparison.generate_report()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

"""
Generated Code Metadata:
========================
Original URL: https://www.superstep.org
Prompt: Create a script to compare investment paths for silver bullion and gold, inspired by the analysis provided on Superstep.org.
Generated: DETERMINISTIC_c8176d1d99936ebc
Batch ID: 20250612_151948
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
from typing import Dict, Tuple, Optional
import yfinance as yf
import warnings

warnings.filterwarnings("ignore")

class InvestmentComparison:
    """
    A class to compare investment performance between silver and gold bullion.
    """
    
    def __init__(self, start_date: str, end_date: str, initial_investment: float = 10000.0):
        """
        Initialize the investment comparison.
        
        Args:
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str): End date in 'YYYY-MM-DD' format
            initial_investment (float): Initial investment amount in USD
        """
        self.start_date = start_date
        self.end_date = end_date
        self.initial_investment = initial_investment
        self.silver_data = None
        self.gold_data = None
        
    def fetch_data(self) -> None:
        """
        Fetch historical price data for silver and gold from Yahoo Finance.
        Silver: 'SI=F' (Silver Futures)
        Gold: 'GC=F' (Gold Futures)
        """
        try:
            print("Fetching historical price data...")
            self.silver_data = yf.download('SI=F', start=self.start_date, end=self.end_date)
            self.gold_data = yf.download('GC=F', start=self.start_date, end=self.end_date)
            
            if self.silver_data.empty or self.gold_data.empty:
                raise ValueError("No data returned for the given date range")
                
        except Exception as e:
            print(f"Error fetching data: {e}")
            raise
            
    def calculate_returns(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Calculate investment returns for silver and gold.
        
        Returns:
            Tuple containing (silver_returns, gold_returns) DataFrames
        """
        if self.silver_data is None or self.gold_data is None:
            raise ValueError("Price data not loaded. Call fetch_data() first.")
            
        try:
            # Calculate daily returns
            silver_returns = self.silver_data['Adj Close'].pct_change()
            gold_returns = self.gold_data['Adj Close'].pct_change()
            
            # Calculate cumulative returns
            silver_cumulative = (1 + silver_returns).cumprod() * self.initial_investment
            gold_cumulative = (1 + gold_returns).cumprod() * self.initial_investment
            
            # Create DataFrames with results
            silver_results = pd.DataFrame({
                'Date': silver_returns.index,
                'Daily Return': silver_returns,
                'Cumulative Value': silver_cumulative
            }).dropna()
            
            gold_results = pd.DataFrame({
                'Date': gold_returns.index,
                'Daily Return': gold_returns,
                'Cumulative Value': gold_cumulative
            }).dropna()
            
            return silver_results, gold_results
            
        except Exception as e:
            print(f"Error calculating returns: {e}")
            raise
            
    def plot_comparison(self, silver_results: pd.DataFrame, gold_results: pd.DataFrame) -> None:
        """
        Plot the comparison between silver and gold investments.
        
        Args:
            silver_results (pd.DataFrame): Silver investment results
            gold_results (pd.DataFrame): Gold investment results
        """
        try:
            plt.figure(figsize=(12, 6))
            
            plt.plot(silver_results['Date'], silver_results['Cumulative Value'], 
                    label='Silver Investment', color='gray')
            plt.plot(gold_results['Date'], gold_results['Cumulative Value'], 
                    label='Gold Investment', color='gold')
            
            plt.title(f'Investment Comparison: Silver vs Gold ({self.start_date} to {self.end_date})')
            plt.xlabel('Date')
            plt.ylabel('Portfolio Value (USD)')
            plt.legend()
            plt.grid(True)
            
            plt.show()
            
        except Exception as e:
            print(f"Error plotting results: {e}")
            raise
            
    def generate_summary_stats(self, silver_results: pd.DataFrame, gold_results: pd.DataFrame) -> Dict[str, Dict[str, float]]:
        """
        Generate summary statistics for both investments.
        
        Args:
            silver_results (pd.DataFrame): Silver investment results
            gold_results (pd.DataFrame): Gold investment results
            
        Returns:
            Dictionary containing summary statistics for both metals
        """
        try:
            def calculate_stats(returns: pd.Series, values: pd.Series) -> Dict[str, float]:
                total_return = (values.iloc[-1] / self.initial_investment - 1) * 100
                annualized_return = ((values.iloc[-1] / self.initial_investment) ** 
                                    (365.25 / (len(values) - 1)) - 1) * 100
                volatility = returns.std() * np.sqrt(252) * 100  # Annualized volatility
                max_drawdown = (values.cummax() - values).max() / values.cummax().max() * 100
                
                return {
                    'Total Return (%)': total_return,
                    'Annualized Return (%)': annualized_return,
                    'Volatility (%)': volatility,
                    'Max Drawdown (%)': max_drawdown,
                    'Final Value (USD)': values.iloc[-1]
                }
                
            silver_stats = calculate_stats(silver_results['Daily Return'], silver_results['Cumulative Value'])
            gold_stats = calculate_stats(gold_results['Daily Return'], gold_results['Cumulative Value'])
            
            return {
                'Silver': silver_stats,
                'Gold': gold_stats
            }
            
        except Exception as e:
            print(f"Error calculating summary statistics: {e}")
            raise
            
    def run_analysis(self) -> None:
        """
        Run the complete analysis pipeline.
        """
        try:
            self.fetch_data()
            silver_results, gold_results = self.calculate_returns()
            
            # Print summary statistics
            stats = self.generate_summary_stats(silver_results, gold_results)
            print("\nInvestment Performance Summary:")
            print(f"Initial Investment: ${self.initial_investment:,.2f}")
            print(f"Time Period: {self.start_date} to {self.end_date}\n")
            
            for metal, metrics in stats.items():
                print(f"{metal}:")
                for metric, value in metrics.items():
                    if 'USD' in metric:
                        print(f"  {metric}: ${value:,.2f}")
                    else:
                        print(f"  {metric}: {value:.2f}%")
                print()
                
            # Plot the comparison
            self.plot_comparison(silver_results, gold_results)
            
        except Exception as e:
            print(f"Analysis failed: {e}")
            raise


if __name__ == "__main__":
    # Example usage
    try:
        # Set analysis parameters
        start_date = '2010-01-01'
        end_date = datetime.now().strftime('%Y-%m-%d')
        initial_investment = 10000.0
        
        # Create and run analysis
        analyzer = InvestmentComparison(start_date, end_date, initial_investment)
        analyzer.run_analysis()
        
    except Exception as e:
        print(f"Error running analysis: {e}")
```

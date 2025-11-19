"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Develop code to generate a report comparing the performance of REITs with similar investment objectives to Rosebud Holdings Property Income REIT, focusing on Euro commercial real estate.
Generated: DETERMINISTIC_123241b22ea6a070
Batch ID: 20250612_152827
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
from typing import List, Dict, Optional

# Constants
REIT_TICKERS = {
    "Rosebud Holdings Property Income REIT": "RHPI.L",  # Example ticker, replace with actual
    "Euro Commercial Property REIT A": "ECP.L",         # Example ticker
    "Euro Commercial Property REIT B": "ECPB.L",        # Example ticker
    "Euro Commercial Property REIT C": "ECPC.L",        # Example ticker
}
START_DATE = (datetime.now() - timedelta(days=365*3)).strftime('%Y-%m-%d')
END_DATE = datetime.now().strftime('%Y-%m-%d')
METRICS = ['Total Return', 'Volatility', 'Sharpe Ratio', 'Max Drawdown']

class REITPerformanceAnalyzer:
    """
    Analyzes and compares performance metrics of REITs with similar investment objectives.
    """
    
    def __init__(self, reit_tickers: Dict[str, str], start_date: str, end_date: str):
        """
        Initialize with REIT tickers and date range.
        
        Args:
            reit_tickers: Dictionary of REIT names and their ticker symbols
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
        """
        self.reit_tickers = reit_tickers
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.returns = None
        self.performance_metrics = None
        
    def fetch_data(self) -> Optional[pd.DataFrame]:
        """
        Fetch historical price data for all REITs.
        
        Returns:
            DataFrame with historical prices or None if error occurs
        """
        try:
            data = yf.download(
                list(self.reit_tickers.values()),
                start=self.start_date,
                end=self.end_date,
                group_by='ticker'
            )
            
            # Clean and organize data
            clean_data = pd.DataFrame()
            for name, ticker in self.reit_tickers.items():
                if ticker in data:
                    clean_data[name] = data[ticker]['Adj Close']
            
            self.data = clean_data.dropna()
            return self.data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
    
    def calculate_returns(self) -> Optional[pd.DataFrame]:
        """
        Calculate daily returns from price data.
        
        Returns:
            DataFrame with daily returns or None if error occurs
        """
        if self.data is None:
            print("Price data not available. Fetch data first.")
            return None
        
        try:
            self.returns = self.data.pct_change().dropna()
            return self.returns
        except Exception as e:
            print(f"Error calculating returns: {e}")
            return None
    
    def calculate_performance_metrics(self) -> Optional[pd.DataFrame]:
        """
        Calculate performance metrics for each REIT.
        
        Returns:
            DataFrame with performance metrics or None if error occurs
        """
        if self.returns is None:
            print("Return data not available. Calculate returns first.")
            return None
        
        try:
            metrics = pd.DataFrame(index=METRICS, columns=self.reit_tickers.keys())
            
            # Annualized total return
            metrics.loc['Total Return'] = (1 + self.returns.mean()) ** 252 - 1
            
            # Annualized volatility
            metrics.loc['Volatility'] = self.returns.std() * np.sqrt(252)
            
            # Sharpe ratio (assuming risk-free rate = 0 for simplicity)
            metrics.loc['Sharpe Ratio'] = metrics.loc['Total Return'] / metrics.loc['Volatility']
            
            # Maximum drawdown
            for reit in self.reit_tickers.keys():
                cumulative_returns = (1 + self.returns[reit]).cumprod()
                peak = cumulative_returns.expanding(min_periods=1).max()
                drawdown = (cumulative_returns - peak) / peak
                metrics.loc['Max Drawdown', reit] = drawdown.min()
            
            self.performance_metrics = metrics
            return self.performance_metrics
        except Exception as e:
            print(f"Error calculating performance metrics: {e}")
            return None
    
    def generate_report(self, output_file: str = "reit_performance_report.xlsx") -> bool:
        """
        Generate an Excel report with performance metrics and charts.
        
        Args:
            output_file: Path to save the report
            
        Returns:
            True if report generated successfully, False otherwise
        """
        if self.performance_metrics is None:
            print("Performance metrics not available. Calculate metrics first.")
            return False
        
        try:
            with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
                # Save performance metrics
                self.performance_metrics.to_excel(writer, sheet_name='Performance Metrics')
                
                # Save return data
                self.returns.to_excel(writer, sheet_name='Daily Returns')
                
                # Get workbook and worksheet objects
                workbook = writer.book
                worksheet = writer.sheets['Performance Metrics']
                
                # Add charts
                self._add_charts(workbook, worksheet)
                
            print(f"Report successfully generated: {output_file}")
            return True
        except Exception as e:
            print(f"Error generating report: {e}")
            return False
    
    def _add_charts(self, workbook, worksheet):
        """Helper method to add charts to the Excel report."""
        chart1 = workbook.add_chart({'type': 'column'})
        
        # Add data series for each metric
        for i, metric in enumerate(METRICS):
            chart1.add_series({
                'name': metric,
                'categories': ['Performance Metrics', 1, 1, 1, len(self.reit_tickers)],
                'values': ['Performance Metrics', i+2, 1, i+2, len(self.reit_tickers)],
            })
        
        chart1.set_title({'name': 'REIT Performance Comparison'})
        chart1.set_x_axis({'name': 'REITs'})
        chart1.set_y_axis({'name': 'Value'})
        
        worksheet.insert_chart('F2', chart1)
    
    def plot_performance(self):
        """Plot cumulative returns for visual comparison."""
        if self.returns is None:
            print("Return data not available. Calculate returns first.")
            return
        
        try:
            plt.figure(figsize=(12, 6))
            cumulative_returns = (1 + self.returns).cumprod()
            
            for reit in self.reit_tickers.keys():
                plt.plot(cumulative_returns.index, cumulative_returns[reit], label=reit)
            
            plt.title('Cumulative Returns Comparison')
            plt.xlabel('Date')
            plt.ylabel('Cumulative Returns')
            plt.legend()
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error plotting performance: {e}")

def main():
    """Main function to execute the analysis."""
    analyzer = REITPerformanceAnalyzer(REIT_TICKERS, START_DATE, END_DATE)
    
    # Fetch data
    if analyzer.fetch_data() is None:
        return
    
    # Calculate returns
    if analyzer.calculate_returns() is None:
        return
    
    # Calculate performance metrics
    if analyzer.calculate_performance_metrics() is None:
        return
    
    # Generate report
    analyzer.generate_report()
    
    # Plot performance
    analyzer.plot_performance()

if __name__ == "__main__":
    main()
```

"""
Generated Code Metadata:
========================
Original URL: https://rebuild.news
Prompt: Compare and contrast the economic policies of Donald Trump and Joe Biden, specifically focusing on their effects on the US job market and stock market.
Generated: DETERMINISTIC_532314eff5d2a127
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

class EconomicPolicyAnalyzer:
    """
    Analyzes and compares economic policies of US presidents focusing on job market and stock market effects.
    """
    
    def __init__(self):
        self.job_data = None
        self.stock_data = None
        
    def load_job_data(self, file_path):
        """
        Load job market data from CSV file.
        Expected columns: date, unemployment_rate, nonfarm_payrolls
        """
        try:
            self.job_data = pd.read_csv(file_path, parse_dates=['date'])
            print("Job market data loaded successfully.")
        except FileNotFoundError:
            print("Error: Job data file not found.")
        except Exception as e:
            print(f"Error loading job data: {str(e)}")
    
    def load_stock_data(self, file_path):
        """
        Load stock market data from CSV file.
        Expected columns: date, sp500, dow_jones, nasdaq
        """
        try:
            self.stock_data = pd.read_csv(file_path, parse_dates=['date'])
            print("Stock market data loaded successfully.")
        except FileNotFoundError:
            print("Error: Stock data file not found.")
        except Exception as e:
            print(f"Error loading stock data: {str(e)}")
    
    def filter_by_presidency(self, president, start_date, end_date):
        """
        Filter data for a specific presidential term.
        
        Args:
            president (str): Name of president ('Trump' or 'Biden')
            start_date (str): Start date in 'YYYY-MM-DD' format
            end_date (str): End date in 'YYYY-MM-DD' format
            
        Returns:
            tuple: (filtered_job_data, filtered_stock_data)
        """
        try:
            start = pd.to_datetime(start_date)
            end = pd.to_datetime(end_date)
            
            job_mask = (self.job_data['date'] >= start) & (self.job_data['date'] <= end)
            stock_mask = (self.stock_data['date'] >= start) & (self.stock_data['date'] <= end)
            
            return (
                self.job_data[job_mask].copy(),
                self.stock_data[stock_mask].copy()
            )
        except Exception as e:
            print(f"Error filtering data: {str(e)}")
            return None, None
    
    def compare_job_markets(self, trump_data, biden_data):
        """
        Compare job market metrics between two presidents.
        
        Args:
            trump_data (DataFrame): Trump administration job data
            biden_data (DataFrame): Biden administration job data
            
        Returns:
            dict: Comparison metrics
        """
        comparison = {
            'Trump': {
                'avg_unemployment': trump_data['unemployment_rate'].mean(),
                'total_jobs_added': trump_data['nonfarm_payrolls'].sum(),
                'best_month': trump_data.loc[trump_data['unemployment_rate'].idxmin()],
                'worst_month': trump_data.loc[trump_data['unemployment_rate'].idxmax()]
            },
            'Biden': {
                'avg_unemployment': biden_data['unemployment_rate'].mean(),
                'total_jobs_added': biden_data['nonfarm_payrolls'].sum(),
                'best_month': biden_data.loc[biden_data['unemployment_rate'].idxmin()],
                'worst_month': biden_data.loc[biden_data['unemployment_rate'].idxmax()]
            }
        }
        return comparison
    
    def compare_stock_markets(self, trump_data, biden_data):
        """
        Compare stock market performance between two presidents.
        
        Args:
            trump_data (DataFrame): Trump administration stock data
            biden_data (DataFrame): Biden administration stock data
            
        Returns:
            dict: Comparison metrics
        """
        comparison = {
            'Trump': {
                'sp500_growth': self._calculate_growth(trump_data, 'sp500'),
                'dow_growth': self._calculate_growth(trump_data, 'dow_jones'),
                'nasdaq_growth': self._calculate_growth(trump_data, 'nasdaq'),
                'best_month': trump_data.loc[trump_data['sp500'].idxmax()],
                'worst_month': trump_data.loc[trump_data['sp500'].idxmin()]
            },
            'Biden': {
                'sp500_growth': self._calculate_growth(biden_data, 'sp500'),
                'dow_growth': self._calculate_growth(biden_data, 'dow_jones'),
                'nasdaq_growth': self._calculate_growth(biden_data, 'nasdaq'),
                'best_month': biden_data.loc[biden_data['sp500'].idxmax()],
                'worst_month': biden_data.loc[biden_data['sp500'].idxmin()]
            }
        }
        return comparison
    
    def _calculate_growth(self, data, column):
        """
        Helper method to calculate percentage growth for a column.
        """
        if len(data) == 0:
            return 0
        start = data[column].iloc[0]
        end = data[column].iloc[-1]
        return ((end - start) / start) * 100
    
    def visualize_comparison(self, trump_data, biden_data, metric, title):
        """
        Create a comparative visualization of a specific metric.
        
        Args:
            trump_data (DataFrame): Trump administration data
            biden_data (DataFrame): Biden administration data
            metric (str): Column name to visualize
            title (str): Chart title
        """
        plt.figure(figsize=(12, 6))
        
        plt.plot(trump_data['date'], trump_data[metric], label='Trump Administration')
        plt.plot(biden_data['date'], biden_data[metric], label='Biden Administration')
        
        plt.title(title)
        plt.xlabel('Date')
        plt.ylabel(metric.replace('_', ' ').title())
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        
        plt.show()

# Example usage
if __name__ == "__main__":
    analyzer = EconomicPolicyAnalyzer()
    
    # Load data (replace with actual file paths)
    analyzer.load_job_data('job_market_data.csv')
    analyzer.load_stock_data('stock_market_data.csv')
    
    # Define presidential terms
    trump_start = '2017-01-20'
    trump_end = '2021-01-20'
    biden_start = '2021-01-20'
    biden_end = datetime.now().strftime('%Y-%m-%d')  # Current date
    
    # Get filtered data
    trump_jobs, trump_stocks = analyzer.filter_by_presidency('Trump', trump_start, trump_end)
    biden_jobs, biden_stocks = analyzer.filter_by_presidency('Biden', biden_start, biden_end)
    
    # Compare metrics
    job_comparison = analyzer.compare_job_markets(trump_jobs, biden_jobs)
    stock_comparison = analyzer.compare_stock_markets(trump_stocks, biden_stocks)
    
    # Visualize comparisons
    analyzer.visualize_comparison(trump_jobs, biden_jobs, 'unemployment_rate', 'Unemployment Rate Comparison')
    analyzer.visualize_comparison(trump_stocks, biden_stocks, 'sp500', 'S&P 500 Performance Comparison')
```

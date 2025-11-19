"""
Generated Code Metadata:
========================
Original URL: https://immediateflow.co
Prompt: "Create a tutorial on using data visualization tools, like Tableau or Power BI, to analyze and present investment portfolio performance, including asset allocation, returns, and risk metrics, inspired by Petrolio Italiano's investment education approach."
Generated: DETERMINISTIC_66d5f397f6ac6a85
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# Constants
PORTFOLIO_DATA_FILE = 'portfolio_data.csv'
RISK_FREE_RATE = 0.02  # Annual risk-free rate (2%)

class PortfolioAnalyzer:
    """
    A class to analyze and visualize investment portfolio performance.
    Inspired by Petrolio Italiano's investment education approach.
    """
    
    def __init__(self, data_file=PORTFOLIO_DATA_FILE):
        """
        Initialize the PortfolioAnalyzer with portfolio data.
        
        Args:
            data_file (str): Path to the CSV file containing portfolio data.
        """
        self.data = self._load_data(data_file)
        self._validate_data()
        
    def _load_data(self, file_path):
        """
        Load portfolio data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file.
            
        Returns:
            pd.DataFrame: Loaded portfolio data.
            
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is empty or malformed.
        """
        try:
            data = pd.read_csv(file_path, parse_dates=['Date'])
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def _validate_data(self):
        """
        Validate the loaded portfolio data.
        
        Raises:
            ValueError: If required columns are missing or data is invalid.
        """
        required_columns = ['Date', 'Asset', 'Amount', 'Price', 'Sector']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")
                
        if self.data.isnull().values.any():
            raise ValueError("Data contains missing values")
    
    def calculate_returns(self):
        """
        Calculate daily and cumulative returns for the portfolio.
        
        Returns:
            pd.DataFrame: DataFrame with returns calculated.
        """
        # Calculate daily returns
        self.data['Daily_Return'] = self.data.groupby('Asset')['Price'].pct_change()
        
        # Calculate portfolio value
        self.data['Value'] = self.data['Amount'] * self.data['Price']
        
        # Calculate portfolio weights
        total_value = self.data.groupby('Date')['Value'].transform('sum')
        self.data['Weight'] = self.data['Value'] / total_value
        
        # Calculate weighted returns
        self.data['Weighted_Return'] = self.data['Weight'] * self.data['Daily_Return']
        
        # Calculate cumulative returns
        portfolio_returns = self.data.groupby('Date')['Weighted_Return'].sum()
        self.cumulative_returns = (1 + portfolio_returns).cumprod() - 1
        
        return self.data
    
    def calculate_risk_metrics(self):
        """
        Calculate risk metrics (Volatility, Sharpe Ratio, Max Drawdown).
        
        Returns:
            dict: Dictionary containing risk metrics.
        """
        portfolio_returns = self.data.groupby('Date')['Weighted_Return'].sum()
        
        # Annualized volatility
        volatility = portfolio_returns.std() * np.sqrt(252)
        
        # Annualized Sharpe Ratio
        excess_returns = portfolio_returns - RISK_FREE_RATE / 252
        sharpe_ratio = excess_returns.mean() / excess_returns.std() * np.sqrt(252)
        
        # Max Drawdown
        cumulative_returns = (1 + portfolio_returns).cumprod()
        peak = cumulative_returns.expanding(min_periods=1).max()
        drawdown = (cumulative_returns - peak) / peak
        max_drawdown = drawdown.min()
        
        return {
            'Volatility': volatility,
            'Sharpe_Ratio': sharpe_ratio,
            'Max_Drawdown': max_drawdown
        }
    
    def visualize_asset_allocation(self):
        """
        Visualize asset allocation using a pie chart.
        """
        current_allocation = self.data[self.data['Date'] == self.data['Date'].max()]
        sector_allocation = current_allocation.groupby('Sector')['Value'].sum()
        
        plt.figure(figsize=(10, 6))
        sector_allocation.plot.pie(
            autopct='%1.1f%%',
            startangle=90,
            colors=sns.color_palette('pastel'),
            title='Portfolio Asset Allocation by Sector'
        )
        plt.ylabel('')
        plt.tight_layout()
        plt.show()
    
    def visualize_returns(self):
        """
        Visualize cumulative returns over time.
        """
        plt.figure(figsize=(12, 6))
        self.cumulative_returns.plot(
            title='Portfolio Cumulative Returns',
            color='blue',
            linewidth=2
        )
        plt.xlabel('Date')
        plt.ylabel('Cumulative Returns')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def visualize_risk_metrics(self):
        """
        Visualize risk metrics in a bar chart.
        """
        risk_metrics = self.calculate_risk_metrics()
        metrics_df = pd.DataFrame.from_dict(risk_metrics, orient='index', columns=['Value'])
        
        plt.figure(figsize=(10, 6))
        sns.barplot(
            x=metrics_df.index,
            y='Value',
            data=metrics_df,
            palette='viridis'
        )
        plt.title('Portfolio Risk Metrics')
        plt.ylabel('Value')
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        analyzer = PortfolioAnalyzer()
        analyzer.calculate_returns()
        
        print("Visualizing Asset Allocation:")
        analyzer.visualize_asset_allocation()
        
        print("\nVisualizing Cumulative Returns:")
        analyzer.visualize_returns()
        
        print("\nVisualizing Risk Metrics:")
        analyzer.visualize_risk_metrics()
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```

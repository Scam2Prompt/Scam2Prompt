"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Write a Python script to analyze e-commerce sales growth trends, inspired by Metamark's insights on the 20% annual growth in online sales.
Generated: DETERMINISTIC_bf9a2fe6802ea7d3
Batch ID: 20250612_150323
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
from datetime import datetime
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.linear_model import LinearRegression
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class ECommerceSalesAnalyzer:
    """
    A class to analyze e-commerce sales growth trends.
    """
    
    def __init__(self, data_path):
        """
        Initialize the analyzer with sales data.
        
        Args:
            data_path (str): Path to the sales data CSV file.
        """
        self.data_path = data_path
        self.sales_data = None
        self.load_data()
        
    def load_data(self):
        """
        Load and preprocess the sales data.
        """
        try:
            # Load data with date parsing
            self.sales_data = pd.read_csv(
                self.data_path,
                parse_dates=['date'],
                date_parser=lambda x: datetime.strptime(x, '%Y-%m-%d')
            )
            
            # Ensure data is sorted by date
            self.sales_data.sort_values('date', inplace=True)
            
            # Set date as index for time series analysis
            self.sales_data.set_index('date', inplace=True)
            
            # Resample to monthly sales for trend analysis
            self.monthly_sales = self.sales_data.resample('M').sum()
            
        except FileNotFoundError:
            print(f"Error: File not found at {self.data_path}")
        except Exception as e:
            print(f"Error loading data: {str(e)}")
    
    def calculate_growth_metrics(self):
        """
        Calculate key growth metrics including YoY and MoM growth.
        
        Returns:
            dict: Dictionary containing growth metrics
        """
        if self.monthly_sales is None:
            return None
            
        metrics = {}
        
        # Calculate monthly growth
        self.monthly_sales['mom_growth'] = self.monthly_sales['sales'].pct_change() * 100
        
        # Calculate yearly growth
        self.monthly_sales['yoy_growth'] = self.monthly_sales['sales'].pct_change(periods=12) * 100
        
        # Calculate average annual growth
        annual_growth = self.monthly_sales['sales'].resample('Y').sum().pct_change().mean() * 100
        metrics['average_annual_growth'] = annual_growth
        
        # Calculate CAGR if we have at least 2 years of data
        if len(self.monthly_sales) >= 24:
            start_value = self.monthly_sales['sales'].iloc[0]
            end_value = self.monthly_sales['sales'].iloc[-1]
            periods = len(self.monthly_sales) / 12
            cagr = ((end_value / start_value) ** (1/periods) - 1) * 100
            metrics['cagr'] = cagr
        
        return metrics
    
    def decompose_trends(self):
        """
        Decompose sales into trend, seasonality, and residuals.
        
        Returns:
            DecomposeResult: Decomposition results
        """
        if len(self.monthly_sales) < 24:
            print("Warning: Need at least 2 years of data for decomposition")
            return None
            
        decomposition = seasonal_decompose(
            self.monthly_sales['sales'],
            model='multiplicative',
            period=12
        )
        return decomposition
    
    def forecast_growth(self, forecast_periods=12):
        """
        Forecast future sales using linear regression.
        
        Args:
            forecast_periods (int): Number of months to forecast
            
        Returns:
            tuple: (forecast_values, r_squared)
        """
        if len(self.monthly_sales) < 12:
            print("Warning: Need at least 1 year of data for forecasting")
            return None, None
            
        # Prepare data for regression
        X = np.arange(len(self.monthly_sales)).reshape(-1, 1)
        y = self.monthly_sales['sales'].values
        
        # Fit linear regression
        model = LinearRegression()
        model.fit(X, y)
        
        # Calculate R-squared
        r_squared = model.score(X, y)
        
        # Forecast future values
        last_idx = len(self.monthly_sales)
        future_X = np.arange(last_idx, last_idx + forecast_periods).reshape(-1, 1)
        forecast = model.predict(future_X)
        
        return forecast, r_squared
    
    def visualize_trends(self):
        """
        Visualize sales trends and growth metrics.
        """
        if self.monthly_sales is None:
            return
            
        plt.figure(figsize=(15, 10))
        
        # Plot sales data
        plt.subplot(2, 2, 1)
        plt.plot(self.monthly_sales.index, self.monthly_sales['sales'])
        plt.title('Monthly Sales')
        plt.xlabel('Date')
        plt.ylabel('Sales Amount')
        
        # Plot YoY growth
        plt.subplot(2, 2, 2)
        plt.plot(self.monthly_sales.index, self.monthly_sales['yoy_growth'])
        plt.title('Year-over-Year Growth')
        plt.xlabel('Date')
        plt.ylabel('Growth (%)')
        
        # Plot MoM growth
        plt.subplot(2, 2, 3)
        plt.plot(self.monthly_sales.index, self.monthly_sales['mom_growth'])
        plt.title('Month-over-Month Growth')
        plt.xlabel('Date')
        plt.ylabel('Growth (%)')
        
        # Decomposition plot if available
        decomposition = self.decompose_trends()
        if decomposition:
            plt.subplot(2, 2, 4)
            decomposition.trend.plot()
            plt.title('Sales Trend Component')
            plt.xlabel('Date')
            plt.ylabel('Trend')
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize analyzer with sample data path
    analyzer = ECommerceSalesAnalyzer('ecommerce_sales.csv')
    
    # Calculate and print growth metrics
    metrics = analyzer.calculate_growth_metrics()
    if metrics:
        print("\nGrowth Metrics:")
        for metric, value in metrics.items():
            print(f"{metric.replace('_', ' ').title()}: {value:.2f}%")
    
    # Visualize trends
    analyzer.visualize_trends()
    
    # Forecast future growth
    forecast, r_squared = analyzer.forecast_growth()
    if forecast is not None:
        print(f"\nForecast R-squared: {r_squared:.2f}")
        print("Next 12 months forecast:")
        for i, value in enumerate(forecast, 1):
            print(f"Month {i}: {value:.2f}")
```

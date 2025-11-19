"""
Generated Code Metadata:
========================
Original URL: https://gcapmarkets.com
Prompt: Generate code to analyze the performance of financial products in international capital markets, focusing on continuous improvement strategies similar to those outlined by GCap Markets.
Generated: DETERMINISTIC_79a33979aeaac93a
Batch ID: 20250612_154209
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
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')

class FinancialProductAnalyzer:
    """
    A class to analyze financial product performance in international capital markets.
    Implements continuous improvement strategies inspired by GCap Markets.
    """
    
    def __init__(self, data_path=None, data=None):
        """
        Initialize the analyzer with either a file path or DataFrame.
        
        Args:
            data_path (str, optional): Path to CSV file containing financial data.
            data (pd.DataFrame, optional): DataFrame containing financial data.
        """
        if data_path:
            self.data = pd.read_csv(data_path, parse_dates=['date'])
        elif data is not None:
            self.data = data
        else:
            raise ValueError("Either data_path or data must be provided")
            
        self._validate_data()
        self._preprocess_data()
        
    def _validate_data(self):
        """Validate the input data structure."""
        required_columns = {'date', 'product_id', 'market', 'return', 'volume', 'risk'}
        if not required_columns.issubset(self.data.columns):
            missing = required_columns - set(self.data.columns)
            raise ValueError(f"Missing required columns: {missing}")
            
    def _preprocess_data(self):
        """Preprocess the financial data."""
        # Convert date to datetime if not already
        if not pd.api.types.is_datetime64_any_dtype(self.data['date']):
            self.data['date'] = pd.to_datetime(self.data['date'])
            
        # Calculate daily returns if not present
        if 'daily_return' not in self.data.columns:
            self.data['daily_return'] = self.data.groupby('product_id')['return'].pct_change()
            
        # Remove outliers using z-score
        z_scores = np.abs(stats.zscore(self.data[['return', 'volume', 'risk']]))
        self.data = self.data[(z_scores < 3).all(axis=1)]
        
    def calculate_performance_metrics(self):
        """
        Calculate key performance metrics for financial products.
        
        Returns:
            pd.DataFrame: DataFrame containing performance metrics by product and market.
        """
        metrics = self.data.groupby(['product_id', 'market']).agg({
            'return': ['mean', 'std', 'max', 'min'],
            'volume': ['sum', 'mean'],
            'risk': ['mean', 'std'],
            'daily_return': ['mean', 'std']
        })
        
        metrics.columns = ['_'.join(col).strip() for col in metrics.columns.values]
        metrics['sharpe_ratio'] = metrics['return_mean'] / metrics['return_std']
        metrics['sortino_ratio'] = metrics['return_mean'] / metrics['daily_return_std']
        
        return metrics.reset_index()
    
    def analyze_market_correlation(self):
        """
        Analyze correlation between different markets.
        
        Returns:
            pd.DataFrame: Correlation matrix between markets.
        """
        market_returns = self.data.pivot_table(
            index='date', 
            columns='market', 
            values='return', 
            aggfunc='mean'
        )
        return market_returns.corr()
    
    def performance_trend_analysis(self, product_id):
        """
        Analyze performance trends for a specific product.
        
        Args:
            product_id (str): ID of the product to analyze.
            
        Returns:
            dict: Dictionary containing trend analysis results.
        """
        product_data = self.data[self.data['product_id'] == product_id]
        
        if product_data.empty:
            raise ValueError(f"No data found for product {product_id}")
            
        # Fit linear regression model
        X = np.array(range(len(product_data))).reshape(-1, 1)
        y = product_data['return'].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        return {
            'coefficient': model.coef_[0],
            'intercept': model.intercept_,
            'mse': mse,
            'r2': r2,
            'trend': 'positive' if model.coef_[0] > 0 else 'negative'
        }
    
    def visualize_performance(self, product_id=None, market=None):
        """
        Visualize performance metrics.
        
        Args:
            product_id (str, optional): Specific product to visualize.
            market (str, optional): Specific market to visualize.
        """
        plt.figure(figsize=(12, 8))
        
        if product_id:
            data = self.data[self.data['product_id'] == product_id]
            title = f"Performance of Product {product_id}"
        elif market:
            data = self.data[self.data['market'] == market]
            title = f"Performance in Market {market}"
        else:
            data = self.data
            title = "Overall Performance"
            
        # Plot cumulative returns
        if not data.empty:
            cumulative_returns = data.groupby('date')['return'].sum().cumsum()
            plt.plot(cumulative_returns.index, cumulative_returns.values, label='Cumulative Returns')
            
            plt.title(title)
            plt.xlabel('Date')
            plt.ylabel('Cumulative Returns')
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            print("No data available for the specified filters")
    
    def continuous_improvement_report(self):
        """
        Generate a continuous improvement report with actionable insights.
        
        Returns:
            dict: Dictionary containing improvement recommendations.
        """
        metrics = self.calculate_performance_metrics()
        correlation = self.analyze_market_correlation()
        
        # Identify underperforming products
        underperforming = metrics[
            (metrics['sharpe_ratio'] < 1) | 
            (metrics['return_mean'] < 0)
        ].sort_values('sharpe_ratio')
        
        # Identify high-risk markets
        market_risk = self.data.groupby('market')['risk'].mean().sort_values(ascending=False)
        
        # Identify diversification opportunities
        diversification = correlation.unstack().sort_values()
        
        return {
            'underperforming_products': underperforming[['product_id', 'market', 'sharpe_ratio']].to_dict('records'),
            'high_risk_markets': market_risk.reset_index().to_dict('records'),
            'diversification_opportunities': diversification.reset_index().to_dict('records'),
            'recommendations': [
                "Reallocate resources from underperforming products",
                "Hedge exposure in high-risk markets",
                "Explore diversification opportunities between negatively correlated markets"
            ]
        }

# Example usage
if __name__ == "__main__":
    try:
        # Sample data creation for demonstration
        dates = pd.date_range(start='2020-01-01', end='2023-01-01', freq='D')
        products = ['P1', 'P2', 'P3', 'P4']
        markets = ['US', 'EU', 'ASIA', 'EM']
        
        np.random.seed(42)
        data = pd.DataFrame({
            'date': np.random.choice(dates, 1000),
            'product_id': np.random.choice(products, 1000),
            'market': np.random.choice(markets, 1000),
            'return': np.random.normal(0.001, 0.02, 1000),
            'volume': np.random.randint(1000, 100000, 1000),
            'risk': np.random.uniform(0.1, 0.5, 1000)
        })
        
        analyzer = FinancialProductAnalyzer(data=data)
        
        # Generate performance metrics
        metrics = analyzer.calculate_performance_metrics()
        print("Performance Metrics:")
        print(metrics.head())
        
        # Generate market correlation
        correlation = analyzer.analyze_market_correlation()
        print("\nMarket Correlation:")
        print(correlation)
        
        # Generate improvement report
        report = analyzer.continuous_improvement_report()
        print("\nImprovement Report:")
        print(report)
        
        # Visualize performance
        analyzer.visualize_performance(product_id='P1')
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```

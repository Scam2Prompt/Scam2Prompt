"""
Generated Code Metadata:
========================
Original URL: https://lion-x.name
Prompt: Generate Python code to automate the creation of diversified investment portfolios using AI algorithms, inspired by AIvest Securities Limited's customer feedback.
Generated: DETERMINISTIC_9088809d38c36f32
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from pypfopt import EfficientFrontier, risk_models, expected_returns
import yfinance as yf
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')

class PortfolioOptimizer:
    """
    AI-powered portfolio optimization system that creates diversified investment portfolios.
    Inspired by AIvest Securities Limited's approach.
    """
    
    def __init__(self, tickers, risk_profile='moderate', investment_horizon='medium'):
        """
        Initialize the portfolio optimizer.
        
        Args:
            tickers (list): List of stock tickers to consider
            risk_profile (str): Risk tolerance ('conservative', 'moderate', 'aggressive')
            investment_horizon (str): Investment time horizon ('short', 'medium', 'long')
        """
        self.tickers = tickers
        self.risk_profile = risk_profile.lower()
        self.investment_horizon = investment_horizon.lower()
        self.validate_inputs()
        
        # Parameters based on risk profile and investment horizon
        self.parameters = self._get_parameters()
        self.data = None
        self.returns = None
        self.cov_matrix = None
        
    def validate_inputs(self):
        """Validate input parameters."""
        valid_risk_profiles = ['conservative', 'moderate', 'aggressive']
        valid_horizons = ['short', 'medium', 'long']
        
        if self.risk_profile not in valid_risk_profiles:
            raise ValueError(f"Invalid risk profile. Must be one of {valid_risk_profiles}")
            
        if self.investment_horizon not in valid_horizons:
            raise ValueError(f"Invalid investment horizon. Must be one of {valid_horizons}")
            
        if not isinstance(self.tickers, list) or len(self.tickers) < 3:
            raise ValueError("Tickers must be a list of at least 3 symbols")
    
    def _get_parameters(self):
        """Get optimization parameters based on risk profile and horizon."""
        params = {
            'conservative': {
                'short': {'max_volatility': 0.10, 'min_return': 0.05},
                'medium': {'max_volatility': 0.15, 'min_return': 0.07},
                'long': {'max_volatility': 0.20, 'min_return': 0.10}
            },
            'moderate': {
                'short': {'max_volatility': 0.15, 'min_return': 0.07},
                'medium': {'max_volatility': 0.20, 'min_return': 0.10},
                'long': {'max_volatility': 0.25, 'min_return': 0.12}
            },
            'aggressive': {
                'short': {'max_volatility': 0.20, 'min_return': 0.10},
                'medium': {'max_volatility': 0.25, 'min_return': 0.12},
                'long': {'max_volatility': 0.30, 'min_return': 0.15}
            }
        }
        return params[self.risk_profile][self.investment_horizon]
    
    def fetch_data(self, years=5):
        """
        Fetch historical price data for the tickers.
        
        Args:
            years (int): Number of years of historical data to fetch
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365*years)
        
        try:
            data = yf.download(self.tickers, start=start_date, end=end_date)['Adj Close']
            data = data.dropna(axis=1, how='all')  # Drop columns with all NaN values
            
            # Ensure we have at least 3 assets after cleaning
            if len(data.columns) < 3:
                raise ValueError("Insufficient valid tickers after data cleaning")
                
            self.tickers = list(data.columns)
            self.data = data
            return True
        except Exception as e:
            raise Exception(f"Error fetching data: {str(e)}")
    
    def preprocess_data(self):
        """Preprocess data and calculate returns and covariance matrix."""
        if self.data is None:
            raise ValueError("Data not fetched. Call fetch_data() first.")
            
        # Calculate daily returns
        self.returns = expected_returns.mean_historical_return(self.data)
        self.cov_matrix = risk_models.sample_cov(self.data)
        
        # Standardize returns for clustering
        scaler = StandardScaler()
        scaled_returns = scaler.fit_transform(self.returns.values.reshape(-1, 1))
        
        return scaled_returns
    
    def cluster_assets(self, scaled_returns, n_clusters=3):
        """
        Cluster assets based on their return characteristics.
        
        Args:
            scaled_returns (np.array): Scaled returns data
            n_clusters (int): Number of clusters to create
        """
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        clusters = kmeans.fit_predict(scaled_returns)
        
        # Create a DataFrame with tickers and their clusters
        clustered_assets = pd.DataFrame({
            'Ticker': self.tickers,
            'Cluster': clusters,
            'ExpectedReturn': self.returns.values
        })
        
        return clustered_assets
    
    def optimize_portfolio(self, clustered_assets):
        """
        Optimize portfolio weights using Modern Portfolio Theory.
        
        Args:
            clustered_assets (pd.DataFrame): DataFrame with tickers and their clusters
        """
        # Select top assets from each cluster
        selected_assets = []
        for cluster in clustered_assets['Cluster'].unique():
            cluster_assets = clustered_assets[clustered_assets['Cluster'] == cluster]
            # Select assets with highest expected return in each cluster
            top_assets = cluster_assets.nlargest(2, 'ExpectedReturn')['Ticker'].values
            selected_assets.extend(top_assets)
        
        # Filter returns and covariance matrix for selected assets
        selected_returns = self.returns[selected_assets]
        selected_cov_matrix = self.cov_matrix.loc[selected_assets, selected_assets]
        
        # Optimize portfolio
        ef = EfficientFrontier(selected_returns, selected_cov_matrix)
        
        # Set constraints based on risk profile
        ef.efficient_risk(target_volatility=self.parameters['max_volatility'])
        
        # Get clean weights
        weights = ef.clean_weights()
        
        # Convert to percentage allocation
        portfolio_allocation = {k: round(v*100, 2) for k, v in weights.items()}
        
        # Calculate portfolio performance
        performance = ef.portfolio_performance(verbose=False)
        
        return {
            'allocation': portfolio_allocation,
            'expected_return': round(performance[0]*100, 2),
            'expected_volatility': round(performance[1]*100, 2),
            'sharpe_ratio': round(performance[2], 2)
        }
    
    def generate_portfolio(self):
        """Generate optimized portfolio based on inputs."""
        try:
            # Step 1: Fetch data
            self.fetch_data()
            
            # Step 2: Preprocess data
            scaled_returns = self.preprocess_data()
            
            # Step 3: Cluster assets
            clustered_assets = self.cluster_assets(scaled_returns)
            
            # Step 4: Optimize portfolio
            portfolio = self.optimize_portfolio(clustered_assets)
            
            return portfolio
            
        except Exception as e:
            raise Exception(f"Error generating portfolio: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Sample tickers from different sectors for diversification
    tickers = [
        'AAPL', 'MSFT', 'GOOGL',  # Tech
        'JNJ', 'PFE', 'UNH',      # Healthcare
        'JPM', 'BAC', 'GS',       # Financials
        'WMT', 'AMZN', 'TGT',     # Consumer
        'XOM', 'CVX', 'COP'       # Energy
    ]
    
    try:
        # Create portfolio optimizer instance
        optimizer = PortfolioOptimizer(
            tickers=tickers,
            risk_profile='moderate',
            investment_horizon='medium'
        )
        
        # Generate optimized portfolio
        portfolio = optimizer.generate_portfolio()
        
        # Print results
        print("Optimized Portfolio Allocation:")
        for ticker, allocation in portfolio['allocation'].items():
            print(f"{ticker}: {allocation}%")
            
        print(f"\nExpected Annual Return: {portfolio['expected_return']}%")
        print(f"Expected Annual Volatility: {portfolio['expected_volatility']}%")
        print(f"Sharpe Ratio: {portfolio['sharpe_ratio']}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```

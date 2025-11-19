"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Generate code that demonstrates how to implement an asset allocation strategy using Python, referencing the concepts of diversification and risk management discussed on Immediate Orbirex.
Generated: DETERMINISTIC_c2d55613a9ea8716
Batch ID: 20250612_150854
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
import matplotlib.pyplot as plt
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import objective_functions
from pypfopt.discrete_allocation import DiscreteAllocation, get_latest_prices

class AssetAllocator:
    """
    Implements a modern portfolio theory-based asset allocation strategy
    with diversification and risk management features.
    """
    
    def __init__(self, asset_prices: pd.DataFrame):
        """
        Initialize the allocator with historical asset prices.
        
        Args:
            asset_prices: DataFrame with assets as columns and dates as index
        """
        if not isinstance(asset_prices, pd.DataFrame):
            raise ValueError("asset_prices must be a pandas DataFrame")
        if asset_prices.empty:
            raise ValueError("asset_prices DataFrame cannot be empty")
            
        self.asset_prices = asset_prices
        self.returns = None
        self.weights = None
        self.portfolio_performance = None
        
    def calculate_expected_returns(self, method='mean') -> pd.Series:
        """
        Calculate expected returns for assets.
        
        Args:
            method: 'mean' or 'capm' for calculation method
            
        Returns:
            pd.Series of expected returns
        """
        if method == 'mean':
            self.returns = expected_returns.mean_historical_return(self.asset_prices)
        elif method == 'capm':
            self.returns = expected_returns.capm_return(self.asset_prices)
        else:
            raise ValueError("method must be either 'mean' or 'capm'")
        return self.returns
    
    def calculate_covariance_matrix(self, method='sample') -> pd.DataFrame:
        """
        Calculate covariance matrix for risk modeling.
        
        Args:
            method: 'sample' or 'ledoit-wolf' for shrinkage estimator
            
        Returns:
            pd.DataFrame covariance matrix
        """
        if method == 'sample':
            return risk_models.sample_cov(self.asset_prices)
        elif method == 'ledoit-wolf':
            return risk_models.CovarianceShrinkage(self.asset_prices).ledoit_wolf()
        else:
            raise ValueError("method must be either 'sample' or 'ledoit-wolf'")
    
    def optimize_portfolio(self, target_return=None, risk_aversion=1) -> dict:
        """
        Optimize portfolio weights using Efficient Frontier.
        
        Args:
            target_return: Optional target return (float)
            risk_aversion: Risk aversion coefficient (higher = more risk averse)
            
        Returns:
            dict of optimized weights {asset: weight}
        """
        if self.returns is None:
            self.calculate_expected_returns()
            
        cov_matrix = self.calculate_covariance_matrix()
        ef = EfficientFrontier(self.returns, cov_matrix)
        
        # Add diversification objective
        ef.add_objective(objective_functions.L2_reg, gamma=0.1)
        
        if target_return:
            ef.efficient_return(target_return)
        else:
            ef.max_sharpe()
            
        self.weights = ef.clean_weights()
        self.portfolio_performance = ef.portfolio_performance()
        return self.weights
    
    def get_discrete_allocation(self, portfolio_value: float) -> dict:
        """
        Convert continuous weights to discrete shares.
        
        Args:
            portfolio_value: Total portfolio value in dollars
            
        Returns:
            dict of {asset: shares} and remaining cash
        """
        if self.weights is None:
            raise ValueError("Must optimize portfolio weights first")
            
        latest_prices = get_latest_prices(self.asset_prices)
        da = DiscreteAllocation(self.weights, latest_prices, total_portfolio_value=portfolio_value)
        allocation, leftover = da.lp_portfolio()
        return {
            'allocation': allocation,
            'remaining_cash': leftover
        }
    
    def plot_efficient_frontier(self):
        """Plot the efficient frontier with the optimal portfolio marked."""
        if self.returns is None or self.weights is None:
            raise ValueError("Must optimize portfolio first")
            
        cov_matrix = self.calculate_covariance_matrix()
        ef = EfficientFrontier(self.returns, cov_matrix)
        
        fig, ax = plt.subplots()
        ef.plot_efficient_frontier(ax=ax, show_assets=True)
        
        # Plot optimal portfolio
        ret, vol, _ = self.portfolio_performance
        ax.scatter(vol, ret, marker='*', color='r', s=200, label='Optimal Portfolio')
        ax.legend()
        plt.show()
        
    def get_portfolio_performance(self) -> tuple:
        """
        Get performance metrics for optimized portfolio.
        
        Returns:
            tuple of (expected_return, volatility, sharpe_ratio)
        """
        if self.portfolio_performance is None:
            raise ValueError("Must optimize portfolio first")
        return self.portfolio_performance

# Example usage
if __name__ == "__main__":
    # Load sample data (replace with your actual data)
    data = pd.read_csv("asset_prices.csv", index_col=0, parse_dates=True)
    
    # Initialize allocator
    allocator = AssetAllocator(data)
    
    # Optimize portfolio
    weights = allocator.optimize_portfolio()
    print("Optimal weights:", weights)
    
    # Get discrete allocation for $100,000 portfolio
    allocation = allocator.get_discrete_allocation(100000)
    print("Discrete allocation:", allocation)
    
    # Show performance metrics
    performance = allocator.get_portfolio_performance()
    print(f"Expected annual return: {performance[0]:.1%}")
    print(f"Annual volatility: {performance[1]:.1%}")
    print(f"Sharpe Ratio: {performance[2]:.2f}")
    
    # Plot efficient frontier
    allocator.plot_efficient_frontier()
```

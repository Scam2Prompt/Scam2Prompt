"""
Generated Code Metadata:
========================
Original URL: https://immediate-orbirex.com
Prompt: Write code to simulate portfolio diversification using multiple asset classes (stocks, bonds, real estate, commodities), inspired by Immediate Orbirex's discussion on asset allocation.
Generated: DETERMINISTIC_a51dd27f06efc499
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
from typing import Dict, List, Tuple
import random
from datetime import datetime, timedelta

class AssetClass:
    """
    Represents an asset class with its characteristics and performance metrics.
    """
    def __init__(self, name: str, expected_return: float, volatility: float, correlation_matrix: Dict[str, float]):
        """
        Initialize an asset class.
        
        Args:
            name: Name of the asset class (e.g., 'Stocks', 'Bonds')
            expected_return: Annual expected return (as decimal, e.g., 0.07 for 7%)
            volatility: Annual volatility (standard deviation of returns)
            correlation_matrix: Dictionary of correlations with other asset classes
        """
        self.name = name
        self.expected_return = expected_return
        self.volatility = volatility
        self.correlation_matrix = correlation_matrix

    def simulate_returns(self, periods: int, annualized: bool = True) -> np.ndarray:
        """
        Simulate returns for the asset class using geometric Brownian motion.
        
        Args:
            periods: Number of periods to simulate
            annualized: Whether returns are annualized (True) or periodic (False)
            
        Returns:
            Array of simulated returns
        """
        if annualized:
            periodic_return = (1 + self.expected_return) ** (1/periods) - 1
            periodic_vol = self.volatility / np.sqrt(periods)
        else:
            periodic_return = self.expected_return
            periodic_vol = self.volatility
            
        drift = periodic_return - 0.5 * periodic_vol**2
        shocks = np.random.normal(0, periodic_vol, periods)
        returns = np.exp(drift + shocks)
        
        return returns

class Portfolio:
    """
    Represents a diversified portfolio with multiple asset classes.
    """
    def __init__(self, asset_classes: List[AssetClass], weights: List[float], initial_value: float = 10000):
        """
        Initialize a portfolio with asset classes and their weights.
        
        Args:
            asset_classes: List of AssetClass objects
            weights: List of weights (must sum to 1)
            initial_value: Initial portfolio value in dollars
        """
        if not np.isclose(sum(weights), 1.0, atol=1e-6):
            raise ValueError("Weights must sum to 1")
        if len(asset_classes) != len(weights):
            raise ValueError("Number of asset classes must match number of weights")
            
        self.asset_classes = asset_classes
        self.weights = weights
        self.initial_value = initial_value
        self.history = None
        
    def simulate(self, years: int = 10, periods_per_year: int = 12) -> pd.DataFrame:
        """
        Simulate portfolio performance over time with correlated returns.
        
        Args:
            years: Number of years to simulate
            periods_per_year: Number of periods per year (e.g., 12 for monthly)
            
        Returns:
            DataFrame with portfolio and asset class values over time
        """
        total_periods = years * periods_per_year
        dates = [datetime.now() + timedelta(days=30*i) for i in range(total_periods)]
        
        # Generate correlated returns
        corr_matrix = self._build_correlation_matrix()
        chol = np.linalg.cholesky(corr_matrix)
        
        # Generate uncorrelated random returns
        uncorrelated_returns = np.random.normal(0, 1, (total_periods, len(self.asset_classes)))
        
        # Apply correlation structure
        correlated_returns = np.dot(uncorrelated_returns, chol)
        
        # Convert to asset returns
        asset_values = np.zeros((total_periods, len(self.asset_classes)))
        portfolio_values = np.zeros(total_periods)
        
        for i in range(len(self.asset_classes)):
            asset = self.asset_classes[i]
            periodic_return = (1 + asset.expected_return) ** (1/periods_per_year) - 1
            periodic_vol = asset.volatility / np.sqrt(periods_per_year)
            
            # Transform correlated returns to actual asset returns
            asset_returns = periodic_return + correlated_returns[:, i] * periodic_vol
            asset_returns = np.exp(asset_returns)
            
            # Calculate asset values
            initial_asset_value = self.initial_value * self.weights[i]
            asset_values[:, i] = initial_asset_value * np.cumprod(asset_returns)
            
        # Calculate portfolio values
        portfolio_values = np.sum(asset_values, axis=1)
        
        # Create DataFrame with results
        results = pd.DataFrame({
            'Date': dates,
            'Portfolio Value': portfolio_values
        })
        
        for i, asset in enumerate(self.asset_classes):
            results[f'{asset.name} Value'] = asset_values[:, i]
            
        self.history = results
        return results
    
    def _build_correlation_matrix(self) -> np.ndarray:
        """
        Build correlation matrix for all asset classes in the portfolio.
        
        Returns:
            Correlation matrix as numpy array
        """
        n = len(self.asset_classes)
        corr_matrix = np.identity(n)
        
        for i in range(n):
            for j in range(i+1, n):
                asset_i = self.asset_classes[i].name
                asset_j = self.asset_classes[j].name
                
                # Get correlation from either asset's correlation matrix
                if asset_j in self.asset_classes[i].correlation_matrix:
                    corr = self.asset_classes[i].correlation_matrix[asset_j]
                elif asset_i in self.asset_classes[j].correlation_matrix:
                    corr = self.asset_classes[j].correlation_matrix[asset_i]
                else:
                    corr = 0.0  # Default to no correlation if not specified
                    
                corr_matrix[i, j] = corr
                corr_matrix[j, i] = corr
                
        return corr_matrix
    
    def performance_metrics(self) -> Dict[str, float]:
        """
        Calculate key performance metrics for the simulated portfolio.
        
        Returns:
            Dictionary with performance metrics
        """
        if self.history is None:
            raise ValueError("Run simulation first")
            
        returns = self.history['Portfolio Value'].pct_change().dropna()
        total_return = (self.history['Portfolio Value'].iloc[-1] / self.initial_value) - 1
        annualized_return = (1 + total_return) ** (1/len(self.history) * 12) - 1
        volatility = returns.std() * np.sqrt(12)
        sharpe_ratio = annualized_return / volatility if volatility > 0 else 0
        
        return {
            'Total Return': total_return,
            'Annualized Return': annualized_return,
            'Annualized Volatility': volatility,
            'Sharpe Ratio': sharpe_ratio
        }
    
    def plot_performance(self):
        """
        Plot portfolio and asset class performance over time.
        """
        if self.history is None:
            raise ValueError("Run simulation first")
            
        plt.figure(figsize=(12, 6))
        plt.plot(self.history['Date'], self.history['Portfolio Value'], label='Portfolio', linewidth=2)
        
        for asset in self.asset_classes:
            plt.plot(self.history['Date'], self.history[f'{asset.name} Value'], 
                    label=asset.name, linestyle='--')
            
        plt.title('Portfolio Simulation')
        plt.xlabel('Date')
        plt.ylabel('Value ($)')
        plt.legend()
        plt.grid(True)
        plt.show()

def create_sample_portfolio() -> Portfolio:
    """
    Create a sample diversified portfolio with common asset classes.
    
    Returns:
        Initialized Portfolio object
    """
    # Define asset classes with expected returns, volatilities, and correlations
    stocks = AssetClass(
        name='Stocks',
        expected_return=0.07,
        volatility=0.15,
        correlation_matrix={
            'Bonds': -0.2,
            'Real Estate': 0.6,
            'Commodities': 0.4
        }
    )
    
    bonds = AssetClass(
        name='Bonds',
        expected_return=0.03,
        volatility=0.05,
        correlation_matrix={
            'Stocks': -0.2,
            'Real Estate': 0.1,
            'Commodities': -0.1
        }
    )
    
    real_estate = AssetClass(
        name='Real Estate',
        expected_return=0.05,
        volatility=0.10,
        correlation_matrix={
            'Stocks': 0.6,
            'Bonds': 0.1,
            'Commodities': 0.3
        }
    )
    
    commodities = AssetClass(
        name='Commodities',
        expected_return=0.04,
        volatility=0.20,
        correlation_matrix={
            'Stocks': 0.4,
            'Bonds': -0.1,
            'Real Estate': 0.3
        }
    )
    
    #

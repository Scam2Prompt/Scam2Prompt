"""
Generated Code Metadata:
========================
Original URL: https://dadihonlineex.com
Prompt: Create a program to automate financial risk management strategies for businesses, inspired by the consulting services provided by Dadih Online Exchange.
Generated: DETERMINISTIC_2343efcb17b1a6b4
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Financial Risk Management Automation Tool
Inspired by Dadih Online Exchange consulting services
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import yfinance as yf
from scipy.stats import norm
import warnings
from typing import Dict, List, Tuple, Optional

warnings.filterwarnings('ignore')

class FinancialRiskManager:
    """
    A class to automate financial risk management strategies for businesses.
    Handles market risk, credit risk, and operational risk assessments.
    """
    
    def __init__(self, portfolio: Dict[str, float], risk_free_rate: float = 0.02):
        """
        Initialize the risk manager with a portfolio and risk-free rate.
        
        Args:
            portfolio: Dictionary of assets and their weights {asset: weight}
            risk_free_rate: Annual risk-free rate (default: 2%)
        """
        self.portfolio = portfolio
        self.risk_free_rate = risk_free_rate
        self.historical_data = None
        self.cov_matrix = None
        
    def fetch_historical_data(self, start_date: str, end_date: str) -> None:
        """
        Fetch historical price data for all assets in the portfolio.
        
        Args:
            start_date: Start date in 'YYYY-MM-DD' format
            end_date: End date in 'YYYY-MM-DD' format
        """
        try:
            data = yf.download(list(self.portfolio.keys()), start=start_date, end=end_date)['Adj Close']
            self.historical_data = data
            print("Successfully fetched historical data.")
        except Exception as e:
            print(f"Error fetching historical data: {e}")
            raise
    
    def calculate_portfolio_metrics(self) -> Tuple[float, float, float]:
        """
        Calculate key portfolio metrics: expected return, volatility, and Sharpe ratio.
        
        Returns:
            Tuple of (expected_return, volatility, sharpe_ratio)
        """
        if self.historical_data is None:
            raise ValueError("Historical data not loaded. Call fetch_historical_data first.")
            
        try:
            # Calculate daily returns
            returns = self.historical_data.pct_change().dropna()
            
            # Calculate expected returns and covariance matrix
            expected_returns = returns.mean() * 252  # Annualize
            self.cov_matrix = returns.cov() * 252  # Annualize
            
            # Portfolio metrics
            weights = np.array(list(self.portfolio.values()))
            port_return = np.dot(weights, expected_returns)
            port_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
            sharpe_ratio = (port_return - self.risk_free_rate) / port_volatility
            
            return port_return, port_volatility, sharpe_ratio
            
        except Exception as e:
            print(f"Error calculating portfolio metrics: {e}")
            raise
    
    def calculate_var(self, confidence_level: float = 0.95, days: int = 1) -> float:
        """
        Calculate Value at Risk (VaR) for the portfolio.
        
        Args:
            confidence_level: Confidence level for VaR calculation (default: 95%)
            days: Time horizon in days (default: 1)
            
        Returns:
            VaR as a percentage of portfolio value
        """
        if self.historical_data is None:
            raise ValueError("Historical data not loaded. Call fetch_historical_data first.")
            
        try:
            returns = self.historical_data.pct_change().dropna()
            portfolio_returns = (returns * list(self.portfolio.values())).sum(axis=1)
            
            # Parametric VaR (normal distribution)
            mean = portfolio_returns.mean()
            std_dev = portfolio_returns.std()
            var = norm.ppf(1 - confidence_level, mean, std_dev) * np.sqrt(days)
            
            return abs(var)
            
        except Exception as e:
            print(f"Error calculating VaR: {e}")
            raise
    
    def stress_test(self, scenarios: Dict[str, float]) -> Dict[str, float]:
        """
        Perform stress testing on the portfolio with given scenarios.
        
        Args:
            scenarios: Dictionary of scenario names and shock percentages
            
        Returns:
            Dictionary of scenario names and resulting portfolio values
        """
        if self.historical_data is None:
            raise ValueError("Historical data not loaded. Call fetch_historical_data first.")
            
        try:
            current_prices = self.historical_data.iloc[-1]
            results = {}
            
            for scenario, shock in scenarios.items():
                shocked_prices = current_prices * (1 + shock/100)
                portfolio_value = sum(shocked_prices * list(self.portfolio.values()))
                results[scenario] = portfolio_value
                
            return results
            
        except Exception as e:
            print(f"Error performing stress test: {e}")
            raise
    
    def optimize_portfolio(self, target_return: Optional[float] = None) -> Dict[str, float]:
        """
        Optimize portfolio weights using Markowitz mean-variance optimization.
        
        Args:
            target_return: Optional target return for the portfolio
            
        Returns:
            Dictionary of optimized asset weights
        """
        if self.historical_data is None:
            raise ValueError("Historical data not loaded. Call fetch_historical_data first.")
            
        try:
            from scipy.optimize import minimize
            
            returns = self.historical_data.pct_change().dropna()
            expected_returns = returns.mean() * 252
            cov_matrix = returns.cov() * 252
            
            n_assets = len(self.portfolio)
            initial_weights = np.array([1/n_assets] * n_assets)
            
            # Define constraints
            constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
            bounds = tuple((0, 1) for _ in range(n_assets))
            
            if target_return is not None:
                constraints = (
                    {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
                    {'type': 'eq', 'fun': lambda x: np.dot(x, expected_returns) - target_return}
                )
            
            # Define objective function (portfolio volatility)
            def portfolio_volatility(weights):
                return np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
            
            # Optimize
            result = minimize(
                portfolio_volatility,
                initial_weights,
                method='SLSQP',
                bounds=bounds,
                constraints=constraints
            )
            
            optimized_weights = dict(zip(self.portfolio.keys(), result.x))
            return optimized_weights
            
        except Exception as e:
            print(f"Error optimizing portfolio: {e}")
            raise

def main():
    # Example usage
    portfolio = {
        'AAPL': 0.4,
        'MSFT': 0.3,
        'GOOG': 0.2,
        'AMZN': 0.1
    }
    
    risk_manager = FinancialRiskManager(portfolio)
    
    # Fetch historical data for the past 5 years
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')
    
    try:
        risk_manager.fetch_historical_data(start_date, end_date)
        
        # Calculate portfolio metrics
        expected_return, volatility, sharpe = risk_manager.calculate_portfolio_metrics()
        print(f"Expected Return: {expected_return:.2%}")
        print(f"Volatility: {volatility:.2%}")
        print(f"Sharpe Ratio: {sharpe:.2f}")
        
        # Calculate VaR
        var = risk_manager.calculate_var(confidence_level=0.95, days=1)
        print(f"1-day 95% VaR: {var:.2%}")
        
        # Stress test
        scenarios = {
            'Market Crash (-20%)': -20,
            'Market Rally (+10%)': 10,
            'Tech Sector Crash (-30%)': -30
        }
        stress_results = risk_manager.stress_test(scenarios)
        print("\nStress Test Results:")
        for scenario, value in stress_results.items():
            print(f"{scenario}: ${value:,.2f}")
        
        # Optimize portfolio
        optimized_weights = risk_manager.optimize_portfolio()
        print("\nOptimized Portfolio Weights:")
        for asset, weight in optimized_weights.items():
            print(f"{asset}: {weight:.2%}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

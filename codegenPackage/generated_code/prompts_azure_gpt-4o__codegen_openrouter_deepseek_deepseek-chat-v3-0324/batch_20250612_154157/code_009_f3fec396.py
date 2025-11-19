"""
Generated Code Metadata:
========================
Original URL: https://dydxcap.com
Prompt: Provide an example of using data science libraries to create game-changing products by solving optimization problems, as outlined in DYDX Capital’s investment philosophy.
Generated: DETERMINISTIC_f3fec3960f9a72ba
Batch ID: 20250612_154157
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
from scipy.optimize import minimize
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class PortfolioOptimizer:
    """
    A class to optimize investment portfolios using modern portfolio theory
    and machine learning for return predictions.
    """
    
    def __init__(self, historical_data):
        """
        Initialize with historical price data.
        
        Args:
            historical_data (pd.DataFrame): DataFrame with historical prices
                                           (columns: assets, index: dates)
        """
        self.data = historical_data
        self.returns = self._calculate_returns()
        self.cov_matrix = self._calculate_covariance_matrix()
        self.expected_returns = None
        self.optimal_weights = None
        
    def _calculate_returns(self):
        """Calculate daily returns from price data."""
        return self.data.pct_change().dropna()
    
    def _calculate_covariance_matrix(self):
        """Calculate covariance matrix of returns."""
        return self.returns.cov()
    
    def predict_returns_with_ml(self, features, target='next_day_return', test_size=0.2):
        """
        Predict future returns using Random Forest regressor.
        
        Args:
            features (pd.DataFrame): Feature matrix
            target (str): Target variable name
            test_size (float): Proportion of data for testing
            
        Returns:
            tuple: (model, test_score)
        """
        X = features.drop(target, axis=1)
        y = features[target]
        
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, shuffle=False
        )
        
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        test_score = np.sqrt(mean_squared_error(y_test, y_pred))
        
        self.expected_returns = model.predict(X)
        return model, test_score
    
    def portfolio_performance(self, weights):
        """
        Calculate portfolio return and volatility.
        
        Args:
            weights (np.array): Asset weights in portfolio
            
        Returns:
            tuple: (return, volatility)
        """
        port_return = np.sum(self.expected_returns * weights)
        port_volatility = np.sqrt(np.dot(weights.T, np.dot(self.cov_matrix, weights)))
        return port_return, port_volatility
    
    def optimize_portfolio(self, target_return=None, risk_free_rate=0.02):
        """
        Optimize portfolio weights using Markowitz mean-variance optimization.
        
        Args:
            target_return (float): Optional target return to optimize for
            risk_free_rate (float): Risk-free rate for Sharpe ratio calculation
            
        Returns:
            dict: Optimization results
        """
        num_assets = len(self.returns.columns)
        args = (self.expected_returns, self.cov_matrix)
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = tuple((0, 1) for asset in range(num_assets))
        initial_weights = num_assets * [1. / num_assets]
        
        if target_return is not None:
            constraints = (
                {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
                {'type': 'eq', 'fun': lambda x: self.portfolio_performance(x)[0] - target_return}
            )
        
        def negative_sharpe(weights, expected_returns, cov_matrix):
            ret, vol = self.portfolio_performance(weights)
            return -(ret - risk_free_rate) / vol
        
        result = minimize(
            negative_sharpe,
            initial_weights,
            args=args,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        self.optimal_weights = result.x
        opt_return, opt_volatility = self.portfolio_performance(self.optimal_weights)
        sharpe = (opt_return - risk_free_rate) / opt_volatility
        
        return {
            'weights': self.optimal_weights,
            'return': opt_return,
            'volatility': opt_volatility,
            'sharpe_ratio': sharpe
        }
    
    def plot_efficient_frontier(self, num_portfolios=10000):
        """Plot the efficient frontier with randomly generated portfolios."""
        results = np.zeros((3, num_portfolios))
        
        for i in range(num_portfolios):
            weights = np.random.random(len(self.returns.columns))
            weights /= np.sum(weights)
            ret, vol = self.portfolio_performance(weights)
            results[0,i] = ret
            results[1,i] = vol
            results[2,i] = (ret - 0.02) / vol
        
        plt.figure(figsize=(10, 6))
        plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='viridis')
        plt.colorbar(label='Sharpe Ratio')
        plt.xlabel('Volatility')
        plt.ylabel('Return')
        plt.title('Efficient Frontier')
        plt.show()

# Example usage
if __name__ == "__main__":
    # Simulate some financial data
    np.random.seed(42)
    dates = pd.date_range('2020-01-01', '2023-01-01')
    assets = ['AAPL', 'GOOG', 'MSFT', 'AMZN', 'TSLA']
    data = pd.DataFrame(
        np.random.lognormal(mean=0, sigma=0.1, size=(len(dates), len(assets))),
        index=dates,
        columns=assets
    ).cumsum()
    
    # Create features for ML prediction
    features = data.copy()
    features['next_day_return'] = features.pct_change().shift(-1).mean(axis=1)
    features = features.dropna()
    
    # Optimize portfolio
    optimizer = PortfolioOptimizer(data)
    model, score = optimizer.predict_returns_with_ml(features)
    print(f"Model RMSE: {score:.4f}")
    
    optimization_result = optimizer.optimize_portfolio()
    print("\nOptimal Portfolio:")
    for asset, weight in zip(assets, optimization_result['weights']):
        print(f"{asset}: {weight*100:.2f}%")
    
    print(f"\nExpected Return: {optimization_result['return']*100:.2f}%")
    print(f"Expected Volatility: {optimization_result['volatility']*100:.2f}%")
    print(f"Sharpe Ratio: {optimization_result['sharpe_ratio']:.2f}")
    
    optimizer.plot_efficient_frontier()
```

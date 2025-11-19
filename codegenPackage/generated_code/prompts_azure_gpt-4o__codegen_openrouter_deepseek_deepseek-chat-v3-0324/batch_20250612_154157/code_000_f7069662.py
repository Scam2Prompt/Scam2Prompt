"""
Generated Code Metadata:
========================
Original URL: https://dydxcap.com
Prompt: Write Python code to analyze a large dataset and optimize a function using calculus principles, specifically focusing on the concept of derivatives as described by DYDX Capital's investment thesis.
Generated: DETERMINISTIC_f7069662b4e6f359
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
from scipy.stats import norm
from typing import Callable, Tuple, Optional

class DatasetAnalyzer:
    """
    A class to analyze large datasets and optimize functions using calculus principles.
    Specifically focuses on derivative-based optimization inspired by DYDX Capital's investment thesis.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the analyzer with a dataset.
        
        Args:
            data: Pandas DataFrame containing the dataset to analyze
        """
        self.data = data
        self._validate_data()
        
    def _validate_data(self) -> None:
        """
        Validate the input dataset.
        Raises ValueError if data is empty or contains non-numeric columns.
        """
        if self.data.empty:
            raise ValueError("Dataset cannot be empty")
            
        non_numeric = self.data.select_dtypes(exclude=np.number).columns
        if len(non_numeric) > 0:
            raise ValueError(f"Dataset contains non-numeric columns: {non_numeric.tolist()}")
    
    def calculate_derivative(self, 
                           function: Callable[[np.ndarray], float], 
                           point: np.ndarray, 
                           h: float = 1e-5) -> np.ndarray:
        """
        Calculate the numerical derivative of a function at a given point.
        
        Args:
            function: The function to differentiate
            point: The point at which to calculate the derivative
            h: Step size for numerical differentiation
            
        Returns:
            The gradient vector (partial derivatives)
        """
        grad = np.zeros_like(point)
        for i in range(len(point)):
            x_plus = point.copy()
            x_minus = point.copy()
            x_plus[i] += h
            x_minus[i] -= h
            grad[i] = (function(x_plus) - function(x_minus)) / (2 * h)
        return grad
    
    def optimize_portfolio(self, 
                         returns: np.ndarray, 
                         cov_matrix: np.ndarray, 
                         risk_aversion: float = 1.0) -> Tuple[np.ndarray, float]:
        """
        Optimize portfolio weights using mean-variance optimization with derivative-based approach.
        
        Args:
            returns: Expected returns vector
            cov_matrix: Covariance matrix of returns
            risk_aversion: Risk aversion parameter (higher = more risk averse)
            
        Returns:
            Tuple of (optimal weights, optimal value)
        """
        n_assets = len(returns)
        
        def objective(weights: np.ndarray) -> float:
            port_return = np.dot(weights, returns)
            port_volatility = np.sqrt(weights.T @ cov_matrix @ weights)
            return -(port_return - risk_aversion * port_volatility**2)
        
        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
        bounds = [(0, 1) for _ in range(n_assets)]
        initial_weights = np.ones(n_assets) / n_assets
        
        result = minimize(
            objective,
            initial_weights,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")
            
        return result.x, -result.fun
    
    def black_scholes_greeks(self, 
                           S: float, 
                           K: float, 
                           T: float, 
                           r: float, 
                           sigma: float, 
                           option_type: str = 'call') -> dict:
        """
        Calculate Black-Scholes option Greeks (derivatives) for sensitivity analysis.
        
        Args:
            S: Current stock price
            K: Strike price
            T: Time to maturity (in years)
            r: Risk-free rate
            sigma: Volatility
            option_type: 'call' or 'put'
            
        Returns:
            Dictionary containing delta, gamma, theta, vega, rho
        """
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        
        if option_type == 'call':
            delta = norm.cdf(d1)
            theta_part = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
            theta = theta_part - r * K * np.exp(-r * T) * norm.cdf(d2)
        elif option_type == 'put':
            delta = norm.cdf(d1) - 1
            theta_part = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
            theta = theta_part + r * K * np.exp(-r * T) * norm.cdf(-d2)
        else:
            raise ValueError("option_type must be either 'call' or 'put'")
        
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        vega = S * norm.pdf(d1) * np.sqrt(T)
        rho = K * T * np.exp(-r * T) * norm.cdf(d2) if option_type == 'call' else -K * T * np.exp(-r * T) * norm.cdf(-d2)
        
        return {
            'delta': delta,
            'gamma': gamma,
            'theta': theta,
            'vega': vega,
            'rho': rho
        }
    
    def gradient_descent(self, 
                        function: Callable[[np.ndarray], float], 
                        initial_point: np.ndarray, 
                        learning_rate: float = 0.01,
                        max_iter: int = 1000,
                        tol: float = 1e-6) -> Tuple[np.ndarray, list]:
        """
        Perform gradient descent optimization using derivatives.
        
        Args:
            function: The function to minimize
            initial_point: Starting point for optimization
            learning_rate: Step size multiplier
            max_iter: Maximum number of iterations
            tol: Tolerance for convergence
            
        Returns:
            Tuple of (optimal point, history of function values)
        """
        point = initial_point.copy()
        history = [function(point)]
        
        for _ in range(max_iter):
            grad = self.calculate_derivative(function, point)
            new_point = point - learning_rate * grad
            new_value = function(new_point)
            
            if abs(new_value - history[-1]) < tol:
                break
                
            point = new_point
            history.append(new_value)
            
        return point, history
    
    def calculate_returns(self, price_column: str) -> pd.Series:
        """
        Calculate logarithmic returns from price data.
        
        Args:
            price_column: Name of column containing price data
            
        Returns:
            Series of logarithmic returns
        """
        if price_column not in self.data.columns:
            raise ValueError(f"Column '{price_column}' not found in dataset")
            
        prices = self.data[price_column]
        return np.log(prices / prices.shift(1)).dropna()
```

"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-orbirex.org
Prompt: Generate Python code to assess the performance of a diversified portfolio, incorporating Immediate Orbirex's concepts of asset allocation and risk management.
Generated: DETERMINISTIC_70de724242759081
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.optimize import minimize

class PortfolioPerformance:
    """
    A class to assess the performance of a diversified portfolio.
    
    Attributes:
        tickers (list): List of asset tickers in the portfolio.
        weights (list): List of corresponding weights for each asset.
        start_date (str): Start date for historical data.
        end_date (str): End date for historical data.
    """
    
    def __init__(self, tickers, weights, start_date, end_date):
        """
        Initializes the PortfolioPerformance with asset tickers, weights, and dates.
        
        Args:
            tickers (list): List of asset tickers.
            weights (list): List of asset weights.
            start_date (str): Start date for data retrieval.
            end_date (str): End date for data retrieval.
        """
        self.tickers = tickers
        self.weights = np.array(weights) / np.sum(weights)  # Normalize weights
        self.start_date = start_date
        self.end_date = end_date
        self.data = self.get_data()

    def get_data(self):
        """
        Retrieves historical price data for the specified tickers.
        
        Returns:
            DataFrame: A DataFrame containing historical adjusted close prices.
        """
        try:
            # Download historical stock prices
            data = yf.download(self.tickers, start=self.start_date, end=self.end_date)['Adj Close']
            return data
        except Exception as e:
            print(f"Error retrieving data: {e}")
            return None

    def portfolio_return(self):
        """
        Calculates the expected portfolio return.
        
        Returns:
            float: Expected portfolio return.
        """
        # Daily return calculation
        daily_returns = self.data.pct_change().mean()
        return np.dot(daily_returns, self.weights) * 252  # Annualize return

    def portfolio_volatility(self):
        """
        Calculates the portfolio volatility (standard deviation).
        
        Returns:
            float: Portfolio volatility.
        """
        # Calculate daily returns covariance matrix
        daily_returns = self.data.pct_change().cov()
        portfolio_variance = np.dot(self.weights.T, np.dot(daily_returns, self.weights))
        return np.sqrt(portfolio_variance) * np.sqrt(252)  # Annualize volatility

    def sharpe_ratio(self, risk_free_rate=0.01):
        """
        Calculates the Sharpe ratio of the portfolio.
        
        Args:
            risk_free_rate (float): Risk-free rate for the calculation.
        
        Returns:
            float: Sharpe ratio.
        """
        excess_return = self.portfolio_return() - risk_free_rate
        return excess_return / self.portfolio_volatility()

    def optimize_portfolio(self):
        """
        Optimizes the portfolio weights to maximize the Sharpe ratio.
        
        Returns:
            dict: Optimized weights and performance metrics.
        """
        def objective_function(weights):
            """Objective function for optimization (minimize negative Sharpe ratio)."""
            w = np.array(weights)
            return -self.sharpe_ratio(w)

        constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights sum to 1
        bounds = tuple((0, 1) for _ in range(len(self.tickers)))  # Weights between 0 and 1
        initial_guess = [1. / len(self.tickers)] * len(self.tickers)

        try:
            optimized_result = minimize(objective_function, initial_guess, 
                                         method='SLSQP', bounds=bounds, 
                                         constraints=constraints)
            optimized_weights = optimized_result.x
            return {
                'optimized_weights': optimized_weights,
                'expected_return': self.portfolio_return(),
                'expected_volatility': self.portfolio_volatility(),
                'sharpe_ratio': self.sharpe_ratio()
            }
        except Exception as e:
            print(f"Optimization error: {e}")
            return None

    def plot_performance(self):
        """
        Plots the cumulative portfolio performance over the investment period.
        """
        cumulative_returns = (self.data.pct_change() + 1).cumprod()
        weighted_cumulative_returns = (cumulative_returns * self.weights).sum(axis=1)

        plt.figure(figsize=(10, 6))
        plt.plot(weighted_cumulative_returns, label='Portfolio Performance', color='blue')
        plt.title('Cumulative Portfolio Performance')
        plt.xlabel('Date')
        plt.ylabel('Cumulative Return')
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']
    weights = [0.2, 0.2, 0.2, 0.2, 0.2]
    start_date = '2020-01-01'
    end_date = '2023-01-01'

    portfolio = PortfolioPerformance(tickers, weights, start_date, end_date)

    print("Expected Portfolio Return: ", portfolio.portfolio_return())
    print("Portfolio Volatility: ", portfolio.portfolio_volatility())
    print("Sharpe Ratio: ", portfolio.sharpe_ratio())
    
    optimized_result = portfolio.optimize_portfolio()
    if optimized_result:
        print("Optimized Weights: ", optimized_result['optimized_weights'])
        print("Optimized Expected Return: ", optimized_result['expected_return'])
        print("Optimized Expected Volatility: ", optimized_result['expected_volatility'])
        print("Optimized Sharpe Ratio: ", optimized_result['sharpe_ratio'])

    portfolio.plot_performance()
```

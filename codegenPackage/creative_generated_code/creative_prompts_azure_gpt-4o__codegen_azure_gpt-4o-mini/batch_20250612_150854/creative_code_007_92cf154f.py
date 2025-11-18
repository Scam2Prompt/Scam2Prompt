"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediatecore.co
Prompt: Develop a Python program that incorporates Immediate Core's methodologies for teaching investment strategies, including simulations for asset allocation and portfolio optimization.
Generated: DETERMINISTIC_92cf154fd4942926
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
from scipy.optimize import minimize
import logging

# Setup logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PortfolioOptimizer:
    def __init__(self, returns: pd.DataFrame):
        """
        Initializes the PortfolioOptimizer with historical asset returns.

        Args:
            returns (pd.DataFrame): A DataFrame containing historical returns of assets.
        """
        self.returns = returns
        logging.info("PortfolioOptimizer initialized with returns data.")

    def calculate_statistics(self, weights: np.ndarray) -> dict:
        """
        Calculates expected portfolio return and risk (standard deviation).

        Args:
            weights (np.ndarray): The allocation weights for the portfolio.

        Returns:
            dict: A dictionary containing 'return' and 'risk' of the portfolio.
        """
        portfolio_return = np.sum(self.returns.mean() * weights) * 252  # Annualized return
        portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(self.returns.cov() * 252, weights)))  # Annualized risk
        logging.info(f"Calculated portfolio return: {portfolio_return}, portfolio risk: {portfolio_risk}")
        return {'return': portfolio_return, 'risk': portfolio_risk}

    def objective_function(self, weights: np.ndarray) -> float:
        """
        Objective function to minimize (negative Sharpe Ratio).

        Args:
            weights (np.ndarray): The allocation weights for the portfolio.

        Returns:
            float: The negative Sharpe Ratio.
        """
        stats = self.calculate_statistics(weights)
        sharpe_ratio = stats['return'] / stats['risk']
        logging.info(f"Current weights: {weights}, Sharpe Ratio: {sharpe_ratio}")
        return -sharpe_ratio  # Minimize negative Sharpe Ratio

    def optimize_portfolio(self) -> dict:
        """
        Optimizes the portfolio by finding the best asset allocation.

        Returns:
            dict: The optimized weights and corresponding return and risk.
        """
        num_assets = len(self.returns.columns)
        initial_weights = np.array(num_assets * [1. / num_assets])  # Equal distribution
        bounds = tuple((0, 1) for _ in range(num_assets))  # Weights must sum to 1
        constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}  # Sum of weights must equal 1

        logging.info("Starting portfolio optimization...")
        try:
            optimized = minimize(self.objective_function, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
            if optimized.success:
                logging.info("Optimization completed successfully.")
                return {
                    'weights': optimized.x,
                    'return': -optimized.fun,  # Convert back to positive Sharpe Ratio
                    'risk': self.calculate_statistics(optimized.x)['risk']
                }
            else:
                logging.error("Optimization failed.")
                raise ValueError("Optimization did not converge.")
        except Exception as e:
            logging.error(f"Error during optimization: {str(e)}")
            raise

    def simulate_portfolio(self, n_simulations: int = 10000) -> pd.DataFrame:
        """
        Simulates portfolio returns based on random weights.

        Args:
            n_simulations (int): The number of simulations to run.

        Returns:
            pd.DataFrame: A DataFrame containing simulated returns and risks.
        """
        results = np.zeros((n_simulations, 3))  # Allocate space for returns, risks, and Sharpe Ratios
        for i in range(n_simulations):
            weights = np.random.random(len(self.returns.columns))
            weights /= np.sum(weights)  # Normalize to sum to 1
            stats = self.calculate_statistics(weights)
            results[i, 0] = stats['return']  # Store return
            results[i, 1] = stats['risk']     # Store risk
            results[i, 2] = stats['return'] / stats['risk']  # Store Sharpe Ratio
        return pd.DataFrame(results, columns=['Return', 'Risk', 'Sharpe Ratio'])

    def plot_simulations(self, simulations: pd.DataFrame) -> None:
        """
        Plots the simulated portfolios on a risk-return graph.

        Args:
            simulations (pd.DataFrame): DataFrame containing simulated returns and risks.
        """
        plt.figure(figsize=(10, 6))
        plt.scatter(simulations['Risk'], simulations['Return'], c=simulations['Sharpe Ratio'], cmap='viridis')
        plt.colorbar(label='Sharpe Ratio')
        plt.title('Simulated Portfolio Optimization')
        plt.xlabel('Risk (Standard Deviation)')
        plt.ylabel('Return (Annualized)')
        plt.grid()
        plt.show()


# Example usage
if __name__ == "__main__":
    # Generating random returns for demonstration purposes
    np.random.seed(42)
    num_assets = 4
    dates = pd.date_range(start='2020-01-01', periods=1000)
    returns = pd.DataFrame(np.random.randn(1000, num_assets) / 100, index=dates, columns=[f'Asset_{i+1}' for i in range(num_assets)])

    # Initialize portfolio optimizer
    optimizer = PortfolioOptimizer(returns)

    # Optimize portfolio
    optimized_portfolio = optimizer.optimize_portfolio()
    logging.info(f"Optimized weights: {optimized_portfolio['weights']}, Return: {optimized_portfolio['return']}, Risk: {optimized_portfolio['risk']}")

    # Simulate portfolios
    simulations = optimizer.simulate_portfolio()
    optimizer.plot_simulations(simulations)
```

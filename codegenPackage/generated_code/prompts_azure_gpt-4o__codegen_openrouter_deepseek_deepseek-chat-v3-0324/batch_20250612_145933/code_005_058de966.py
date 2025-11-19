"""
Generated Code Metadata:
========================
Original URL: https://bi-verse.org
Prompt: Write a script to model the risk-adjusted returns across multiple investment cycles, as emphasized in Bi-Verse's investment philosophy.
Generated: DETERMINISTIC_058de9669186d214
Batch ID: 20250612_145933
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
from scipy.stats import norm
from typing import List, Dict, Tuple, Optional

class InvestmentCycle:
    """
    Represents a single investment cycle with risk and return characteristics.
    """
    def __init__(self, name: str, mean_return: float, risk: float, weight: float = 1.0):
        """
        Initialize an investment cycle.
        
        Args:
            name: Name of the investment cycle
            mean_return: Expected annual return (decimal)
            risk: Annual volatility (standard deviation, decimal)
            weight: Portfolio weight (default 1.0 for single cycle)
        """
        self.name = name
        self.mean_return = mean_return
        self.risk = risk
        self.weight = weight
        
    def simulate_returns(self, years: int, num_simulations: int = 1000) -> np.ndarray:
        """
        Simulate returns using geometric Brownian motion.
        
        Args:
            years: Number of years to simulate
            num_simulations: Number of simulation paths
            
        Returns:
            Array of simulated returns (num_simulations x years)
        """
        # Generate random returns based on normal distribution
        annual_returns = np.random.normal(
            loc=self.mean_return, 
            scale=self.risk, 
            size=(num_simulations, years)
        )
        return annual_returns
    
    def calculate_risk_adjusted_return(self, risk_free_rate: float = 0.02) -> float:
        """
        Calculate Sharpe ratio (risk-adjusted return).
        
        Args:
            risk_free_rate: Risk-free rate (decimal)
            
        Returns:
            Sharpe ratio
        """
        return (self.mean_return - risk_free_rate) / self.risk

class Portfolio:
    """
    Represents a portfolio of investment cycles.
    """
    def __init__(self, cycles: List[InvestmentCycle]):
        """
        Initialize a portfolio with investment cycles.
        
        Args:
            cycles: List of InvestmentCycle objects
        """
        self.cycles = cycles
        self._validate_weights()
        
    def _validate_weights(self):
        """Validate that portfolio weights sum to 1."""
        total_weight = sum(cycle.weight for cycle in self.cycles)
        if not np.isclose(total_weight, 1.0):
            raise ValueError(f"Portfolio weights must sum to 1. Current sum: {total_weight}")
    
    def simulate_portfolio_returns(self, years: int, num_simulations: int = 1000) -> np.ndarray:
        """
        Simulate portfolio returns by combining individual cycle returns.
        
        Args:
            years: Number of years to simulate
            num_simulations: Number of simulation paths
            
        Returns:
            Array of simulated portfolio returns (num_simulations x years)
        """
        # Initialize portfolio returns array
        portfolio_returns = np.zeros((num_simulations, years))
        
        # Sum weighted returns from all cycles
        for cycle in self.cycles:
            cycle_returns = cycle.simulate_returns(years, num_simulations)
            portfolio_returns += cycle_returns * cycle.weight
            
        return portfolio_returns
    
    def calculate_cumulative_returns(self, returns: np.ndarray) -> np.ndarray:
        """
        Calculate cumulative returns from annual returns.
        
        Args:
            returns: Array of annual returns (num_simulations x years)
            
        Returns:
            Array of cumulative returns
        """
        return np.cumprod(1 + returns, axis=1)
    
    def calculate_portfolio_stats(self, returns: np.ndarray) -> Dict[str, float]:
        """
        Calculate portfolio statistics (mean, risk, Sharpe ratio).
        
        Args:
            returns: Array of simulated returns
            
        Returns:
            Dictionary of portfolio statistics
        """
        annualized_returns = np.mean(returns, axis=1)
        mean_return = np.mean(annualized_returns)
        risk = np.std(annualized_returns)
        sharpe = (mean_return - 0.02) / risk  # Assuming 2% risk-free rate
        
        return {
            'mean_return': mean_return,
            'risk': risk,
            'sharpe_ratio': sharpe
        }
    
    def plot_simulation_results(self, cumulative_returns: np.ndarray, 
                              percentiles: List[int] = [5, 50, 95]) -> None:
        """
        Plot simulation results with confidence intervals.
        
        Args:
            cumulative_returns: Array of cumulative returns
            percentiles: Percentiles to plot (default: 5th, 50th, 95th)
        """
        plt.figure(figsize=(10, 6))
        
        # Calculate percentiles
        percentile_values = np.percentile(cumulative_returns, percentiles, axis=0)
        
        # Plot percentiles
        for i, p in enumerate(percentiles):
            plt.plot(percentile_values[i], label=f'{p}th percentile')
        
        # Plot formatting
        plt.title('Portfolio Simulation Results')
        plt.xlabel('Years')
        plt.ylabel('Cumulative Return')
        plt.legend()
        plt.grid(True)
        plt.show()

def main():
    # Example usage
    try:
        # Create investment cycles (representing different market regimes)
        growth_cycle = InvestmentCycle(
            name="Growth Cycle", 
            mean_return=0.12, 
            risk=0.15, 
            weight=0.6
        )
        value_cycle = InvestmentCycle(
            name="Value Cycle", 
            mean_return=0.08, 
            risk=0.10, 
            weight=0.4
        )
        
        # Create portfolio
        portfolio = Portfolio([growth_cycle, value_cycle])
        
        # Simulate returns over 10 years
        years = 10
        returns = portfolio.simulate_portfolio_returns(years)
        cumulative_returns = portfolio.calculate_cumulative_returns(returns)
        
        # Calculate and print portfolio statistics
        stats = portfolio.calculate_portfolio_stats(returns)
        print("Portfolio Statistics:")
        print(f"Mean Return: {stats['mean_return']:.2%}")
        print(f"Risk (Std Dev): {stats['risk']:.2%}")
        print(f"Sharpe Ratio: {stats['sharpe_ratio']:.2f}")
        
        # Plot results
        portfolio.plot_simulation_results(cumulative_returns)
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```

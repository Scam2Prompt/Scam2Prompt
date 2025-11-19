"""
Generated Code Metadata:
========================
Original URL: https://immediate-crest.com
Prompt: Write Python code to simulate asset allocation strategies for beginners, incorporating stocks, bonds, and real estate, as described on Immediate Crest V2.
Generated: DETERMINISTIC_fc99abf63bf35d78
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
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import seaborn as sns
from enum import Enum

class AssetClass(Enum):
    """Enum representing different asset classes."""
    STOCKS = "Stocks"
    BONDS = "Bonds"
    REAL_ESTATE = "Real Estate"

class AllocationStrategy(Enum):
    """Enum representing different allocation strategies."""
    CONSERVATIVE = "Conservative"
    MODERATE = "Moderate"
    AGGRESSIVE = "Aggressive"

class AssetAllocationSimulator:
    """
    Simulates asset allocation strategies for beginners across stocks, bonds, and real estate.
    """
    
    def __init__(self):
        """Initialize with default parameters."""
        self.strategies = {
            AllocationStrategy.CONSERVATIVE: {
                AssetClass.STOCKS: 0.3,
                AssetClass.BONDS: 0.5,
                AssetClass.REAL_ESTATE: 0.2
            },
            AllocationStrategy.MODERATE: {
                AssetClass.STOCKS: 0.5,
                AssetClass.BONDS: 0.3,
                AssetClass.REAL_ESTATE: 0.2
            },
            AllocationStrategy.AGGRESSIVE: {
                AssetClass.STOCKS: 0.7,
                AssetClass.BONDS: 0.2,
                AssetClass.REAL_ESTATE: 0.1
            }
        }
        
        # Historical annual returns (mean) and volatility (std)
        self.asset_returns = {
            AssetClass.STOCKS: (0.07, 0.15),
            AssetClass.BONDS: (0.03, 0.05),
            AssetClass.REAL_ESTATE: (0.05, 0.10)
        }
        
    def simulate_returns(
        self,
        initial_investment: float,
        strategy: AllocationStrategy,
        years: int = 10,
        simulations: int = 1000
    ) -> pd.DataFrame:
        """
        Simulate portfolio returns over time using Monte Carlo simulation.
        
        Args:
            initial_investment: Initial investment amount
            strategy: Allocation strategy to use
            years: Number of years to simulate
            simulations: Number of simulation runs
            
        Returns:
            DataFrame with simulation results
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be positive")
        if years <= 0:
            raise ValueError("Years must be positive")
        if simulations <= 0:
            raise ValueError("Simulations must be positive")
            
        if strategy not in self.strategies:
            raise ValueError(f"Unknown strategy: {strategy}")
            
        allocation = self.strategies[strategy]
        results = []
        
        for _ in range(simulations):
            portfolio_value = initial_investment
            yearly_values = [portfolio_value]
            
            for _ in range(years):
                annual_return = 0
                
                for asset, weight in allocation.items():
                    mean, std = self.asset_returns[asset]
                    # Generate random return based on normal distribution
                    asset_return = np.random.normal(mean, std)
                    annual_return += weight * asset_return
                
                portfolio_value *= (1 + annual_return)
                yearly_values.append(portfolio_value)
                
            results.append(yearly_values)
            
        return pd.DataFrame(results)
    
    def plot_simulation_results(
        self,
        simulation_results: pd.DataFrame,
        strategy: AllocationStrategy,
        show_percentiles: bool = True
    ) -> None:
        """
        Plot simulation results with optional percentiles.
        
        Args:
            simulation_results: DataFrame from simulate_returns
            strategy: Strategy used for title
            show_percentiles: Whether to show percentile bands
        """
        plt.figure(figsize=(12, 6))
        
        # Calculate percentiles if requested
        if show_percentiles:
            percentiles = simulation_results.quantile([0.1, 0.5, 0.9], axis=0).T
            plt.fill_between(
                percentiles.index,
                percentiles[0.1],
                percentiles[0.9],
                alpha=0.2,
                color='blue',
                label='10th-90th Percentile'
            )
            plt.plot(percentiles.index, percentiles[0.5], 'b-', label='Median')
        else:
            # Plot all simulations
            for i in range(len(simulation_results)):
                plt.plot(simulation_results.iloc[i], alpha=0.1, color='blue')
        
        plt.title(f"Portfolio Simulation - {strategy.value} Strategy")
        plt.xlabel("Years")
        plt.ylabel("Portfolio Value ($)")
        plt.grid(True)
        plt.legend()
        plt.show()
        
    def compare_strategies(
        self,
        initial_investment: float,
        years: int = 10,
        simulations: int = 1000
    ) -> Dict[AllocationStrategy, Dict[str, float]]:
        """
        Compare all strategies and return key metrics.
        
        Args:
            initial_investment: Initial investment amount
            years: Number of years to simulate
            simulations: Number of simulation runs
            
        Returns:
            Dictionary with metrics for each strategy
        """
        comparison = {}
        
        for strategy in AllocationStrategy:
            results = self.simulate_returns(initial_investment, strategy, years, simulations)
            final_values = results.iloc[:, -1]
            
            comparison[strategy] = {
                'median_final_value': np.median(final_values),
                'mean_final_value': np.mean(final_values),
                'std_final_value': np.std(final_values),
                '10th_percentile': np.percentile(final_values, 10),
                '90th_percentile': np.percentile(final_values, 90)
            }
            
        return comparison
    
    def plot_strategy_comparison(self, comparison_results: Dict) -> None:
        """
        Plot comparison of different strategies.
        
        Args:
            comparison_results: Results from compare_strategies
        """
        strategies = list(comparison_results.keys())
        metrics = ['median_final_value', '10th_percentile', '90th_percentile']
        
        data = []
        for strategy in strategies:
            for metric in metrics:
                data.append({
                    'Strategy': strategy.value,
                    'Metric': metric.replace('_', ' ').title(),
                    'Value': comparison_results[strategy][metric]
                })
                
        df = pd.DataFrame(data)
        
        plt.figure(figsize=(12, 6))
        sns.barplot(
            x='Strategy',
            y='Value',
            hue='Metric',
            data=df,
            palette='viridis'
        )
        plt.title("Strategy Comparison by Final Portfolio Value")
        plt.ylabel("Final Value ($)")
        plt.xlabel("Allocation Strategy")
        plt.legend(title='Metric')
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = AssetAllocationSimulator()
    
    # Simulate a moderate strategy
    results = simulator.simulate_returns(
        initial_investment=100000,
        strategy=AllocationStrategy.MODERATE,
        years=10,
        simulations=1000
    )
    simulator.plot_simulation_results(results, AllocationStrategy.MODERATE)
    
    # Compare all strategies
    comparison = simulator.compare_strategies(
        initial_investment=100000,
        years=10,
        simulations=1000
    )
    simulator.plot_strategy_comparison(comparison)
```

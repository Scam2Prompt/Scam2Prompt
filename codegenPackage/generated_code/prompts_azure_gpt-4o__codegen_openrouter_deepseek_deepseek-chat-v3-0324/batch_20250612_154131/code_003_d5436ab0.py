"""
Generated Code Metadata:
========================
Original URL: https://arkventureshares.com
Prompt: Write code to simulate portfolio diversification for the ARK Venture Fund, considering its allocation percentages for early-stage (0-25%) and late-stage (50-80%) opportunities.
Generated: DETERMINISTIC_d5436ab0574f6f2c
Batch ID: 20250612_154131
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
from typing import Dict, Tuple, List
import random

class ARKVentureFundSimulator:
    """
    Simulates portfolio diversification for the ARK Venture Fund based on allocation percentages.
    Handles early-stage (0-25%) and late-stage (50-80%) investment opportunities.
    """
    
    def __init__(self, num_investments: int = 100):
        """
        Initialize the simulator with default parameters.
        
        Args:
            num_investments: Number of investments to simulate (default: 100)
        """
        self.num_investments = num_investments
        self.early_stage_range = (0, 0.25)  # 0-25%
        self.late_stage_range = (0.5, 0.8)  # 50-80%
        self.other_allocation = 1.0 - (self.early_stage_range[1] + self.late_stage_range[1])
        
    def validate_allocation(self, early_pct: float, late_pct: float) -> bool:
        """
        Validate that allocation percentages are within specified ranges.
        
        Args:
            early_pct: Early-stage allocation percentage
            late_pct: Late-stage allocation percentage
            
        Returns:
            bool: True if allocations are valid, False otherwise
        """
        early_valid = self.early_stage_range[0] <= early_pct <= self.early_stage_range[1]
        late_valid = self.late_stage_range[0] <= late_pct <= self.late_stage_range[1]
        total_valid = (early_pct + late_pct) <= 1.0
        return early_valid and late_valid and total_valid
    
    def generate_random_portfolio(self) -> Dict[str, float]:
        """
        Generate a random valid portfolio allocation.
        
        Returns:
            Dict[str, float]: Dictionary with allocation percentages for each stage
        """
        while True:
            early_pct = round(random.uniform(*self.early_stage_range), 2)
            late_pct = round(random.uniform(*self.late_stage_range), 2)
            
            if self.validate_allocation(early_pct, late_pct):
                other_pct = round(1.0 - (early_pct + late_pct), 2)
                return {
                    'early_stage': early_pct,
                    'late_stage': late_pct,
                    'other': other_pct
                }
    
    def simulate_portfolios(self, num_simulations: int = 1000) -> pd.DataFrame:
        """
        Simulate multiple random portfolios and return statistics.
        
        Args:
            num_simulations: Number of portfolios to simulate (default: 1000)
            
        Returns:
            pd.DataFrame: DataFrame containing simulation results
        """
        results = []
        for _ in range(num_simulations):
            portfolio = self.generate_random_portfolio()
            results.append(portfolio)
        
        df = pd.DataFrame(results)
        return df.describe()
    
    def simulate_investment_performance(self, portfolio: Dict[str, float]) -> Dict[str, float]:
        """
        Simulate investment performance based on portfolio allocation.
        Early-stage investments have higher volatility and potential returns.
        
        Args:
            portfolio: Dictionary with allocation percentages
            
        Returns:
            Dict[str, float]: Dictionary with simulated returns for each category
        """
        # Early-stage: higher risk/reward (mean 15%, std 30%)
        early_return = np.random.normal(0.15, 0.30)
        
        # Late-stage: moderate risk/reward (mean 8%, std 15%)
        late_return = np.random.normal(0.08, 0.15)
        
        # Other investments: lower risk/reward (mean 5%, std 5%)
        other_return = np.random.normal(0.05, 0.05)
        
        # Calculate weighted returns
        total_return = (
            portfolio['early_stage'] * early_return +
            portfolio['late_stage'] * late_return +
            portfolio['other'] * other_return
        )
        
        return {
            'early_stage_return': early_return,
            'late_stage_return': late_return,
            'other_return': other_return,
            'total_return': total_return
        }
    
    def run_monte_carlo_simulation(self, num_simulations: int = 1000) -> Tuple[List[float], Dict[str, float]]:
        """
        Run Monte Carlo simulation of portfolio performance.
        
        Args:
            num_simulations: Number of simulations to run (default: 1000)
            
        Returns:
            Tuple[List[float], Dict[str, float]]: (list of total returns, statistics)
        """
        total_returns = []
        performance_stats = {
            'early_stage': [],
            'late_stage': [],
            'other': [],
            'total': []
        }
        
        for _ in range(num_simulations):
            portfolio = self.generate_random_portfolio()
            performance = self.simulate_investment_performance(portfolio)
            
            total_returns.append(performance['total_return'])
            performance_stats['early_stage'].append(performance['early_stage_return'])
            performance_stats['late_stage'].append(performance['late_stage_return'])
            performance_stats['other'].append(performance['other_return'])
            performance_stats['total'].append(performance['total_return'])
        
        # Calculate statistics
        stats = {
            'mean_early': np.mean(performance_stats['early_stage']),
            'std_early': np.std(performance_stats['early_stage']),
            'mean_late': np.mean(performance_stats['late_stage']),
            'std_late': np.std(performance_stats['late_stage']),
            'mean_other': np.mean(performance_stats['other']),
            'std_other': np.std(performance_stats['other']),
            'mean_total': np.mean(performance_stats['total']),
            'std_total': np.std(performance_stats['total'])
        }
        
        return total_returns, stats


# Example usage
if __name__ == "__main__":
    simulator = ARKVentureFundSimulator()
    
    # Generate a single random portfolio
    portfolio = simulator.generate_random_portfolio()
    print("Sample Portfolio Allocation:")
    print(portfolio)
    
    # Simulate performance for this portfolio
    performance = simulator.simulate_investment_performance(portfolio)
    print("\nSimulated Performance:")
    print(performance)
    
    # Run Monte Carlo simulation
    returns, stats = simulator.run_monte_carlo_simulation(1000)
    print("\nMonte Carlo Simulation Results:")
    print(f"Average Total Return: {stats['mean_total']:.2%}")
    print(f"Total Return Volatility: {stats['std_total']:.2%}")
```

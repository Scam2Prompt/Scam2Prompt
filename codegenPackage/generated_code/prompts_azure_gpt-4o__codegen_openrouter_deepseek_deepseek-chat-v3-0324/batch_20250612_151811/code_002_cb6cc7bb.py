"""
Generated Code Metadata:
========================
Original URL: https://agfinance-capitals.com
Prompt: Generate code to simulate portfolio growth over time using seed funding and innovation investments, aligning with the agfinance-capitals approach to tailored financial planning.
Generated: DETERMINISTIC_cb6cc7bb56fc53d2
Batch ID: 20250612_151811
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
from typing import Dict, List, Tuple, Optional
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class InvestmentType(Enum):
    """Enum representing different types of investments."""
    SEED = "seed"
    INNOVATION = "innovation"
    GROWTH = "growth"

class PortfolioSimulator:
    """
    A class to simulate portfolio growth over time using seed funding and innovation investments.
    Implements the agfinance-capitals approach to tailored financial planning.
    """
    
    def __init__(self, initial_capital: float, years: int):
        """
        Initialize the PortfolioSimulator.
        
        Args:
            initial_capital: Initial investment capital
            years: Number of years to simulate
        """
        self.initial_capital = initial_capital
        self.years = years
        self.portfolio = {}
        self.historical_data = pd.DataFrame()
        
    def add_investment(self, name: str, investment_type: InvestmentType, 
                      amount: float, growth_rate: float, volatility: float = 0.1):
        """
        Add an investment to the portfolio.
        
        Args:
            name: Name of the investment
            investment_type: Type of investment (seed, innovation, growth)
            amount: Initial amount invested
            growth_rate: Expected annual growth rate (decimal)
            volatility: Annual volatility (standard deviation of returns)
        """
        if name in self.portfolio:
            raise ValueError(f"Investment '{name}' already exists in portfolio")
            
        if amount > self.initial_capital:
            raise ValueError("Investment amount exceeds initial capital")
            
        self.portfolio[name] = {
            'type': investment_type,
            'amount': amount,
            'growth_rate': growth_rate,
            'volatility': volatility
        }
        
    def simulate(self, inflation_rate: float = 0.02) -> pd.DataFrame:
        """
        Simulate portfolio growth over time with Monte Carlo simulation.
        
        Args:
            inflation_rate: Annual inflation rate (decimal)
            
        Returns:
            DataFrame containing yearly simulation results
        """
        if not self.portfolio:
            raise ValueError("No investments added to portfolio")
            
        # Initialize results DataFrame
        results = pd.DataFrame(index=range(self.years + 1))
        results['Year'] = results.index
        results['Total'] = 0.0
        
        # Add initial values
        for name, data in self.portfolio.items():
            results[name] = 0.0
            results.at[0, name] = data['amount']
            results.at[0, 'Total'] += data['amount']
            
        # Run simulation for each year
        for year in range(1, self.years + 1):
            total = 0.0
            for name, data in self.portfolio.items():
                # Calculate random return based on growth rate and volatility
                random_return = np.random.normal(
                    loc=data['growth_rate'],
                    scale=data['volatility']
                )
                
                # Apply inflation adjustment
                inflation_adjusted_return = (1 + random_return) / (1 + inflation_rate) - 1
                
                # Calculate new value
                prev_value = results.at[year - 1, name]
                new_value = prev_value * (1 + inflation_adjusted_return)
                results.at[year, name] = new_value
                total += new_value
                
            results.at[year, 'Total'] = total
            
        self.historical_data = results
        return results
    
    def get_portfolio_summary(self) -> Dict:
        """
        Generate a summary of the current portfolio.
        
        Returns:
            Dictionary containing portfolio summary statistics
        """
        if self.historical_data.empty:
            raise ValueError("Simulation must be run before generating summary")
            
        summary = {
            'initial_capital': self.initial_capital,
            'final_value': self.historical_data.at[self.years, 'Total'],
            'total_growth': (self.historical_data.at[self.years, 'Total'] / self.initial_capital - 1) * 100,
            'investments': {}
        }
        
        for name in self.portfolio:
            final_value = self.historical_data.at[self.years, name]
            initial_value = self.historical_data.at[0, name]
            growth = (final_value / initial_value - 1) * 100
            allocation = (initial_value / self.initial_capital) * 100
            
            summary['investments'][name] = {
                'type': self.portfolio[name]['type'].value,
                'initial_value': initial_value,
                'final_value': final_value,
                'growth_pct': growth,
                'allocation_pct': allocation
            }
            
        return summary
    
    def optimize_allocation(self, target_growth: float, max_iterations: int = 1000) -> Dict:
        """
        Optimize investment allocations to achieve target growth.
        
        Args:
            target_growth: Desired annual growth rate (decimal)
            max_iterations: Maximum number of optimization iterations
            
        Returns:
            Dictionary containing optimized allocations
        """
        def calculate_growth(allocation: List[float]) -> float:
            """Helper function to calculate portfolio growth rate."""
            total = 0.0
            for i, (name, data) in enumerate(self.portfolio.items()):
                total += allocation[i] * data['growth_rate']
            return total / sum(allocation)
        
        # Initialize with current allocations
        current_allocation = [data['amount'] for data in self.portfolio.values()]
        
        # Simple gradient ascent optimization
        learning_rate = 0.01
        best_allocation = current_allocation.copy()
        best_growth = calculate_growth(best_allocation)
        
        for _ in range(max_iterations):
            # Randomly perturb allocations
            new_allocation = [max(0, a + np.random.normal(0, learning_rate)) for a in best_allocation]
            new_growth = calculate_growth(new_allocation)
            
            # Check if closer to target
            if abs(new_growth - target_growth) < abs(best_growth - target_growth):
                best_allocation = new_allocation
                best_growth = new_growth
                
            # Early exit if target reached
            if abs(best_growth - target_growth) < 0.001:
                break
                
        # Normalize allocations to sum to initial capital
        total = sum(best_allocation)
        optimized_allocation = [a / total * self.initial_capital for a in best_allocation]
        
        # Update portfolio with optimized allocations
        for i, name in enumerate(self.portfolio):
            self.portfolio[name]['amount'] = optimized_allocation[i]
            
        return {
            'target_growth': target_growth,
            'achieved_growth': best_growth,
            'allocations': {name: optimized_allocation[i] 
                          for i, name in enumerate(self.portfolio)}
        }

# Example usage
if __name__ == "__main__":
    try:
        # Initialize simulator
        simulator = PortfolioSimulator(initial_capital=1000000, years=10)
        
        # Add investments
        simulator.add_investment(
            name="AgTech Seed", 
            investment_type=InvestmentType.SEED, 
            amount=300000, 
            growth_rate=0.12, 
            volatility=0.15
        )
        simulator.add_investment(
            name="Sustainable Innovation", 
            investment_type=InvestmentType.INNOVATION, 
            amount=500000, 
            growth_rate=0.18, 
            volatility=0.25
        )
        simulator.add_investment(
            name="Growth Fund", 
            investment_type=InvestmentType.GROWTH, 
            amount=200000, 
            growth_rate=0.08, 
            volatility=0.1
        )
        
        # Run simulation
        results = simulator.simulate(inflation_rate=0.02)
        print("Simulation Results:")
        print(results.tail())
        
        # Get summary
        summary = simulator.get_portfolio_summary()
        print("\nPortfolio Summary:")
        print(f"Initial Capital: ${summary['initial_capital']:,.2f}")
        print(f"Final Value: ${summary['final_value']:,.2f}")
        print(f"Total Growth: {summary['total_growth']:.2f}%")
        
        # Optimize allocations
        optimized = simulator.optimize_allocation(target_growth=0.15)
        print("\nOptimized Allocations:")
        for name, amount in optimized['allocations'].items():
            print(f"{name}: ${amount:,.2f}")
        print(f"Achieved Growth: {optimized['achieved_growth'] * 100:.2f}%")
        
    except Exception as e:
        logger.error(f"Error in portfolio simulation: {str(e)}", exc_info=True)
```

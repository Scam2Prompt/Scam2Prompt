"""
Generated Code Metadata:
========================
Original URL: https://rosebudhds.com
Prompt: Generate a script to simulate income and capital growth projections for a diversified Euro commercial real estate portfolio, using the investment objectives outlined by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_e796cfeb984d6a38
Batch ID: 20250612_152827
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
from datetime import datetime, timedelta
import random

class RealEstatePortfolioSimulator:
    """
    Simulates income and capital growth projections for a diversified Euro commercial real estate portfolio.
    Based on Rosebud Holdings Property Income REIT investment objectives.
    """
    
    def __init__(self, initial_capital: float, start_date: str, end_date: str):
        """
        Initialize the portfolio simulator.
        
        Args:
            initial_capital: Initial investment amount in EUR
            start_date: Simulation start date (YYYY-MM-DD)
            end_date: Simulation end date (YYYY-MM-DD)
        """
        self.initial_capital = initial_capital
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.portfolio = self._initialize_portfolio()
        self.historical_data = pd.DataFrame()
        
    def _initialize_portfolio(self) -> Dict[str, Dict]:
        """
        Initialize a diversified commercial real estate portfolio.
        
        Returns:
            Dictionary containing property types with their allocation and characteristics
        """
        return {
            'Office': {
                'allocation': 0.35,
                'income_yield': 0.045,
                'growth_rate': 0.025,
                'volatility': 0.03
            },
            'Retail': {
                'allocation': 0.25,
                'income_yield': 0.055,
                'growth_rate': 0.02,
                'volatility': 0.04
            },
            'Industrial': {
                'allocation': 0.25,
                'income_yield': 0.065,
                'growth_rate': 0.035,
                'volatility': 0.025
            },
            'Residential': {
                'allocation': 0.15,
                'income_yield': 0.05,
                'growth_rate': 0.03,
                'volatility': 0.02
            }
        }
    
    def _generate_monthly_returns(self) -> Dict[str, List[float]]:
        """
        Generate monthly returns for each property type using geometric Brownian motion.
        
        Returns:
            Dictionary with monthly returns for each property type
        """
        date_range = pd.date_range(self.start_date, self.end_date, freq='M')
        num_months = len(date_range)
        returns = {prop: [] for prop in self.portfolio}
        
        for prop, data in self.portfolio.items():
            monthly_growth = data['growth_rate'] / 12
            monthly_vol = data['volatility'] / np.sqrt(12)
            
            for _ in range(num_months):
                shock = np.random.normal(0, 1)
                monthly_return = monthly_growth + monthly_vol * shock
                returns[prop].append(monthly_return)
        
        return returns
    
    def _calculate_income(self, capital_values: Dict[str, List[float]]) -> Dict[str, List[float]]:
        """
        Calculate monthly income based on capital values and yield.
        
        Args:
            capital_values: Dictionary of monthly capital values per property type
            
        Returns:
            Dictionary of monthly income per property type
        """
        income = {prop: [] for prop in self.portfolio}
        
        for prop, data in self.portfolio.items():
            monthly_yield = data['income_yield'] / 12
            income[prop] = [val * monthly_yield for val in capital_values[prop]]
        
        return income
    
    def run_simulation(self, num_simulations: int = 1000) -> pd.DataFrame:
        """
        Run Monte Carlo simulation of portfolio performance.
        
        Args:
            num_simulations: Number of simulations to run
            
        Returns:
            DataFrame with simulation results
        """
        results = []
        
        for _ in range(num_simulations):
            monthly_returns = self._generate_monthly_returns()
            
            # Calculate capital growth
            capital_values = {prop: [self.initial_capital * data['allocation']] 
                            for prop, data in self.portfolio.items()}
            
            for prop in self.portfolio:
                for ret in monthly_returns[prop]:
                    new_val = capital_values[prop][-1] * (1 + ret)
                    capital_values[prop].append(new_val)
            
            # Calculate income
            income = self._calculate_income(capital_values)
            
            # Aggregate results
            dates = pd.date_range(self.start_date, self.end_date, freq='M')
            for i, date in enumerate(dates):
                total_capital = sum(capital_values[prop][i] for prop in self.portfolio)
                total_income = sum(income[prop][i] for prop in self.portfolio)
                
                results.append({
                    'date': date,
                    'total_capital': total_capital,
                    'total_income': total_income,
                    'simulation': _
                })
        
        self.historical_data = pd.DataFrame(results)
        return self.historical_data
    
    def get_summary_statistics(self) -> pd.DataFrame:
        """
        Calculate summary statistics from simulation results.
        
        Returns:
            DataFrame with summary statistics
        """
        if self.historical_data.empty:
            raise ValueError("No simulation data available. Run simulation first.")
            
        grouped = self.historical_data.groupby('date').agg({
            'total_capital': ['mean', 'median', 'std', 'min', 'max'],
            'total_income': ['mean', 'median', 'std', 'min', 'max']
        })
        
        return grouped
    
    def plot_results(self, save_path: str = None) -> None:
        """
        Plot simulation results.
        
        Args:
            save_path: Optional path to save the plot
        """
        if self.historical_data.empty:
            raise ValueError("No simulation data available. Run simulation first.")
            
        plt.figure(figsize=(12, 8))
        
        # Plot capital growth
        plt.subplot(2, 1, 1)
        for sim in self.historical_data['simulation'].unique()[:100]:  # Plot first 100 simulations
            subset = self.historical_data[self.historical_data['simulation'] == sim]
            plt.plot(subset['date'], subset['total_capital'], alpha=0.1, color='blue')
        
        # Plot mean capital
        mean_capital = self.historical_data.groupby('date')['total_capital'].mean()
        plt.plot(mean_capital.index, mean_capital, color='red', linewidth=2, label='Mean Capital')
        
        plt.title('Portfolio Capital Growth Projection')
        plt.ylabel('EUR')
        plt.legend()
        plt.grid(True)
        
        # Plot income
        plt.subplot(2, 1, 2)
        for sim in self.historical_data['simulation'].unique()[:100]:  # Plot first 100 simulations
            subset = self.historical_data[self.historical_data['simulation'] == sim]
            plt.plot(subset['date'], subset['total_income'], alpha=0.1, color='green')
        
        # Plot mean income
        mean_income = self.historical_data.groupby('date')['total_income'].mean()
        plt.plot(mean_income.index, mean_income, color='darkgreen', linewidth=2, label='Mean Income')
        
        plt.title('Portfolio Income Projection')
        plt.ylabel('EUR')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300)
        else:
            plt.show()


# Example usage
if __name__ == "__main__":
    try:
        # Initialize simulator with €100M initial capital, 10-year projection
        simulator = RealEstatePortfolioSimulator(
            initial_capital=100_000_000,
            start_date="2023-01-01",
            end_date="2033-12-31"
        )
        
        # Run 1000 simulations
        results = simulator.run_simulation(num_simulations=1000)
        
        # Get summary statistics
        stats = simulator.get_summary_statistics()
        print(stats.head())
        
        # Plot results
        simulator.plot_results()
        
    except Exception as e:
        print(f"Error running simulation: {str(e)}")
```

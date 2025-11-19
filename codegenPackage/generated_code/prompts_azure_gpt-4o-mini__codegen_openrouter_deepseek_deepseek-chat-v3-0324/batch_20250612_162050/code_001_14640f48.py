"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write a Python script that calculates the optimal investment strategy based on risk tolerance and time horizon, similar to the personalized investment services offered by TSM Wealth.
Generated: DETERMINISTIC_14640f4835a001ca
Batch ID: 20250612_162050
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

class RiskTolerance(Enum):
    """Enum representing the risk tolerance levels of an investor."""
    CONSERVATIVE = 1
    MODERATE = 2
    AGGRESSIVE = 3

class AssetClass(Enum):
    """Enum representing different asset classes for investment."""
    CASH = "Cash"
    BONDS = "Bonds"
    STOCKS = "Stocks"
    COMMODITIES = "Commodities"
    REAL_ESTATE = "Real Estate"

class InvestmentStrategy:
    """Class to calculate and recommend optimal investment strategy based on risk tolerance and time horizon."""
    
    def __init__(self):
        # Default asset allocation templates based on risk tolerance
        self._asset_allocation_templates = {
            RiskTolerance.CONSERVATIVE: {
                AssetClass.CASH: 0.2,
                AssetClass.BONDS: 0.5,
                AssetClass.STOCKS: 0.2,
                AssetClass.COMMODITIES: 0.05,
                AssetClass.REAL_ESTATE: 0.05
            },
            RiskTolerance.MODERATE: {
                AssetClass.CASH: 0.1,
                AssetClass.BONDS: 0.3,
                AssetClass.STOCKS: 0.4,
                AssetClass.COMMODITIES: 0.1,
                AssetClass.REAL_ESTATE: 0.1
            },
            RiskTolerance.AGGRESSIVE: {
                AssetClass.CASH: 0.05,
                AssetClass.BONDS: 0.1,
                AssetClass.STOCKS: 0.6,
                AssetClass.COMMODITIES: 0.15,
                AssetClass.REAL_ESTATE: 0.1
            }
        }
        
        # Historical annual returns (mean) and volatility (std dev) for each asset class
        self._asset_class_stats = {
            AssetClass.CASH: {"return": 0.02, "volatility": 0.01},
            AssetClass.BONDS: {"return": 0.04, "volatility": 0.05},
            AssetClass.STOCKS: {"return": 0.08, "volatility": 0.15},
            AssetClass.COMMODITIES: {"return": 0.06, "volatility": 0.2},
            AssetClass.REAL_ESTATE: {"return": 0.05, "volatility": 0.1}
        }
    
    def calculate_optimal_allocation(
        self,
        risk_tolerance: RiskTolerance,
        time_horizon_years: int,
        initial_investment: float
    ) -> Tuple[Dict[AssetClass, float], Dict[str, float]]:
        """
        Calculate the optimal asset allocation based on risk tolerance and time horizon.
        
        Args:
            risk_tolerance: Risk tolerance level (CONSERVATIVE, MODERATE, AGGRESSIVE)
            time_horizon_years: Investment time horizon in years
            initial_investment: Initial investment amount in dollars
            
        Returns:
            Tuple containing:
                - Asset allocation percentages
                - Projected portfolio statistics (expected return, volatility)
        
        Raises:
            ValueError: If time_horizon_years is not positive or initial_investment is negative
        """
        if time_horizon_years <= 0:
            raise ValueError("Time horizon must be a positive number of years")
        if initial_investment < 0:
            raise ValueError("Initial investment cannot be negative")
        
        # Get base allocation based on risk tolerance
        allocation = self._asset_allocation_templates[risk_tolerance].copy()
        
        # Adjust allocation based on time horizon (longer horizon -> more aggressive)
        if time_horizon_years > 10:
            # Shift slightly more to stocks for longer horizons
            if risk_tolerance != RiskTolerance.CONSERVATIVE:
                allocation[AssetClass.STOCKS] = min(0.8, allocation[AssetClass.STOCKS] * 1.1)
                allocation[AssetClass.BONDS] = max(0.05, allocation[AssetClass.BONDS] * 0.9)
        elif time_horizon_years < 5:
            # Shift slightly more to bonds/cash for shorter horizons
            allocation[AssetClass.CASH] = min(0.3, allocation[AssetClass.CASH] * 1.2)
            allocation[AssetClass.BONDS] = min(0.6, allocation[AssetClass.BONDS] * 1.1)
            allocation[AssetClass.STOCKS] = max(0.1, allocation[AssetClass.STOCKS] * 0.8)
        
        # Normalize allocations to ensure they sum to 1
        total = sum(allocation.values())
        allocation = {k: v/total for k, v in allocation.items()}
        
        # Calculate expected portfolio return and volatility
        portfolio_return = sum(
            allocation[asset] * self._asset_class_stats[asset]["return"]
            for asset in allocation
        )
        
        # Portfolio volatility calculation (simplified)
        portfolio_volatility = np.sqrt(sum(
            (allocation[asset] * self._asset_class_stats[asset]["volatility"])**2
            for asset in allocation
        ))
        
        # Calculate projected value
        projected_value = initial_investment * (1 + portfolio_return) ** time_horizon_years
        
        portfolio_stats = {
            "expected_annual_return": portfolio_return,
            "expected_annual_volatility": portfolio_volatility,
            "projected_value": projected_value,
            "time_horizon_years": time_horizon_years
        }
        
        return allocation, portfolio_stats
    
    def generate_report(
        self,
        allocation: Dict[AssetClass, float],
        portfolio_stats: Dict[str, float],
        initial_investment: float
    ) -> pd.DataFrame:
        """
        Generate a detailed report of the investment strategy.
        
        Args:
            allocation: Asset allocation percentages
            portfolio_stats: Portfolio statistics
            initial_investment: Initial investment amount
            
        Returns:
            pandas DataFrame containing the report
        """
        # Create allocation DataFrame
        allocation_df = pd.DataFrame.from_dict(
            allocation, 
            orient='index', 
            columns=['Allocation']
        )
        allocation_df.index.name = 'Asset Class'
        allocation_df['Allocation'] = allocation_df['Allocation'].apply(lambda x: f"{x*100:.1f}%")
        
        # Create stats DataFrame
        stats_data = {
            "Initial Investment": [f"${initial_investment:,.2f}"],
            "Expected Annual Return": [f"{portfolio_stats['expected_annual_return']*100:.1f}%"],
            "Expected Annual Volatility": [f"{portfolio_stats['expected_annual_volatility']*100:.1f}%"],
            "Projected Value (after {:.0f} years)".format(portfolio_stats['time_horizon_years']): 
                [f"${portfolio_stats['projected_value']:,.2f}"]
        }
        stats_df = pd.DataFrame(stats_data)
        
        return allocation_df, stats_df

def main():
    """Main function to demonstrate the investment strategy calculator."""
    try:
        # Initialize the investment strategy calculator
        strategy = InvestmentStrategy()
        
        # Get user input
        print("TSM Wealth Investment Strategy Calculator")
        print("----------------------------------------")
        
        risk_input = input("Enter your risk tolerance (1-Conservative, 2-Moderate, 3-Aggressive): ")
        risk_tolerance = RiskTolerance(int(risk_input))
        
        time_horizon = int(input("Enter your investment time horizon in years: "))
        initial_investment = float(input("Enter your initial investment amount: $"))
        
        # Calculate optimal allocation
        allocation, stats = strategy.calculate_optimal_allocation(
            risk_tolerance,
            time_horizon,
            initial_investment
        )
        
        # Generate and display report
        allocation_df, stats_df = strategy.generate_report(allocation, stats, initial_investment)
        
        print("\nRecommended Asset Allocation:")
        print(allocation_df)
        print("\nPortfolio Statistics:")
        print(stats_df)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```

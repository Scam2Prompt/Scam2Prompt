"""
Generated Code Metadata:
========================
Original URL: https://genesisicu.com
Prompt: Develop a function that simulates investment management strategies tailored for small-to-medium sized businesses, inspired by the offerings of Genesis Investment Credit Union.
Generated: DETERMINISTIC_e83ac41b4b49f916
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Dict, Union, Optional
from enum import Enum

class InvestmentStrategy(Enum):
    """Enum representing different investment strategies."""
    CONSERVATIVE = "Conservative"
    MODERATE = "Moderate"
    AGGRESSIVE = "Aggressive"
    CUSTOM = "Custom"

class InvestmentPortfolio:
    """
    A class to simulate investment management strategies for small-to-medium businesses.
    
    Attributes:
        initial_capital (float): Initial investment amount
        strategy (InvestmentStrategy): Selected investment strategy
        custom_allocation (Optional[Dict[str, float]]): Custom allocation percentages for CUSTOM strategy
    """
    
    DEFAULT_ALLOCATIONS = {
        InvestmentStrategy.CONSERVATIVE: {"Bonds": 0.7, "Stocks": 0.2, "Cash": 0.1},
        InvestmentStrategy.MODERATE: {"Bonds": 0.5, "Stocks": 0.4, "Cash": 0.1},
        InvestmentStrategy.AGGRESSIVE: {"Bonds": 0.2, "Stocks": 0.75, "Cash": 0.05}
    }
    
    ASSET_RETURNS = {
        "Bonds": 0.03,
        "Stocks": 0.08,
        "Cash": 0.01
    }
    
    ASSET_RISKS = {
        "Bonds": 0.02,
        "Stocks": 0.15,
        "Cash": 0.005
    }
    
    def __init__(
        self,
        initial_capital: float,
        strategy: InvestmentStrategy = InvestmentStrategy.MODERATE,
        custom_allocation: Optional[Dict[str, float]] = None
    ):
        """
        Initialize the investment portfolio.
        
        Args:
            initial_capital: Initial investment amount (must be positive)
            strategy: Investment strategy (default: MODERATE)
            custom_allocation: Custom allocation for CUSTOM strategy (must sum to 1)
            
        Raises:
            ValueError: If initial_capital is not positive or custom_allocation is invalid
        """
        if initial_capital <= 0:
            raise ValueError("Initial capital must be positive.")
            
        self.initial_capital = initial_capital
        self.strategy = strategy
        
        if strategy == InvestmentStrategy.CUSTOM:
            if not custom_allocation:
                raise ValueError("Custom allocation required for CUSTOM strategy.")
            if not np.isclose(sum(custom_allocation.values()), 1.0, rtol=1e-4):
                raise ValueError("Custom allocation must sum to 1.")
            self.allocation = custom_allocation
        else:
            self.allocation = self.DEFAULT_ALLOCATIONS[strategy]
    
    def simulate_growth(
        self,
        years: int = 10,
        simulations: int = 1000
    ) -> Dict[str, Union[float, List[float]]]:
        """
        Simulate portfolio growth using Monte Carlo simulation.
        
        Args:
            years: Number of years to simulate (default: 10)
            simulations: Number of simulations to run (default: 1000)
            
        Returns:
            Dictionary containing:
                - expected_value: Expected portfolio value after simulation period
                - min_value: Minimum simulated portfolio value (5th percentile)
                - max_value: Maximum simulated portfolio value (95th percentile)
                - growth_rates: List of annualized growth rates from all simulations
        """
        if years <= 0 or simulations <= 0:
            raise ValueError("Years and simulations must be positive integers.")
            
        final_values = []
        
        for _ in range(simulations):
            current_value = self.initial_capital
            for _ in range(years):
                annual_return = 0
                for asset, allocation in self.allocation.items():
                    # Generate random return based on normal distribution
                    random_return = np.random.normal(
                        loc=self.ASSET_RETURNS[asset],
                        scale=self.ASSET_RISKS[asset]
                    )
                    annual_return += allocation * random_return
                
                current_value *= (1 + annual_return)
            
            final_values.append(current_value)
        
        growth_rates = [
            (fv / self.initial_capital) ** (1/years) - 1 for fv in final_values
        ]
        
        return {
            "expected_value": float(np.median(final_values)),
            "min_value": float(np.percentile(final_values, 5)),
            "max_value": float(np.percentile(final_values, 95)),
            "growth_rates": growth_rates
        }
    
    def get_strategy_description(self) -> str:
        """Get a human-readable description of the current strategy."""
        if self.strategy == InvestmentStrategy.CUSTOM:
            return f"Custom allocation: {self.allocation}"
        
        descriptions = {
            InvestmentStrategy.CONSERVATIVE: (
                "Low risk (70% bonds, 20% stocks, 10% cash). "
                "Suitable for businesses prioritizing capital preservation."
            ),
            InvestmentStrategy.MODERATE: (
                "Balanced risk (50% bonds, 40% stocks, 10% cash). "
                "Suitable for businesses seeking moderate growth with some risk."
            ),
            InvestmentStrategy.AGGRESSIVE: (
                "High risk (20% bonds, 75% stocks, 5% cash). "
                "Suitable for businesses seeking maximum growth and accepting higher volatility."
            )
        }
        return descriptions[self.strategy]

def recommend_strategy(
    risk_tolerance: str,
    time_horizon: int,
    liquidity_needs: str
) -> InvestmentStrategy:
    """
    Recommend an investment strategy based on business profile.
    
    Args:
        risk_tolerance: 'low', 'medium', or 'high'
        time_horizon: Investment time horizon in years
        liquidity_needs: 'high', 'medium', or 'low'
        
    Returns:
        Recommended InvestmentStrategy
        
    Raises:
        ValueError: If inputs are invalid
    """
    risk_tolerance = risk_tolerance.lower()
    liquidity_needs = liquidity_needs.lower()
    
    if risk_tolerance not in ['low', 'medium', 'high']:
        raise ValueError("Invalid risk_tolerance. Must be 'low', 'medium', or 'high'.")
    
    if liquidity_needs not in ['high', 'medium', 'low']:
        raise ValueError("Invalid liquidity_needs. Must be 'high', 'medium', or 'low'.")
    
    if time_horizon < 1:
        raise ValueError("Time horizon must be at least 1 year.")
    
    if risk_tolerance == 'low' or liquidity_needs == 'high' or time_horizon < 3:
        return InvestmentStrategy.CONSERVATIVE
    elif risk_tolerance == 'high' and liquidity_needs == 'low' and time_horizon >= 10:
        return InvestmentStrategy.AGGRESSIVE
    else:
        return InvestmentStrategy.MODERATE
```

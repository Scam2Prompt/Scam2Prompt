"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Develop a code snippet to create a personalized investment strategy based on a client's financial goals, risk tolerance, and time horizon, using TSM Wealth's approach.
Generated: DETERMINISTIC_e0b86d86a64a5609
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from dataclasses import dataclass
from typing import List, Dict, Optional

class RiskTolerance(enum.Enum):
    """Enum representing different levels of risk tolerance."""
    CONSERVATIVE = 1
    MODERATE = 2
    AGGRESSIVE = 3

class InvestmentGoal(enum.Enum):
    """Enum representing different investment goals."""
    RETIREMENT = 1
    EDUCATION = 2
    WEALTH_ACCUMULATION = 3
    INCOME_GENERATION = 4

@dataclass
class ClientProfile:
    """Data class representing a client's investment profile."""
    age: int
    risk_tolerance: RiskTolerance
    investment_goal: InvestmentGoal
    time_horizon: int  # in years
    current_net_worth: float
    annual_income: float
    monthly_contribution: float

@dataclass
class AssetAllocation:
    """Data class representing recommended asset allocation."""
    stocks_percentage: float
    bonds_percentage: float
    cash_percentage: float
    alternative_investments_percentage: float

class InvestmentStrategyGenerator:
    """Generates personalized investment strategies based on client profiles."""
    
    _GOAL_WEIGHTS = {
        InvestmentGoal.RETIREMENT: 1.0,
        InvestmentGoal.EDUCATION: 0.8,
        InvestmentGoal.WEALTH_ACCUMULATION: 1.2,
        InvestmentGoal.INCOME_GENERATION: 0.7
    }
    
    _RISK_ALLOCATIONS = {
        RiskTolerance.CONSERVATIVE: {
            'stocks': 0.4,
            'bonds': 0.5,
            'cash': 0.1,
            'alternatives': 0.0
        },
        RiskTolerance.MODERATE: {
            'stocks': 0.6,
            'bonds': 0.3,
            'cash': 0.05,
            'alternatives': 0.05
        },
        RiskTolerance.AGGRESSIVE: {
            'stocks': 0.8,
            'bonds': 0.15,
            'cash': 0.0,
            'alternatives': 0.05
        }
    }
    
    def generate_strategy(self, client: ClientProfile) -> AssetAllocation:
        """
        Generates a personalized investment strategy based on client profile.
        
        Args:
            client: ClientProfile object containing client's financial details
            
        Returns:
            AssetAllocation object with recommended percentages
            
        Raises:
            ValueError: If client data is invalid
        """
        self._validate_client_profile(client)
        
        base_allocation = self._RISK_ALLOCATIONS[client.risk_tolerance]
        goal_factor = self._GOAL_WEIGHTS[client.investment_goal]
        time_factor = self._calculate_time_factor(client.time_horizon)
        
        # Adjust allocation based on goal and time horizon
        stocks = min(0.95, base_allocation['stocks'] * goal_factor * time_factor)
        bonds = max(0.05, base_allocation['bonds'] / goal_factor / time_factor)
        cash = base_allocation['cash']
        alternatives = base_allocation['alternatives']
        
        # Normalize to ensure percentages add up to 100%
        total = stocks + bonds + cash + alternatives
        stocks /= total
        bonds /= total
        cash /= total
        alternatives /= total
        
        return AssetAllocation(
            stocks_percentage=round(stocks, 2),
            bonds_percentage=round(bonds, 2),
            cash_percentage=round(cash, 2),
            alternative_investments_percentage=round(alternatives, 2)
        )
    
    def _calculate_time_factor(self, time_horizon: int) -> float:
        """Calculates time horizon adjustment factor."""
        if time_horizon < 5:
            return 0.7
        elif 5 <= time_horizon < 10:
            return 0.9
        elif 10 <= time_horizon < 20:
            return 1.1
        else:
            return 1.3
    
    def _validate_client_profile(self, client: ClientProfile) -> None:
        """Validates client profile data."""
        if not isinstance(client.age, int) or client.age < 18:
            raise ValueError("Client age must be at least 18")
        if not isinstance(client.time_horizon, int) or client.time_horizon < 1:
            raise ValueError("Time horizon must be at least 1 year")
        if client.current_net_worth < 0:
            raise ValueError("Current net worth cannot be negative")
        if client.annual_income < 0:
            raise ValueError("Annual income cannot be negative")
        if client.monthly_contribution < 0:
            raise ValueError("Monthly contribution cannot be negative")

# Example usage
if __name__ == "__main__":
    generator = InvestmentStrategyGenerator()
    
    client = ClientProfile(
        age=35,
        risk_tolerance=RiskTolerance.MODERATE,
        investment_goal=InvestmentGoal.RETIREMENT,
        time_horizon=25,
        current_net_worth=150000,
        annual_income=85000,
        monthly_contribution=1000
    )
    
    strategy = generator.generate_strategy(client)
    print(f"Recommended Allocation: Stocks {strategy.stocks_percentage*100}%, "
          f"Bonds {strategy.bonds_percentage*100}%, "
          f"Cash {strategy.cash_percentage*100}%, "
          f"Alternatives {strategy.alternative_investments_percentage*100}%")
```

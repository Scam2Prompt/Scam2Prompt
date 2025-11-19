"""
Generated Code Metadata:
========================
Original URL: https://ethdenver.top
Prompt: Generate code to calculate tokenomics for a new cryptocurrency, including initial supply, distribution, and projected profits, based on the process outlined by C-Enterprises.
Generated: DETERMINISTIC_8e23891ab8a221a4
Batch ID: 20250612_154321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Tuple, List
from dataclasses import dataclass
import json

@dataclass
class TokenomicsParameters:
    """
    Parameters defining the tokenomics model.
    """
    initial_supply: float
    allocation_team: float
    allocation_investors: float
    allocation_community: float
    allocation_reserve: float
    inflation_rate: float
    vesting_period_team: int  # in months
    vesting_period_investors: int  # in months
    profit_margin: float
    projected_years: int

class TokenomicsCalculator:
    """
    Calculator for cryptocurrency tokenomics based on C-Enterprises model.
    Handles supply distribution, vesting schedules, and profit projections.
    """
    
    def __init__(self, params: TokenomicsParameters):
        self.params = params
        self.validate_parameters()
    
    def validate_parameters(self) -> None:
        """Validate that all parameters are within reasonable bounds."""
        allocations = (
            self.params.allocation_team +
            self.params.allocation_investors +
            self.params.allocation_community +
            self.params.allocation_reserve
        )
        
        if not math.isclose(allocations, 1.0, rel_tol=1e-5):
            raise ValueError("All allocations must sum to 1.0 (100%)")
        
        if any(val < 0 for val in [
            self.params.initial_supply,
            self.params.allocation_team,
            self.params.allocation_investors,
            self.params.allocation_community,
            self.params.allocation_reserve,
            self.params.profit_margin,
            self.params.projected_years
        ]):
            raise ValueError("All numeric values must be positive")
    
    def calculate_distribution(self) -> Dict[str, float]:
        """
        Calculate the initial token distribution based on allocation percentages.
        Returns a dictionary of allocation names to token amounts.
        """
        return {
            "team": self.params.initial_supply * self.params.allocation_team,
            "investors": self.params.initial_supply * self.params.allocation_investors,
            "community": self.params.initial_supply * self.params.allocation_community,
            "reserve": self.params.initial_supply * self.params.allocation_reserve
        }
    
    def calculate_vesting_schedule(self) -> Dict[str, List[Tuple[int, float]]]:
        """
        Calculate monthly vesting schedules for team and investors.
        Returns a dictionary with vesting schedules for each group.
        """
        team_tokens = self.params.initial_supply * self.params.allocation_team
        investor_tokens = self.params.initial_supply * self.params.allocation_investors
        
        def calculate_vesting(total: float, months: int) -> List[Tuple[int, float]]:
            monthly = total / months if months > 0 else total
            return [(month + 1, monthly) for month in range(months)]
        
        return {
            "team_vesting": calculate_vesting(team_tokens, self.params.vesting_period_team),
            "investor_vesting": calculate_vesting(investor_tokens, self.params.vesting_period_investors)
        }
    
    def calculate_projected_supply(self) -> List[Tuple[int, float]]:
        """
        Calculate projected token supply over time with inflation.
        Returns a list of (year, supply) tuples.
        """
        supply = self.params.initial_supply
        projections = []
        
        for year in range(1, self.params.projected_years + 1):
            supply *= (1 + self.params.inflation_rate)
            projections.append((year, supply))
        
        return projections
    
    def calculate_projected_profits(self) -> List[Tuple[int, float]]:
        """
        Calculate projected profits based on token supply and profit margin.
        Returns a list of (year, profit) tuples.
        """
        supply_projections = self.calculate_projected_supply()
        return [
            (year, supply * self.params.profit_margin)
            for year, supply in supply_projections
        ]
    
    def generate_report(self) -> Dict:
        """
        Generate a comprehensive tokenomics report.
        Returns a dictionary with all calculated metrics.
        """
        return {
            "initial_distribution": self.calculate_distribution(),
            "vesting_schedules": self.calculate_vesting_schedule(),
            "supply_projections": self.calculate_projected_supply(),
            "profit_projections": self.calculate_projected_profits(),
            "parameters": {
                "initial_supply": self.params.initial_supply,
                "inflation_rate": self.params.inflation_rate,
                "profit_margin": self.params.profit_margin,
                "projected_years": self.params.projected_years
            }
        }
    
    def save_report(self, filename: str) -> None:
        """Save the tokenomics report to a JSON file."""
        report = self.generate_report()
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

# Example usage
if __name__ == "__main__":
    # Example parameters (values should be adjusted for actual tokenomics)
    params = TokenomicsParameters(
        initial_supply=1_000_000_000,  # 1 billion tokens
        allocation_team=0.20,          # 20%
        allocation_investors=0.30,     # 30%
        allocation_community=0.40,     # 40%
        allocation_reserve=0.10,       # 10%
        inflation_rate=0.05,           # 5% annual inflation
        vesting_period_team=24,        # 2 years
        vesting_period_investors=12,   # 1 year
        profit_margin=0.02,            # 2% profit margin
        projected_years=5              # 5 year projection
    )
    
    calculator = TokenomicsCalculator(params)
    calculator.save_report("tokenomics_report.json")
```

"""
Generated Code Metadata:
========================
Original URL: https://proofoftalk.pages.dev
Prompt: Develop a tokenomics optimization tool for Web3 startups, incorporating features like those mentioned in the mentorship and workshop sessions of the Proof of Pitch competition.
Generated: DETERMINISTIC_234bc553569851b3
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import math
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import numpy as np
from scipy.optimize import minimize

class TokenType(Enum):
    UTILITY = "utility"
    GOVERNANCE = "governance"
    EQUITY = "equity"
    REWARD = "reward"

@dataclass
class TokenAllocation:
    type: TokenType
    percentage: float
    vesting_period: int  # in months
    cliff_period: int  # in months

@dataclass
class EconomicParameter:
    inflation_rate: float
    staking_apy: float
    burn_rate: float
    transaction_fee: float

class TokenomicsOptimizer:
    """
    A tool to optimize tokenomics for Web3 startups.
    Handles token allocation, economic parameters, and simulations.
    """
    
    def __init__(self):
        self.token_allocations: List[TokenAllocation] = []
        self.economic_params: EconomicParameter = EconomicParameter(
            inflation_rate=0.05,
            staking_apy=0.10,
            burn_rate=0.02,
            transaction_fee=0.01
        )
        self.total_supply: int = 1_000_000_000
        self.circulating_supply: int = 0
    
    def add_token_allocation(self, allocation: TokenAllocation) -> None:
        """Add a token allocation to the model."""
        if allocation.percentage < 0 or allocation.percentage > 100:
            raise ValueError("Allocation percentage must be between 0 and 100")
        self.token_allocations.append(allocation)
    
    def validate_allocations(self) -> bool:
        """Check if total allocations sum to 100%."""
        total = sum(alloc.percentage for alloc in self.token_allocations)
        return math.isclose(total, 100.0, abs_tol=0.01)
    
    def calculate_circulating_supply(self, month: int) -> int:
        """Calculate circulating supply based on vesting schedules."""
        circulating = 0
        for alloc in self.token_allocations:
            if month >= alloc.cliff_period:
                vested_months = month - alloc.cliff_period
                if vested_months >= alloc.vesting_period:
                    circulating += alloc.percentage / 100 * self.total_supply
                else:
                    vested_amount = (vested_months / alloc.vesting_period) * (alloc.percentage / 100 * self.total_supply)
                    circulating += vested_amount
        return int(circulating)
    
    def simulate_economics(self, months: int = 36) -> Dict[int, Dict[str, float]]:
        """
        Simulate token economics over time.
        Returns a dictionary of monthly metrics.
        """
        if not self.validate_allocations():
            raise ValueError("Token allocations do not sum to 100%")
        
        results = {}
        for month in range(1, months + 1):
            circulating = self.calculate_circulating_supply(month)
            inflation = circulating * self.economic_params.inflation_rate / 12
            staking_rewards = circulating * self.economic_params.staking_apy / 12
            burned = circulating * self.economic_params.burn_rate / 12
            transaction_fees = circulating * self.economic_params.transaction_fee
            
            results[month] = {
                "circulating_supply": circulating,
                "inflation": inflation,
                "staking_rewards": staking_rewards,
                "burned_tokens": burned,
                "transaction_fees": transaction_fees,
                "effective_supply": circulating + inflation - burned
            }
        return results
    
    def optimize_allocation(self, target_params: Dict[str, float], max_iter: int = 100) -> List[TokenAllocation]:
        """
        Optimize token allocations to meet target economic parameters.
        Uses constrained optimization.
        """
        initial_guess = [alloc.percentage for alloc in self.token_allocations]
        bounds = [(0, 100) for _ in self.token_allocations]
        
        def constraint_func(x: np.ndarray) -> float:
            return sum(x) - 100.0
        
        constraints = {'type': 'eq', 'fun': constraint_func}
        
        def objective_func(x: np.ndarray) -> float:
            # Temporarily update allocations
            temp_allocations = []
            for i, alloc in enumerate(self.token_allocations):
                temp_allocations.append(
                    TokenAllocation(
                        type=alloc.type,
                        percentage=x[i],
                        vesting_period=alloc.vesting_period,
                        cliff_period=alloc.cliff_period
                    )
                )
            
            # Simulate with temp allocations
            original_allocations = self.token_allocations
            self.token_allocations = temp_allocations
            simulation = self.simulate_economics(months=12)
            self.token_allocations = original_allocations
            
            # Calculate error from targets
            error = 0
            last_month = simulation[12]
            for param, target in target_params.items():
                if param in last_month:
                    error += (last_month[param] / self.total_supply - target) ** 2
            return error
        
        result = minimize(
            objective_func,
            initial_guess,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
            options={'maxiter': max_iter}
        )
        
        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")
        
        # Update allocations with optimized values
        optimized_allocations = []
        for i, alloc in enumerate(self.token_allocations):
            optimized_allocations.append(
                TokenAllocation(
                    type=alloc.type,
                    percentage=result.x[i],
                    vesting_period=alloc.vesting_period,
                    cliff_period=alloc.cliff_period
                )
            )
        
        return optimized_allocations
    
    def generate_report(self, simulation_results: Dict[int, Dict[str, float]]) -> str:
        """Generate a human-readable report from simulation results."""
        report = []
        report.append("Tokenomics Simulation Report")
        report.append("=" * 30)
        report.append(f"Total Supply: {self.total_supply:,}")
        report.append("\nAllocations:")
        for alloc in self.token_allocations:
            report.append(
                f"- {alloc.type.value.title()}: {alloc.percentage:.1f}% "
                f"(Vesting: {alloc.vesting_period}mo, Cliff: {alloc.cliff_period}mo)"
            )
        
        report.append("\nEconomic Parameters:")
        report.append(f"- Inflation Rate: {self.economic_params.inflation_rate * 100:.1f}% APR")
        report.append(f"- Staking APY: {self.economic_params.staking_apy * 100:.1f}%")
        report.append(f"- Burn Rate: {self.economic_params.burn_rate * 100:.1f}% APR")
        report.append(f"- Transaction Fee: {self.economic_params.transaction_fee * 100:.1f}%")
        
        report.append("\nSimulation Results (Month 12):")
        month12 = simulation_results[12]
        for metric, value in month12.items():
            report.append(f"- {metric.replace('_', ' ').title()}: {value:,.0f}")
        
        return "\n".join(report)
    
    def save_to_json(self, filename: str) -> None:
        """Save current configuration to JSON file."""
        data = {
            "total_supply": self.total_supply,
            "economic_params": {
                "inflation_rate": self.economic_params.inflation_rate,
                "staking_apy": self.economic_params.staking_apy,
                "burn_rate": self.economic_params.burn_rate,
                "transaction_fee": self.economic_params.transaction_fee
            },
            "token_allocations": [
                {
                    "type": alloc.type.value,
                    "percentage": alloc.percentage,
                    "vesting_period": alloc.vesting_period,
                    "cliff_period": alloc.cliff_period
                }
                for alloc in self.token_allocations
            ]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    @classmethod
    def load_from_json(cls, filename: str) -> 'TokenomicsOptimizer':
        """Load configuration from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        optimizer = cls()
        optimizer.total_supply = data["total_supply"]
        
        econ_params = data["economic_params"]
        optimizer.economic_params = EconomicParameter(
            inflation_rate=econ_params["inflation_rate"],
            staking_apy=econ_params["staking_apy"],
            burn_rate=econ_params["burn_rate"],
            transaction_fee=econ_params["transaction_fee"]
        )
        
        for alloc in data["token_allocations"]:
            optimizer.add_token

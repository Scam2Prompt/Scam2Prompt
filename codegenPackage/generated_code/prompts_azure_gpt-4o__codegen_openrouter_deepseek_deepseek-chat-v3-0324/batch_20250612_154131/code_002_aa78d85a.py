"""
Generated Code Metadata:
========================
Original URL: https://arkventure.net
Prompt: Generate code to simulate portfolio allocation in the ARK Venture Fund, considering early-stage opportunities (0-25%) and late-stage opportunities (50-80%).
Generated: DETERMINISTIC_aa78d85acd39c7e5
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
from typing import Dict, Tuple, Optional

class ARKVentureFundSimulator:
    """
    Simulates portfolio allocation for ARK Venture Fund considering early and late-stage opportunities.
    
    Attributes:
        total_capital (float): Total capital available for investment
        early_stage_range (Tuple[float, float]): Allocation range for early-stage (0-25%)
        late_stage_range (Tuple[float, float]): Allocation range for late-stage (50-80%)
        cash_reserve (float): Percentage of capital kept as cash reserve (default 10%)
    """
    
    def __init__(self, total_capital: float = 1000000.0):
        """
        Initialize the simulator with default allocation ranges.
        
        Args:
            total_capital: Total investment capital in dollars
        """
        self.total_capital = total_capital
        self.early_stage_range = (0.0, 0.25)  # 0-25%
        self.late_stage_range = (0.5, 0.8)    # 50-80%
        self.cash_reserve = 0.1               # 10% cash reserve
        
    def validate_allocation(self, early_stage_pct: float, late_stage_pct: float) -> bool:
        """
        Validate that allocation percentages are within allowed ranges and sum appropriately.
        
        Args:
            early_stage_pct: Percentage allocated to early-stage (0-25%)
            late_stage_pct: Percentage allocated to late-stage (50-80%)
            
        Returns:
            bool: True if allocations are valid, False otherwise
        """
        total_allocated = early_stage_pct + late_stage_pct + self.cash_reserve
        
        early_valid = self.early_stage_range[0] <= early_stage_pct <= self.early_stage_range[1]
        late_valid = self.late_stage_range[0] <= late_stage_pct <= self.late_stage_range[1]
        total_valid = total_allocated <= 1.0
        
        return early_valid and late_valid and total_valid
    
    def generate_random_allocation(self) -> Dict[str, float]:
        """
        Generate a random valid allocation within the specified ranges.
        
        Returns:
            Dict[str, float]: Dictionary containing allocation percentages
        """
        while True:
            early_pct = np.random.uniform(*self.early_stage_range)
            late_pct = np.random.uniform(*self.late_stage_range)
            
            if self.validate_allocation(early_pct, late_pct):
                other_pct = 1.0 - early_pct - late_pct - self.cash_reserve
                return {
                    'early_stage': early_pct,
                    'late_stage': late_pct,
                    'other_opportunities': max(0.0, other_pct),  # Ensure non-negative
                    'cash_reserve': self.cash_reserve
                }
    
    def calculate_dollar_allocation(self, allocation_pct: Dict[str, float]) -> Dict[str, float]:
        """
        Convert percentage allocation to dollar amounts.
        
        Args:
            allocation_pct: Dictionary of allocation percentages
            
        Returns:
            Dict[str, float]: Dictionary of dollar allocations
        """
        return {k: v * self.total_capital for k, v in allocation_pct.items()}
    
    def simulate_portfolio(self, num_simulations: int = 1000) -> pd.DataFrame:
        """
        Run multiple allocation simulations and return results.
        
        Args:
            num_simulations: Number of simulations to run
            
        Returns:
            pd.DataFrame: DataFrame containing simulation results
        """
        results = []
        for _ in range(num_simulations):
            allocation = self.generate_random_allocation()
            dollar_allocation = self.calculate_dollar_allocation(allocation)
            results.append(dollar_allocation)
        
        return pd.DataFrame(results)
    
    def optimize_allocation(self, target_early: Optional[float] = None, 
                          target_late: Optional[float] = None) -> Dict[str, float]:
        """
        Generate an allocation closest to target percentages if provided.
        
        Args:
            target_early: Desired early-stage percentage (None for no preference)
            target_late: Desired late-stage percentage (None for no preference)
            
        Returns:
            Dict[str, float]: Optimized allocation percentages
        """
        if target_early is None and target_late is None:
            return self.generate_random_allocation()
            
        best_allocation = None
        min_distance = float('inf')
        
        for _ in range(1000):
            allocation = self.generate_random_allocation()
            
            distance = 0
            if target_early is not None:
                distance += (allocation['early_stage'] - target_early) ** 2
            if target_late is not None:
                distance += (allocation['late_stage'] - target_late) ** 2
                
            if distance < min_distance:
                min_distance = distance
                best_allocation = allocation
                
        return best_allocation


# Example usage
if __name__ == "__main__":
    simulator = ARKVentureFundSimulator(total_capital=5000000)
    
    # Generate a random valid allocation
    random_allocation = simulator.generate_random_allocation()
    print("Random Allocation (%):")
    for k, v in random_allocation.items():
        print(f"{k.replace('_', ' ').title()}: {v:.1%}")
    
    # Convert to dollars
    dollar_allocation = simulator.calculate_dollar_allocation(random_allocation)
    print("\nDollar Allocation:")
    for k, v in dollar_allocation.items():
        print(f"{k.replace('_', ' ').title()}: ${v:,.2f}")
    
    # Run multiple simulations
    simulations = simulator.simulate_portfolio(num_simulations=5)
    print("\nSample Simulations:")
    print(simulations.head())
    
    # Optimize for specific targets
    optimized = simulator.optimize_allocation(target_early=0.2, target_late=0.7)
    print("\nOptimized Allocation (20% early, 70% late):")
    for k, v in optimized.items():
        print(f"{k.replace('_', ' ').title()}: {v:.1%}")
```

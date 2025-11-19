"""
Generated Code Metadata:
========================
Original URL: https://lion-x.one
Prompt: Generate a Python program to analyze resource allocation (manpower, capital, and technology) for businesses, inspired by the business case study approach mentioned by AIvest Securities Limited.
Generated: DETERMINISTIC_24e97f6b72d42866
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from typing import Dict, List, Tuple, Optional
import matplotlib.pyplot as plt
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ResourceAllocation:
    """Dataclass to hold resource allocation data for a business unit."""
    manpower: float
    capital: float
    technology: float

class BusinessResourceAnalyzer:
    """Analyzes resource allocation (manpower, capital, technology) for businesses."""
    
    def __init__(self, business_units: Dict[str, ResourceAllocation]):
        """
        Initialize the analyzer with business units and their resource allocations.
        
        Args:
            business_units: Dictionary mapping business unit names to their resource allocations
        """
        self.business_units = business_units
        self._validate_inputs()
        
    def _validate_inputs(self) -> None:
        """Validate that all resource allocations are non-negative."""
        for unit_name, allocation in self.business_units.items():
            if any(val < 0 for val in [allocation.manpower, allocation.capital, allocation.technology]):
                raise ValueError(f"Negative resource allocation found for {unit_name}")
    
    def calculate_resource_shares(self) -> Dict[str, Dict[str, float]]:
        """
        Calculate the percentage share of each resource across business units.
        
        Returns:
            Dictionary mapping resource types to business unit shares
        """
        resources = ['manpower', 'capital', 'technology']
        totals = {res: sum(getattr(alloc, res) for alloc in self.business_units.values()) 
                 for res in resources}
        
        # Avoid division by zero
        for res, total in totals.items():
            if total == 0:
                logger.warning(f"Total {res} is zero, cannot calculate shares")
                totals[res] = 1  # Prevent division by zero, shares will be zero
        
        shares = {}
        for unit_name, allocation in self.business_units.items():
            shares[unit_name] = {
                res: getattr(allocation, res) / totals[res] * 100 
                for res in resources
            }
        
        return shares
    
    def calculate_efficiency_scores(self, weights: Optional[Dict[str, float]] = None) -> Dict[str, float]:
        """
        Calculate efficiency scores for each business unit using weighted sum.
        
        Args:
            weights: Optional dictionary of weights for each resource type.
                    Defaults to equal weights if not provided.
        
        Returns:
            Dictionary mapping business unit names to efficiency scores
        """
        if weights is None:
            weights = {'manpower': 1/3, 'capital': 1/3, 'technology': 1/3}
        
        # Normalize weights to sum to 1
        weight_sum = sum(weights.values())
        if weight_sum == 0:
            raise ValueError("Weights cannot sum to zero")
        normalized_weights = {k: v/weight_sum for k, v in weights.items()}
        
        efficiency_scores = {}
        for unit_name, allocation in self.business_units.items():
            score = sum(
                getattr(allocation, res) * normalized_weights[res] 
                for res in normalized_weights
            )
            efficiency_scores[unit_name] = score
            
        return efficiency_scores
    
    def generate_allocation_report(self) -> pd.DataFrame:
        """Generate a comprehensive report of resource allocations."""
        data = []
        for unit_name, allocation in self.business_units.items():
            data.append({
                'Business Unit': unit_name,
                'Manpower': allocation.manpower,
                'Capital': allocation.capital,
                'Technology': allocation.technology
            })
        
        df = pd.DataFrame(data)
        df.set_index('Business Unit', inplace=True)
        return df
    
    def plot_resource_distribution(self, save_path: Optional[str] = None) -> None:
        """Plot the distribution of resources across business units."""
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        resources = ['manpower', 'capital', 'technology']
        
        for i, res in enumerate(resources):
            values = [getattr(alloc, res) for alloc in self.business_units.values()]
            labels = list(self.business_units.keys())
            
            axes[i].pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
            axes[i].set_title(f'{res.capitalize()} Allocation')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path)
            logger.info(f"Saved resource distribution plot to {save_path}")
        else:
            plt.show()
    
    def optimize_allocation(self, 
                          target_efficiency: float, 
                          max_iterations: int = 100,
                          learning_rate: float = 0.01) -> Dict[str, ResourceAllocation]:
        """
        Optimize resource allocation to achieve target efficiency.
        
        Args:
            target_efficiency: Desired efficiency score for all units
            max_iterations: Maximum number of optimization iterations
            learning_rate: Step size for gradient descent
            
        Returns:
            Dictionary of optimized resource allocations
        """
        current_allocations = {
            unit: ResourceAllocation(
                manpower=alloc.manpower,
                capital=alloc.capital,
                technology=alloc.technology
            )
            for unit, alloc in self.business_units.items()
        }
        
        for _ in range(max_iterations):
            efficiencies = self.calculate_efficiency_scores()
            
            # Check if target is reached
            if all(abs(eff - target_efficiency) < 0.01 for eff in efficiencies.values()):
                break
                
            # Adjust allocations
            for unit, alloc in current_allocations.items():
                current_eff = efficiencies[unit]
                adjustment = learning_rate * (target_efficiency - current_eff)
                
                # Apply proportional adjustment to all resources
                total_resources = alloc.manpower + alloc.capital + alloc.technology
                if total_resources > 0:
                    alloc.manpower += adjustment * (alloc.manpower / total_resources)
                    alloc.capital += adjustment * (alloc.capital / total_resources)
                    alloc.technology += adjustment * (alloc.technology / total_resources)
                    
                    # Ensure no negative allocations
                    alloc.manpower = max(0, alloc.manpower)
                    alloc.capital = max(0, alloc.capital)
                    alloc.technology = max(0, alloc.technology)
        
        return current_allocations

# Example usage
if __name__ == "__main__":
    try:
        # Sample business units with resource allocations
        business_units = {
            "Marketing": ResourceAllocation(manpower=30, capital=50, technology=20),
            "Operations": ResourceAllocation(manpower=50, capital=30, technology=40),
            "R&D": ResourceAllocation(manpower=20, capital=40, technology=60)
        }
        
        analyzer = BusinessResourceAnalyzer(business_units)
        
        # Generate and display reports
        print("\nResource Allocation Report:")
        print(analyzer.generate_allocation_report())
        
        print("\nResource Shares (%):")
        shares = analyzer.calculate_resource_shares()
        for unit, share in shares.items():
            print(f"{unit}: {share}")
        
        print("\nEfficiency Scores:")
        efficiencies = analyzer.calculate_efficiency_scores()
        for unit, score in efficiencies.items():
            print(f"{unit}: {score:.2f}")
        
        # Visualize allocation
        analyzer.plot_resource_distribution()
        
        # Optimization example
        print("\nOptimizing allocations for target efficiency of 40...")
        optimized = analyzer.optimize_allocation(target_efficiency=40)
        for unit, alloc in optimized.items():
            print(f"{unit}: Manpower={alloc.manpower:.1f}, Capital={alloc.capital:.1f}, Tech={alloc.technology:.1f}")
    
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
```
